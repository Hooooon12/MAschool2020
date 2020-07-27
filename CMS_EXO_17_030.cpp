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

  // Choose signal region
  cout << "[CMS_EXO_17_030::Initialize] Choose your signal region (1, 2, 3, 4): ";
  cin >> SR;

  try {
	if (! (0<SR&&SR<5)) throw SR;
  }
  catch (int SR) {
	cerr << "[CMS_EXO_17_030::Initialize] SR = " << endl;
	cerr << "[CMS_EXO_17_030::Initialize] Wrong SR" << endl;
	exit(EXIT_FAILURE);
  }
  
  // Choose to run with gen-matched tools
  int gen_matched;
  cout << "[CMS_EXO_17_030::Initialize] Is triplets gen-matched? (0 for no, 1 for yes): "; 
  cin >> gen_matched;
  
  try {
	if (! (gen_matched==0 || gen_matched==1)) throw gen_matched;
	trigGen = gen_matched;
	cout << "[CMS_EXO_17_030::Initialize] trigGen = " << trigGen << endl;
  }
  catch (int gen_matched) {
	cerr << "[CMS_EXO_17_030::Initialize] gen_matched = " << gen_matched << endl;
	cerr << "[CMS_EXO_17_030::Initialize] Wrong input" << endl;
	exit(EXIT_FAILURE);
  }

  // Declaration of Jet ID cut
  Manager()->AddCut("LOW: preselection", Low_Mass_Region);
  Manager()->AddCut("HIGH: preselection", High_Mass_Region);
    
  // Declaration of the jet-pt cuts and HT cuts
  // pt(jets) requires all jet pt > ~GeV
  
  Manager()->AddCut("LOW: Njets>=6", Low_Mass_Region);
  Manager()->AddCut("HIGH: Njets>=6", High_Mass_Region);

  Manager()->AddCut("LOW: HT > 650GeV", Low_Mass_Region);
  Manager()->AddCut("HIGH: HT > 900GeV", High_Mass_Region);
  
  // Declaration of the sixth jet-pt cut
  Manager()->AddCut("SR1: pt(j6) > 40GeV", "Mg_200to400");
  Manager()->AddCut("SR2: pt(j6) > 50GeV", "Mg_400to700");
  Manager()->AddCut("SR3: pt(j6) > 125GeV", "Mg_700to1200");
  Manager()->AddCut("SR4: pt(j6) > 175GeV", "Mg_1200to2000");
  
  // Declaration of the D^2[6,3+3,2] cut
  Manager()->AddCut("SR1: D^2[6,3+3,2] < 1.25", "Mg_200to400");
  Manager()->AddCut("SR2: D^2[6,3+3,2] < 1.0", "Mg_400to700");
  Manager()->AddCut("SR3: D^2[6,3+3,2] < 0.9", "Mg_700to1200");
  Manager()->AddCut("SR4: D^2[6,3+3,2] < 0.75", "Mg_1200to2000");
  
  // Declaration of the Am cut - TripletPair cut
  Manager()->AddCut("SR1: Am < 0.25", "Mg_200to400");
  Manager()->AddCut("SR2: Am < 0.175", "Mg_400to700");
  Manager()->AddCut("SR3: Am < 0.15", "Mg_700to1200");
  Manager()->AddCut("SR4: Am < 0.15", "Mg_1200to2000");
  
  // Declaration of the Delta cut - Triplet cut
  Manager()->AddCut("SR1: Delta > 250GeV", "Mg_200to400");
  Manager()->AddCut("SR2: Delta > 180GeV", "Mg_400to700");
  Manager()->AddCut("SR3: Delta > 20GeV", "Mg_700to1200");
  Manager()->AddCut("SR4: Delta > -120GeV", "Mg_1200to2000");
                    
  // Declaration of the D^2[3,2] cut - Triplet cut
  Manager()->AddCut("SR1: D^2[3,2] < 0.05", "Mg_200to400");
  Manager()->AddCut("SR2: D^2[3,2] < 0.175", "Mg_400to700");
  Manager()->AddCut("SR3: D^2[3,2] < 0.2", "Mg_700to1200");
  Manager()->AddCut("SR4: D^2[3,2] < 0.25", "Mg_1200to2000");

  // validation histograms
  if (!trigGen) f = new TFile("test_SR" + TString::Itoa(SR, 10) + ".root", "recreate");
  if (trigGen) f = new TFile("gen_test_SR" + TString::Itoa(SR, 10) + ".root", "recreate");
  tr = new TTree("SR" + TString::Itoa(SR, 10), "");
  cutflow_event = new TH1D("cutflow_event_SR" + TString::Itoa(SR, 10), "", 10, 0., 10.);
  cutflow_pair = new TH1D("cutflow_pair_SR" + TString::Itoa(SR, 10), "", 10, 0., 10.);
  cutflow_triplet = new TH1D("cutflow_triplet_SR" + TString::Itoa(SR, 10), "", 10, 0., 10.);

  tr->Branch("triplet_mass", &triplet_mass);
  tr->Branch("triplet_deltaR", &triplet_delta);
  tr->Branch("triplet_mds32", &triplet_mds32);

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

  f->cd();
  cutflow_event->Write();
  cutflow_pair->Write();
  cutflow_triplet->Write();

  tr->Write();

  f->Close();

  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool CMS_EXO_17_030::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Event weight
  // using unbiased events, set the weight = 1. to calculated the acceptance
  double weight = 1.;
  Manager()->InitializeForNewEvent(weight);
  double nTrips = 20.;
  
  //if (Configuration().IsNoEventWeight()) myEventWeight=1.;
  //else if (event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  //else {
	//WARNING << "Found one event with a zero weight. Skipping...\n";
    //return false;
  //}
  //Manager()->InitializeForNewEvent(myEventWeight);
  //out << "myEventWeight = " << myEventWeight << endl;
  
  double ptCut[] = {30, 30, 50, 50};
  double HTcut[] = {650, 650, 900, 900};
  double l6ptCut[] = {40, 50, 125, 175};
  double mds6332Cut[] = {1.25, 1., 0.9, 0.75};
  double asymmCut[] = {0.25, 0.175, 0.15, 0.15};
  double deltaCut[] = {250, 180, 20, -120};
  double mds32Cut[] = {0.05, 0.175, 0.2, 0.25};
  bool passFlag = true;
  
  // The event loop start here
  if(event.rec() == 0) return true;
  
  // Select jets satisfying pt&eta cut
  double etaCut = 2.4;
  JetCollection jets = jetSelection(event, ptCut[SR-1], etaCut);
  SORTER->sort(jets);

  if (jets.size() == 0) passFlag = false;
  if (passFlag) {
	// preselection
	cutflow_event->Fill(0., weight);
	cutflow_triplet->Fill(0., weight*nTrips);
  }
  
  if (jets.size() < 6) passFlag = false;
  if (passFlag) {
	// Nj selection
	cutflow_event->Fill(1., weight);
	cutflow_triplet->Fill(1., weight*nTrips);
  }

  // Jet ID
  Manager()->SetCurrentEventWeight(weight*nTrips);
  if(!Manager()->ApplyCut(jets.size() != 0, "LOW: preselection")) return true;
  if(!Manager()->ApplyCut(jets.size() != 0, "HIGH: preselection")) return true;

  // Nj cut for low and high mass regions
  Manager()->SetCurrentEventWeight(weight*nTrips);
  if(!Manager()->ApplyCut(jets.size() >= 6, "LOW: Njets>=6") ) return true;
  if(!Manager()->ApplyCut(jets.size() >= 6, "HIGH: Njets>=6") ) return true;
  
  // HT cuts	
  double H_T = HT(jets);
  double l6pt = jets.at(5)->pt();

  if (H_T < HTcut[SR-1]) passFlag = false;
  if (passFlag) {
	// HT selection
	cutflow_event->Fill(2., weight);
	cutflow_triplet->Fill(2., weight*nTrips);
  }


  if (l6pt < l6ptCut[SR-1]) passFlag = false;
  if (passFlag) {
	// 6th jet pt selection
	cutflow_event->Fill(3., weight);
	cutflow_triplet->Fill(3., weight*nTrips);
  }

  // HT cut for low and high mass regions
  Manager()->SetCurrentEventWeight(weight*nTrips);
  if(!Manager()->ApplyCut(H_T > HTcut[0], "LOW: HT > 650GeV")) return true;
  if(!Manager()->ApplyCut(H_T > HTcut[2], "HIGH: HT > 900GeV")) return true;

  // 6th Jet Pt cut for each regions
  Manager()->SetCurrentEventWeight(weight*nTrips);
  if(!Manager()->ApplyCut(l6pt > l6ptCut[0], "SR1: pt(j6) > 40GeV") ) return true;
  if(!Manager()->ApplyCut(l6pt > l6ptCut[1], "SR2: pt(j6) > 50GeV") ) return true;
  if(!Manager()->ApplyCut(l6pt > l6ptCut[2], "SR3: pt(j6) > 125GeV")) return true;
  if(!Manager()->ApplyCut(l6pt > l6ptCut[3], "SR4: pt(j6) > 175GeV")) return true;

  // Mds6332 cut for each regions
  double evtMds6332 = mds6332(jets);

  if (evtMds6332 > mds6332Cut[SR-1]) passFlag = false;
  if (passFlag) {
	// mds6332 selection
	cutflow_event->Fill(4., weight);
	cutflow_triplet->Fill(4., weight*nTrips);
  }
  
  Manager()->SetCurrentEventWeight(weight*nTrips);
  if(!Manager()->ApplyCut(evtMds6332 < mds6332Cut[0], "SR1: D^2[6,3+3,2] < 1.25")) return true;
  if(!Manager()->ApplyCut(evtMds6332 < mds6332Cut[1], "SR2: D^2[6,3+3,2] < 1.0") ) return true;
  if(!Manager()->ApplyCut(evtMds6332 < mds6332Cut[2], "SR3: D^2[6,3+3,2] < 0.9") ) return true;
  if(!Manager()->ApplyCut(evtMds6332 < mds6332Cut[3], "SR4: D^2[6,3+3,2] < 0.75")) return true; 

  // Mass asymmetry cut
  // for each TripletPairs
  PairCollection tripPairs = makePairCollection(jets);
  TripletCollection trips = pairSelection(tripPairs, asymmCut[SR-1]);

  if (trigGen) trips = GenMatchedTriplets(event, trips);
  
  double nTrips_passAsymm = trips.size();
  nTrips *= nTrips_passAsymm / nTrips;

  // update flag
  if (trips.size() == 0) passFlag = false;

  // draw cutflow
  if (passFlag) {
	// mass asymmetry selection
	cutflow_event->Fill(5., weight);
	cutflow_triplet->Fill(5., weight*nTrips);
  }
	
  Manager()->SetCurrentEventWeight(weight*nTrips);
  if(!Manager()->ApplyCut(trips.size() != 0, "SR1: Am < 0.25")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR2: Am < 0.175")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR3: Am < 0.15")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR4: Am < 0.15")) return true;
  
  // Delta cut
  // for each Triplets
  trips = deltaSelection(trips, deltaCut[SR-1]);
	
  // update weight
  double nTrips_passDelta = trips.size();
  nTrips *= nTrips_passDelta/nTrips_passAsymm;

  // update flag
  if (trips.size() == 0) passFlag = false;

  // draw cutflow
  if (passFlag) {
	// delta selection
	cutflow_event->Fill(6., weight);
	cutflow_triplet->Fill(6., weight*nTrips);
  }
  
  Manager()->SetCurrentEventWeight(weight*nTrips);
  if(!Manager()->ApplyCut(trips.size() != 0, "SR1: Delta > 250GeV")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR2: Delta > 180GeV")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR3: Delta > 20GeV")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR4: Delta > -120GeV")) return true;
  
  // mds32 cut
  // for each Triplets
  trips = mds32Selection(trips, mds32Cut[SR-1]);

  // update weight
  double nTrips_passMDS32 = trips.size();
  nTrips *= nTrips_passMDS32/nTrips_passDelta;

  // update flag
  if (trips.size() == 0) passFlag = false;

  // draw cutflow
  if (passFlag) {
	// mds32
    cutflow_event->Fill(7., weight);
    cutflow_triplet->Fill(7., weight*nTrips);
  }
     
  Manager()->SetCurrentEventWeight(weight*nTrips);
  if(!Manager()->ApplyCut(trips.size() != 0, "SR1: D^2[3,2] < 0.05")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR2: D^2[3,2] < 0.175")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR3: D^2[3,2] < 0.2")) return true;
  if(!Manager()->ApplyCut(trips.size() != 0, "SR4: D^2[3,2] < 0.25")) return true;
  
  // fill trees
  triplet_mass.clear();
  triplet_delta.clear();
  triplet_mds32.clear();
  if (passFlag) {
	for (const auto &trip : trips) {
	  triplet_mass.push_back(mass(trip));
	  triplet_delta.push_back(delta(trip));
	  triplet_mds32.push_back(mds32(trip));
	}
  }
  tr->Fill();
  
  return true;  
}

//==== Functions to use
//==== 1. kinematic variables
MALorentzVector CMS_EXO_17_030::momentum(const Triplet &trip) { 
  return trip[0]->momentum() + trip[1]->momentum() + trip[2]->momentum();
}

double CMS_EXO_17_030::mass(const Triplet &trip) {
  MALorentzVector mom = momentum(trip);
  return mom.M();
}
  
double CMS_EXO_17_030::HT(const JetCollection &jetcoll) {
  double this_HT = 0;
  for (const auto &j : jetcoll) this_HT += j->pt();
  return this_HT;
}

double CMS_EXO_17_030::dalitz32(const Triplet &trip, const int &idx1, const int &idx2) {
  double M = pow((trip[idx1]->momentum()+trip[idx2]->momentum()).M(), 2);
  double M_123 = pow((trip[0]->momentum()+trip[1]->momentum()+trip[2]->momentum()).M(), 2);
  double M_1 = pow((trip[0]->momentum()).M(), 2);
  double M_2 = pow((trip[1]->momentum()).M(), 2);
  double M_3 = pow((trip[2]->momentum()).M(), 2);
  return M/(M_123+M_1+M_2+M_3);
}

double CMS_EXO_17_030::mds32(const Triplet &trip) {
  double c = 1./sqrt(3.);
  double out = 0.;
  for (int i = 0; i < 3; i++) {
	for (int j = i+1; j < 3; j++) {
	  out += pow( sqrt(dalitz32(trip, i, j))-c, 2);
	}
  }
  return out;
}

double CMS_EXO_17_030::dalitz6332(const JetCollection &jetcoll, const int &idx1, const int &idx2, const int &idx3) {
  double M = pow((jetcoll.at(idx1)->momentum() + jetcoll.at(idx2)->momentum() + jetcoll.at(idx3)->momentum() ).M(), 2); 
  MALorentzVector PTv;
  double massSum = 0;
  for (int i = 0; i < 6; i++) { 
	PTv += jetcoll.at(i)->momentum(); 
	massSum += pow((jetcoll.at(i)->momentum()).M(), 2);
  }
  double M_inv = pow(PTv.M(), 2);

  return M / (4*M_inv + 6*massSum);
}

double CMS_EXO_17_030::mds6332(const JetCollection &jetcoll) {
  double out = 0; double c = 1./sqrt(20.);
  try {
	if (jetcoll.size() < 6) throw jetcoll;

	for (int i = 0; i < 6; i++) {
	  for (int j = i+1; j < 6; j++) {
		for (int k = j+1; k < 6; k++) {
		  Triplet this_trip = {jetcoll.at(i), jetcoll.at(j), jetcoll.at(k)};
		  double this_sum = dalitz6332(jetcoll, i, j, k) + mds32(this_trip);
		  this_sum = sqrt(this_sum) - c;
		  out += pow(this_sum, 2);
		}
	  }
	}
	return out;
  }
  
  catch (JetCollection jetcoll) {
	cerr << "[CMS_EXO_17_030::mds6332] nJets should be 6" << endl;
	exit(EXIT_FAILURE);
  }
}

double CMS_EXO_17_030::massAsymm(const TripletPair &pair) {
  double mass1 = mass(pair.first);
  double mass2 = mass(pair.second);

  return fabs(mass1 - mass2) / (mass1 + mass2);
}

double CMS_EXO_17_030::delta(const Triplet &trip) {
  double this_HT = 0.;
  for (const auto &j : trip) this_HT += j->pt();
  double this_mass = mass(trip);
  
  return this_HT - this_mass;
}

//==== 2. selections
JetCollection CMS_EXO_17_030::jetSelection(const EventFormat &event, const double &ptCut, const double &etaCut) {
  JetCollection out;
  
  for (const auto &j : event.rec()->jets() ) {
	if (j.pt() > ptCut && fabs(j.eta()) < etaCut) out.push_back(&j); 
  }
  
  return out;
}

TripletCollection CMS_EXO_17_030::pairSelection(const PairCollection &pairs, const double &asymmCut) {
  TripletCollection out;
  
  for (const auto &pair : pairs) {
	if (massAsymm(pair) < asymmCut) {
	  out.push_back(pair.first);
	  out.push_back(pair.second);
	}
  }
  
  return out;
}

TripletCollection CMS_EXO_17_030::deltaSelection(const TripletCollection &trips, const double &deltaCut) {
  TripletCollection out;

  for (const auto &trip : trips) {
	if (delta(trip) > deltaCut) out.push_back(trip);
  }
  
  return out;
}

TripletCollection CMS_EXO_17_030::mds32Selection(const TripletCollection &trips, const double &mdsCut) {
  TripletCollection out;

  for (const auto &trip : trips) {
	if (mds32(trip) < mdsCut) out.push_back(trip);
  }

  return out;
}

//==== 3. tools
PairCollection CMS_EXO_17_030::makePairCollection(const JetCollection &jetcoll) {
  PairCollection out;
  
  try {
	if (jetcoll.size() < 6) throw jetcoll;

	TripletCollection trips;
	for (int i = 0; i < 6; i++) {
	  for (int j = i+1; j < 6; j++) {
		for (int k = j+1; k < 6; k++) {
		  trips.push_back({jetcoll.at(i), jetcoll.at(j), jetcoll.at(k)});
		}
	  }
	}

	for (int i = 0; i < 10; i++) out.push_back(make_pair(trips.at(i), trips.at(19-i)));
	return out;
  }

  catch (JetCollection jetcoll) {
	cerr << "[CMS_EXO_17_030::makePairCollection] need at least 6 jets to make a collection" << endl;
	exit(EXIT_FAILURE);
  }
}

TripletCollection CMS_EXO_17_030::GenMatchedTriplets(const EventFormat &event, const JetCollection &jetcoll) {
  JetCollection matched_jets1, matched_jets2;
  TripletCollection matched_trips;
  const vector<MCParticleFormat> &gens = event.mc()->particles();

  bool matched;
  for (const auto &gen : gens) {
	if (1<=gen.pdgid()&&gen.pdgid()<=3&&(gen.mothers()).at(0)->pdgid()==1000021) {
	  for (const auto &j : jetcoll) {
		matched = (j->momentum()).DeltaR(gen.momentum()) < 0.3;
		if (matched) matched_jets1.push_back(j);
	  }
	}
	else if (-3<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)->pdgid()==1000021) {
	  for (const auto &j : jetcoll) {
		matched = (j->momentum()).DeltaR(gen.momentum()) < 0.3;
		if (matched) matched_jets2.push_back(j);
	  }
	}
  }

  // remove double matching
  sort(matched_jets1.begin(), matched_jets1.end());
  auto last1 = unique(matched_jets1.begin(), matched_jets1.end());
  matched_jets1.erase(last1, matched_jets1.end());

  sort(matched_jets2.begin(), matched_jets2.end());
  auto last2 = unique(matched_jets2.begin(), matched_jets2.end());
  matched_jets2.erase(last2, matched_jets2.end());

  if (matched_jets1.size() == 3) matched_trips.push_back({matched_jets1.at(0), matched_jets1.at(1), matched_jets1.at(2)});
  if (matched_jets2.size() == 3) matched_trips.push_back({matched_jets2.at(0), matched_jets2.at(1), matched_jets2.at(2)});

  return matched_trips;
}

TripletCollection CMS_EXO_17_030::GenMatchedTriplets(const EventFormat &event, const TripletCollection &trips) {
  JetCollection matched_jets1, matched_jets2;
  TripletCollection matched_trips;
  const vector<MCParticleFormat> &gens = event.mc()->particles();

  bool matched;
  for (const auto &trip : trips) {
	for (const auto &gen : gens) {
	  if (1<=gen.pdgid()&&gen.pdgid()<=3&&(gen.mothers()).at(0)->pdgid()==1000021) {
		for (const auto &j : trip) {
		  matched = (j->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets1.push_back(j);
		}
	  }
	  else if (-3<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)->pdgid()==1000021) {
		for (const auto &j : trip) {
		  matched = (j->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets2.push_back(j);
		}
	  }
	}
	
	// remove double matching
	sort(matched_jets1.begin(), matched_jets1.end());
	auto last1 = unique(matched_jets1.begin(), matched_jets1.end());
	matched_jets1.erase(last1, matched_jets1.end());

	sort(matched_jets2.begin(), matched_jets2.end());
	auto last2 = unique(matched_jets2.begin(), matched_jets2.end());
	matched_jets2.erase(last2, matched_jets2.end());

	if (matched_jets1.size() == 3) matched_trips.push_back({matched_jets1.at(0), matched_jets1.at(1), matched_jets1.at(2)});
	if (matched_jets2.size() == 3) matched_trips.push_back({matched_jets2.at(0), matched_jets2.at(1), matched_jets2.at(2)});
	
	// prepare for next iteration	
	matched_jets1.clear();
	matched_jets2.clear();
  } 
  
  return matched_trips;
}
