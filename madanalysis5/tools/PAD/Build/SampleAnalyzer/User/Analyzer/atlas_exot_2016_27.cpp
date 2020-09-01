#include "SampleAnalyzer/User/Analyzer/atlas_exot_2016_27.h"
#include <TCanvas.h>
using namespace MA5;
using namespace std;
// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_exot_2016_27::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: atlas_exot_2016_27                <>" << endmsg;
  INFO << "        <>    Monojet @sqrt(s) = 13 TeV, 36.2 fb^-1 luminosity  <>" << endmsg;
  INFO << "        <>    Recasted by: D. Sengupta <>" << endmsg;
  INFO << "        <>    Contact: dipan@lpsc.in2p3.fr           <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.3 and above        <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase <>" << endmsg;
  INFO << "        <>    Validated on signal region EMs, Cutflows for IMs not available" << endmsg;
  INFO << "        <>    Signal region EM7 and IM7 are identical, only EM7 used" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

// =====Declare the signal regions in this analysis=====
  Manager()->AddRegionSelection("EM1");
  Manager()->AddRegionSelection("EM2");
  Manager()->AddRegionSelection("EM3");
  Manager()->AddRegionSelection("EM4");
  Manager()->AddRegionSelection("EM5");
  Manager()->AddRegionSelection("EM6");
  Manager()->AddRegionSelection("EM7");
  Manager()->AddRegionSelection("EM8");
  Manager()->AddRegionSelection("EM9");
  
  
//===================================//
  Manager()->AddRegionSelection("IM1");
  Manager()->AddRegionSelection("IM2");
  Manager()->AddRegionSelection("IM3");
  Manager()->AddRegionSelection("IM4");
  Manager()->AddRegionSelection("IM5");
  Manager()->AddRegionSelection("IM6");
  Manager()->AddRegionSelection("IM7");
  Manager()->AddRegionSelection("IM8");
  Manager()->AddRegionSelection("IM9");
  Manager()->AddRegionSelection("IM10");
  
//=============General Cuts=================//
 Manager()->AddCut("MET > 250 GeV");
 Manager()->AddCut("ElectronVeto");
 Manager()->AddCut("MuonVeto");
 Manager()->AddCut("Njets <= 4");
 Manager()->AddCut("dphij1met > 0.4");
 Manager()->AddCut("dphij2met > 0.4");
 Manager()->AddCut("dphij3met > 0.4");
 Manager()->AddCut("dphij4met > 0.4");
 Manager()->AddCut("Leading jet pT > 250 GeV");
//======Signal Region Cuts====RegionEMs==========
  Manager()->AddCut("250 < MET < 300 GeV", "EM1");
  Manager()->AddCut("300 < MET < 350 GeV", "EM2");
  Manager()->AddCut("350 < MET < 400 GeV", "EM3");
  Manager()->AddCut("400 < MET < 500 GeV", "EM4");
  Manager()->AddCut("500 < MET < 600 GeV", "EM5");
  Manager()->AddCut("600 < MET < 700 GeV", "EM6");
  Manager()->AddCut("700 < MET < 800 GeV", "EM7");
  Manager()->AddCut("800 < MET < 900 GeV", "EM8");
  Manager()->AddCut("900 < MET < 1000 GeV","EM9");
//===Signal Region Cuts==RegionIMs===============
  Manager()->AddCut("MET > 250 GeV(IM1)", "IM1");
  Manager()->AddCut("MET > 300 GeV(IM2)", "IM2");
  Manager()->AddCut("MET > 350 GeV(IM3)", "IM3");
  Manager()->AddCut("MET > 400 GeV(IM4)", "IM4");
  Manager()->AddCut("MET > 500 GeV(IM5)", "IM5");
  Manager()->AddCut("MET > 600 GeV(IM6)", "IM6");
  Manager()->AddCut("MET > 700 GeV(IM7)", "IM7");
  Manager()->AddCut("MET > 800 GeV(IM8)", "IM8");
  Manager()->AddCut("MET > 900 GeV(IM9)", "IM9");
  Manager()->AddCut("MET > 1000 GeV(IM10)", "IM10"); 
//================================================
  return true;
}


// Finalize
// function called one time at the end of the analysis
void atlas_exot_2016_27::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
//For plots, not required 
//  TCanvas* can = new TCanvas("can","",600,600);
}

bool atlas_exot_2016_27::Execute(SampleFormat& sample, const EventFormat& event)
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
       EventFormat myEvent;
       myEvent = event;


//=====MET filter of 100 GeV at the MC level==================//
//==Used only for validation===//
//==Validated on SUSY simplified models with a neutralino LSP//
/*
        unsigned int n = event.mc()->particles().size();
        MALorentzVector sum_MET;

        for(unsigned int i=0; i<n; i++)
        {
          MCParticleFormat* prt = &myEvent.mc()->particles()[i];
          if(prt->pdgid() == 1000022)
          { // neutralino
            sum_MET += prt->momentum();
          }
         else if(prt->pdgid() == 12)
          { // neu_e
            sum_MET += prt->momentum();
          }
          else if(prt->pdgid() == 14)
          { // neu_m
            sum_MET += prt->momentum();
          }
          else if(prt->pdgid() == 16)
          { // neu_t
            sum_MET += prt->momentum();
          }

        }

         if(!Manager()->ApplyCut((sum_MET.Pt() > 100.),"MET Filter > 100"))
         return true;

*/



 //Defining the containers
   vector<const RecJetFormat*> SignalJets;
   vector<const RecLeptonFormat*>SignalMuons,SignalElectrons;
   vector<const RecTauFormat*>SignalTaus;
 
//the MET
           MALorentzVector pTmiss = event.rec()->MET().momentum();
           double MET = pTmiss.Pt();
       
          if(!Manager()->ApplyCut((MET > 250),"MET > 250 GeV"))
          return true;




//the jets
      for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++)
       {
        const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
        if ( CurrentJet->pt() > 30.0 && abs(CurrentJet->eta())<2.8)
        SignalJets.push_back(CurrentJet);
        }

//electron with pt>20
       for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++)
        {
        const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ie]);
        double pt = CurrentElectron->pt();
        double abseta = fabs(CurrentElectron->eta());
        if(pt > 20. && abseta < 2.47)
        SignalElectrons.push_back(CurrentElectron);
        }



//muons with pt > 10
 for(unsigned int im=0; im<event.rec()->muons().size(); im++)
  {
    const RecLeptonFormat * CurrentMuon = &(event.rec()->muons()[im]);
      double pt = CurrentMuon->pt();
     double abseta = fabs(CurrentMuon->eta());

      if(pt > 10. && abseta < 2.47)
      SignalMuons.push_back(CurrentMuon);
  }

for(int ie=SignalElectrons.size()-1;ie>=0;ie--)
  {
    const RecLeptonFormat * myElectron = &(event.rec()->electrons()[ie]);
    double myept=myElectron->pt();
    double chargepte=PHYSICS->Isol->eflow->sumIsolation(myElectron,event.rec(),0.2,0.,IsolationEFlow::TRACK_COMPONENT);
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


//======Overlap removal of jets===================//
     SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, SignalElectrons, 0.4);
     SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, SignalMuons,     0.4);


//=======================================================//   
//======Ordering jet according to their PT==============//

    SORTER->sort(SignalJets, PTordering);
   int  NumSignalJets = SignalJets.size() ; 



//======Electron Veto==============//

   if(!Manager()->ApplyCut((SignalElectrons.size())==0 ,"ElectronVeto"))
   return true;
  
//============Muon Veto==========//

   if(!Manager()->ApplyCut((SignalMuons.size())==0 ,"MuonVeto"))
   return true;

//=====Four Jets at Most====//  
   if(!Manager()->ApplyCut((NumSignalJets < 5),"Njets <= 4"))
   return true;

//======DeltaPhi==================//
   double DeltaPhiJet1 = 0.0;
   double DeltaPhiJet2 = 0.0 ;
   double DeltaPhiJet3 =0.0;
   double DeltaPhiJet4 =0.0;
  
if( NumSignalJets > 0)
{DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2=9999999.9;
DeltaPhiJet3=9999999.9;
DeltaPhiJet4=9999999.9;
}

if( NumSignalJets > 1)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3=999999.9;
DeltaPhiJet4=9999999.9;
}

if( NumSignalJets > 2)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3= SignalJets[2]->dphi_0_pi(pTmiss);
DeltaPhiJet4=9999999.9;
}

if( NumSignalJets > 3)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3= SignalJets[2]->dphi_0_pi(pTmiss);
DeltaPhiJet4 = SignalJets[3]->dphi_0_pi(pTmiss);
}

//========DeltaPhi Cuts===========================//

    if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4),"dphij1met > 0.4"))
      return true;
     if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4),"dphij2met > 0.4"))
      return true;
    if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4),"dphij3met > 0.4"))
     return true;
    if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.4),"dphij4met > 0.4"))
      return true;

//=============Leading jet pT cut=================//
    if(!Manager()->ApplyCut(( SignalJets[0]->pt() > 250 && abs(SignalJets[0]->eta()) < 2.4 ),"Leading jet pT > 250 GeV"))
      return true;


//=======Signal Region Specific Cuts==============//
//===Exclusive signal regions EM1-7, validated on ATLAS cutflows ====////
//=====SREM1===//
   if(!Manager()->ApplyCut((MET > 250 && MET < 300),"250 < MET < 300 GeV"))
   return true;
//=====SREM2===//
   if(!Manager()->ApplyCut((MET > 300 && MET < 350),"300 < MET < 350 GeV"))
   return true;
//====SREM3===//
  if(!Manager()->ApplyCut((MET > 350 && MET < 400),"350 < MET < 400 GeV"))
  return true;
//====SREM4===//
  if(!Manager()->ApplyCut((MET > 400 && MET < 500),"400 < MET < 500 GeV"))
  return true;
//=====SREM5====//
  if(!Manager()->ApplyCut((MET > 500 && MET < 600),"500 < MET < 600 GeV"))
  return true;
//====SREM6====//
  if(!Manager()->ApplyCut((MET > 600 && MET < 700),"600 < MET < 700 GeV"))
  return true;
//===SREM7=====//
  if(!Manager()->ApplyCut((MET > 700 && MET < 800 ),"700 < MET < 800 GeV"))
  return true;
//===SREM8=====//
  if(!Manager()->ApplyCut((MET > 800 && MET < 900 ),"800 < MET < 900 GeV"))
  return true;
//===SREM9=====//
  if(!Manager()->ApplyCut((MET > 900 && MET < 1000 ),"900 < MET < 1000 GeV"))
  return true;
//===============================================================================//

//=====SRIM1===//
   if(!Manager()->ApplyCut((MET > 250 ),"MET > 250 GeV(IM1)"))
    return true;
//=====SRIM2===//
   if(!Manager()->ApplyCut((MET > 300 ),"MET > 300 GeV(IM2)"))
   return true;
//=====SRIM3===//
   if(!Manager()->ApplyCut((MET > 350),"MET > 350 GeV(IM3)"))
   return true;
//=====SRIM4===//
   if(!Manager()->ApplyCut((MET > 400 ),"MET > 400 GeV(IM4)"))
   return true;
//=====SRIM5===//
   if(!Manager()->ApplyCut((MET > 500 ),"MET > 500 GeV(IM5)"))
   return true;
//=====SRIM6===//
   if(!Manager()->ApplyCut((MET > 600 ),"MET > 600 GeV(IM6)"))
   return true;
//=====SRIM7===//
   if(!Manager()->ApplyCut((MET > 700 ),"MET > 700 GeV(IM7)"))
   return true;
//=====SRIM8===//
   if(!Manager()->ApplyCut((MET > 800 ),"MET > 800 GeV(IM8)"))
   return true;
//=====SRIM9===//
   if(!Manager()->ApplyCut((MET > 900 ),"MET > 900 GeV(IM9)"))
   return true;
//=====SRIM10===//
   if(!Manager()->ApplyCut((MET > 1000 ),"MET > 1000 GeV(IM10)"))
   return true;



//==========End===================//





  return true;
}



