#include "SampleAnalyzer/User/Analyzer/cms_exo_12_048.h"
#include <TCanvas.h>
using namespace MA5;
using namespace std;
// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_exo_12_048::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: CMS-EXO-12-048                <>" << endmsg;
  INFO << "        <>              (Monojet)                     <>" << endmsg;
  INFO << "        <>    Recasted by: J. Guo, E. Conte & B. Fuks <>" << endmsg;
  INFO << "        <>    Contact: Jun.Guo@iphc.cnrs.fr           <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.2             <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/ <>" << endmsg;
  INFO << "        <>    /PhysicsAnalysisDatabase                <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // =====Declare the 7 signal regions in this analysis=====
  Manager()->AddRegionSelection("MET>250");
  Manager()->AddRegionSelection("MET>300");
  Manager()->AddRegionSelection("MET>350");
  Manager()->AddRegionSelection("MET>400");
  Manager()->AddRegionSelection("MET>450");
  Manager()->AddRegionSelection("MET>500");
  Manager()->AddRegionSelection("MET>550");

  // Signal regions cuts
  Manager()->AddCut("1 large pt jet");			       // 1.
  Manager()->AddCut("Njet<3");				       // 2.
  Manager()->AddCut("2th jet condition");		       // 3.
  Manager()->AddCut("Nelectron<1");			       // 4.
  Manager()->AddCut("Nmuon<1"); 			       // 5.
  Manager()->AddCut("Ntauon<1");			       // 6.

   Manager()->AddCut("MET>250","MET>250");		       // 7.
   Manager()->AddCut("MET>300","MET>300");		       // 7.
   Manager()->AddCut("MET>350","MET>350");		       // 7.
   Manager()->AddCut("MET>400","MET>400");		       // 7.
   Manager()->AddCut("MET>450","MET>450");		       // 7.
   Manager()->AddCut("MET>500","MET>500");		       // 7.
   Manager()->AddCut("MET>550","MET>550");		       // 7.

  return true;
}


// Finalize
// function called one time at the end of the analysis
void cms_exo_12_048::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

bool cms_exo_12_048::Execute(SampleFormat& sample, const EventFormat& event)
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
  if (event.rec()==0) {return true;}

  //Defining the containers
  vector<const RecJetFormat*> SignalJets;
  vector<const RecLeptonFormat*>SignalMuons,SignalElectrons;
  vector<const RecTauFormat*>SignalTaus;

  //the MET
  MALorentzVector pTmiss = event.rec()->MET().momentum();
  double MET = pTmiss.Pt();

  //the jets
  for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++)
  {
    const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
    if ( CurrentJet->pt() > 30.0 && abs(CurrentJet->eta())<4.5)
       SignalJets.push_back(CurrentJet);
  }

  //electron with pt>10
  for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++)
  {
    const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ie]);
    if(CurrentElectron->pt()>10.0)
      SignalElectrons.push_back(CurrentElectron);
  }

  // Muons with pT>10
  for(unsigned int im=0; im<event.rec()->muons().size(); im++)
  {
    const RecLeptonFormat * CurrentMuon = &(event.rec()->muons()[im]);
    if(CurrentMuon->pt()>10.)
      SignalMuons.push_back(CurrentMuon);
  }

  // tau with pT>20, abs(eta)<2.3
  for(unsigned int it=0; it<event.rec()->taus().size(); it++)
  {
    const RecTauFormat * CurrentTau = &(event.rec()->taus()[it]);
    if(CurrentTau->pt()>20.&& abs(CurrentTau->eta())<2.3)
      SignalTaus.push_back(CurrentTau);
  }

  //start the cut
  double preselection=0.96*myEventWeight;
  Manager()->SetCurrentEventWeight(preselection);


  //cut1 need 1 jet with pT>110, |eta|<2.4
  // Ordering jet according to their PT
  SORTER->sort(SignalJets, PTordering);

  bool test = true;
  if(SignalJets.size()==0) {test=false;}
  else if(SignalJets.size()>0)
  {
    test=(fabs(SignalJets[0]->eta())<2.4 && SignalJets[0]->pt()>110.);
  }
  if(!Manager()->ApplyCut(test,"1 large pt jet"))
     return true;

  //cut2 Njet<3
  bool test1=true;
  if(SignalJets.size()>2)test1=false;
  if(!Manager()->ApplyCut(test1,"Njet<3"))
    return true;

  //cut3 the 2th jet's condition
  bool test0=true;
  if(SignalJets.size()==1) test0=true;
  else if(SignalJets.size()==2)
  {
    double detaphi = SignalJets[1]->dphi_0_pi(SignalJets[0]);
    if(detaphi>2.5){test0=false;}
  }
  if(!Manager()->ApplyCut(test0,"2th jet condition"))
      return true;

  for(int ie=SignalElectrons.size()-1;ie>=0;ie--)
  {
    const RecLeptonFormat * myElectron = &(event.rec()->electrons()[ie]);
    double myept=myElectron->pt();
    double chargepte=PHYSICS->Isol->eflow->sumIsolation(myElectron,event.rec(),0.4,0.,IsolationEFlow::TRACK_COMPONENT);
    double neutralpte=PHYSICS->Isol->eflow->sumIsolation(myElectron,event.rec(),0.4,0.,IsolationEFlow::NEUTRAL_COMPONENT);
    double photonpte=PHYSICS->Isol->eflow->sumIsolation(myElectron,event.rec(),0.4,0.,IsolationEFlow::PHOTON_COMPONENT);
    double ttpte=chargepte + neutralpte + photonpte;
    if(ttpte > 0.2*myept)
       SignalElectrons.erase(SignalElectrons.begin()+ie);
  }

  for(int im=SignalMuons.size()-1;im>=0;im--)
  {
    const RecLeptonFormat * myMuon = &(event.rec()->muons()[im]);
    double mympt=myMuon->pt();
    double chargeptm=PHYSICS->Isol->eflow->sumIsolation(myMuon,event.rec(),0.4,0.,IsolationEFlow::TRACK_COMPONENT);
    double neutralptm=PHYSICS->Isol->eflow->sumIsolation(myMuon,event.rec(),0.4,0.,IsolationEFlow::NEUTRAL_COMPONENT);
    double photonptm=PHYSICS->Isol->eflow->sumIsolation(myMuon,event.rec(),0.4,0.,IsolationEFlow::PHOTON_COMPONENT);
    double ttptm=chargeptm + neutralptm + photonptm;
    if(ttptm > 0.2*mympt)
       SignalMuons.erase(SignalMuons.begin()+im);
  }

  for(int it=SignalTaus.size()-1;it>=0;it--)
  {
     const RecTauFormat * myTau = &(event.rec()->taus()[it]);
     double mytpt=myTau->pt();
     double chargeptt=PHYSICS->Isol->eflow->sumIsolation(myTau,event.rec(),0.4,0.,IsolationEFlow::TRACK_COMPONENT);
     double neutralptt=PHYSICS->Isol->eflow->sumIsolation(myTau,event.rec(),0.4,0.,IsolationEFlow::NEUTRAL_COMPONENT);
     double photonptt=PHYSICS->Isol->eflow->sumIsolation(myTau,event.rec(),0.4,0.,IsolationEFlow::PHOTON_COMPONENT);
     double ttptt=chargeptt + neutralptt + photonptt;
     if(ttptt > 0.2*mytpt)
        SignalTaus.erase(SignalTaus.begin()+it);
  }

  //cut4 Nelectron<1
  if(!Manager()->ApplyCut((SignalElectrons.size())==0 ,"Nelectron<1"))
      return true;

  //cut5 Nmuon<1
  if(!Manager()->ApplyCut((SignalMuons.size())==0 ,"Nmuon<1"))
      return true;

  //cut6 Ntauon<1
  if(!Manager()->ApplyCut((SignalTaus.size())==0 ,"Ntauon<1"))
      return true;

  if (MET > 1000){MET = 999.0;}

  //==========================================
  // Apply the Signal Region - dependent cuts =======
  // ==========================================
  Manager()->ApplyCut(MET>250, "MET>250");
  Manager()->ApplyCut(MET>300, "MET>300");
  Manager()->ApplyCut(MET>350, "MET>350");
  Manager()->ApplyCut(MET>400, "MET>400");
  Manager()->ApplyCut(MET>450, "MET>450");
  Manager()->ApplyCut(MET>500, "MET>500");
  Manager()->ApplyCut(MET>550, "MET>550");

  return true;
}
