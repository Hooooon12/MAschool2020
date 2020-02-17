#include "SampleAnalyzer/User/Analyzer/atlas_exot_2014_06.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_exot_2014_06::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: atlas_exot_2014_06             <>" << endmsg;
  INFO << "        <>              (Monophoton)                  <>" << endmsg;
  INFO << "        <>    Recasted by: D.Barducci                 <>" << endmsg;
  INFO << "        <>    Contact: barducci@lapth.cnrs.fr         <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.1.11          <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/ <>" << endmsg;
  INFO << "        <>    /PhysicsAnalysisDatabase                <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Declaring signal region(s)
  // This analysis has one signal region
  Manager()->AddRegionSelection("S1");
  
  //----------------------------------------------//
  //              CUT FLOW                        //
  //       (in the order of Tab.1 of the          //
  //        aux material available at             //
  //        https://atlas.web.cern.ch/Atlas/      //
  //        GROUPS/PHYSICS/PAPERS/EXOT-2014-06/)  //
  //----------------------------------------------//  
  
  // Signal regions cuts
  Manager()->AddCut("MET>150 GeV","S1");                      // 1.
  Manager()->AddCut("1+ photon, pT>125, |eta|<2.37","S1");    // 2.
  Manager()->AddCut("Tight leading photon |eta|<1.37","S1");  // 3.
  Manager()->AddCut("Isolated leading photon","S1");          // 4.
  Manager()->AddCut("DPhi(leading photon,MET)>0.4","S1");     // 5.
  Manager()->AddCut("Njet<2 and DPhi(jet,MET)>0.4","S1");     // 6.
  Manager()->AddCut("Lepton veto","S1");                      // 7.
  
  return true;
  
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_exot_2014_06::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_exot_2014_06::Execute(SampleFormat& sample, const EventFormat& event)
{


  // ***************************************************************************
  // Example of analysis with reconstructed objects
  // Concerned samples : 
  //   - LHCO samples
  //   - LHE/STDHEP/HEPMC samples after applying jet-clustering algorithm
  // ***************************************************************************
    
  // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
  // Book-keeping with the event weight; no need to modify this.
  // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
  {
    //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
    return false;
  }
  Manager()->InitializeForNewEvent(myEventWeight);
    

  if (event.rec()!=0){ 
    
    // defining containers
    vector<const RecPhotonFormat*> SignalPhotons;
    vector<const RecJetFormat*> SignalJets;
    vector<const RecLeptonFormat*>SignalMuons,SignalElectrons;
   
    // Finding MET
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();  

    //--------------------------------------------//
    //    Here we collect the various objects     //
    //--------------------------------------------//
   
    // Electrons with pT>7, |eta|<2.47
    for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++){
      const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ie]);
      if(CurrentElectron->pt()>7.0 && fabs(CurrentElectron->eta())<2.47){
        SignalElectrons.push_back(CurrentElectron);	 
      }
    }
    // We then apply a loose isolation to remove non-prompt electrons    
    SignalElectrons = PHYSICS->Isol->tracker->getRelIsolated(SignalElectrons,event.rec(),0.2,0.2,0.5);

    // Muons with pT>6, |eta|<2.5
    for(unsigned int im=0; im<event.rec()->muons().size(); im++){
    const RecLeptonFormat * CurrentMuon = &(event.rec()->muons()[im]);
      if(CurrentMuon->pt()>6.0 && fabs(CurrentMuon->eta())<2.5){
        SignalMuons.push_back(CurrentMuon);	 
      }
    }

    // Photons with pT>10, |eta|<2.37 taking into account the crack into the detector between 1.37 < |eta| < 1.52
    for(unsigned int ia=0; ia<event.rec()->photons().size(); ia++){
      const RecPhotonFormat * CurrentPhoton = &(event.rec()->photons()[ia]);
      if(CurrentPhoton->pt()>10.0  && (fabs(CurrentPhoton->eta())<1.37 || (fabs(CurrentPhoton->eta())>1.52 && fabs(CurrentPhoton->eta())<2.37))){
        SignalPhotons.push_back(CurrentPhoton);
      }
    }

    // We then apply a loose isolation to remove non-prompt photon    
    for(int ii=SignalPhotons.size()-1;ii>=0;ii--)
     if(PHYSICS->Isol->calorimeter->sumIsolation(SignalPhotons[ii],event.rec(),0.2)>SignalPhotons[ii]->et()+5.)
         SignalPhotons.erase(SignalPhotons.begin()+ii);

    // Jets with pT > 30, |eta|< 4.5
    for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++){
      const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
      if ( CurrentJet->pt() > 30.0 && fabs(CurrentJet->eta()) < 4.5){
        SignalJets.push_back(CurrentJet);
      }
    }
   
    //-------------------------------------//
    //     Here the cut flow starts        //
    //-------------------------------------//
    
    // We want to reproduce the good vertex and cleaning cuts present in the event pre-selection from which
    // in the provided cut flow, the pass from 8582 to 8213 events.
    // Since is not possible to reproduce this within a fast detector simulation we scale our events for that ratio, while 
    // while applying also the first Signal Region cut.
    // In this way one however is not sensitive to any model dependency of this Pre-selection requirements
   
    double preselection=myEventWeight*8213.0/8582.0;   

    Manager()->SetCurrentEventWeight(preselection);
  
    // SR cut 1.
    if(!Manager()->ApplyCut((MET > 150.),"MET>150 GeV")){
      return true;    
    }
   
    // SR cut 2.
    // Note that |eta|<2.37 is already satisfied
   
    if(!Manager()->ApplyCut(SignalPhotons.size()>0 && SignalPhotons[0]->pt()>125 ,"1+ photon, pT>125, |eta|<2.37")){     
      return true;    
    }
   
    // A tight photon has further requirement. The efficiency is about 90 % for E above 125, so reweigh by hand
    // (https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/EGAMMA/PublicPlots/20140611/ATL-COM-PHYS-2014-542/ATL-COM-PHYS-2014-542.pdf)
    double tight=0.9;
    Manager()->SetCurrentEventWeight(preselection*tight);
    
    // SR cut 3.
    if(!Manager()->ApplyCut(fabs(SignalPhotons[0]->eta())<1.37,"Tight leading photon |eta|<1.37")){
      return true; 
    }     
   
    // Now we ask the leading photon to be isolated
    
    bool isolphoton = (PHYSICS->Isol->calorimeter->sumIsolation(SignalPhotons[0],event.rec(),0.4)<5.+SignalPhotons[0]->et());
   
    // SR cut 4.
    if(!Manager()->ApplyCut(isolphoton,"Isolated leading photon")){
      return true; 
    }    
     
    // SR cut 5.
    if(!Manager()->ApplyCut((SignalPhotons[0]->dphi_0_pi(pTmiss))>0.4,"DPhi(leading photon,MET)>0.4")){
      return true;  
    }     
    
    // Next we want jets with distance deltaR>0.2 to the closes preselected electron or photon,
    // otherwise they will be discarded. As for the implementation of cms_sus_13_011 note that in other analyses
    // it's common to see electrons discarded if they're too close to jets; not here.

    SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, SignalElectrons, 0.2);
    SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, SignalPhotons, 0.2);


    // SR cut 6.
    if(!Manager()->ApplyCut((SignalJets.size()==0)||(SignalJets.size()==1 && (SignalJets[0]->dphi_0_pi(pTmiss))>0.4) ,"Njet<2 and DPhi(jet,MET)>0.4")){
     return true;
    }
   
    // Searching for lepton which will cause a veto   
    bool lepton_veto = true;
    if(SignalElectrons.size()>0 || SignalMuons.size()>0){
      lepton_veto = false; 
    }
    
    // SR cut 7.
    if(!Manager()->ApplyCut(lepton_veto ,"Lepton veto")){
      return true;
    }

  }// end loop on events
  return true;
}


