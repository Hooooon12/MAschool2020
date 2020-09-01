#include "SampleAnalyzer/User/Analyzer/cms_exo_12_047.h"
#include <TCanvas.h>

using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------

bool cms_exo_12_047::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: CMS-EXO-12-047                <>" << endmsg;
  INFO << "        <>              (Monophoton)                  <>" << endmsg;
  INFO << "        <>    Recasted by: J. Guo, E. Conte & B. Fuks <>" << endmsg;
  INFO << "        <>    Contact: Jun.Guo@iphc.cnrs.fr           <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.2             <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/ <>" << endmsg;
  INFO << "        <>    /PhysicsAnalysisDatabase                <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Declaring signal region(s)
  // This analysis has one signal region
  Manager()->AddRegionSelection("S1");

  // Signal regions cuts
  Manager()->AddCut("ET_gamma >145 GeV |eta|<1.44","S1");      // 1.
  Manager()->AddCut("isolation","S1");                         // 2.
  Manager()->AddCut("MET>140 GeV", "S1");                      // 3.
  Manager()->AddCut("DPhi(leading photon,MET)>2","S1");        // 4.
  Manager()->AddCut("Nlepton<1","S1");                         // 5.
  Manager()->AddCut("Njet<2","S1");                            // 6.

  return true;
}

// Finalize
// function called one time at the end of the analysis
void cms_exo_12_047::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

// function called each time one event is read
bool cms_exo_12_047::Execute(SampleFormat& sample, const EventFormat& event)
{
  // unchange
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
  {
    //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
    return false;
  }
  Manager()->InitializeForNewEvent(myEventWeight);

  //the loop start
  if (event.rec()==0) { return true;}
  //Defining the containers
  vector<const RecPhotonFormat*> SignalPhotons;
  vector<const RecJetFormat*> SignalJets;
  vector<const RecLeptonFormat*>SignalMuons,SignalElectrons;

  //the MET
  MALorentzVector pTmiss = event.rec()->MET().momentum();
  double MET = pTmiss.Pt();

  //electron with pt>10
  for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++)
  {
    const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ie]);
    if(CurrentElectron->pt()>10.0)
      SignalElectrons.push_back(CurrentElectron);
  }

  //electron isolation
  for(int ii=SignalElectrons.size()-1;ii>=0;ii--)
    for(unsigned int jj=0; jj<SignalElectrons[ii]->isolCones().size(); jj++)
      if(fabs(SignalElectrons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        if(SignalElectrons[ii]->isolCones()[jj].sumPT() > 0.2*SignalElectrons[ii]->pt())
          SignalElectrons.erase(SignalElectrons.begin()+ii);

  // Muons with pT>10
  for(unsigned int im=0; im<event.rec()->muons().size(); im++)
  {
    const RecLeptonFormat * CurrentMuon = &(event.rec()->muons()[im]);
    if(CurrentMuon->pt()>10.)
      SignalMuons.push_back(CurrentMuon);
  }

  //muon isolation
  for(int ii=SignalMuons.size()-1;ii>=0;ii--)
    for(unsigned int jj=0; jj<SignalMuons[ii]->isolCones().size(); jj++)
      if(fabs(SignalMuons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        if(SignalMuons[ii]->isolCones()[jj].sumPT() > 0.1*SignalMuons[ii]->pt())
          SignalMuons.erase(SignalMuons.begin()+ii);

  //the photon selection
  for(unsigned int ia=0; ia<event.rec()->photons().size(); ia++)
  {
    const RecPhotonFormat * CurrentPhoton = &(event.rec()->photons()[ia]);
    if(CurrentPhoton->pt()>145.0  && fabs(CurrentPhoton->eta())<1.44)
      SignalPhotons.push_back(CurrentPhoton);
  }

  //the jets
  for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++)
  {
      const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
      if ( CurrentJet->pt() > 30.0 )
        SignalJets.push_back(CurrentJet);
  }

  // start the cuts
  double preselection=myEventWeight*0.96;
  Manager()->SetCurrentEventWeight(preselection);

  //cut1 more than one expect photon
  if(!Manager()->ApplyCut(SignalPhotons.size()>0 ,"ET_gamma >145 GeV |eta|<1.44"))
    return true;

  //remove the un-isolated photon 
  for(int ii=SignalPhotons.size()-1;ii>=0;ii--)
  {
    const RecPhotonFormat * myPhoton = &(event.rec()->photons()[ii]);
    double mypt=myPhoton->pt();
    double chargept=PHYSICS->Isol->eflow->sumIsolation(myPhoton,event.rec(),0.3,0.,IsolationEFlow::TRACK_COMPONENT);
    double neutralpt=PHYSICS->Isol->eflow->sumIsolation(myPhoton,event.rec(),0.3,0.,IsolationEFlow::NEUTRAL_COMPONENT);
    double photonpt=PHYSICS->Isol->eflow->sumIsolation(myPhoton,event.rec(),0.3,0.,IsolationEFlow::PHOTON_COMPONENT);
    double photonplt=photonpt-mypt;
    double photonID=SignalPhotons[ii]->HEoverEE();
    if(chargept > 1.5||neutralpt > (1.0+0.04*mypt)||photonplt > (0.7+0.005*mypt)||photonID > 0.05)
       SignalPhotons.erase(SignalPhotons.begin()+ii);
  }

  //cut2 photon isolation
  if(!Manager()->ApplyCut(SignalPhotons.size()>0 ,"isolation"))
    return true;

  //cut3 MET
  if(!Manager()->ApplyCut((MET > 140.),"MET>140 GeV"))
    return true;

  //cut4 DPhi(leading photon,MET)>2
  if(!Manager()->ApplyCut((SignalPhotons[0]->dphi_0_pi(pTmiss))>2.0,"DPhi(leading photon,MET)>2"))
    return true;

  //the distance dr between photon-jet, photon -electron, as given by the paper
  //the jets
  bool do_erase1 = false;
  for(int ii=SignalJets.size()-1; ii>=0; ii--)
  {
    for(unsigned int jj=0; jj<SignalPhotons.size(); jj++)
    {
      if(SignalJets[ii]->dr(SignalPhotons[jj]) < 0.5)
      {
        do_erase1 = true;
        break;
      }
    }
    if(do_erase1)
    {
      SignalJets.erase(SignalJets.begin()+ii);
      do_erase1 = false;
    }
  }

  //the electrons
  bool do_erase2 = false;
  for(int ii=SignalElectrons.size()-1; ii>=0; ii--)
  {
    for(unsigned int jj=0; jj<SignalPhotons.size(); jj++)
    {
      if(SignalElectrons[ii]->dr(SignalPhotons[jj]) < 0.5)
      {
        do_erase2 = true;
        break;
      }
    }
    if(do_erase2)
    {
      SignalElectrons.erase(SignalElectrons.begin()+ii);
      do_erase2 = false;
    }
  }

  //the muons
  bool do_erase3 = false;
  for(int ii=SignalMuons.size()-1; ii>=0; ii--)
  {
    for(unsigned int jj=0; jj<SignalPhotons.size(); jj++)
    {
      if(SignalMuons[ii]->dr(SignalPhotons[jj]) < 0.5)
      {
        do_erase3 = true;
        break;
      }
    }
    if(do_erase3)
    {
      SignalMuons.erase(SignalMuons.begin()+ii);
      do_erase3 = false;
    }
  }

  //cut5 Nlepton<1
  if(!Manager()->ApplyCut((SignalElectrons.size()+SignalMuons.size())==0 ,"Nlepton<1"))
    return true;
  if(!Manager()->ApplyCut(SignalJets.size()<2 ,"Njet<2"))
    return true;

  //the loop end

  return true;
}

