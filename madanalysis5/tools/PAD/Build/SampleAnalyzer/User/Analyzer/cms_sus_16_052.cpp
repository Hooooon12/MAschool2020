#include "SampleAnalyzer/User/Analyzer/cms_sus_16_052.h"
#include <TCanvas.h>
using namespace MA5;
using namespace std;
// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_sus_16_052::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: cms_sus_16_052                <>" << endmsg;
  INFO << "        <>    Monojet @sqrt(s) = 13 TeV, 36.2 fb^-1 luminosity  <>" << endmsg;
  INFO << "        <>    Recasted by: D. Sengupta <>" << endmsg;
  INFO << "        <>    Contact: dipan@pa.msu.edu           <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.5 and above        <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase <>" << endmsg;
 

// =========Declare the signal regions in this analysis=====//
  Manager()->AddRegionSelection("SR1aX");
  Manager()->AddRegionSelection("SR1aY");
  Manager()->AddRegionSelection("SR1bX");
  Manager()->AddRegionSelection("SR1bY");
  Manager()->AddRegionSelection("SR1cX");
  Manager()->AddRegionSelection("SR1cY");

  Manager()->AddRegionSelection("SR2aX");
  Manager()->AddRegionSelection("SR2aY");
  Manager()->AddRegionSelection("SR2bX");
  Manager()->AddRegionSelection("SR2bY");
  Manager()->AddRegionSelection("SR2cX");
  Manager()->AddRegionSelection("SR2cY");
//========================================================//

  std::string SR_1[]={"SR1aX","SR1aY","SR1bX","SR1bY","SR1cX","SR1cY"};
  std::string SR_2[]={"SR2aX","SR2aY","SR2bX","SR2bY","SR2cX","SR2cY" };
//=====================================================================//
    std::string SR_1a[]={"SR1aX","SR1aY"};
    std::string SR_1b[]={"SR1bX","SR1bY"};
    std::string SR_1c[]={"SR1cX","SR1cY"};
    std::string SR_2a[]={"SR2aX","SR2aY"};
    std::string SR_2b[]={"SR2bX","SR2bY"};
    std::string SR_2c[]={"SR2cX","SR2cY"};
//=============General Cuts=================//

 Manager()->AddCut("Njets > 0");
 Manager()->AddCut("MET > 200 GeV");
 Manager()->AddCut("PT(ISR) > 100 GeV");
 Manager()->AddCut("HT> 300 GeV");
 Manager()->AddCut("dPhi(j1,j2)<2.5");  
 Manager()->AddCut("Nhardjet < 3");
 Manager()->AddCut("Ntau = 0");  
 Manager()->AddCut("Nlepton >= 1");
 Manager()->AddCut("Nlepton(pt > 20) =< 2");
  Manager()->AddCut("PT(l) < 30 GeV");
//======Signal Region Cuts====RegionSR1==========
  Manager()->AddCut("Nbjet=0",SR_1 );
  Manager()->AddCut("CT1 > 300 GeV",SR_1 );
  Manager()->AddCut("|eta|_l < 1.5",SR_1 );  
  
  Manager()->AddCut("MT1<60",SR_1a);
  Manager()->AddCut("QL1a",SR_1a );
  Manager()->AddCut("CT1aX 300-400","SR1aX");
  Manager()->AddCut("CT1aY > 400", "SR1aY");



  Manager()->AddCut("MT1  60-95", SR_1b);
  Manager()->AddCut("QL1b", SR_1b );
  Manager()->AddCut("CT1bX 300-400","SR1bX");
  Manager()->AddCut("CT1bY > 400", "SR1bY");  


  Manager()->AddCut("MT1 > 95",SR_1c);
  Manager()->AddCut("CT1cX 300-400","SR1cX");
  Manager()->AddCut("CT1cY > 400","SR1cY");     
 
//================Signal Region Cuts SR2================// 
 
  Manager()->AddCut("Nbjetsoft=1",SR_2 );
  Manager()->AddCut("CT2 > 300 GeV",SR_2 );


  Manager()->AddCut("MT(2) < 60",SR_2a);
  Manager()->AddCut("CT2aX 300-400","SR2aX" );
  Manager()->AddCut("CT2aY > 400","SR2aY" );
  
 
  Manager()->AddCut("MT(2)  60-95",SR_2b);
  Manager()->AddCut("CT2bX 300-400","SR2bX" );
  Manager()->AddCut("CT2bY > 400","SR2bY" );  

  Manager()->AddCut("MT(2) > 95", SR_2c);
  Manager()->AddCut("CT2cX 300-400","SR2cX" );
  Manager()->AddCut("CT2cY > 400","SR2cY" ); 
//=====END====================================//


  return true;
}


// Finalize
// function called one time at the end of the analysis
void cms_sus_16_052::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
//For plots, not required 
//  TCanvas* can = new TCanvas("can","",600,600);
}

bool cms_sus_16_052::Execute(SampleFormat& sample, const EventFormat& event)
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






 //Defining the containers
   vector<const RecJetFormat*> SignalJets;
   vector<const RecLeptonFormat*>SignalMuons,SignalElectrons,SignalLeptons;
   vector<const RecTauFormat*>SignalTaus;
 
//the MET
           MALorentzVector pTmiss = event.rec()->MET().momentum();
           double MET = pTmiss.Pt();
 



//the jets
       double HT =0. ;  
       int nhardjet =0;
       int nbtag =0;
      for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++)
       {
        const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
        if ( CurrentJet->pt() > 30.0 && abs(CurrentJet->eta())<2.4)
        {SignalJets.push_back(CurrentJet);
        HT = HT + CurrentJet->pt();
         
                }
    
      
        }

//electron with pt>5
       for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++)
        {
        const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ie]);
        double pt = CurrentElectron->pt();
        double abseta = fabs(CurrentElectron->eta());
        if(pt > 5 && abseta < 2.5)
        SignalElectrons.push_back(CurrentElectron);
               }



//muons with pt > 3.5
 for(unsigned int im=0; im<event.rec()->muons().size(); im++)
  {
    const RecLeptonFormat * CurrentMuon = &(event.rec()->muons()[im]);
      double pt = CurrentMuon->pt();
     double abseta = fabs(CurrentMuon->eta());

      if(pt > 3.5 && abseta < 2.4)
      SignalMuons.push_back(CurrentMuon);
  }

  

//taus with pt>5
       for(unsigned int ie=0; ie<event.rec()->taus().size(); ie++)
        {
        const RecTauFormat * CurrentTau = &(event.rec()->taus()[ie]);
        double pt = CurrentTau->pt();
        double abseta = fabs(CurrentTau->eta());
        if(pt > 5 && abseta < 2.5)
        SignalTaus.push_back(CurrentTau);
        }

//====Isolation===========================================
for(int ie=SignalElectrons.size()-1;ie>=0;ie--)
  {
    const RecLeptonFormat * myElectron = &(event.rec()->electrons()[ie]);
    double myept=myElectron->pt();
    double chargepte=PHYSICS->Isol->eflow->sumIsolation(myElectron,event.rec(),0.3,0.,IsolationEFlow::TRACK_COMPONENT);
    double neutralpte=PHYSICS->Isol->eflow->sumIsolation(myElectron,event.rec(),0.3,0.,IsolationEFlow::NEUTRAL_COMPONENT);
    double photonpte=PHYSICS->Isol->eflow->sumIsolation(myElectron,event.rec(),0.3,0.,IsolationEFlow::PHOTON_COMPONENT);
    double ttpte=chargepte + neutralpte + photonpte;
    if(ttpte > 0.2*myept)
       SignalElectrons.erase(SignalElectrons.begin()+ie);
  }


  
 for(int ie1=SignalElectrons.size()-1;ie1>=0;ie1--)
 {
  SignalLeptons.push_back(SignalElectrons[ie1]);
 }

  
//===========Isolation=======================================================================================//  

  for(int im=SignalMuons.size()-1;im>=0;im--)
  {
    const RecLeptonFormat * myMuon = &(event.rec()->muons()[im]);
    double mympt=myMuon->pt();
    double chargeptm=PHYSICS->Isol->eflow->sumIsolation(myMuon,event.rec(),0.3,0.,IsolationEFlow::TRACK_COMPONENT);
    double neutralptm=PHYSICS->Isol->eflow->sumIsolation(myMuon,event.rec(),0.3,0.,IsolationEFlow::NEUTRAL_COMPONENT);
    double photonptm=PHYSICS->Isol->eflow->sumIsolation(myMuon,event.rec(),0.3,0.,IsolationEFlow::PHOTON_COMPONENT);
   double ttptm=chargeptm + neutralptm + photonptm;
    if(ttptm > 0.2*mympt)
       SignalMuons.erase(SignalMuons.begin()+im);
  }


  for(int im1=SignalMuons.size()-1;im1>=0;im1--)
 {
  SignalLeptons.push_back(SignalMuons[im1]);
 }
//==========================================================================================================//
   bool lcentral = false ;
   bool ncharge = false ;
    for(int il=SignalLeptons.size()-1;il>=0;il--)
 {
  if (SignalLeptons[il]->charge() < 0 ) {ncharge = true;} else {ncharge = false;}
  if (abs(SignalLeptons[il]->eta()) < 1.5 ) {lcentral = true;} else {lcentral = false;}
 }



//=============================Overlap removal of Jets=============================// 
     SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, SignalElectrons, 0.3);
     SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, SignalMuons,     0.3);


//==============================================================================//   
//=================Ordering jets and leptons according to their PT==============//

    SORTER->sort(SignalJets, PTordering);
    int  NumSignalJets = SignalJets.size() ; 

    SORTER->sort(SignalLeptons, PTordering);
    int  NumSignalLeptons = SignalLeptons.size() ; 

//======B tags= all, hard, and soft=============================================//
    
         int nbtagsoft =0;
         int  nbtaghard =0;
         for (int ij1=SignalJets.size()-1;ij1>=0;ij1--){
     
      if (SignalJets[ij1]->btag()) nbtag = nbtag +1;
      if (SignalJets[ij1]->pt() < 60 ) {
      if (SignalJets[ij1]->btag()) nbtagsoft = nbtagsoft +1;
       }
       if (SignalJets[ij1]->pt() > 60 ) {
      if (SignalJets[ij1]->btag()) nbtaghard = nbtaghard +1;
       }

      }

//========================================MT,CT1,CT2============================//
         double MT =0;
         if (NumSignalLeptons > 0)
         MT = SignalLeptons[0]->mt_met(pTmiss);

        double CT1 = 0;
        if (MET < (HT-100) ) {CT1 = MET;}
        else{ CT1 = HT -100 ; }

        double CT2 =0;
         if( NumSignalJets > 0){
        if (MET < (SignalJets[0]->pt() - 25) ) {CT2 = MET;}
        else{ CT2 = SignalJets[0]->pt() - 25 ; }
         }
        

//==========================================DeltaPhi============================//
   double DeltaPhiJet1 = 999999.9;
      if( NumSignalJets > 1)
   {DeltaPhiJet1= SignalJets[0]->dphi_0_pi(SignalJets[1]);
   }
    
//====================================General Cuts=============================//
      
          if(!Manager()->ApplyCut(( NumSignalJets > 0),"Njets > 0"))
          return true;
     
          if(!Manager()->ApplyCut((MET > 200),"MET > 200 GeV"))
          return true;

          if(!Manager()->ApplyCut((SignalJets[0]->pt() > 100),"PT(ISR) > 100 GeV"))
          return true;
           
          if(!Manager()->ApplyCut((HT > 300),"HT> 300 GeV"))
          return true;

//=========================DeltaPhi + hardjet Cut==============================//

       if(!Manager()->ApplyCut((DeltaPhiJet1 < 2.5),"dPhi(j1,j2)<2.5"))
       return true;
         
        if(NumSignalJets > 2){
        if (SignalJets[2]->pt() > 60 )
         nhardjet = 3; }
      
       if(!Manager()->ApplyCut(( nhardjet < 3 ),"Nhardjet < 3"))
        return true;
//===================================Lepton Cuts==============================//  

      if(!Manager()->ApplyCut((SignalTaus.size() < 1),"Ntau = 0"))
          return true;
      if(!Manager()->ApplyCut((SignalLeptons.size() > 0),"Nlepton >= 1"))
          return true;
  
      int nhardlepton = 2 ; 
      if (NumSignalLeptons > 2){
      if (SignalLeptons[2]->pt() > 20 )
      nhardlepton = 3;}
  
      if(!Manager()->ApplyCut(( nhardlepton < 3 ),"Nlepton(pt > 20) =< 2"))
       return true;
 
      if(!Manager()->ApplyCut((SignalLeptons[0]->pt() < 30 ),"PT(l) < 30 GeV"))
      return true;
      

//=================Common to SR1s==================================//
        if(!Manager()->ApplyCut((nbtag < 1 ),"Nbjet=0"))
          return true;
        
        if(!Manager()->ApplyCut((CT1 > 300 ),"CT1 > 300 GeV"))
        return true;

        if(!Manager()->ApplyCut(lcentral,"|eta|_l < 1.5"))
        return true;

//=============================SR1a==================================//
     if(!Manager()->ApplyCut((MT < 60),"MT1<60"))
          return true;

      if(!Manager()->ApplyCut(ncharge,"QL1a"))
        return true;

       if(!Manager()->ApplyCut((CT1 > 300 && CT1 < 400 ),"CT1aX 300-400"))
      return true;
           if(!Manager()->ApplyCut(( CT1 > 400 ),"CT1aY > 400"))
      return true;
//==================SR1b=========================================//
     if(!Manager()->ApplyCut((MT > 60 && MT < 95),"MT1  60-95"))
     return true;
      if(!Manager()->ApplyCut(ncharge,"QL1b"))
        return true;
       if(!Manager()->ApplyCut((CT1 > 300 && CT1 < 400 ),"CT1bX 300-400"))
      return true;
           if(!Manager()->ApplyCut(( CT1 > 400 ),"CT1bY > 400"))
      return true;
//================SR1c==========================================//

   if(!Manager()->ApplyCut(( MT > 95),"MT1 > 95"))
          return true;
    if(!Manager()->ApplyCut((CT1 > 300 && CT1 < 400 ),"CT1cX 300-400"))
      return true;
   if(!Manager()->ApplyCut(( CT1 > 400 ),"CT1cY > 400"))
      return true;

  
//================================SR2s=================================//
    if(!Manager()->ApplyCut((nbtagsoft == 1  && nbtaghard==0 ),"Nbjetsoft=1"))
          return true;
    if(!Manager()->ApplyCut((CT2 > 300 ),"CT2 > 300 GeV"))
      return true;       
//===========================SR2a======================================//

     if(!Manager()->ApplyCut((MT < 60),"MT(2) < 60"))
     return true;
     if(!Manager()->ApplyCut((CT2 > 300 && CT2 < 400 ),"CT2aX 300-400"))
     return true;
     if(!Manager()->ApplyCut(( CT2 > 400 ),"CT2aY > 400"))
      return true;

//========================SR2b=========================================//
     
     if(!Manager()->ApplyCut((MT > 60 && MT < 95 ),"MT(2)  60-95"))
     return true;
     if(!Manager()->ApplyCut((CT2 > 300 && CT2 < 400 ),"CT2bX 300-400"))
     return true;
     if(!Manager()->ApplyCut(( CT2 > 400 ),"CT2bY > 400"))
     return true;

//===========================SR2C ===================================//

     if(!Manager()->ApplyCut(( MT > 95),"MT(2) > 95"))
     return true;
     if(!Manager()->ApplyCut((CT2 > 300 && CT2 < 400 ),"CT2cX 300-400"))
     return true;
     if(!Manager()->ApplyCut(( CT2 > 400 ),"CT2cY > 400"))
      return true;

//========================End======================================//





  return true;
}



