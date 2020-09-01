#include "SampleAnalyzer/User/Analyzer/atlas_exot_2016_32.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_exot_2016_32::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: ATLAS_EXOT_2016 (arXiv:1704.03848)      <>" << endmsg;
  INFO << "        <>              (Monophoton)                            <>" << endmsg;
  INFO << "        <>    Recasted by: Seungwon Baek, Tae Hyun Jung         <>" << endmsg;
  INFO << "        <>    Contact: swbaek@kias.re.kr, thjung0720@ibs.re.kr  <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.1.11                    <>" << endmsg;
  INFO << "        <>    For more information, see                         <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/           <>" << endmsg;
  INFO << "        <>    /PhysicsAnalysisDatabase                          <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Declaring signal region(s)
  // This analysis has five signal region
    Manager()->AddRegionSelection("SRI1");
    Manager()->AddRegionSelection("SRI2");
    Manager()->AddRegionSelection("SRI3");
    Manager()->AddRegionSelection("SRE1");
    Manager()->AddRegionSelection("SRE2");
  //----------------------------------------------//
  //              CUT FLOW                        //
  //       (in the order of Tab.1 of the          //
  //        aux material available at             //
  //        https://atlas.web.cern.ch/Atlas/      //
  //        GROUPS/PHYSICS/PAPERS/EXOT-2014-06/)  //
  //----------------------------------------------//  
  
  // Signal regions cuts

  Manager()->AddCut("MET>150 GeV","SRI1");  
  Manager()->AddCut("MET>225 GeV","SRI2");  
  Manager()->AddCut("MET>300 GeV","SRI3");  
  Manager()->AddCut("225>MET>150 GeV","SRE1");  
  Manager()->AddCut("300>MET>225 GeV","SRE2"); 
  Manager()->AddCut("1+ photon, pT>150, |eta|<2.37");  
  Manager()->AddCut("Tight leading photon |eta|<1.37"); 
  Manager()->AddCut("DPhi(leading photon,MET)>0.4");
  Manager()->AddCut("MET/sqrt(MET)>8.5 GeV^1/2");
  Manager()->AddCut("Njet<2 and DPhi(jet,MET)>0.4"); 
  Manager()->AddCut("Lepton veto"); 


 
  return true;
  
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_exot_2016_32::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_exot_2016_32::Execute(SampleFormat& sample, const EventFormat& event)
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
   
    // Finding MET //It is not the definition that used in the paper.. Later, met will be defined properly.
    MALorentzVector pTmiss = event.rec()->MET().momentum();

    //--------------------------------------------//
    //    Here we collect the various objects     //
    //--------------------------------------------//

    // Photons with pT>10, |eta|<2.37 taking into account the crack into the detector between 1.37 < |eta| < 1.52
    for(unsigned int ia=0; ia<event.rec()->photons().size(); ia++){
      const RecPhotonFormat * CurrentPhoton = &(event.rec()->photons()[ia]);
      if(CurrentPhoton->pt()>10.0  && (fabs(CurrentPhoton->eta())<1.37 || (fabs(CurrentPhoton->eta())>1.52 && fabs(CurrentPhoton->eta())<2.37))){
        SignalPhotons.push_back(CurrentPhoton);
      }
    }
    // We then apply an isolation (tight).    
    for(int ii=SignalPhotons.size()-1;ii>=0;ii--){     

        double iso_var1 = PHYSICS->Isol->calorimeter->sumIsolation(SignalPhotons[ii],event.rec(),0.4,0.);
        double iso_var2 = PHYSICS->Isol->tracker->sumIsolation(SignalPhotons[ii],event.rec(),0.2,0.);
	  if(iso_var1>2.45+0.022*SignalPhotons[ii]->pt() || iso_var2>0.05 * SignalPhotons[ii]->pt()){
            SignalPhotons.erase(SignalPhotons.begin()+ii);
          }
      
    }

   
    // Electrons with pT>7, |eta|<2.47
    for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++){
      const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ie]);
      if(CurrentElectron->pt()>7.0 && fabs(CurrentElectron->eta())<2.47){
        SignalElectrons.push_back(CurrentElectron);	 
      }
    }
    // We then apply a loose isolation to remove non-prompt electrons    
    for(int ii=SignalElectrons.size()-1;ii>=0;ii--){     
      for(unsigned int jj=0; jj<SignalElectrons[ii]->isolCones().size(); jj++){
        if(fabs(SignalElectrons[ii]->isolCones()[jj].deltaR() - 0.2) < 0.001){
          if(SignalElectrons[ii]->isolCones()[jj].sumPT() > 0.2*SignalElectrons[ii]->pt()){   
            SignalElectrons.erase(SignalElectrons.begin()+ii);
          }
        }
      }
    }    
    
    // Muons with pT>6, |eta|<2.5
    for(unsigned int im=0; im<event.rec()->muons().size(); im++){
    const RecLeptonFormat * CurrentMuon = &(event.rec()->muons()[im]);
      if(CurrentMuon->pt()>6.0 && fabs(CurrentMuon->eta())<2.5){
        SignalMuons.push_back(CurrentMuon);	 
      }
    }   
 


    // Jets with pT > 30, |eta|< 4.5
    for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++){
      const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
      if ( CurrentJet->pt() > 30.0 && fabs(CurrentJet->eta()) < 4.5){
        SignalJets.push_back(CurrentJet);
      }
    }


	MALorentzVector met_vec = MALorentzVector();
	MALorentzVector CPhoton;
	MALorentzVector CElectron;
	MALorentzVector CMuon;
	MALorentzVector CJet;

// Defining met properly. met is obtained from negative vector sum of 
//the momenta of candidate physics objects, selected as described above. (p8 of the paper)

// Important : Tracks from the primary vertex not associated with any such objects 
//            are not included unlike what paper did. (p8 of the paper)

// met_scalar (sum ET in the paper p.9) is calculated as the scalar sum of all pT from objects 
//and the tracks contributing to the met reconstruction described above.

    double met_scalar = 0.0;

    for(int ii=SignalPhotons.size()-1;ii>=0;ii--){   
     CPhoton.SetPtEtaPhiE
       (SignalPhotons[ii]->momentum().Pt(), SignalPhotons[ii]->momentum().Eta(),
        SignalPhotons[ii]->momentum().Phi(), SignalPhotons[ii]->momentum().E());
     
     met_vec = met_vec - CPhoton;
     met_scalar = met_scalar + CPhoton.Pt();
	}

    for(int ii=SignalMuons.size()-1;ii>=0;ii--){ 
     CMuon.SetPtEtaPhiE
       (SignalMuons[ii]->momentum().Pt(), SignalMuons[ii]->momentum().Eta(),
        SignalMuons[ii]->momentum().Phi(), SignalMuons[ii]->momentum().E());

     met_vec = met_vec - CMuon;
     met_scalar = met_scalar + CMuon.Pt();
	}

    for(int ii=SignalElectrons.size()-1;ii>=0;ii--){ 
     CElectron.SetPtEtaPhiE
       (SignalElectrons[ii]->momentum().Pt(), SignalElectrons[ii]->momentum().Eta(),
        SignalElectrons[ii]->momentum().Phi(), SignalElectrons[ii]->momentum().E());

     met_vec = met_vec - CElectron;
     met_scalar = met_scalar + CElectron.Pt();
	}

    for(int ii=SignalJets.size()-1;ii>=0;ii--){ 
     CJet.SetPtEtaPhiE
       (SignalJets[ii]->momentum().Pt(), SignalJets[ii]->momentum().Eta(),
        SignalJets[ii]->momentum().Phi(), SignalJets[ii]->momentum().E());

     met_vec = met_vec - CJet;
     met_scalar = met_scalar + CJet.Pt();
	}



    double met = met_vec.Pt();
//    cout<< "met/MET=" << met <<"/" << MET << "=" << met/MET <<endl;

 
    //-------------------------------------//
    //     Here the cut flow starts        //
    //-------------------------------------//
    
    // We want to reproduce the good vertex and cleaning cuts present in the event pre-selection from which
    // in the provided cut flow, the pass from 8582 to 8213 events.
    // Since is not possible to reproduce this within a fast detector simulation we scale our events for that ratio, while 
    // while applying also the first Signal Region cut.
    // In this way one however is not sensitive to any model dependency of this Pre-selection requirements
   
//    double preselection=9466.0/10000.0;   

//    Manager()->SetCurrentEventWeight(preselection);

//MET>150
    // SRI1 cut.
    if(!Manager()->ApplyCut((met > 150.),"MET>150 GeV")){
      return true;    
    }
    // SRI2 cut.
    if(!Manager()->ApplyCut((met > 225.),"MET>225 GeV")){
      return true;    
    }
    // SRI3 cut.
    if(!Manager()->ApplyCut((met > 300.),"MET>300 GeV")){
      return true;    
    }
    // SRE1 cut.
    if(!Manager()->ApplyCut((met > 150. && met < 255.),"225>MET>150 GeV")){
      return true;    
    }
    // SRE2 cut.
    if(!Manager()->ApplyCut((met > 225. && met < 300),"300>MET>225 GeV")){
      return true;    
    }
  

// At least one photon, pT>150, |eta|<2.37
    // Note that |eta|<2.37 is already satisfied
   
    if(!Manager()->ApplyCut(SignalPhotons.size()>0 && SignalPhotons[0]->pt()>150 ,"1+ photon, pT>150, |eta|<2.37")){     
      return true;    
    }

//z0
   
    // A tight photon has further requirement. The efficiency is about 90 % for E above 125, so reweigh by hand
    // (https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/EGAMMA/PublicPlots/20140611/ATL-COM-PHYS-2014-542/ATL-COM-PHYS-2014-542.pdf)
    double tight=myEventWeight*0.9;
    Manager()->SetCurrentEventWeight(tight);
    
// tight photon
    if(!Manager()->ApplyCut(fabs(SignalPhotons[0]->eta())<1.37,"Tight leading photon |eta|<1.37")){
      return true; 
    }  

//isolation already done


//delta phi gamma met.
    if(!Manager()->ApplyCut((SignalPhotons[0]->dphi_0_pi(pTmiss))>0.4,"DPhi(leading photon,MET)>0.4")){
      return true;  
    }     

// MET/sqrtMET cut 8.5GeV^1/2
    if(!Manager()->ApplyCut(met / sqrt(met_scalar) > 8.5,"MET/sqrt(MET)>8.5 GeV^1/2")){
      return true;  
    }  

//Jet veto    
    // Next we want jets with distance deltaR>0.2 to the closes preselected electron or photon,
    // otherwise they will be discarded. As for the implementation of cms_sus_13_011 note that in other analyses
    // it's common to see electrons discarded if they're too close to jets; not here.
    bool do_erase = false;
    for(int ii=SignalJets.size()-1; ii>=0; ii--){
      for(unsigned int jj=0; jj<SignalElectrons.size(); jj++){
        if(SignalJets[ii]->dr(SignalElectrons[jj]) < 0.2){
          do_erase = true;
          break;
        }
      }
      for(unsigned int jj=0; jj<SignalPhotons.size(); jj++){
        if(SignalJets[ii]->dr(SignalPhotons[jj]) < 0.2){
          do_erase = true;
          break;
        }
      }
      if(do_erase){
        SignalJets.erase(SignalJets.begin()+ii);
        do_erase = false;
      }
    }   

    if(!Manager()->ApplyCut((SignalJets.size()==0)||(SignalJets.size()==1 && (SignalJets[0]->dphi_0_pi(pTmiss))>0.4) ,"Njet<2 and DPhi(jet,MET)>0.4")){
     return true;
    }


//Lepton veto

    // Searching for lepton which will cause a veto   
    bool lepton_veto = true;
    if(SignalElectrons.size()>0 || SignalMuons.size()>0){
      lepton_veto = false; 
    }
    
    if(!Manager()->ApplyCut(lepton_veto ,"Lepton veto")){
      return true;
    }


   



  }// end loop on events
  return true;
}

