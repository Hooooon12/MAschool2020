#include "SampleAnalyzer/User/Analyzer/atlas_conf_2019_040.h"
using namespace MA5;
using namespace std;


// Overlap Removal
template<typename T1, typename T2> std::vector<const T1*>
  Removal(std::vector<const T1*> &v1, std::vector<const T2*> &v2,
  const double &drmin)
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



// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_conf_2019_040::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: atlas_conf_2019_040                                   <>" << endmsg;
  INFO << "        <>    0 lepton, 2-6 jets = 13 TeV, 139 fb^-1 luminosity               <>" << endmsg;
  INFO << "        <>    Recast by: F. Ambrogi                                           <>" << endmsg;
  INFO << "        <>    Contact: federico.ambrogi@univie.ac.at                          <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.5 and above                           <>" << endmsg;
  INFO << "        <>    For more information, see                                       <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase   <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;


  // Definition of the Signal Regions (SRs) of the analysis

  Manager()->AddRegionSelection("SR2j_1600");
  Manager()->AddRegionSelection("SR2j_2200");
  Manager()->AddRegionSelection("SR2j_2800");

  Manager()->AddRegionSelection("SR4j_1000");
  Manager()->AddRegionSelection("SR4j_2200");
  Manager()->AddRegionSelection("SR4j_3400");

  Manager()->AddRegionSelection("SR5j_1600");

  Manager()->AddRegionSelection("SR6j_1000");
  Manager()->AddRegionSelection("SR6j_2200"); 
  Manager()->AddRegionSelection("SR6j_3400");


  // *** Definition of the prelesection cuts, common to all SRs
  Manager()->AddCut("Preselection");
  Manager()->AddCut("njets>=2");

  // *** Jets multiplicity 
  std::string njets04[] = {"SR4j_1000","SR4j_2200","SR4j_3400"};
  Manager()->AddCut("njets>=4" , njets04);
  
  std::string njets05[] = {"SR5j_1600"};
  Manager()->AddCut("njets>=5" , njets05);

  std::string njets06[] = {"SR6j_1000","SR6j_2200","SR6j_3400" };
  Manager()->AddCut("njets>=6" , njets06);


  // Definition of the SR specific cuts

  // *** Delta phi of the first 3 leading jets
  std::string DPhi3jets04[] = {"SR2j_2200", "SR4j_1000","SR4j_2200","SR4j_3400" , "SR5j_1600" , "SR6j_1000", "SR6j_2200", "SR6j_3400"};
  Manager()->AddCut("DPhi(jet1,2,(3),ptmiss)>04", DPhi3jets04 );

  std::string DPhi3jets08[] = {"SR2j_1600","SR2j_2800"};
  Manager()->AddCut("DPhi(jet1,2,(3),ptmiss)>08", DPhi3jets08);


  // *** Delta phi of the remaining jets
  std::string DPhirest02[] = {"SR2j_2200","SR4j_1000","SR4j_2200","SR4j_3400", "SR5j_1600","SR6j_1000","SR6j_2200","SR6j_3400"};
  Manager()->AddCut("Dphi(ptmiss,j>3)>02" , DPhirest02);

  std::string DPhirest04[] = {"SR2j_1600", "SR2j_2800" };
  Manager()->AddCut("Dphi(ptmiss,j>3)>04", DPhirest04);


  // *** pt of a specific jet
  std::string jet1pt600[] = {"SR2j_2200","SR5j_1600"};
  Manager()->AddCut("jet1pt>600" , jet1pt600);

  std::string jet2pt250[] = {"SR2j_1600" , "SR2j_2800"};
  Manager()->AddCut("jet2pt>250" , jet2pt250);

  std::string jet4pt100[] = {"SR4j_1000","SR4j_2200","SR4j_3400"};
  Manager()->AddCut("jet4pt>100" , jet4pt100);

  std::string jet6pt75[] = {"SR6j_1000","SR6j_2200","SR6j_3400"};
  Manager()->AddCut("jet6pt>75" , jet6pt75);


  // *** Eta of the jets
  Manager()->AddCut("j2eta<12" , "SR2j_2800");
  Manager()->AddCut("j2eta<20" , "SR2j_1600");
  Manager()->AddCut("j2eta<28" , "SR2j_2200");

  std::string jet4eta20[] = {"SR4j_1000","SR4j_2200","SR4j_3400"};
  Manager()->AddCut("j4eta<20" , jet4eta20);

  Manager()->AddCut("j5eta<28" , "SR5j_1600");

  std::string jet6eta20[] = {"SR6j_1000","SR6j_2200","SR6j_3400"};
  Manager()->AddCut("j6eta<20" , jet6eta20);


  // *** Aplanarity
  std::string Aplanarity004[] = {"SR4j_1000","SR4j_2200","SR4j_3400"};
  Manager()->AddCut("Aplanarity>004", Aplanarity004);

  std::string Aplanarity008[] = {"SR6j_1000", "SR6j_2200","SR6j_3400"};
  Manager()->AddCut("Aplanarity>008", Aplanarity008);


  // specific cuts on MET over sqrt(HT)
  std::string MET_HT_16[] = {"SR2j_2200", "SR2j_1600","SR2j_2800", "SR4j_1000","SR4j_2200", "SR6j_1000", "SR6j_2200", "SR5j_1600"};
  Manager()->AddCut("MET_HT>16" , MET_HT_16 );

    std::string MET_HT_10[] = {"SR4j_3400" , "SR6j_3400"};
  Manager()->AddCut("MET_HT>10" , MET_HT_10);





  // specific cuts on Meff
  std::string Meff_1000[] = {"SR4j_1000" , "SR6j_1000"};
  Manager()->AddCut("Meff>1000", Meff_1000);

  std::string Meff_1600[] = {"SR2j_1600" , "SR5j_1600"};
  Manager()->AddCut("Meff>1600", Meff_1600);

  std::string Meff_2200[] = {"SR2j_2200" , "SR4j_2200", "SR6j_2200" };
  Manager()->AddCut("Meff>2200", Meff_2200);

  std::string Meff_2800[] = {"SR2j_2800"};
  Manager()->AddCut("Meff>2800", Meff_2800);

  std::string Meff_3400[] = {"SR4j_3400", "SR6j_3400"};
  Manager()->AddCut("Meff>3400", Meff_3400);

  return true;
  
}



// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_conf_2019_040::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_conf_2019_040::Execute(SampleFormat& sample, const EventFormat& event)
{

 if (event.rec()!=0)
   {

     
    double myEventWeight;
    if(Configuration().IsNoEventWeight()) myEventWeight=1.;
    else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
    else 
    { //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
    return false;	}

    Manager()->InitializeForNewEvent(myEventWeight); 
    vector<const RecLeptonFormat*> electrons, muons ; // isolated electrons and muons (probably non isolated are not necessary...) 
    vector<const RecJetFormat*>    signalJets ; // jets
  
    // Selecting Jets
    double jetpt  = 50;
    double jeteta = 2.8 ;

    for(unsigned int i=0; i<event.rec()->jets().size(); i++)
    {  const RecJetFormat *thisJet= &(event.rec()->jets()[i]);
       double pT = thisJet->momentum().Pt() , eta =  thisJet->eta() ;
       if (pT > jetpt and fabs(eta) < jeteta )
          { signalJets.push_back(thisJet); }
     }


    SORTER->sort(signalJets);


    // Selecting leptons (veto on leptons, with different eta requirements for muons and electrons) 
    double muonpt      = 6.0;
    double muoneta     = 2.8;
    double electronpt  = 7.0;
    double electroneta = 2.47 ;

    //  Muons
    for(unsigned int i=0; i<event.rec()->muons().size(); i++)
    { const RecLeptonFormat *thisMuon = &(event.rec()->muons()[i]);
      double pt = thisMuon->pt() , eta =  thisMuon->momentum().Eta() ;
      if ( pt > muonpt  and fabs(eta) < muoneta) {
      muons.push_back(thisMuon); }
     }

    //  Electrons
    for(unsigned int i=0; i<event.rec()->electrons().size(); i++)
    { const RecLeptonFormat *thisElectron = &(event.rec()->electrons()[i]);
      double pt = thisElectron->pt() , eta =  thisElectron->momentum().Eta() ;
      if (pt> electronpt  and fabs(eta) < electroneta ) {
      electrons.push_back(thisElectron); }
     }

    // Overlap removal
    signalJets = Removal(signalJets, electrons,  0.2);
    electrons = Removal(electrons, signalJets,  0.4);
    muons = Removal(muons, signalJets,  0.4);


    // Definition of HT
    double HT = 0;
    for(unsigned int j = 0; j < signalJets.size(); j++)
      { HT += signalJets[j]->momentum().Pt(); }

    // Definition of MET
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();

    // Definition of Meff
    double Meff = MET + HT ;
    
    // MET over sqrt(HT)
    double MET_HT = MET/sqrt(HT);

    //cout << Meff << "_" << MET_HT << "_" << MET << "_" << HT << endl;
    // Checking the preselection requirements
    // a. leading jet pt > 200 and 2nd jet pt > 50 GeV

    bool j1_pt=false;
    bool j2_pt=false;
    if (signalJets.size()>0) 
	{ j1_pt = signalJets[0]->pt()>200.0;
          }
    if (signalJets.size()>1)
	{ j2_pt = signalJets[1]->pt()>50.0; }

    // b. lepton veto
    bool leptonVeto = ((electrons.size()+muons.size())==0);

    // c. Meff > 800 GeV
    bool Meff_pre   = (Meff > 800.0);
    // d. MET > 300 GeV
    bool MET_pre    = (MET > 300.0);


    if(!Manager()->ApplyCut(j1_pt && j2_pt && Meff_pre && leptonVeto && MET_pre, "Preselection")) return true;

    //cout << "jets pt=" << j1_pt << "," << j2_pt << "---" << "meff=" << " " << Meff_pre << " MET=" << MET_pre << " bool Deltaphi" << Dphi_3jets_MET << endl;
    if(!Manager()->ApplyCut( signalJets.size()>=2 , "njets>=2")) return true;

    // SR dependent cuts
    // Njets >= 4
    if(!Manager()->ApplyCut( signalJets.size()>=4, "njets>=4")) return true;
    // Njets >= 5                                                                                                                          
    if(!Manager()->ApplyCut( signalJets.size()>=5, "njets>=5")) return true;
    // Njets >= 6                                                                                                                          
    if(!Manager()->ApplyCut( signalJets.size()>=6, "njets>=6")) return true;

    // DPhi  of the 3 leading pt jets

    bool Dphi_3jets_MET_04 = true;
    //if (signalJets.size()==1) { Dphi_3jets_MET_04 = ( signalJets[0]->dphi_0_pi(pTmiss) > 0.4 ); }
    if (signalJets.size()==2) { Dphi_3jets_MET_04 = ( signalJets[0]->dphi_0_pi(pTmiss) > 0.4 && signalJets[1]->dphi_0_pi(pTmiss) > 0.4 ); }
    if (signalJets.size()>=3) { Dphi_3jets_MET_04 = ( signalJets[0]->dphi_0_pi(pTmiss) > 0.4 && signalJets[1]->dphi_0_pi(pTmiss) > 0.4 &&  signalJets[2]->dphi_0_pi(pTmiss) > 0.4); }

    
    if(!Manager()->ApplyCut( Dphi_3jets_MET_04, "DPhi(jet1,2,(3),ptmiss)>04")) return true;

    bool Dphi_3jets_MET_08 = true;
    //if (signalJets.size()==1) { Dphi_3jets_MET_08 = ( signalJets[0]->dphi_0_pi(pTmiss) > 0.8 ); }
    if (signalJets.size()==2) { Dphi_3jets_MET_08 = ( signalJets[0]->dphi_0_pi(pTmiss) > 0.8 && signalJets[1]->dphi_0_pi(pTmiss) > 0.8 ); }
    if (signalJets.size()>=3) { Dphi_3jets_MET_08 = ( signalJets[0]->dphi_0_pi(pTmiss) > 0.8 && signalJets[1]->dphi_0_pi(pTmiss) > 0.8 &&  signalJets[2]->dphi_0_pi(pTmiss) > 0.8); }

    if(!Manager()->ApplyCut( Dphi_3jets_MET_08, "DPhi(jet1,2,(3),ptmiss)>08")) return true;
    
    // DPhi  of the rest of the jets (from the 4th on)
    bool DPhiRest02 = true;
    bool DPhiRest04 = true;

    for(unsigned int j = 0; j < signalJets.size(); j++) {
      if (j > 2) {
	if (signalJets[j]->dphi_0_pi(pTmiss) < 0.2) {
            DPhiRest02 = false; 
          }
	if (signalJets[j]->dphi_0_pi(pTmiss) < 0.4) {
            DPhiRest04 = false; 
          }
      }
    }

    if(!Manager()->ApplyCut( DPhiRest02, "Dphi(ptmiss,j>3)>02")) return true;
    if(!Manager()->ApplyCut( DPhiRest04, "Dphi(ptmiss,j>3)>04")) return true;

    // Cut on specific jet pt    
    bool jet1pt_600 = (signalJets[0]->pt() > 600.0);
    bool jet2pt_250 = (signalJets[1]->pt() > 250.0);
    bool jet4pt_100 = true;
    if (signalJets.size() >3) { jet4pt_100 = (signalJets[3]->pt() > 100.0);}
    bool jet6pt_75 = true;
    if (signalJets.size() >5) { jet6pt_75 = (signalJets[5]->pt() > 75.0);}
    
    if(!Manager()->ApplyCut( jet1pt_600, "jet1pt>600")) return true;
    if(!Manager()->ApplyCut( jet2pt_250, "jet2pt>250")) return true;
    if(!Manager()->ApplyCut( jet4pt_100, "jet4pt>100")) return true;
    if(!Manager()->ApplyCut( jet6pt_75,  "jet6pt>75")) return true;

    // |eta| for the first n signal jets
    bool j2eta_20 = fabs(signalJets[0]->eta())<2.0 && fabs(signalJets[1]->eta())<2.0 ;
    bool j2eta_12 = fabs(signalJets[0]->eta())<1.2 && fabs(signalJets[1]->eta())<1.2 ;
    bool j2eta_28 = fabs(signalJets[0]->eta())<2.8 && fabs(signalJets[1]->eta())<2.8 ;
    bool j4eta = true;
    bool j5eta = true;
    bool j6eta = true;

    // jeta eta for SR4
    if ( signalJets.size() > 3 ) { j4eta =  fabs(signalJets[0]->eta())<2.0 && 
					    fabs(signalJets[1]->eta())<2.0 && 
                                            fabs(signalJets[2]->eta())<2.0 && 
                                            fabs(signalJets[3]->eta())<2.0 ; }
    // jeta eta for SR5
    if ( signalJets.size() > 4 ) { j5eta =  fabs(signalJets[0]->eta())<2.8 && 
                                            fabs(signalJets[1]->eta())<2.8 &&  
                                            fabs(signalJets[2]->eta())<2.8 && 
					    fabs(signalJets[3]->eta())<2.8 && 
					    fabs(signalJets[4]->eta())<2.8 ; }
    // jeta eta for SR6
    if ( signalJets.size() > 5 ) { j6eta =  fabs(signalJets[0]->eta())<2.0 && 
					    fabs(signalJets[1]->eta())<2.0 &&  
					    fabs(signalJets[2]->eta())<2.0 && 
	                                    fabs(signalJets[3]->eta())<2.0 && 
					    fabs(signalJets[4]->eta())<2.0 && 
				            fabs(signalJets[5]->eta())<2.0 ; }
    
    if(!Manager()->ApplyCut( j2eta_12, "j2eta<12" )) return true;
    if(!Manager()->ApplyCut( j2eta_20, "j2eta<20" )) return true;
    if(!Manager()->ApplyCut( j2eta_28, "j2eta<28" )) return true;
    if(!Manager()->ApplyCut( j4eta,    "j4eta<20" )) return true;
    if(!Manager()->ApplyCut( j5eta,    "j5eta<28" )) return true;
    if(!Manager()->ApplyCut( j6eta,    "j6eta<20" )) return true;

    // APLANARITY
    // Construction of the sphericity tensor, calculation of the aplanarity
    // using the Cardano algorithm
    // see http://inspirehep.net/record/1510490/files/atlas_1605_03814.cpp?version=1
    double S12=0., S31=0., S23=0., S11=0., S22=0., S33=0., Stot=0.;
    for (unsigned int i=0; i<signalJets.size(); i++)
    {
      S11+=signalJets[i]->px()*signalJets[i]->px();
      S12+=signalJets[i]->px()*signalJets[i]->py();
      S22+=signalJets[i]->py()*signalJets[i]->py();
      S23+=signalJets[i]->py()*signalJets[i]->pz();
      S31+=signalJets[i]->pz()*signalJets[i]->px();
      S33+=signalJets[i]->pz()*signalJets[i]->pz();
      Stot+=signalJets[i]->p()*signalJets[i]->p();
    }
    S11=S11/Stot; S12=S12/Stot; S22=S22/Stot; S23=S23/Stot; S31=S31/Stot; S33=S33/Stot;
    double Sii = S11+S22+S33;
    double C0 = S11*S23*S23 + S22*S31*S31 + S33*S12*S12 - S11*S22*S33 - 2.*S31*S12*S23;
    double C1 = S11*S22 + S22*S33 + S11*S33 - S12*S12 - S23*S23 - S31*S31;
    double P = Sii*Sii - 3.*C1;
    double Q = Sii*(P-1.5*C1) - 13.5*C0;
    double phi = atan2(sqrt(fabs(27.*(C1*C1/4.*(P-C1) + C0*(Q+6.75*C0)))),Q)/3.;
    double cth = sqrt(fabs(P))*cos(phi);
    double sth = sqrt(fabs(P))*sin(phi)/sqrt(3.);
    double a1 = (Sii-cth)/3.+sth;
    double a2 = (Sii-cth)/3.-sth;
    double a3 = (Sii-cth)/3.+cth;
    double lam3 = 1.5*std::min(std::min(a1,a2),a3);


    // Aplanarity cut
    if(!Manager()->ApplyCut(lam3>0.04,"Aplanarity>004")) return true;
    if(!Manager()->ApplyCut(lam3>0.08,"Aplanarity>008")) return true;


    // MET over sqrt(HT)
    if(!Manager()->ApplyCut(MET_HT>16,"MET_HT>16")) return true;
    if(!Manager()->ApplyCut(MET_HT>10,"MET_HT>10")) return true;

    // cout << Meff << "_" << MET_HT << "_" << MET << "_" << HT << endl;

    if(!Manager()->ApplyCut(Meff > 1000.0, "Meff>1000")) return true;
    if(!Manager()->ApplyCut(Meff > 1600.0, "Meff>1600")) return true;
    if(!Manager()->ApplyCut(Meff > 2200.0, "Meff>2200")) return true;
    if(!Manager()->ApplyCut(Meff > 2800.0, "Meff>2800")) return true;
    if(!Manager()->ApplyCut(Meff > 3400.0, "Meff>3400")) return true;

    
    
    return true; 

   }
return true;
}



