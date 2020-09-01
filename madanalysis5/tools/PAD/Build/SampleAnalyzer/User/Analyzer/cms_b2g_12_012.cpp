#include "SampleAnalyzer/User/Analyzer/cms_b2g_12_012.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_b2g_12_012::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: cms_b2g_12_012	         <>" << endmsg;
  INFO << "        <>              (Same-sign dilepton)          <>" << endmsg;
  INFO << "        <>    Recasted by: D.Barducci and C. Delaunay <>" << endmsg;
  INFO << "        <>    Contact: barducci@lapth.cnrs.fr         <>" << endmsg;
  INFO << "        <>    Contact: delaunay@lapth.cnrs.fr         <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.2             <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/ <>" << endmsg;
  INFO << "        <>    /PhysicsAnalysisDatabase                <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  
  
  // Declaring signal region
  // This analysis has one signal region
  Manager()->AddRegionSelection("S1");
  
  // Signal regions cuts
  Manager()->AddCut("2SS leptons","S1");                      
  Manager()->AddCut("Z veto","S1");      
  Manager()->AddCut(">=2 jets","S1");  
  Manager()->AddCut("3l veto","S1");    
  Manager()->AddCut(">=7 Const.","S1");    
  Manager()->AddCut("HT>900 GeV","S1");   
  

  Manager()->AddHisto("HT",10,0,2000); 
  Manager()->AddHisto("HTbis",16,0,2000); 
  
  Manager()->AddHisto("HTeebis",16,0,2000); 
  Manager()->AddHisto("HTmmbis",16,0,2000); 
  Manager()->AddHisto("HTembis",16,0,2000);   
  
  Manager()->AddHisto("pTee",20,0,500); 
  Manager()->AddHisto("pTmm",20,0,500); 
  Manager()->AddHisto("pTem",20,0,500); 
  Manager()->AddHisto("pTlep",20,0,500);   
  
  Manager()->AddHisto("nee",1,0,1); 
  Manager()->AddHisto("nmm",1,0,1); 
  Manager()->AddHisto("nem",1,0,1); 
  
  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_b2g_12_012::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_b2g_12_012::Execute(SampleFormat& sample, const EventFormat& event)
{
  
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else{
    //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
    return false;
  }
  Manager()->InitializeForNewEvent(myEventWeight);
  

  
  if (event.rec()!=0){
    
    // Defining containers
    vector<const RecLeptonFormat*>SignalMuons,SignalElectrons,LooseSignalMuons,LooseSignalElectrons;  
    vector<const RecJetFormat*> SignalJets;
    
    //--------------------------------------------//
    //    Here we collect the various objects     //
    //--------------------------------------------//    
    
    // Electrons with pT>7, |eta|<2.47 
    for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++){
      const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ie]);
      if(CurrentElectron->pt()>30.0 && fabs(CurrentElectron->eta())<2.4){
        SignalElectrons.push_back(CurrentElectron);
      }
      if(CurrentElectron->pt()>15.0 && fabs(CurrentElectron->eta())<2.4){
        LooseSignalElectrons.push_back(CurrentElectron);
      }      
    }
    // We apply a tight isolation criteria to electrons
    SignalElectrons = PHYSICS->Isol->tracker->getRelIsolated(SignalElectrons,event.rec(),0.15,0.3,0.5);
    // We apply a loose isolation criteria to electrons
    LooseSignalElectrons = PHYSICS->Isol->tracker->getRelIsolated(LooseSignalElectrons,event.rec(),0.60,0.3,0.5);
    
    // Muons with pT>6, |eta|<2.5 
    for(unsigned int im=0; im<event.rec()->muons().size(); im++){
    const RecLeptonFormat * CurrentMuon = &(event.rec()->muons()[im]);
      if(CurrentMuon->pt()>30.0 && fabs(CurrentMuon->eta())<2.4){
        SignalMuons.push_back(CurrentMuon);
      }
      if(CurrentMuon->pt()>15.0 && fabs(CurrentMuon->eta())<2.4){
        LooseSignalMuons.push_back(CurrentMuon);
      }  
    }    
    // We apply a tight isolation criteria to muons
    SignalMuons = PHYSICS->Isol->tracker->getRelIsolated(SignalMuons,event.rec(),0.2,0.4,0.5);
    // We apply a loose isolation criteria to muons    
    LooseSignalMuons = PHYSICS->Isol->tracker->getRelIsolated(LooseSignalMuons,event.rec(),0.4,0.4,0.5);
    
    // Jets with pT > 30, |eta|< 2.4 
    for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++){
      const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
      if ( CurrentJet->pt() > 30.0 && fabs(CurrentJet->eta()) < 2.4){
        SignalJets.push_back(CurrentJet);
      }
    }    
    
    // We perform an overlap removal between jets and leptons
    SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, SignalElectrons, 0.3);
    SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, SignalMuons, 0.3);
    
    
    //----------------------------------------------//
    // 		HERE THE CUTFLOW STARTS             //
    //----------------------------------------------//
    
    // Here we check how many tight lepton of each charge we have
    vector<const RecLeptonFormat*>PosElectrons,PosMuons,NegElectrons,NegMuons;

    
    for(unsigned int ie=0;ie<SignalElectrons.size();ie++){
      if(SignalElectrons[ie]->charge()>0){
	PosElectrons.push_back(SignalElectrons[ie]);
      }
      if(SignalElectrons[ie]->charge()<0){
	NegElectrons.push_back(SignalElectrons[ie]);
      }      
    }
    for(unsigned int im=0;im<SignalMuons.size();im++){
      if(SignalMuons[im]->charge()>0){
	PosMuons.push_back(SignalMuons[im]);
      }
      if(SignalMuons[im]->charge()<0){
	NegMuons.push_back(SignalMuons[im]);
      }      
    }    
    
    // This will be needed to understand which SS pair we have (ee,emu or mumu)
    double PT1steP=0.0;
    double PT2ndeP=0.0;
    if(PosElectrons.size()>0){
      PT1steP=PosElectrons[0]->pt();
      if(PosElectrons.size()>1){
	PT2ndeP=PosElectrons[1]->pt();
      }
    }
    double PT1steN=0.0;
    double PT2ndeN=0.0;
    if(NegElectrons.size()>0){
      PT1steN=NegElectrons[0]->pt();
      if(NegElectrons.size()>1){
	PT2ndeN=NegElectrons[1]->pt();
      }
    }     
    double PT1stmP=0.0;
    double PT2ndmP=0.0;
    if(PosMuons.size()>0){
      PT1stmP=PosMuons[0]->pt();
      if(PosMuons.size()>1){
	PT2ndmP=PosMuons[1]->pt();
      }
    }  
    double PT1stmN=0.0;
    double PT2ndmN=0.0;
    if(NegMuons.size()>0){
      PT1stmN=NegMuons[0]->pt();
      if(NegMuons.size()>1){
	PT2ndmN=NegMuons[1]->pt();
      }
    }    
    
    // SR cut 1.
    if(!Manager()->ApplyCut((PosElectrons.size()+PosMuons.size())>1 || (NegElectrons.size()+NegMuons.size())>1,"2SS leptons")){
      return true;    
    } 
    
    // Here we have at least 1 SS pair. Now we need to disentangle which flavour pair we have   
    unsigned int nlep=0;
    unsigned int nposlep=0;
    unsigned int nneglep=0;
    
    nlep=PosElectrons.size()+NegElectrons.size()+PosMuons.size()+NegMuons.size();    
    nposlep=PosElectrons.size()+PosMuons.size();
    nneglep=NegElectrons.size()+NegMuons.size(); 
    
    bool ePeP=false;
    bool ePmP=false;    
    bool mPmP=false;        

    
    bool eNeN=false;
    bool eNmN=false;    
    bool mNmN=false;     
    
    
    // if 2 leptons this is necessary just only one SS pair, easy case to disentangle ee, \mu\mu and e\mu case
    if(nlep==2){
      if(PosElectrons.size()==2){
	ePeP=true;
      }
      else if(NegElectrons.size()==2){
	eNeN=true;
      }      
      else if(PosMuons.size()==2){
	mPmP=true;
      }
      else if(NegMuons.size()==2){
	mNmN=true;
      }  
      else if(PosElectrons.size()==1 && PosMuons.size()==1){
	ePmP=true;
      }    
      else if(NegElectrons.size()==1 && NegMuons.size()==1){
	eNmN=true;
      }        
    }
    // If more than 2 leptons there can be more cases
    
    // In this case the sign of the SS pair is ++, need to decide if ee,mm or emu
    if(nposlep>=2 && nneglep<=1){
      if(PT1steP>PT1stmP){
	if(PT2ndeP > PT1stmP){
	  ePeP = true; 
	}
	else{
	  ePmP=true; 
	}
      }
      if(PT1stmP>PT1steP){
	if(PT2ndmP > PT1steP){
	  mPmP = true; 
	}
	else{
	  ePmP=true; 
	}
      }      
    }
    // In this case the sign of the SS pair is --, need to decide if ee,mm or emu
    if(nneglep>=2 && nposlep<=1){
      if(PT1steN>PT1stmN){
	if(PT2ndeN > PT1stmN){
	  eNeN = true; 
	}
	else{
	  eNmN=true; 
	}
      }
      if(PT1stmN>PT1steN){
	if(PT2ndmN > PT1steN){
	  mNmN = true; 
	}
	else{
	  eNmN=true; 
	}
      }      
    }    
    // In case where more than two positive and two negative leptons are present, we need to check more
    if(nposlep>=2 && nneglep>=2){
      if(max(PT1steP,PT1stmP)>max(PT1steN,PT1stmN)){
	// in this case the SS pair is ++
        if(PT1steP>PT1stmP){
	  if(PT2ndeP > PT1stmP){
	    ePeP = true; 
	  }
	  else{
	    ePmP=true; 
	  }
        }
        if(PT1stmP>PT1steP){
	  if(PT2ndmP > PT1steP){
	    mPmP = true; 
	  }
	  else{
	    ePmP=true; 
	  }
        }  	
      } 
      if(max(PT1steP,PT1stmP)<max(PT1steN,PT1stmN)){
      // in this case the SS pair is --
        if(PT1steN>PT1stmN){
	  if(PT2ndeN > PT1stmN){
	    eNeN = true; 
          }
	  else{
	    eNmN=true; 
	  }
        }
        if(PT1stmN>PT1steN){
	  if(PT2ndmN > PT1steN){
	    mNmN = true; 
	  }
	  else{
	    eNmN=true; 
	  }
        }  	
      }
    }

    
    // Z boson veto only on the dielectron sample
    double mee=0.0;    
    if(ePeP){
      mee=(PosElectrons[0]->momentum()+PosElectrons[1]->momentum()).M();
    }
    if(eNeN){
      mee=(NegElectrons[0]->momentum()+NegElectrons[1]->momentum()).M();     
    }
//     
    // SR cut 2.
    if(!Manager()->ApplyCut(mee<76.0 || mee>106.0,"Z veto")){
      return true;    
    }    
    // This cut is applied so as we can check some distribution made after the >=2 Jets requirement and reported on the twiki web page https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsB2G12012 and on the hepdata web page http://hepdata.cedar.ac.uk/view/ins1268328
    if(!Manager()->ApplyCut(SignalJets.size()>=2,">=2 jets")){
      return true;    
    }       
    
    // Here we compute HT that is needed to reproduce some exp. plots.
    double HT=0;
    
    for(unsigned int ij=0; ij<SignalJets.size();ij++){
       HT=HT+SignalJets[ij]->pt(); 
    }
    for(unsigned int ie=0; ie<SignalElectrons.size();ie++){
       HT=HT+SignalElectrons[ie]->pt(); 
    }
    for(unsigned int im=0; im<SignalMuons.size();im++){
       HT=HT+SignalMuons[im]->pt(); 
    }     
    
    
    Manager()->FillHisto("HTbis",HT); 
    
    if(ePeP){
      Manager()->FillHisto("pTee",PosElectrons[0]->pt());
      Manager()->FillHisto("pTlep",PosElectrons[0]->pt());
      Manager()->FillHisto("HTeebis",HT);
    }
    if(eNeN){
      Manager()->FillHisto("pTee",NegElectrons[0]->pt());
      Manager()->FillHisto("pTlep",NegElectrons[0]->pt()); 
      Manager()->FillHisto("HTeebis",HT);      
    }

    if(mPmP){
      Manager()->FillHisto("pTmm",PosMuons[0]->pt());
      Manager()->FillHisto("pTlep",PosMuons[0]->pt());  
      Manager()->FillHisto("HTmmbis",HT);    
    }
    if(mNmN){
      Manager()->FillHisto("pTmm",NegMuons[0]->pt());
      Manager()->FillHisto("pTlep",NegMuons[0]->pt());   
      Manager()->FillHisto("HTmmbis",HT);  
    }
    
    if(ePmP){
      if(PT1steP>PT1stmP){
        Manager()->FillHisto("pTem",PosElectrons[0]->pt());
	Manager()->FillHisto("pTlep",PosElectrons[0]->pt());
        Manager()->FillHisto("HTembis",HT);
      }
      else {
        Manager()->FillHisto("pTem",PosMuons[0]->pt());
	Manager()->FillHisto("pTlep",PosMuons[0]->pt());
	Manager()->FillHisto("HTembis",HT);
      }
    }


    if(eNmN){
      if(PT1steN>PT1stmN){
        Manager()->FillHisto("pTem",NegElectrons[0]->pt());
	Manager()->FillHisto("pTlep",NegElectrons[0]->pt());
	Manager()->FillHisto("HTembis",HT);
      }
      else {
        Manager()->FillHisto("pTem",NegMuons[0]->pt());
	Manager()->FillHisto("pTlep",NegMuons[0]->pt());
	Manager()->FillHisto("HTembis",HT);
      }
    }    
     
   // Trilepton veto     
    double mll=0;
    bool mllveto = true;
    
    if(ePeP){
      for(unsigned int ie=0;ie<PosElectrons.size();ie++){
 	for(unsigned int iel=0;iel<LooseSignalElectrons.size();iel++){
	  if(PosElectrons[ie]->charge()*LooseSignalElectrons[iel]->charge()<0){
	    mll=(PosElectrons[ie]->momentum()+LooseSignalElectrons[iel]->momentum()).M();
	    if(mll>76.0 && mll<106.00){
              mllveto = false;
              break;	    
	    }
	  }	  
	}
      }
    }
    if(eNeN){
      for(unsigned int ie=0;ie<NegElectrons.size();ie++){
 	for(unsigned int iel=0;iel<LooseSignalElectrons.size();iel++){
	  if(NegElectrons[ie]->charge()*LooseSignalElectrons[iel]->charge()<0){
	    mll=(NegElectrons[ie]->momentum()+LooseSignalElectrons[iel]->momentum()).M();
	    if(mll>76.0 && mll<106.00){
              mllveto = false;
              break;	    
	    }
	  }	  
	}
      }
    }    
    if(mPmP){
      for(unsigned int im=0;im<PosMuons.size();im++){
 	for(unsigned int iml=0;iml<LooseSignalMuons.size();iml++){
	  if(PosMuons[im]->charge()*LooseSignalMuons[iml]->charge()<0){
	    mll=(PosMuons[im]->momentum()+LooseSignalMuons[iml]->momentum()).M();
	    if(mll>76.0 && mll<106.00){
              mllveto = false;
              break;	    
	    }
	  }	  
	}
      }
    }    
    if(mNmN){
      for(unsigned int im=0;im<NegMuons.size();im++){
 	for(unsigned int iml=0;iml<LooseSignalMuons.size();iml++){
	  if(NegMuons[im]->charge()*LooseSignalMuons[iml]->charge()<0){
	    mll=(NegMuons[im]->momentum()+LooseSignalMuons[iml]->momentum()).M();
	    if(mll>76.0 && mll<106.00){
              mllveto = false;
              break;	    
	    }
	  }	  
	}
      }
    }       
    if(ePmP){
      for(unsigned int iel=0;iel<LooseSignalElectrons.size();iel++){
        if(PosElectrons[0]->charge()*LooseSignalElectrons[iel]->charge()<0){
	  mll=(PosElectrons[0]->momentum()+LooseSignalElectrons[iel]->momentum()).M();
	  if(mll>76.0 && mll<106.00){
            mllveto = false;
            break;	    
	  }
	}	  
      }
      for(unsigned int iml=0;iml<LooseSignalMuons.size();iml++){
        if(PosMuons[0]->charge()*LooseSignalMuons[iml]->charge()<0){
	  mll=(PosMuons[0]->momentum()+LooseSignalMuons[iml]->momentum()).M();
	  if(mll>76.0 && mll<106.00){
            mllveto = false;
            break;	    
	  }
	}	  
      }  	
    }
    if(eNmN){
      for(unsigned int iel=0;iel<LooseSignalElectrons.size();iel++){
        if(NegElectrons[0]->charge()*LooseSignalElectrons[iel]->charge()<0){
	  mll=(NegElectrons[0]->momentum()+LooseSignalElectrons[iel]->momentum()).M();
	  if(mll>76.0 && mll<106.00){
            mllveto = false;
            break;	    
	  }
	}	  
      }
      for(unsigned int iml=0;iml<LooseSignalMuons.size();iml++){
        if(NegMuons[0]->charge()*LooseSignalMuons[iml]->charge()<0){
	  mll=(NegMuons[0]->momentum()+LooseSignalMuons[iml]->momentum()).M();
	  if(mll>76.0 && mll<106.00){
            mllveto = false;
            break;	    
	  }
	}	  
      }  	
    }    
    
    // SR cut 3.
    if(!Manager()->ApplyCut(mllveto,"3l veto")){
      return true;    
    } 
    // SR cut 4.
    if(!Manager()->ApplyCut(SignalJets.size()+SignalElectrons.size()+SignalMuons.size()>6,">=7 Const.")){
      return true;    
    } 
 
    // This reproduce Fig.1 of the published paper
    Manager()->FillHisto("HT",HT); 
    // SR cut 5.
    if(!Manager()->ApplyCut(HT>900,"HT>900 GeV")){
      return true;    
    }     
    
    
    // This fake histogram give us the number of events in all the categories to be compared with Tab.I of the published paper
    if(ePeP || eNeN){
      Manager()->FillHisto("nee",1);    
    }
    if(mPmP || mNmN){
      Manager()->FillHisto("nmm",1);    
    }
    if(ePmP || eNmN){
      Manager()->FillHisto("nem",1);    
    }

  }// end of loop into an event

  return true;
}

