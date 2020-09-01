#include "SampleAnalyzer/User/Analyzer/cms_top_18_003.h"
using namespace MA5;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_top_18_003::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>   Analysis: CMS-TOP-18-003, arXiv:xxxxxxxx <>" << endmsg;
  INFO << "      <>             (four top - SS2L & multilepton)  <>" << endmsg;
  INFO << "      <>   Recaster: B. Fuks, L. Darme               <>" << endmsg;
  INFO << "      <>   Contact:  fuks@lpthe.jussieu.fr            <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.6                <>" << endmsg;
  INFO << "      <>   DOI: XX.YYYY/ZZZ                           <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Declaration of the signal regions
  Manager()->AddRegionSelection("SR1");
  Manager()->AddRegionSelection("SR2");
  Manager()->AddRegionSelection("SR3");
  Manager()->AddRegionSelection("SR4");
  Manager()->AddRegionSelection("SR5");
  Manager()->AddRegionSelection("SR6");
  Manager()->AddRegionSelection("SR7");
  Manager()->AddRegionSelection("SR8");
  Manager()->AddRegionSelection("SR9");
  Manager()->AddRegionSelection("SR10");
  Manager()->AddRegionSelection("SR11");
  Manager()->AddRegionSelection("SR12");
  Manager()->AddRegionSelection("SR13");
  Manager()->AddRegionSelection("SR14");

  // Declaration of the preselection cuts
  Manager()->AddCut("baseline");
  Manager()->AddCut("mee > 12 GeV");
  Manager()->AddCut("veto_3l");
  Manager()->AddCut("InSR");

  // Histograms
  Manager()->AddHisto("njets", 11,0.5,11.5);
  Manager()->AddHisto("nb",    6,0.5, 6.5);
  Manager()->AddHisto("HT",  16,0.,1600.);
  Manager()->AddHisto("MET", 15,0., 600.);

  // Declaration of the selection cuts
  std::string TwoLeps[] = { "SR1", "SR2", "SR3", "SR4", "SR5", "SR6","SR7","SR8"};
  std::string MoreLeps[] = { "SR9", "SR10", "SR11", "SR12", "SR13", "SR14"};
  Manager()->AddCut("2 leptons", TwoLeps);
  Manager()->AddCut("more leptons", MoreLeps);

  std::string TwoBs[] = { "SR1", "SR2", "SR3", "SR9", "SR10", "SR11"};
  std::string ThreeBs[] = { "SR4", "SR5", "SR6", "SR7"};
  std::string MoreThreeBs[] = {"SR12", "SR13", "SR14"};
  Manager()->AddCut("2 bjets", TwoBs);
  Manager()->AddCut("3 bjets", ThreeBs);
  Manager()->AddCut("more4 bjets", "SR8");
  Manager()->AddCut("more3 bjets", MoreThreeBs);

  std::string More8Js[] = { "SR3", "SR7"};
  std::string FiveJs[] = { "SR4", "SR9", "SR13"};
  std::string SixJs[] = { "SR1", "SR5", "SR10"};
  std::string SevenJs[] = { "SR2", "SR6"};
  Manager()->AddCut("4 jets","SR12");
  Manager()->AddCut("5 jets",FiveJs);
  Manager()->AddCut("6 jets",SixJs);
  Manager()->AddCut("7 jets", SevenJs);
  Manager()->AddCut("more5 jets", "SR8");
  Manager()->AddCut("more6 jets", "SR14");
  Manager()->AddCut("more7 jets", "SR11");
  Manager()->AddCut("more8 jets", More8Js);

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_top_18_003::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_top_18_003::Execute(SampleFormat& sample, const EventFormat& event)
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
  std::vector<const RecLeptonFormat*> LooseElectrons;
  for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
  {
    const RecLeptonFormat *myElec = &(event.rec()->electrons()[ii]);
    if(IsLooseLepton(myElec, event, 5., 2.5))
      LooseElectrons.push_back(myElec);
  }

  // Muons
  std::vector<const RecLeptonFormat*> LooseMuons;
  for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
  {
    const RecLeptonFormat *myMuon = &(event.rec()->muons()[ii]);
    if(IsLooseLepton(myMuon, event, 7., 2.4))
      LooseMuons.push_back(myMuon);
  }

  // Jets
  std::vector <const RecJetFormat*> IsoJets, SignalJets;
  unsigned int nj=0, nb=0;
  double HT=0.;
  for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
  {
    const RecJetFormat * myJet = &(event.rec()->jets()[ii]);
    double eta = std::fabs(myJet->eta());
    double pt = myJet->pt();
    double iso = true, isL = false;
    for (unsigned int jj=0; jj<LooseElectrons.size(); jj++)
    {
      if(myJet->dr(LooseElectrons[jj])<0.1) { isL = true;  break; }
      if(myJet->dr(LooseElectrons[jj])<0.4) { iso = false; break; }
    }
    if(iso && !isL)
    {
      for (unsigned int jj=0; jj<LooseMuons.size(); jj++)
      {
        if(myJet->dr(LooseMuons[jj])<0.1) { isL = true;  break; }
        if(myJet->dr(LooseMuons[jj])<0.4) { iso = false; break; }
      }
    }
    if(!iso && !isL /*&& pt>5.*/) IsoJets.push_back(myJet);
    else if(!isL && eta<2.4 && iso)
    {
      if(pt>25. && myJet->btag()) nb++;
      if(pt>40.) { nj++; HT+=myJet->pt(); SignalJets.push_back(myJet);}
    }
  }

  // Lepton isolation
  std::vector<const RecLeptonFormat*> IsoElectrons, IsoMuons;
  std::vector<const RecLeptonFormat*> SignalLeptons, SignalElectrons, SignalMuons;
  for (unsigned int jj=0; jj<LooseElectrons.size(); jj++)
    if(IsIsolated(LooseElectrons[jj],IsoJets,event,0.12,0.80,7.2))
    {
      if(LooseElectrons[jj]->pt()>20.)
      {
        SignalLeptons.push_back(LooseElectrons[jj]);
        SignalElectrons.push_back(LooseElectrons[jj]);
      }
      IsoElectrons.push_back(LooseElectrons[jj]);
    }
  for (unsigned int jj=0; jj<LooseMuons.size(); jj++)
    if(IsIsolated(LooseMuons[jj],IsoJets,event,0.16,0.76,7.2))
    {
      if(LooseMuons[jj]->pt()>20.)
      {
        SignalLeptons.push_back(LooseMuons[jj]);
        SignalMuons.push_back(LooseMuons[jj]);
      }
      IsoMuons.push_back(LooseMuons[jj]);
    }
  SORTER->sort(SignalLeptons, PTordering);
  unsigned int nl = SignalLeptons.size();

  // MET
  double MET = event.rec()->MET().pt();

  // Cut-0: baseline
  bool base_jets = (nj>=2) && (nb>=2) && (HT>300.);
  bool base_leps = (nl>=2) && (SignalLeptons[0]->pt()>25.) && (SignalLeptons[1]->pt()>20.); // LD -- Added Trail lepton
  bool SS_leps = false;
  unsigned int iSS=99;
  for(unsigned int ii=1; ii<SignalLeptons.size(); ii++)
    if(SignalLeptons[0]->charge()==SignalLeptons[ii]->charge())
    {
      if(iSS==99) {SS_leps=true; iSS=ii; }
      else {SS_leps=false; break; }
    }
  if(!Manager()->ApplyCut( base_jets && base_leps && SS_leps && MET > 50.,"baseline")) return true;

  // cut-1: Mee > 12 GeV
  bool mee_12=false;
  for(unsigned int ii=0; ii<SignalElectrons.size(); ii++)
    for(unsigned int jj=ii+1; jj<SignalElectrons.size(); jj++)
    {
       if(SignalElectrons[ii]->charge()==SignalElectrons[jj]->charge())
       {
         double mee = (SignalElectrons[ii]->momentum()+SignalElectrons[jj]->momentum()).M();
         if(mee<12.) {mee_12=true; break;}
       }
    }
  if(!Manager()->ApplyCut(!mee_12,"mee > 12 GeV")) return true;

  // cut-3: 3rd lepton
  bool veto_3l=false;
  for(unsigned int jj=0; jj<IsoMuons.size();jj++)
  {
    if(IsoMuons[jj]->dr(SignalLeptons[0])<0.1) continue;
    if(IsoMuons[jj]->dr(SignalLeptons[iSS])<0.1) continue;
    for(unsigned int ii=0;ii<SignalMuons.size();ii++)
    {
       if(SignalMuons[ii]->dr(SignalLeptons[0])>0.1 &&
          SignalMuons[ii]->dr(SignalLeptons[iSS])>0.1) continue;
       if(IsoMuons[jj]->charge()==SignalMuons[ii]->charge()) continue;
       double mll = (SignalMuons[ii]->momentum()+IsoMuons[jj]->momentum()).M();
       double ThirdmupT= SignalMuons[ii]->pt();
       if((ThirdmupT >5) && (mll<12. || (mll>76. && mll<106.)) ) { veto_3l=true; break; } // LD -- Added pt limit
    }
    if (veto_3l) break;
  }
  if(!veto_3l)
  {
    for(unsigned int jj=0; jj<IsoElectrons.size();jj++)
    {
      if(IsoElectrons[jj]->dr(SignalLeptons[0])<0.1) continue;
      if(IsoElectrons[jj]->dr(SignalLeptons[iSS])<0.1) continue;
      for(unsigned int ii=0;ii<SignalElectrons.size();ii++)
      {
         if(SignalElectrons[ii]->dr(SignalLeptons[0])>0.1 &&
            SignalElectrons[ii]->dr(SignalLeptons[iSS])>0.1) continue;
         if(IsoElectrons[jj]->charge()==SignalElectrons[ii]->charge()) continue;
         double mll = (SignalElectrons[ii]->momentum()+IsoElectrons[jj]->momentum()).M();
         double ThirdepT= SignalElectrons[ii]->pt();
         if((ThirdepT >7) && (mll<12. || (mll>76. && mll<106.)) ) { veto_3l=true; break; }// LD -- Added pt limit
      }
      if (veto_3l) break;
    }
  }
  if(!Manager()->ApplyCut(!veto_3l,"veto_3l")) return true;
  if(!Manager()->ApplyCut( (nl==2 && nb<4 && (nb+nj)>7) || (nl==2 && nb>3 && nj>4) ||
     (nl>2 && nb==2 && nj>4) || (nl>2 && nb>2 && nj>3)    ,"InSR")) return true;


  // Crazy observable
  // SORTER->sort(SignalJets, PTordering);
  // MALorentzVector HTvec(0.,0.,0.,0.);
  // for(unsigned ii=1;ii<SignalJets.size();ii++)
  //   HTvec=HTvec+SignalJets[ii]->momentum();
  // double crazy = std::fabs(SignalJets[0]->phi() - HTvec.Phi());
  // if(crazy>M_PI) crazy=2.*M_PI-crazy;

  // Histograms
  Manager()->FillHisto("njets",nj);
  Manager()->FillHisto("nb"   ,nb);
  Manager()->FillHisto("HT"  ,HT);
  Manager()->FillHisto("MET" ,MET);
  // Manager()->FillHisto("test1" ,crazy);



  // SR definitions : leptons
  if(!Manager()->ApplyCut(nl==2,"2 leptons")) return true;
  if(!Manager()->ApplyCut(nl> 2,"more leptons")) return true;

  // SR definitions : b-jets
  if(!Manager()->ApplyCut(nb==2,"2 bjets")) return true;
  if(!Manager()->ApplyCut(nb==3,"3 bjets")) return true;
  if(!Manager()->ApplyCut(nb> 3,"more4 bjets")) return true;
  if(!Manager()->ApplyCut(nb> 2,"more3 bjets")) return true;

  // SR definitions : jets
  if(!Manager()->ApplyCut(nj==4,"4 jets")) return true;
  if(!Manager()->ApplyCut(nj==5,"5 jets")) return true;
  if(!Manager()->ApplyCut(nj==6,"6 jets")) return true;
  if(!Manager()->ApplyCut(nj==7,"7 jets")) return true;
  if(!Manager()->ApplyCut(nj> 4,"more5 jets")) return true;
  if(!Manager()->ApplyCut(nj> 5,"more6 jets")) return true;
  if(!Manager()->ApplyCut(nj> 6,"more7 jets")) return true;
  if(!Manager()->ApplyCut(nj> 7,"more8 jets")) return true;

return true;
}


// -----------------------------------------------------------------------------
// User-defined methods
// -----------------------------------------------------------------------------
bool cms_top_18_003::IsLooseLepton(const RecLeptonFormat* Lep, const EventFormat& event,
  const double &ptTH, const double &etaTH)
{
  double eta = std::fabs(Lep->eta());
  double pt = Lep->pt();

  double DR = 10./std::min(std::max(pt,50.),200.);
  double imini = (PHYSICS->Isol->eflow->sumIsolation(Lep,
    event.rec(),DR,0.,IsolationEFlow::ALL_COMPONENTS))/pt;

  if( eta<etaTH && pt>ptTH && imini<0.4) return true;
  return false;
}


bool cms_top_18_003::IsIsolated(const RecLeptonFormat* Lep,
   std::vector<const RecJetFormat*> IsoJets, const EventFormat& event,
   const double &I1, const double &I2, const double &I3)
{
  double pt  = Lep->pt();
  // I1
  double DR = 10./std::min(std::max(pt,50.),200.);
  double imini = (PHYSICS->Isol->eflow->sumIsolation(Lep,
     event.rec(),DR,0.,IsolationEFlow::ALL_COMPONENTS))/pt;
  // Closest jet
  unsigned int ijet=9999;
  double drmin=1e+09;
  for(unsigned int ii=0; ii<IsoJets.size(); ii++)
    if(Lep->dr(IsoJets[ii])<drmin) { drmin=Lep->dr(IsoJets[ii]); ijet=ii; }
  // I2
  double ptratio=1.;
  if (ijet!=9999)  ptratio = pt/IsoJets[ijet]->pt();
  // I3
  double ptrel = 0.;
  if (ijet!=9999)
  {
     MAVector3 axis(IsoJets[ijet]->momentum().Vect() - Lep->momentum().Vect());
     ptrel = (axis.Cross(Lep->momentum().Vect())).Mag()/axis.Mag();
  }
  // output
  if (imini<I1 && (ptratio>I2 || ptrel>I3)) return true;
  return false;
}
