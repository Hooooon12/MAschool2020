#include "SampleAnalyzer/User/Analyzer/CMS_EXO_17_030.h"

using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool CMS_EXO_17_030::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  cout << "BEGIN Initialization" << endl;
  // initialize variables, histos
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>    Analysis: CMS_EXO_17_030                  <>" << endmsg;
  INFO << "      <>             arXiv:1810.10092                 <>" << endmsg;
  INFO << "      <>             (multijet)                       <>" << endmsg;
  INFO << "      <>   Recasters: KANG Yechan,Kim Jihun,          <>" << endmsg;
  INFO << "      <>              Choi Jin, Yun SooHyun           <>" << endmsg;
  INFO << "      <>   Contact: fuks@lpthe.jussieu.fr             <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.8                <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  
  // Declaration of the signal regions (SR)
  Manager()->AddRegionSelection("Mg_200to400");
  Manager()->AddRegionSelection("Mg_400to700");
  Manager()->AddRegionSelection("Mg_700to1200");
  Manager()->AddRegionSelection("Mg_1200to2000");
  
  // Signal Region Partitions
  std::string ALL_Samples[]={"Mg_200to400", "Mg_400to700", "Mg_700to1200", "Mg_1200to2000"};

  std::string Low_Mass_Region[] = {"Mg_200to400", "Mg_400to700"};
  std::string High_Mass_Region[] = {"Mg_700to1200", "Mg_1200to2000"};

  // Declaration of Jet ID cut
  Manager()->AddCut("preselection Low", Low_Mass_Region);
  Manager()->AddCut("preselection High", High_Mass_Region);
    
  // Declaration of the jet-pt cuts and HT cuts
  // pt(jets) requires all jet pt > ~GeV
  
  Manager()->AddCut("Njets>=6 Low",  Low_Mass_Region);
  Manager()->AddCut("Njets>=6 High", High_Mass_Region);

  Manager()->AddCut("HT > 650GeV", Low_Mass_Region);
  Manager()->AddCut("HT > 900GeV", High_Mass_Region);
  
  // Declaration of the sixth jet-pt cut
  Manager()->AddCut("pt(j6) > 40GeV", "Mg_200to400");
  Manager()->AddCut("pt(j6) > 50GeV", "Mg_400to700");
  Manager()->AddCut("pt(j6) > 125GeV", "Mg_700to1200");
  Manager()->AddCut("pt(j6) > 175GeV", "Mg_1200to2000");
  
  // Declaration of the D^2[6,3+3,2] cut
  Manager()->AddCut("D^2[6,3+3,2] < 1.25", "Mg_200to400");
  Manager()->AddCut("D^2[6,3+3,2] < 1.0", "Mg_400to700");
  Manager()->AddCut("D^2[6,3+3,2] < 0.9", "Mg_700to1200");
  Manager()->AddCut("D^2[6,3+3,2] < 0.75", "Mg_1200to2000");
  
  // Declaration of the Am cut - TripletPair cut
  Manager()->AddCut("Am < 0.25", "Mg_200to400");
  Manager()->AddCut("Am < 1.75", "Mg_400to700");
  Manager()->AddCut("Am < 0.15", "Mg_700to1200");
  Manager()->AddCut("Am < 0.15", "Mg_1200to2000");
  
  // Declaration of the Delta cut - Triplet cut
  Manager()->AddCut("Delta > 250GeV", "Mg_200to400");
  Manager()->AddCut("Delta > 180GeV", "Mg_400to700");
  Manager()->AddCut("Delta > 20GeV", "Mg_700to1200");
  Manager()->AddCut("Delta > -120GeV", "Mg_1200to2000");
                    
  // Declaration of the D^2[3,2] cut - Triplet cut
  Manager()->AddCut("D^2[3,2] < 0.05", "Mg_200to400");
  Manager()->AddCut("D^2[3,2] < 0.175", "Mg_400to700");
  Manager()->AddCut("D^2[3,2] < 0.2", "Mg_700to1200");
  Manager()->AddCut("D^2[3,2] < 0.25", "Mg_1200to2000");

  // ====(Jin)MESSAGE: Choose best triplet for each signal
  // ==== that has the closest invMass to targeted gluino mass
  // ==== Note: this cut is to check whether the def. of the acceptance in the paper(i.e. Ntrip / Nevent) could affect the normal def.(i.e. Nevnet/Nevnet)
  Manager()->AddCut("SigTripInSR1", "Mg_200to400");
  Manager()->AddCut("SigTripInSR2", "Mg_400to700");
  Manager()->AddCut("SigTripInSR3", "Mg_700to1200");
  Manager()->AddCut("SigTripInSR4", "Mg_1200to2000");
  
  cout << "Preparing ROOT output" << endl;
  // Prepare ROOT output
  fOut = new TFile("test.root", "recreate");
  for (int i = 0; i < 4; i++) {
    tSr[i] = new TTree(Form("SR_%d", i+1), Form("Signal Region %d", i));
    tSr[i]->Branch("tripletPt", &triplet_pt[i]);
    tSr[i]->Branch("tripletEta", &triplet_eta[i]);
    tSr[i]->Branch("tripletPhi", &triplet_phi[i]);
    tSr[i]->Branch("tripletM", &triplet_mass[i]);
    cutFlow_Evt[i] = new TH1D(Form("SR_Evt_%d",i+1), Form("SR_Evt_%d",i+1), 10, 0, 10);
    cutFlow_TripletPair[i] = new TH1D(Form("SR_Triplet_Pair_%d",i+1), Form("SR_Triplet_Pair_%d",i+1), 10, 0, 10);
    cutFlow_Triplet[i] = new TH1D(Form("SR_Triplet_%d",i+1), Form("SR_Triplet_%d",i+1), 10, 0, 10);
  }
  cout << "ROOT output has prepared" << endl;

  cout << "END   Initialization" << endl;
  
  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void CMS_EXO_17_030::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  fOut->cd();
  for (int i = 0; i < 4; i++) {
    tSr[i]->Write();
    cutFlow_Evt[i]->Write();
    cutFlow_TripletPair[i]->Write();
    cutFlow_Triplet[i]->Write();
  }
  fOut->Close();
  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
unsigned int Nevents = 0;

bool CMS_EXO_17_030::Execute(SampleFormat& sample, const EventFormat& event)
{
  Nevents = Nevents + 1;
//   cout << " N° event = " << Nevents << endl;
  // Event weight
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
  {
    WARNING << "Found one event with a zero weight. Skipping...\n";
    return false;
  }
  Manager()->InitializeForNewEvent(myEventWeight);
  
  
  double pTcut[] = {30, 30, 50, 50};
  double HTcut[] = {650, 650, 900, 900};
  double lpTcut[] = {40, 50, 125, 175};
  double mds6332Cut[] = {1.25, 1., 0.9, 0.75};
  double asymmCut[] = {0.25, 0.175, 0.15, 0.15};
  double deltaCut[] = {250, 180, 20, -120};
  double mds32Cut[] = {0.05, 0.175, 0.2, 0.25};
  
  // ==== (Jin)Message: To choose final triplet for each events
  // ==== compare the triplets' invariant mass with gluinoMass in ArXiv1810.10092 figure4
  // ==== and leave the triplet that has the most closest invariant mass with gluinos
  // ==== for each signal regions
  double gluinoMass[] = {300., 500., 900., 1500.};

  // The event loop start here
  if(event.rec()!=0) {

    // Select jets satisfying pt&eta cut
    JetCollection Jets[4];
    for (int i = 0; i < 4; i++) {
      cutFlow_Evt[i]->Fill(0.5);
      Jets[i] = jetSelection(event, pTcut[i]);
      SORTER->sort(Jets[i]);
      if (Jets[i].size() >= 6) cutFlow_Evt[i]->Fill(1.5);
    }

    // Jet ID
    if(!Manager()->ApplyCut(Jets[0].size() != 0, "preselection Low")) return true;
    if(!Manager()->ApplyCut(Jets[2].size() != 0, "preselection High")) return true;

    // Number of Jets cut for low and high mass regions
    if(!Manager()->ApplyCut(Jets[0].size() >= 6, "Njets>=6 Low") ) return true;
    if(!Manager()->ApplyCut(Jets[2].size() >= 6, "Njets>=6 High")) return true;
    //cout << "[DEBUG] : NJets: " << Jets[3].size() << endl;
    // get HT for each signal regions
    double HT[4];
    for (int i = 0; i < 4; i++) {
      HT[i] = getHT(Jets[i]);
    }

    double lpT[4] = {0.};
    for (int i = 0; i < 4; i++) {
      if (Jets[i].size() < 6) {
        Jets[i].clear();
        continue;
      }
      else if (HT[i] < HTcut[i]) {
        Jets[i].clear();
        continue;
      } else if (Jets[i][5]->pt() < lpTcut[i]) {
        Jets[i].clear();
        continue;
      }
      lpT[i] = Jets[i][5]->pt();
      cutFlow_Evt[i]->Fill(2.5);
    }

    // HT cut for low and high mass regions
    if(!Manager()->ApplyCut(HT[0] > HTcut[0], "HT > 650GeV")) return true;
    if(!Manager()->ApplyCut(HT[2] > HTcut[2], "HT > 900GeV")) return true;

    // 6th Jet Pt cut for each regions
    if(!Manager()->ApplyCut(lpT[0] > lpTcut[0], "pt(j6) > 40GeV") ) return true;
    if(!Manager()->ApplyCut(lpT[1] > lpTcut[1], "pt(j6) > 50GeV") ) return true;
    if(!Manager()->ApplyCut(lpT[2] > lpTcut[2], "pt(j6) > 125GeV")) return true;
    if(!Manager()->ApplyCut(lpT[3] > lpTcut[3], "pt(j6) > 175GeV")) return true;
    
    // Mds6332 cut for each regions
    double evtMds6332[4];
    for (int i = 0; i < 4; i++) {
      evtMds6332[i] = mds6332(Jets[i]);
      if (Jets[i].size() < 6) continue;
      if (evtMds6332[i] > mds6332Cut[i]) {
        Jets[i].clear();
        continue;
       }
      cutFlow_Evt[i]->Fill(3.5);
    }
    if(!Manager()->ApplyCut(evtMds6332[0] < mds6332Cut[0], "D^2[6,3+3,2] < 1.25")) return true;
    if(!Manager()->ApplyCut(evtMds6332[1] < mds6332Cut[1], "D^2[6,3+3,2] < 1.0") ) return true;
    if(!Manager()->ApplyCut(evtMds6332[2] < mds6332Cut[2], "D^2[6,3+3,2] < 0.9") ) return true;
    if(!Manager()->ApplyCut(evtMds6332[3] < mds6332Cut[3], "D^2[6,3+3,2] < 0.75")) return true; 

    // Mass asymmetry cut
    // for each TripletPairs
    PairCollection tripPairs[4];
    TripletCollection trips[4];
    for (int i = 0; i < 4; i++) {
      tripPairs[i] = makePairCollection(Jets[i]);
      cutFlow_TripletPair[i]->Fill(0.5, tripPairs[i].size());
      cutFlow_Triplet[i]->Fill(0.5, tripPairs[i].size()*2);
      trips[i] = pairSelection(tripPairs[i], asymmCut[i]);
      cutFlow_TripletPair[i]->Fill(1.5, trips[i].size()/2);
      cutFlow_Triplet[i]->Fill(1.5, trips[i].size());
    }
    if(!Manager()->ApplyCut(trips[0].size() != 0, "Am < 0.25")) return true;
    if(!Manager()->ApplyCut(trips[1].size() != 0, "Am < 1.75")) return true;
    if(!Manager()->ApplyCut(trips[2].size() != 0, "Am < 0.15")) return true;
    if(!Manager()->ApplyCut(trips[3].size() != 0, "Am < 0.15")) return true;

    // Delta cut
    // for each Triplets
    for (int i = 0; i < 4; i++) {
      trips[i] = deltaSelection(trips[i], deltaCut[i]);
      cutFlow_Triplet[i]->Fill(2.5, trips[i].size());
    }
    if(!Manager()->ApplyCut(trips[0].size() != 0, "Delta > 250GeV" )) return true;
    if(!Manager()->ApplyCut(trips[1].size() != 0, "Delta > 180GeV" )) return true;
    if(!Manager()->ApplyCut(trips[2].size() != 0, "Delta > 20GeV"  )) return true;
    if(!Manager()->ApplyCut(trips[3].size() != 0, "Delta > -120GeV")) return true;

    // mds32 cut
    // for each Triplets
    for (int i = 0; i < 4; i++) {
      trips[i] = mds32Selection(trips[i], mds32Cut[i]);
      cutFlow_Triplet[i]->Fill(3.5, trips[i].size());
    }
    for (int i = 0; i < 4; i++) {
      triplet_pt[i].clear();
      triplet_eta[i].clear();
      triplet_phi[i].clear();
      triplet_mass[i].clear();

      for (int j = 0; j < trips[i].size(); j++) {
        MALorentzVector mom = getMomentum(trips[i][j]);
        triplet_pt[i].push_back(mom.Pt());
        triplet_eta[i].push_back(mom.Eta());
        triplet_phi[i].push_back(mom.Phi());
        triplet_mass[i].push_back(mom.M());
      }
      tSr[i]->Fill();
    }
    if(!Manager()->ApplyCut(trips[0].size() != 0, "D^2[3,2] < 0.05" )) return true;
    if(!Manager()->ApplyCut(trips[1].size() != 0, "D^2[3,2] < 0.175")) return true;
    if(!Manager()->ApplyCut(trips[2].size() != 0, "D^2[3,2] < 0.2"  )) return true;
    if(!Manager()->ApplyCut(trips[3].size() != 0, "D^2[3,2] < 0.25" )) return true;

    // (Jin)MESSAGE: choose the best candidate from the Triplets
    // If there is no triplet in the event, then return empty vector(might change)
    Triplet SigTrip[4];
    for (int i = 0; i < 4; i++) {
      SigTrip[i] = chooseSigTrip(trips[i], gluinoMass[i]);
    }
    for (int i = 0; i < 4; i++) {
      if (trips[i].size() == 0) continue;
      trips[i][0] = SigTrip[i];
    }
    if(!Manager()->ApplyCut(trips[0].size() == 0, "SigTripInSR1")) return true;
    if(!Manager()->ApplyCut(trips[1].size() == 0, "SigTripInSR2")) return true;
    if(!Manager()->ApplyCut(trips[2].size() == 0, "SigTripInSR3")) return true;
    if(!Manager()->ApplyCut(trips[3].size() == 0, "SigTripInSR4")) return true;
   
  }
  return true;  
}

//==== Functions to use ====
//==== (Jin)Message: I defined "double getMass(Triplet trip)" since 1.it is widely used in several functions and 2. to fill the histogram

MALorentzVector CMS_EXO_17_030::getMomentum( Triplet trip ){
  return trip[0]->momentum() + trip[1]->momentum() + trip[2]->momentum();
}

double CMS_EXO_17_030::getMass( Triplet trip) {
  double res;
  res = (trip[0]->momentum() + trip[1]->momentum() + trip[2]->momentum()).M();
  return res;
}

JetCollection CMS_EXO_17_030::jetSelection( const EventFormat& event, double ptCut) {
  JetCollection Jets;
  for(unsigned int j=0; j < event.rec()->jets().size(); j++)
  {
    const RecJetFormat *CurrentJet = &(event.rec()->jets()[j]);
    if(CurrentJet->pt()> ptCut && fabs(CurrentJet->eta())<2.4)
      Jets.push_back(CurrentJet);
  }
  return Jets;
}

double CMS_EXO_17_030::getHT( JetCollection jets ) {
  double ht = 0.;
  for (unsigned int i = 0; i < jets.size(); i++) {
    ht += jets[i]->pt();
  }
  return ht;
}

TripletCollection CMS_EXO_17_030::pairSelection( PairCollection tripPairs, double asymmCut) {
  TripletCollection trips;
  for (unsigned int i = 0; i < tripPairs.size(); i++) {
    TripletPair tripPair = tripPairs[i];
    if ( massAsymm(tripPair) < asymmCut ) {
      trips.push_back(tripPair.first);
      trips.push_back(tripPair.second);
    }
  }
  return trips;
}

TripletCollection CMS_EXO_17_030::deltaSelection( TripletCollection trips, double deltaCut ) {
  TripletCollection sigTrips;
  for (unsigned int i = 0; i < trips.size(); i++) {
    Triplet trip = trips[i];
    double delta_ = delta(trip);
    //cout << "[DEBUG]: Delta" << delta_ << endl;
    if (delta_ < deltaCut) continue;
    sigTrips.push_back(trip);
  }
  return sigTrips;
}

TripletCollection CMS_EXO_17_030::mds32Selection( TripletCollection trips, double mds32Cut ) {
  TripletCollection sigTrips;
  for (unsigned int i = 0; i < trips.size(); i++) {
    Triplet trip = trips[i];
    double mds32_ = mds32(trip);
    if (mds32_ > mds32Cut) continue;
    sigTrips.push_back(trip);
  }
  return sigTrips;
}

double CMS_EXO_17_030::mds32(Triplet t) {
  double c = 1./sqrt(3.);
  double res = 0.;
  for (int i = 0; i < 3; i++) {
    for (int j = i+1; j < 3; j++) {
      res += pow(sqrt(dalitz32(t, i, j)) - c, 2);
    }
  }
  //cout << "[DEBUG]: MDS32 " << res << endl;
  return res;
}

double CMS_EXO_17_030::mds6332(JetCollection jets) {
  double res = 0.;
  double c = 1./sqrt(20.);
  double temp;
  if (jets.size() < 6) return 10.;
  for (int i = 0; i < 6; i++) {
    for (int j = i + 1; j < 6; j++) {
      for (int k = j + 1; k < 6; k++) {
        Triplet t = { jets[i], jets[j], jets[k] };
        temp = pow(dalitz63(jets, i, j, k), 1) + pow(mds32(t), 1);
        temp = sqrt(temp) - c;
        res += temp*temp;
      }
    }
  }
  return res;
}

double CMS_EXO_17_030::massAsymm( TripletPair tp) {
  Triplet trip1 = tp.first;
  Triplet trip2 = tp.second;
  double M1 = (trip1[0]->momentum() + trip2[1]->momentum() + trip1[2]->momentum()).M();
  double M2 = (trip2[0]->momentum() + trip2[1]->momentum() + trip2[2]->momentum()).M();

  double Am = (fabs(M1 - M2) / (M1 + M2));
  return Am;
}

// Delta - input as invariant mass(cut for a triplet)
double CMS_EXO_17_030::delta( Triplet trip ) {
  double HT = 0.;
  for(int i = 0; i < 3; i++) {
    HT += trip[i]->pt();
  }
  double M = (trip[0]->momentum() + trip[1]->momentum() + trip[2]->momentum()).M();
  double Delta = HT - M;
  return Delta;
}

double CMS_EXO_17_030::dalitz32(Triplet trip, int idx1, int idx2) {
  double M_ = pow( (trip[idx1]->momentum()+trip[idx2]->momentum()).M(), 2);
  double M_123 = pow( (trip[0]->momentum()+trip[1]->momentum()+trip[2]->momentum()).M(), 2);
  double M_1 = pow( (trip[0]->momentum()).M(), 2);
  double M_2 = pow( (trip[1]->momentum()).M(), 2);
  double M_3 = pow( (trip[2]->momentum()).M(), 2);
  return M_/(M_123+M_1+M_2+M_3);
}

double CMS_EXO_17_030::dalitz63(JetCollection trip, int idx1, int idx2, int idx3) {
  double M_ = pow( (trip[idx1]->momentum() + trip[idx2]->momentum() + trip[idx3]->momentum()).M(), 2);
  double M_inv = pow( (trip[0]->momentum()+trip[1]->momentum()+trip[2]->momentum()
                      +trip[3]->momentum()+trip[4]->momentum()+trip[5]->momentum()).M(), 2);
  double massSum = 0.;
  for (int i = 0; i < 6; i++) {
    massSum += pow( (trip[i]->momentum()).M(), 2);
  }

  return M_ / (4*M_inv + 6 * massSum);
}

PairCollection CMS_EXO_17_030::makePairCollection(JetCollection Jets) {
  PairCollection res;
  if (Jets.size() < 6) return res;
  TripletCollection trips;
  for (int i = 0 ; i < 6; i++) {
    for (int j = i+1; j < 6; j++){
      for (int k = j+1; k < 6; k++) {
        trips.push_back({Jets[i] , Jets[j], Jets[k]});
      }
    }
  }
  for (int i = 0; i < 10; i++) {
    res.push_back(make_pair(trips[i], trips[19-i]));
  }
  return res;
}

// ==== (Jin)Message: functions to choose the best triplet candidate
double CMS_EXO_17_030::compareMass(Triplet trip, double gluinoM) {
  double invM = getMass(trip);
  double res = fabs(invM - gluinoM);
  return res;
}

Triplet CMS_EXO_17_030::chooseSigTrip(TripletCollection trips, double gluinoM) {
  Triplet res_trip;
  if ( trips.size() == 0 ) return res_trip;
  res_trip = trips.at(0);
  for (unsigned int i = 0; i < trips.size(); i++) {
    if (compareMass(trips.at(i), gluinoM) < compareMass(res_trip, gluinoM)) res_trip = trips.at(i);
    else continue;
  }
  return res_trip;
} 
