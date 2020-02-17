#include "SampleAnalyzer/User/Analyzer/cms_sus_16_033.h"
using namespace MA5;
using namespace std;

bool cms_sus_16_033::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: cms_sus_16_033                <>" << endmsg;
  INFO << "        <>    Multijet,HT,MHT = 13 TeV, 35.9 fb^-1 luminosity  <>" << endmsg;
  INFO << "        <>    Recast by: F. Ambrogi, J.Sonneveld  <>" << endmsg;
  INFO << "        <>    Contact: federico.ambrogi88@gmail.com , jory.sonneveld@desy.de <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.5 and above <>" << endmsg;
  INFO << "        <>    For more information, see             <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase <>" << endmsg;
  
 // Define the 12 aggregated signal region
  Manager()->AddRegionSelection("SR1_Njet2_Nb0_HT500_MHT500" );
  Manager()->AddRegionSelection("SR2_Njet3_Nb0_HT1500_MHT750");
  Manager()->AddRegionSelection("SR3_Njet5_Nb0_HT500_MHT_500");
  Manager()->AddRegionSelection("SR4_Njet5_Nb0_HT1500_MHT750");
  Manager()->AddRegionSelection("SR5_Njet9_Nb0_HT1500_MHT750");
  Manager()->AddRegionSelection("SR6_Njet2_Nb2_HT500_MHT500" );
  Manager()->AddRegionSelection("SR7_Njet3_Nb1_HT750_MHT750" );
  Manager()->AddRegionSelection("SR8_Njet5_Nb3_HT500_MHT500" );
  Manager()->AddRegionSelection("SR9_NJet5_Nb2_HT1500_MHT750");
  Manager()->AddRegionSelection("SR10_Njet9_Nb3_HT750_MHT750");
  Manager()->AddRegionSelection("SR11_Njet7_Nb1_HT300_MHT300");
  Manager()->AddRegionSelection("SR12_Njet5_Nb1_HT750_MHT750");

  // Define the preselection cuts (not including Jet,Nb,HT,MHT binnings)
  Manager()->AddCut("Njet>=2")           ; // more or equal 2 jets with |eta|<2.4
  Manager()->AddCut("HT>300")            ; // HT = scalar sum of jets pt>30 GeV 
  Manager()->AddCut("MHT>300")           ; // HTM = magnitude of the the vector HTMiss, i.e. negative of the vector sum of all jets pt within |eta|<5 
  Manager()->AddCut("NoIsoMuons")        ; // No isolated muons with pt>10 GeV
  Manager()->AddCut("NoMuonsTracks")     ; // No isolated muons tracks 
  Manager()->AddCut("NoIsoElectrons")    ; // No isolated electron with pt>10 GeV                                                                                                                   
  Manager()->AddCut("NoElectronsTracks") ; // No isolated electron tracks                                                                                                              
  Manager()->AddCut("NoIsoTracks")       ; // no isolated tracks with mT<100 GeV and pT>10 GeV
                                           // (pT > 5 GeV if track is a PF electron or muon)
                                           // mT = transverse mass formed with the pTmiss (all pT of the PF objects) and the iso track

  Manager()->AddCut("DPhi(MHTj1)>0.5") ; // Azimutal angle between MHT and the pT of the 'i' jet
  Manager()->AddCut("DPhi(MHTj2)>0.5") ;  
  Manager()->AddCut("DPhi(MHTj3)>0.3") ;
  Manager()->AddCut("DPhi(MHTj4)>0.3") ;

  // Jets multiplicity selection

  Manager()->AddCut("SR1_Njet2_Nb0_HT500_MHT500" ,"SR1_Njet2_Nb0_HT500_MHT500");
  Manager()->AddCut("SR2_Njet3_Nb0_HT1500_MHT750","SR2_Njet3_Nb0_HT1500_MHT750");
  Manager()->AddCut("SR3_Njet5_Nb0_HT500_MHT_500","SR3_Njet5_Nb0_HT500_MHT_500");
  Manager()->AddCut("SR4_Njet5_Nb0_HT1500_MHT750","SR4_Njet5_Nb0_HT1500_MHT750");
  Manager()->AddCut("SR5_Njet9_Nb0_HT1500_MHT750","SR5_Njet9_Nb0_HT1500_MHT750");
  Manager()->AddCut("SR6_Njet2_Nb2_HT500_MHT500" ,"SR6_Njet2_Nb2_HT500_MHT500");
  Manager()->AddCut("SR7_Njet3_Nb1_HT750_MHT750" ,"SR7_Njet3_Nb1_HT750_MHT750");
  Manager()->AddCut("SR8_Njet5_Nb3_HT500_MHT500" ,"SR8_Njet5_Nb3_HT500_MHT500");
  Manager()->AddCut("SR9_NJet5_Nb2_HT1500_MHT750","SR9_NJet5_Nb2_HT1500_MHT750");
  Manager()->AddCut("SR10_Njet9_Nb3_HT750_MHT750","SR10_Njet9_Nb3_HT750_MHT750");
  Manager()->AddCut("SR11_Njet7_Nb1_HT300_MHT300","SR11_Njet7_Nb1_HT300_MHT300");
  Manager()->AddCut("SR12_Njet5_Nb1_HT750_MHT750","SR12_Njet5_Nb1_HT750_MHT750");

  
  // ********* Kinematic Distributions for the points in the supplementary material )                                                                               

  Manager()->AddHisto("nJets_Pre", 11,0,11);
  Manager()->AddHisto("bJets_Pre", 5,0,5);
  Manager()->AddHisto("HT_Pre"   , 40,0,3000);
  Manager()->AddHisto("MHT_Pre"  , 30,0,1500);

  return true;
}


// Finalize ==================================================                  
// function called one time at the end of the analysis =======
// ==========================================================
void cms_sus_16_033::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  cout << "END   Finalization" << endl;
  return;
}


bool cms_sus_16_033::Execute(SampleFormat& sample, const EventFormat& event)
{
  

  if (event.rec()!=0)
   {

     
    double myEventWeight;
    if(Configuration().IsNoEventWeight()) myEventWeight=1.;
    else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
    else 
    { //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
    return false;	}
    

     //double myEventWeight = 1; 

    Manager()->InitializeForNewEvent(myEventWeight); 
    vector<const RecLeptonFormat*> electrons, muons, isoElectrons, isoMuons    ; // isolated electrons and muons (probably non isolated are not necessary...) 
    vector<const RecJetFormat*>    signalJets, bJets, jetsLargeEta             ; // jets, bjets, large eta jets
    vector<const RecTrackFormat*>  electronIsoTracks, muonIsoTracks, isoTracks ; // tracks, tracks identified as electons, and as muons
    
// **********************************************
// **** Objects Selection and Reconstruction ****   
// **********************************************

    // Selecting muons
    for(unsigned int i=0; i<event.rec()->muons().size(); i++)
    {  const RecLeptonFormat *thisMuon = &(event.rec()->muons()[i]);
      double pt = thisMuon->pt() , eta =  thisMuon->momentum().Eta() ;
      if (!(pt>10 and fabs(eta) < 2.4)) continue;
      muons.push_back(thisMuon);
      double IsoCone    = Determine_DeltaR(thisMuon);         // selecting the proper Radius
      double All        = PHYSICS->Isol->eflow->sumIsolation(thisMuon,event.rec() , IsoCone ,0.,IsolationEFlow::ALL_COMPONENTS);
      double Isolation     = (All)/pt ;
      if (Isolation < 0.2) { isoMuons.push_back(thisMuon); }
     }
 
    // Selecting electrons
    for(unsigned int i=0; i<event.rec()->electrons().size(); i++)
      {  const RecLeptonFormat *thisElectron = &(event.rec()->electrons()[i]);
	double pt = thisElectron->pt() , eta =  thisElectron->momentum().Eta() ;
	if (!(pt>10 and fabs(eta) < 2.5)) continue;
	electrons.push_back(thisElectron);
        double IsoCone    = Determine_DeltaR(thisElectron);         // selecting the proper Radius                                                        
        double All        = PHYSICS->Isol->eflow->sumIsolation(thisElectron,event.rec() , IsoCone ,0.,IsolationEFlow::ALL_COMPONENTS);
        double Isolation  = All/pt;

	if (Isolation < 0.1) { isoElectrons.push_back(thisElectron); } }


    // Selecting tracks
	for(unsigned int i=0; i<event.rec()->tracks().size(); i++)
      {  const RecTrackFormat *thisTrack = &(event.rec()->tracks()[i]);
	double pt = thisTrack->momentum().Pt() , eta =  thisTrack->momentum().Eta() , mT = thisTrack->mt_met(event.rec()->MET().momentum());
	if(!(fabs(eta) < 2.4)) continue;  // selecting tracks pT,eta
	
	int particleId    =  thisTrack->pdgid() ; // here I identify if the track is an electron or a muon, since this gives different iso requirements    
	bool isElectron   = ( particleId== 11 or particleId == -11) ;
	bool isMuon       = ( particleId== 13 or particleId == -13) ;                                               
	double IsoCone    = 0.3 ;
	double ChargedSum = PHYSICS->Isol->eflow->sumIsolation(thisTrack,event.rec() , IsoCone ,0.,IsolationEFlow::TRACK_COMPONENT) / pt;
        if      ( isElectron and pt > 5   and mT < 100 and ChargedSum < 0.2 )       // selecting isolated electrons tracks    
	        { electronIsoTracks.push_back(thisTrack); }
        if      ( isMuon     and pt > 5   and mT < 100 and ChargedSum < 0.2 )
	        { muonIsoTracks.push_back(thisTrack); }   
        if      ( !(isMuon or isElectron) and  pt > 10 and mT < 100 and ChargedSum < 0.1)
		  {isoTracks.push_back(thisTrack); }                                                  

      }

    // Selecting JETS
    for(unsigned int i=0; i<event.rec()->jets().size(); i++)
    {  const RecJetFormat *thisJet= &(event.rec()->jets()[i]);
       double pT = thisJet->momentum().Pt() , eta =  thisJet->momentum().Eta() ;
       if (pT > 30 and fabs(eta) < 5   )  {jetsLargeEta.push_back(thisJet) ;} // this extended eta range will be used to calculate MHT     
       if (pT > 30 and fabs(eta) < 2.4 )
          { signalJets.push_back(thisJet);
            if (thisJet->btag()) { bJets.push_back(thisJet); }
          }
     }
    
    SORTER->sort(signalJets);
    SORTER->sort(jetsLargeEta);
    SORTER->sort(bJets);
    SORTER->sort(isoMuons);
    SORTER->sort(isoElectrons);

    signalJets   = Removal(signalJets, isoMuons,  0.2);
    signalJets   = Removal(signalJets, isoElectrons,  0.2);
   
  
// *******************************************************
// Preselection Cuts 
// *******************************************************

// Defining the kinematic variables    
   int nb = bJets.size();
   int nJets = signalJets.size();
   //   cout << "Njets" << nJets << endl;

    // Calculate the HT
    double HT = 0;
    for(unsigned int j = 0; j < signalJets.size(); j++)
      {
        HT += signalJets[j]->momentum().Pt();
      }
    // Calculate the MHT
    double MHT = 0;
    MALorentzVector VectorMHT = MALorentzVector();
    MALorentzVector CurrentJet;
    for(unsigned int j = 0; j < jetsLargeEta.size(); j++)
      {
        CurrentJet.SetPtEtaPhiE
          (jetsLargeEta[j]->momentum().Pt(), jetsLargeEta[j]->momentum().Eta(),
           jetsLargeEta[j]->momentum().Phi(),jetsLargeEta[j]->momentum().E());
        VectorMHT -= CurrentJet;
      }
    MHT = VectorMHT.Pt();



   double DeltaPhi_j1MHT , DeltaPhi_j2MHT , DeltaPhi_j3MHT , DeltaPhi_j4MHT ;

   MALorentzVector jet1 = MALorentzVector();
   MALorentzVector jet2 = MALorentzVector();
   MALorentzVector jet3 = MALorentzVector();
   MALorentzVector jet4 = MALorentzVector();

   // Calculating the DeltaPhi.
   // Since the preselection requires certain vales of DPhi based on different number of jets,
   // the DPhi for j3 and j4 assume the required values for passing the cut, so that if in the event there are less than 3 and 4 jets, the cut on the 3rd and 4th jets has no effect
   if ( nJets >= 1 ) { jet1.SetPtEtaPhiE (signalJets[0]->momentum().Pt(), signalJets[0]->momentum().Eta(), signalJets[0]->momentum().Phi(), signalJets[0]->momentum().E());
                       DeltaPhi_j1MHT = fabs(VectorMHT.DeltaPhi(jet1));  }  
   if ( nJets  < 1 ) { DeltaPhi_j1MHT = 0.5 ; }

   if ( nJets >= 2 ) { jet2.SetPtEtaPhiE (signalJets[1]->momentum().Pt(), signalJets[1]->momentum().Eta(), signalJets[1]->momentum().Phi(), signalJets[1]->momentum().E());
                       DeltaPhi_j2MHT = fabs(VectorMHT.DeltaPhi(jet2));  }
   if ( nJets  < 2 ) { DeltaPhi_j2MHT = 0.5 ; }

   if ( nJets >= 3 ) { jet3.SetPtEtaPhiE (signalJets[2]->momentum().Pt(), signalJets[2]->momentum().Eta(), signalJets[2]->momentum().Phi(), signalJets[2]->momentum().E());
                       DeltaPhi_j3MHT = fabs(VectorMHT.DeltaPhi(jet3));  }
   if ( nJets  < 3 ) { DeltaPhi_j3MHT = 0.3 ; }

   if ( nJets >= 4 ) { jet3.SetPtEtaPhiE (signalJets[3]->momentum().Pt(), signalJets[3]->momentum().Eta(), signalJets[3]->momentum().Phi(), signalJets[3]->momentum().E());
                       DeltaPhi_j4MHT = fabs(VectorMHT.DeltaPhi(jet4));  }
   if ( nJets  < 4 ) { DeltaPhi_j4MHT = 0.3 ; }

   bool DPhi_1 = DeltaPhi_j1MHT >= 0.5 ;
   bool DPhi_2 = DeltaPhi_j2MHT >= 0.5 ;
   bool DPhi_3 = DeltaPhi_j3MHT >= 0.3 ;
   bool DPhi_4 = DeltaPhi_j4MHT >= 0.3 ;
   bool DPhi   = DPhi_1 and DPhi_2 and DPhi_3 and DPhi_4 ; // Total condition on DPhi angles

// ******************************************************
// Filling the histograms (for validation) *
// ******************************************************
   
   int isoE = isoElectrons.size(), isoM = isoMuons.size() , isoEtracks = electronIsoTracks.size(), isoMtracks = muonIsoTracks.size() , isoTr = isoTracks.size() ;
   bool Isolation = (isoE == 0 and isoM==0 and isoEtracks == 0 and isoMtracks == 0 and isoTr == 0) ;
   if (Isolation and HT > 300   and MHT > 300 and DPhi                     ) { 
       Manager()->FillHisto("nJets_Pre", nJets ) ;}
   if (Isolation and nJets >=2  and HT  > 300 and MHT >300 and DPhi) { Manager()->FillHisto("bJets_Pre", nb    ) ;}
   if (Isolation and nJets >=2  and MHT > 300              and DPhi) { Manager()->FillHisto("HT_Pre",    HT    ) ;}
   if (Isolation and nJets >=2  and HT  > 300              and DPhi) { Manager()->FillHisto("MHT_Pre",   MHT   ) ;}

// ******************************************************                                                                                                                    
// Applying the preselection cuts *                                                                                          
// ******************************************************
      
// 1) Cut on NJet >= 2                                                                                        
   if(!Manager()->ApplyCut((nJets >= 2),"Njet>=2")) return true;
// 2) Cut on HT > 300
   if(!Manager()->ApplyCut((HT>300),    "HT>300")) return true;  
// 3) Cut on HT > 300
   if(!Manager()->ApplyCut((MHT>300),   "MHT>300")) return true;  
// 4) No isolated muons
//   cout << "how many isol Mu is: " << isoMuons.size() << endl; 
   if(!Manager()->ApplyCut((isoM       == 0),"NoIsoMuons")) return true;
// 5) No isolated muons tracks
   if(!Manager()->ApplyCut((isoMtracks == 0),"NoMuonsTracks")) return true;
// 6) No isolated electrons
   if(!Manager()->ApplyCut((isoE       == 0),"NoIsoElectrons")) return true;
// 7) No electrons tracks
   if(!Manager()->ApplyCut((isoEtracks == 0),"NoElectronsTracks")) return true;
// 8) No hadronic tracks                                                                                                                        
   if(!Manager()->ApplyCut((isoTr      == 0),"NoIsoTracks")) return true;
// 9) DeltaPhi between jets and MHT

   if(!Manager()->ApplyCut(DPhi_1                      , "DPhi(MHTj1)>0.5") ) return true;                                                                                             if(!Manager()->ApplyCut(DPhi_2                      , "DPhi(MHTj2)>0.5") ) return true; 
   if(!Manager()->ApplyCut(DPhi_3                      , "DPhi(MHTj3)>0.3") ) return true;
   if(!Manager()->ApplyCut(DPhi_4                      , "DPhi(MHTj4)>0.3") ) return true;

// ************************************************* 
// Specific cuts for the aggregated Signal Regions *
// *************************************************

   if(!Manager()->ApplyCut(HT > 500  && MHT > 500 && nJets >= 2 && nb == 0, "SR1_Njet2_Nb0_HT500_MHT500"  ) ) return true;
   if(!Manager()->ApplyCut(HT > 1500 && MHT > 750 && nJets >= 3 && nb == 0, "SR2_Njet3_Nb0_HT1500_MHT750" ) ) return true;
   if(!Manager()->ApplyCut(HT > 500  && MHT > 500 && nJets >= 5 && nb == 0, "SR3_Njet5_Nb0_HT500_MHT_500" ) ) return true;
   if(!Manager()->ApplyCut(HT > 1500 && MHT > 750 && nJets >= 5 && nb == 0, "SR4_Njet5_Nb0_HT1500_MHT750" ) ) return true;
   if(!Manager()->ApplyCut(HT > 1500 && MHT > 750 && nJets >= 9 && nb == 0, "SR5_Njet9_Nb0_HT1500_MHT750" ) ) return true;
   if(!Manager()->ApplyCut(HT > 500  && MHT > 500 && nJets >= 2 && nb >= 2, "SR6_Njet2_Nb2_HT500_MHT500"  ) ) return true;
   if(!Manager()->ApplyCut(HT > 750  && MHT > 750 && nJets >= 3 && nb >= 1, "SR7_Njet3_Nb1_HT750_MHT750"  ) ) return true;
   if(!Manager()->ApplyCut(HT > 500  && MHT > 500 && nJets >= 5 && nb >= 3, "SR8_Njet5_Nb3_HT500_MHT500"  ) ) return true;
   if(!Manager()->ApplyCut(HT > 1500 && MHT > 750 && nJets >= 5 && nb >= 2, "SR9_NJet5_Nb2_HT1500_MHT750" ) ) return true;
   if(!Manager()->ApplyCut(HT > 750  && MHT > 750 && nJets >= 9 && nb >= 3, "SR10_Njet9_Nb3_HT750_MHT750" ) ) return true;
   if(!Manager()->ApplyCut(HT > 300  && MHT > 300 && nJets >= 7 && nb >= 1, "SR11_Njet7_Nb1_HT300_MHT300" ) ) return true;
   if(!Manager()->ApplyCut(HT > 750  && MHT > 750 && nJets >= 5 && nb >= 1, "SR12_Njet5_Nb1_HT750_MHT750" ) ) return true; 
  }

  return true;
}

// Overlap Removal
template<typename T1, typename T2> std::vector<const T1*> cms_sus_16_033::Removal(std::vector<const T1*> &v1,
								  std::vector<const T2*> &v2, const double &drmin)
{
  // Determining with objects should be removed
  std::vector<bool> mask(v1.size(),false);
  for (unsigned int j=0;j<v1.size();j++)
    for (unsigned int i=0;i<v2.size();i++)
      if (v2[i]->dr(v1[j]) < drmin)
	{
	  mask[j]=true;
	  break;
	}

  // Building the cleaned container
  std::vector<const T1*> cleaned_v1;
  for (unsigned int i=0;i<v1.size();i++)
    if (!mask[i]) cleaned_v1.push_back(v1[i]);

  return cleaned_v1;
}

template<typename T1> std::vector<const T1*> cms_sus_16_033::Removal(std::vector<const T1*> &v1,
						     const double &drmin)
{
  // Determining with objects should be removed (objects are sorted)
  std::vector<bool> mask(v1.size(),false);
  for (unsigned int j=0;j<v1.size();j++)
    for (unsigned int i=j+1;i<v1.size();i++)
      {
	if (mask[i]) continue;
	if (v1[i]->dr(v1[j]) < drmin)
	  {
	    mask[i]=true;
	    continue;
	  }
      }

  // Building the cleaned container
  std::vector<const T1*> cleaned_v1;
  for (unsigned int i=0;i<v1.size();i++)
    if (!mask[i]) cleaned_v1.push_back(v1[i]);

  return cleaned_v1;
}


// This function returns the DeltaR depending on the pT of the lepton considered, 
// required for selecting isolated leptons
double cms_sus_16_033::Determine_DeltaR(const RecLeptonFormat* thisLepton) 
{ double DeltaR=0.;
  double pT = thisLepton->momentum().Pt();
  if      (pT <= 50.0 )                { DeltaR = 0.2     ; }
  else if (pT > 50.0 and pT <= 200.0 ) { DeltaR = 10.0/pT ; }
  else if (pT > 200.0 )		       { DeltaR = 0.05    ; }
  return DeltaR;
}
