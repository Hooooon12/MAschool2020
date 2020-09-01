#include "SampleAnalyzer/User/Analyzer/cms_exo_16_010.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_exo_16_010::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>   Analysis: CMS-EXO-16-010, arXiv:1701.02042 <>" << endmsg;
  INFO << "      <>             (mono Z-boson)                   <>" << endmsg;
  INFO << "      <>   Recaster: Benjamin Fuks                    <>" << endmsg;
  INFO << "      <>   Contact:  fuks@lpthe.jussieu.fr            <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.6                <>" << endmsg;
  INFO << "      <>   DOI: XX.YYYY/ZZZ                           <>" << endmsg;
  INFO << "      <>   Please cite arXiv:1709.nnnnn [hep-ph]      <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Declaration of the signal regions
  Manager()->AddRegionSelection("ee");
  Manager()->AddRegionSelection("mumu");

  // Declaration of the preselection cuts
  Manager()->AddCut("2_electrons", "ee");
  Manager()->AddCut("2_muons", "mumu");
  Manager()->AddCut("on-Z");
  Manager()->AddCut("dilepton_pt");
  Manager()->AddCut("3rd_lepton_veto");
  Manager()->AddCut("b_veto");

  // Declaration of the selection cuts
  Manager()->AddCut("dphi(met,Z)");
  Manager()->AddCut("mom_balance");
  Manager()->AddCut("met");
  Manager()->AddCut("at_most_one_jet");

  // Histogram declaration
  Manager()->AddHisto("MET_preselected_e",15,0,1200,"ee");
  Manager()->AddHisto("MET_preselected_mu",15,0,1200, "mumu");
  Manager()->AddHisto("MET_selected_e",15,0,1200, "ee");
  Manager()->AddHisto("MET_selected_mu",15,0,1200, "mumu");

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_exo_16_010::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_exo_16_010::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Event weight
  double myWeight;
  if(Configuration().IsNoEventWeight()) myWeight=1.;
  else if(event.mc()->weight()!=0.) myWeight=event.mc()->weight();
  else
  {
    //WARNING << "Found one event with a zero weight. Skipping...\n";
    return false;
  }
  Manager()->InitializeForNewEvent(myWeight);

  // Security for empty events
  if (event.rec()==0) return true;

  // Electrons
  std::vector<const RecLeptonFormat*> SignalLeptons, LooseElectrons;
  for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
  {
    const RecLeptonFormat *myElec = &(event.rec()->electrons()[ii]);
    double eta = fabs(myElec->eta());
    double pt = myElec->pt();
    double iso_var = PHYSICS->Isol->eflow->sumIsolation(myElec,
        event.rec(),0.4,0.,IsolationEFlow::ALL_COMPONENTS);

    if( (eta > 1.44) and (eta<1.57) ) continue;
    if(eta > 2.5) continue;

    if(iso_var>0.15*pt) continue;

    if (pt>20)  SignalLeptons.push_back(myElec);
    if (pt>10)  LooseElectrons.push_back(myElec);
  }
  unsigned int ne=SignalLeptons.size(); // number of electrons

  // Muons
  std::vector<const RecLeptonFormat*> LooseMuons;
  for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
  {
    const RecLeptonFormat *myMuon = &(event.rec()->muons()[ii]);
    double eta = fabs(myMuon->eta());
    double pt = myMuon->pt();
    double iso_var = PHYSICS->Isol->eflow->sumIsolation(myMuon,
        event.rec(),0.4,0.,IsolationEFlow::TRACK_COMPONENT);

    if(eta > 2.4) continue;

    if(iso_var>0.20*pt) continue;

    if (pt>20)  SignalLeptons.push_back(myMuon);
    if (pt>10)  LooseMuons.push_back(myMuon);
  }
  unsigned int nmu = SignalLeptons.size() - ne;
  unsigned int nloose = LooseElectrons.size()+LooseMuons.size();

  // Taus
  unsigned int ntau = 0;
  for(unsigned int ii=0; ii<event.rec()->taus().size(); ii++)
  {
    const RecTauFormat *myTau = &(event.rec()->taus()[ii]);
    double pt = myTau->pt();
    double iso_var = PHYSICS->Isol->eflow->sumIsolation(myTau,
        event.rec(),0.4,0.,IsolationEFlow::ALL_COMPONENTS);

    if(iso_var<0.20*pt and pt>20)  ntau++;
  }

  // Jets
  std::vector<const RecJetFormat*> SignalJets, BtaggedJets;
  for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
  {
    const RecJetFormat * myJet = &(event.rec()->jets()[ii]);
    double eta = fabs(myJet->eta());
    double pt = myJet->pt();

    if(eta > 5.) continue;

    if(pt>30.) SignalJets.push_back(myJet);
    if(pt>20. && eta<2.5 && myJet->btag())
       BtaggedJets.push_back(myJet);
  }
  SignalJets  = PHYSICS->Isol->JetCleaning(SignalJets,  LooseElectrons, 0.2);
  BtaggedJets = PHYSICS->Isol->JetCleaning(BtaggedJets, LooseElectrons, 0.2);

  unsigned int nb = BtaggedJets.size();
  unsigned int nj = SignalJets.size();

  // MET
  MALorentzVector pTm = event.rec()->MET().momentum();
  double MET = pTm.Pt();


  // Cut 1: two OSSF leptons
  double charge=0.;
  if(ne==2 || nmu==2) charge=SignalLeptons[0]->charge()*SignalLeptons[1]->charge();
  if(!Manager()->ApplyCut( (ne==2) && (charge<0.),"2_electrons")) return true;
  if(!Manager()->ApplyCut( (nmu==2) && (charge<0.),"2_muons")) return true;

  // Cut 2: on-Z requirement
  MALorentzVector pZ=SignalLeptons[0]->momentum()+SignalLeptons[1]->momentum();
  if(!Manager()->ApplyCut(fabs(pZ.M() - 90.)<10., "on-Z"))
    return true;

  // Cut 3: pT of the reconstructed Z-boson
  if(!Manager()->ApplyCut(pZ.Pt()>50., "dilepton_pt"))
    return true;

  // Cut 4: veto on the third lepton and on taus
  if(!Manager()->ApplyCut( (nloose<3) && (ntau==0),"3rd_lepton_veto"))
    return true;

  // Cut 5: b-veto
  if(!Manager()->ApplyCut(nb==0,"b_veto"))
    return true;

  // MET distribution after the preslectiopn
  if(ne==2)
    Manager()->FillHisto("MET_preselected_e",MET);
  if(nmu==2)
    Manager()->FillHisto("MET_preselected_mu",MET);

  // Cut 6: dPHI (met ,Z)
  if(!Manager()->ApplyCut(fabs(pZ.DeltaPhi(pTm)) > 2.7,"dphi(met,Z)"))
    return true;

  // Cut 7: momentum balance of the event
  if(!Manager()->ApplyCut( (fabs(MET-pZ.Pt())/pZ.Pt()) < 0.2,"mom_balance"))
    return true;

  // Cut 8: MET
  if(!Manager()->ApplyCut(MET > 80,"met"))
    return true;

  // Cut 9: number of jets
  if(!Manager()->ApplyCut(nj <= 1,"at_most_one_jet"))
    return true;

  // MET distribution after the fianl slectiopn
  if(ne==2)
    Manager()->FillHisto("MET_selected_e",MET);
  if(nmu==2)
    Manager()->FillHisto("MET_selected_mu",MET);

  return true;
}

