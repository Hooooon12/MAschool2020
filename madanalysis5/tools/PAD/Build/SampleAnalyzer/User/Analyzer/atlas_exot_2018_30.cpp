#include "SampleAnalyzer/User/Analyzer/atlas_exot_2018_30.h"
using namespace MA5;
using namespace std;


template<typename T1, typename T2> std::vector<const T1*> Removal(std::vector<const T1*> &v1, std::vector<const T2*> &v2, const MAdouble64 &drmin) {
  // Determining with objects should be removed
  std::vector<bool> mask(v1.size(), false);
  for (MAuint32 j=0; j<v1.size(); j++)
    for (MAuint32 i=0; i<v2.size(); i++)
      if (v2[i]->dr(v1[j]) < drmin) {
        mask[j] = true;
        break;
      } 

  // Building the cleaned container
  std::vector<const T1*> cleaned_v1;
  for (MAuint32 i=0; i<v1.size(); i++)
    if (!mask[i]) cleaned_v1.push_back(v1[i]);

  return cleaned_v1; 
}

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_exot_2018_30::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  cout << "BEGIN Initialization" << endl;

  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>   Analysis: ATLAS-EXOT-2018-30, arXiv:1906.05609                 <>" << endmsg;
  INFO << "      <>             W' to single lepton + MET, 139 fb^-1 lumi (13 TeV)   <>" << endmsg;
  INFO << "      <>   Recast by: Kyungmin Park                                       <>" << endmsg;
  INFO << "      <>   Contact:  jazzykm0110@uos.ac.kr                                <>" << endmsg; 
  INFO << "      <>   Based on MadAnalysis 5 v1.8.40                                 <>" << endmsg;
  INFO << "      <>   For more information, see                                      <>" << endmsg;
  INFO << "      <>   http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase  <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;


  // Declaration of the signal regions
  Manager()->AddRegionSelection("SR_Electron_MT_130_400");
  Manager()->AddRegionSelection("SR_Electron_MT_400_600");
  Manager()->AddRegionSelection("SR_Electron_MT_600_1000");
  Manager()->AddRegionSelection("SR_Electron_MT_1000_2000");
  Manager()->AddRegionSelection("SR_Electron_MT_2000_3000");
  Manager()->AddRegionSelection("SR_Electron_MT_3000_10000");
  Manager()->AddRegionSelection("SR_Electron_MT_130_inf");

  Manager()->AddRegionSelection("SR_Muon_MT_110_400");
  Manager()->AddRegionSelection("SR_Muon_MT_400_600");
  Manager()->AddRegionSelection("SR_Muon_MT_600_1000");
  Manager()->AddRegionSelection("SR_Muon_MT_1000_2000");
  Manager()->AddRegionSelection("SR_Muon_MT_2000_3000");
  Manager()->AddRegionSelection("SR_Muon_MT_3000_10000");
  Manager()->AddRegionSelection("SR_Muon_MT_110_inf");


  // Cuts for each SR
  std::string OneElec[] = { "SR_Electron_MT_130_400", "SR_Electron_MT_400_600", "SR_Electron_MT_600_1000", "SR_Electron_MT_1000_2000", "SR_Electron_MT_2000_3000", "SR_Electron_MT_3000_10000", "SR_Electron_MT_130_inf" };
  std::string OneMuon[] = { "SR_Muon_MT_110_400", "SR_Muon_MT_400_600", "SR_Muon_MT_600_1000", "SR_Muon_MT_1000_2000", "SR_Muon_MT_2000_3000", "SR_Muon_MT_3000_10000", "SR_Muon_MT_110_inf" };
  
  std::string MT_400_600[] = { "SR_Electron_MT_400_600", "SR_Muon_MT_400_600" };
  std::string MT_600_1000[] = { "SR_Electron_MT_600_1000", "SR_Muon_MT_600_1000" };
  std::string MT_1000_2000[] = { "SR_Electron_MT_1000_2000", "SR_Muon_MT_1000_2000" };
  std::string MT_2000_3000[] = { "SR_Electron_MT_2000_3000", "SR_Muon_MT_2000_3000" };
  std::string MT_3000_10000[] = { "SR_Electron_MT_3000_10000", "SR_Muon_MT_3000_10000" };

  Manager()->AddCut("One Electron", OneElec);
  Manager()->AddCut("One Muon", OneMuon);
  
  Manager()->AddCut("Lepton Veto for Electrons", OneElec);
  Manager()->AddCut("Lepton Veto for Muons", OneMuon);

  Manager()->AddCut("$\\slashed{E}_T > 55$ [GeV]", OneMuon);
  Manager()->AddCut("$\\slashed{E}_T > 65$ [GeV]", OneElec);
  Manager()->AddCut("$M_T > 130$ [GeV]", OneElec);
  Manager()->AddCut("$M_T > 110$ [GeV]", OneMuon);

  Manager()->AddCut("$110 < M_T < 400$ [GeV]", OneMuon[0]);
  Manager()->AddCut("$130 < M_T < 400$ [GeV]", OneElec[0]);
  Manager()->AddCut("$400 < M_T < 600$ [GeV]", MT_400_600);
  Manager()->AddCut("$600 < M_T < 1000$ [GeV]", MT_600_1000);
  Manager()->AddCut("$1000 < M_T < 2000$ [GeV]", MT_1000_2000);
  Manager()->AddCut("$2000 < M_T < 3000$ [GeV]", MT_2000_3000);
  Manager()->AddCut("$3000 < M_T < 10000$ [GeV]", MT_3000_10000);


  // Histogram declaration
  //Manager()->AddHisto("MT > 110 GeV for Muon Channel", 50, 110, 7200, OneMuon[6]);
  //Manager()->AddHisto("MT > 130 GeV for Electron Channel", 60, 130, 7200, OneElec[6]);

  Manager()->AddHistoLogX("MT > 110 GeV for Muon Channel (finer log bins)", 100, 110, 7200, OneMuon[6]);
  Manager()->AddHistoLogX("MT > 130 GeV for Electron Channel (finer log bins)", 120, 130, 7200, OneElec[6]);
   
  Manager()->AddHistoLogX("MT > 110 GeV for Muon Channel (log bins)", 50, 110, 7200, OneMuon[6]);
  Manager()->AddHistoLogX("MT > 130 GeV for Electron Channel (log bins)",60, 130, 7200, OneElec[6]);

  cout << "END   Initialization" << endl;
  return true;
}


// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_exot_2018_30::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  cout << "END   Finalization" << endl;
}


// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_exot_2018_30::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Event weight
  double myWeight;
  if (Configuration().IsNoEventWeight()) myWeight = 1.;
  else if (event.mc()->weight() != 0.) myWeight = event.mc()->weight();
  else { return false; }
  Manager()->InitializeForNewEvent(myWeight);

  // Security for empty events
  if (event.rec() == 0) return true;


  // Muon
  std::vector<const RecLeptonFormat*> SignalMuons, VetoedMuons;
  for (unsigned int i=0; i<event.rec()->muons().size(); i++) {
    const RecLeptonFormat *Muon = &(event.rec()->muons()[i]);

    // Kinematics
    double eta = Muon->abseta();
    double pt = Muon->pt();

    // Isolation
    double iso_dR = std::min(10./pt, 0.3);
    double iso_tracks = PHYSICS->Isol->eflow->relIsolation(Muon, event.rec(), iso_dR, 1., IsolationEFlow::TRACK_COMPONENT);
    bool iso = (iso_tracks < 0.15);

    // Signal Muons
    if ( (0.1 < eta && eta < 1.01) || (1.1 < eta  && eta < 2.4) ) {
      if (  pt > 55. ) { 
        if ( iso ) { SignalMuons.push_back(Muon); continue; }
      }
    }

    // Vetoed Muons
    if ( pt > 20. ) { VetoedMuons.push_back(Muon); }
  }


  // Electron
  std::vector<const RecLeptonFormat*> SignalElectrons, VetoedElectrons, VetoedElectronsDeltaR;
  for (unsigned int i=0; i<event.rec()->electrons().size(); i++) {
    const RecLeptonFormat *Elec = &(event.rec()->electrons()[i]);   

    // Kinematics
    double eta = Elec->abseta();
    double pt = Elec->pt();
    double Et = Elec->et();

    // Isolation
    double iso_tracks = PHYSICS->Isol->eflow->relIsolation(Elec, event.rec(), 0.2, 0., IsolationEFlow::TRACK_COMPONENT);
    double iso_all = PHYSICS->Isol->eflow->relIsolation(Elec, event.rec(), 0.2, 0., IsolationEFlow::ALL_COMPONENTS);
    bool iso = (iso_tracks < 0.06 && iso_all < 0.06);

    // Signal Electrons
    if ( eta < 1.37 || ( 1.52 < eta && eta < 2.47 ) ) { 
      if ( Et > 65. && iso ) { SignalElectrons.push_back(Elec); continue; }    
    }
    
    // Vetoed Electrons
    if ( pt > 20. ) { 
      VetoedElectrons.push_back(Elec); 
      // additional condition for delta R
      if ( SignalMuons.size() == 1 && SignalMuons[0]->dr(Elec) >= 0.1 ) { VetoedElectronsDeltaR.push_back(Elec); } 
    }  
  }


  // Jet
  std::vector<const RecJetFormat*> Jets;
  for (unsigned int i=0; i<event.rec()->jets().size(); i++) {
    const RecJetFormat *Jet = &(event.rec()->jets()[i]);
    double eta = Jet->abseta();
    double pt = Jet->pt();
    if ( eta < 2.4 && pt > 20. ) { Jets.push_back(Jet); }
    else if ( eta > 2.4 && pt > 30. ) { Jets.push_back(Jet); }
  }
  Jets = PHYSICS->Isol->JetCleaning(Jets, SignalElectrons, 0.1);


  // MET & MT
  double MET = event.rec()->MET().pt();

  double Mt = 0;  
  if ( SignalElectrons.size() == 1 && SignalMuons.size() == 0) { Mt = sqrt(2*SignalElectrons[0]->pt()*MET*(1-cos(SignalElectrons[0]->dphi_0_pi(event.rec()->MET())))); }
  else if ( SignalMuons.size() == 1 && SignalElectrons.size() == 0) { Mt = sqrt(2*SignalMuons[0]->pt()*MET*(1-cos(SignalMuons[0]->dphi_0_pi(event.rec()->MET())))); }


  // Cuts
  if (!Manager()->ApplyCut( SignalElectrons.size() == 1 && SignalMuons.size() == 0, "One Electron")) return true;
  if (!Manager()->ApplyCut( SignalMuons.size() == 1 && SignalElectrons.size() == 0, "One Muon")) return true;

  if (!Manager()->ApplyCut( VetoedElectrons.size() == 0 && VetoedMuons.size() == 0, "Lepton Veto for Electrons" )) return true;
  if (!Manager()->ApplyCut( VetoedElectronsDeltaR.size() == 0 && VetoedMuons.size() == 0, "Lepton Veto for Muons" )) return true;

  if (!Manager()->ApplyCut( MET > 55., "$\\slashed{E}_T > 55$ [GeV]")) return true; 
  if (!Manager()->ApplyCut( MET > 65., "$\\slashed{E}_T > 65$ [GeV]")) return true; 
  if (!Manager()->ApplyCut( Mt > 110., "$M_T > 110$ [GeV]")) return true;
  if (!Manager()->ApplyCut( Mt > 130., "$M_T > 130$ [GeV]")) return true;

  if (!Manager()->ApplyCut( Mt > 110. && Mt < 400., "$110 < M_T < 400$ [GeV]")) return true; 
  if (!Manager()->ApplyCut( Mt > 130. && Mt < 400., "$130 < M_T < 400$ [GeV]")) return true; 
  if (!Manager()->ApplyCut( Mt > 400. && Mt < 600., "$400 < M_T < 600$ [GeV]")) return true; 
  if (!Manager()->ApplyCut( Mt > 600. && Mt < 1000., "$600 < M_T < 1000$ [GeV]")) return true; 
  if (!Manager()->ApplyCut( Mt > 1000. && Mt < 2000., "$1000 < M_T < 2000$ [GeV]")) return true; 
  if (!Manager()->ApplyCut( Mt > 2000. && Mt < 3000., "$2000 < M_T < 3000$ [GeV]")) return true; 
  if (!Manager()->ApplyCut( Mt > 3000. && Mt < 10000., "$3000 < M_T < 10000$ [GeV]")) return true; 


  // Fill Histograms
  //Manager()->FillHisto("MT > 110 GeV for Muon Channel", Mt);
  //Manager()->FillHisto("MT > 130 GeV for Electron Channel", Mt); 

  Manager()->FillHisto("MT > 110 GeV for Muon Channel (finer log bins)", Mt);
  Manager()->FillHisto("MT > 130 GeV for Electron Channel (finer log bins)", Mt); 

  Manager()->FillHisto("MT > 110 GeV for Muon Channel (log bins)", Mt);
  Manager()->FillHisto("MT > 130 GeV for Electron Channel (log bins)", Mt); 


  return true;
}
