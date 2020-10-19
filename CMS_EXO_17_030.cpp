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
  INFO << "      <>   Contact: choij@cern.ch                     <>" << endmsg;
  INFO << "      <>            soohyun.yun@cern.ch               <>" << endmsg;
  INFO << "      <>            jihun.k@cern.ch                   <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.8                <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  
  // Declaration of the signal regions (SR)
  Manager()->AddRegionSelection("Mg_200to400");
  Manager()->AddRegionSelection("Mg_400to700");
  Manager()->AddRegionSelection("Mg_700to1200");
  Manager()->AddRegionSelection("Mg_1200to2000");
  
  // Signal Region Partitions
  std::string All_Region[]={"Mg_200to400", "Mg_400to700", "Mg_700to1200", "Mg_1200to2000"};

  std::string Low_Mass_Region[] = {"Mg_200to400", "Mg_400to700"};
  std::string High_Mass_Region[] = {"Mg_700to1200", "Mg_1200to2000"};

  // Declaration of Jet ID cut
  //Manager()->AddCut("ALL: perselection", All_Region);
  Manager()->AddCut("LOW: preselection", Low_Mass_Region);
  Manager()->AddCut("HIGH: preselection", High_Mass_Region);
    
  // Declaration of the jet-pt cuts and HT cuts
  // pt(jets) requires all jet pt > ~GeV
  
  //Manager()->AddCut("ALL: Njets>=6", All_Region);
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
  double weight;
  if (Configuration().IsNoEventWeight()) weight = 1.;
  else if (event.mc()->weight() != 0.) weight = event.mc()->weight();
  else return false;
  
  //double nTrips = 20.;
  //double nTrips[] = {20., 20., 20., 20.};
  Manager()->InitializeForNewEvent(weight*20.);
  
  double ptCut[] = {30, 30, 50, 50};
  double HTcut[] = {650, 650, 900, 900};
  double l6ptCut[] = {40, 50, 125, 175};
  double mds6332Cut[] = {1.25, 1., 0.9, 0.75};
  double asymmCut[] = {0.25, 0.175, 0.15, 0.15};
  double deltaCut[] = {250, 180, 20, -120};
  double mds32Cut[] = {0.05, 0.175, 0.2, 0.25};
  
  // The event loop start here
  if(event.rec() == 0) return true;
  
  // Select jets satisfying pt&eta cut
  double etaCut = 2.4;
  JetCollection jets[4];
  for (int i = 0; i < 4; i++) {
	jets[i] = jetSelection(event, ptCut[i], etaCut);
	SORTER->sort(jets[i]);
  }
  //JetCollection jets = jetSelection(event, ptCut[SR-1], etaCut);
  //SORTER->sort(jets);
  // Jet ID
  //if(!Manager()->ApplyCut(jets.size() != 0, "ALL: preselection")) return true;
  if(!Manager()->ApplyCut(jets[0].size() != 0, "LOW: preselection")) return true;
  if(!Manager()->ApplyCut(jets[2].size() != 0, "HIGH: preselection")) return true;

  // Nj cut for low and high mass regions
  //if(!Manager()->ApplyCut(jets.size() >= 6, "ALL: Njets>=6")) return true;
  if(!Manager()->ApplyCut(jets[0].size() >= 6, "LOW: Njets>=6")) return true;
  if(!Manager()->ApplyCut(jets[2].size() >= 6, "HIGH: Njets>=6")) return true;
  
  // HT cuts
  double H_T[4], l6pt[4];
  for (int i = 0; i < 4; i++) {
	H_T[i] = HT(jets[i]);
	if (jets[i].size() > 5)
	  l6pt[i] = jets[i].at(5)->pt();
	else l6pt[i] = 0.;
  }
  
  //double H_T = HT(jets);
  //double l6pt = jets.at(5)->pt();

  // HT cut for low and high mass regions
  if(!Manager()->ApplyCut(H_T[0] > HTcut[0], "LOW: HT > 650GeV")) return true;
  if(!Manager()->ApplyCut(H_T[2] > HTcut[2], "HIGH: HT > 900GeV")) return true;

  // 6th Jet Pt cut for each regions
  if(!Manager()->ApplyCut(l6pt[0] > l6ptCut[0], "SR1: pt(j6) > 40GeV") ) return true;
  if(!Manager()->ApplyCut(l6pt[1] > l6ptCut[1], "SR2: pt(j6) > 50GeV") ) return true;
  if(!Manager()->ApplyCut(l6pt[2] > l6ptCut[2], "SR3: pt(j6) > 125GeV")) return true;
  if(!Manager()->ApplyCut(l6pt[3] > l6ptCut[3], "SR4: pt(j6) > 175GeV")) return true;
  
  // Mds6332 cut for each regions
  double evtMds6332[4];
  for (int i = 0; i < 4; i++) {
	if (jets[i].size() > 5)
	  evtMds6332[i] = mds6332(jets[i]);
	else evtMds6332[i] = 999.;
  }
  
  //double evtMds6332 = mds6332(jets);

  if(!Manager()->ApplyCut(evtMds6332[0] < mds6332Cut[0], "SR1: D^2[6,3+3,2] < 1.25")) return true;
  if(!Manager()->ApplyCut(evtMds6332[1] < mds6332Cut[1], "SR2: D^2[6,3+3,2] < 1.0") ) return true;
  if(!Manager()->ApplyCut(evtMds6332[2] < mds6332Cut[2], "SR3: D^2[6,3+3,2] < 0.9") ) return true;
  if(!Manager()->ApplyCut(evtMds6332[3] < mds6332Cut[3], "SR4: D^2[6,3+3,2] < 0.75")) return true; 

  // Mass asymmetry cut
  // for each TripletPairs
  PairCollection tripPairs[4];
  TripletCollection trips[4];
  for (int i = 0; i < 4; i++) {
	if (jets[i].size() > 5)
	  tripPairs[i] = makePairCollection(jets[i]);
	trips[i] = pairSelection(tripPairs[i], asymmCut[i]);
	trips[i] = GenMatchedTriplets(event, trips[i]);
  }
  
  //PairCollection tripPairs = makePairCollection(jets);
  //TripletCollection trips = pairSelection(tripPairs, asymmCut[SR-1]);
  //trips = GenMatchedTriplets(event, trips);
  
  double nTrips_passAsymm[4];
  for (int i = 0; i < 4; i++) {
	nTrips_passAsymm[i] = trips[i].size();
    //nTrips[i] *= nTrips_passAsymm[i] / nTrips[i];
  }
  
  Manager()->SetCurrentEventWeight(weight*nTrips_passAsymm[0]); 
  if(!Manager()->ApplyCut(trips[0].size() != 0, "SR1: Am < 0.25")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passAsymm[1]);
  if(!Manager()->ApplyCut(trips[1].size() != 0, "SR2: Am < 0.175")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passAsymm[2]);
  if(!Manager()->ApplyCut(trips[2].size() != 0, "SR3: Am < 0.15")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passAsymm[3]);
  if(!Manager()->ApplyCut(trips[3].size() != 0, "SR4: Am < 0.15")) return true;

  // Delta cut
  //trips = deltaSelection(trips, deltaCut[SR-1]);
  double nTrips_passDelta[4];
  for (int i = 0; i < 4; i++) {
	// select triplets
	trips[i] = deltaSelection(trips[i], deltaCut[i]);

	// update nTrips
	nTrips_passDelta[i] = trips[i].size();
	//nTrips[i] *= nTrips_passDelta[i]/nTrips_passAsymm[i];
  }
  
  Manager()->SetCurrentEventWeight(weight*nTrips_passDelta[0]);
  if(!Manager()->ApplyCut(trips[0].size() != 0, "SR1: Delta > 250GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passDelta[1]);
  if(!Manager()->ApplyCut(trips[1].size() != 0, "SR2: Delta > 180GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passDelta[2]);
  if(!Manager()->ApplyCut(trips[2].size() != 0, "SR3: Delta > 20GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passDelta[3]);
  if(!Manager()->ApplyCut(trips[3].size() != 0, "SR4: Delta > -120GeV")) return true;

  // mds32 cut
  // for each Triplets
  double nTrips_passMDS32[4];
  for (int i = 0; i < 4; i++) {
	// select triplets
	trips[i] = mds32Selection(trips[i], mds32Cut[i]);
	
	// update nTrips
	nTrips_passMDS32[i] = trips[i].size();
	//nTrips[i] *= nTrips_passMDS32[i]/nTrips_passDelta[i];
  }
  
  //trips = mds32Selection(trips, mds32Cut[SR-1]);

  // update nTrips
  //double nTrips_passMDS32 = trips.size();
  //nTrips *= nTrips_passMDS32/nTrips_passDelta;
  Manager()->SetCurrentEventWeight(weight*nTrips_passMDS32[0]);
  if(!Manager()->ApplyCut(trips[0].size() != 0, "SR1: D^2[3,2] < 0.05")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passMDS32[1]);
  if(!Manager()->ApplyCut(trips[1].size() != 0, "SR2: D^2[3,2] < 0.175")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passMDS32[2]);
  if(!Manager()->ApplyCut(trips[2].size() != 0, "SR3: D^2[3,2] < 0.2")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passMDS32[3]);
  if(!Manager()->ApplyCut(trips[3].size() != 0, "SR4: D^2[3,2] < 0.25")) return true;

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
  for (unsigned int i = 0; i < jetcoll.size(); i++)
	this_HT += jetcoll.at(i)->pt();
  //for (const auto &j : jetcoll) this_HT += j->pt();
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

double CMS_EXO_17_030::massAsymm(const TripletPair &pair) {
  double mass1 = mass(pair.first);
  double mass2 = mass(pair.second);

  return fabs(mass1 - mass2) / (mass1 + mass2);
}

double CMS_EXO_17_030::delta(const Triplet &trip) {
  double this_HT = 0.;
  for (unsigned int i = 0; i < trip.size(); i++)
	this_HT += trip.at(i)->pt();
  //for (const auto &j : trip) this_HT += j->pt();
  double this_mass = mass(trip);
  
  return this_HT - this_mass;
}

//==== 2. selections
JetCollection CMS_EXO_17_030::jetSelection(const EventFormat &event, const double &ptCut, const double &etaCut) {
  JetCollection out;
  
  for (unsigned int i = 0; i < (event.rec()->jets()).size(); i++) {
	const RecJetFormat& this_jet = (event.rec()->jets()).at(i);
	if ((this_jet.pt() > ptCut) && (fabs(this_jet.eta()) < etaCut))
	  out.push_back(&this_jet);
  }

  //  for (const auto &j : event.rec()->jets())
  //	if (j.pt() > ptCut && fabs(j.eta()) < etaCut) 
  //	  out.push_back(&j); 

  
  return out;
}

TripletCollection CMS_EXO_17_030::pairSelection(const PairCollection &pairs, const double &asymmCut) {
  TripletCollection out;
 
  for (unsigned int i = 0; i < pairs.size(); i++) {
	const TripletPair& this_pair = pairs.at(i);
	if (massAsymm(this_pair) < asymmCut) {
	  out.push_back(this_pair.first);
	  out.push_back(this_pair.second);
	}
  }

  //for (const auto &pair : pairs) {
  //	if (massAsymm(pair) < asymmCut) {
  //	  out.push_back(pair.first);
  //	  out.push_back(pair.second);
  //	}
  //}
  
  return out;
}

TripletCollection CMS_EXO_17_030::deltaSelection(const TripletCollection &trips, const double &deltaCut) {
  TripletCollection out;

  for (unsigned int i = 0; i < trips.size(); i++) {
	const Triplet& this_trip = trips.at(i);
	if (delta(this_trip) > deltaCut)
	  out.push_back(this_trip);
  }

  //for (const auto &trip : trips) {
  //	if (delta(trip) > deltaCut) out.push_back(trip);
  //}
  
  return out;
}

TripletCollection CMS_EXO_17_030::mds32Selection(const TripletCollection &trips, const double &mdsCut) {
  TripletCollection out;

  for (unsigned int i = 0; i < trips.size(); i++) {
	const Triplet& this_trip = trips.at(i);
	if (mds32(this_trip) < mdsCut)
	  out.push_back(this_trip);
  }

  //for (const auto &trip : trips) {
  //	if (mds32(trip) < mdsCut) out.push_back(trip);
  //}

  return out;
}

//==== 3. tools
PairCollection CMS_EXO_17_030::makePairCollection(const JetCollection &jetcoll) {
  PairCollection out;

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

TripletCollection CMS_EXO_17_030::GenMatchedTriplets(const EventFormat &event, const TripletCollection &trips) {
  JetCollection matched_jets1, matched_jets2, matched_jets3, matched_jets4;
  TripletCollection matched_trips;
  const vector<MCParticleFormat> &gens = event.mc()->particles();
  vector<const MCParticleFormat*> p_gluinos;
 
  for (unsigned int i = 0; i < gens.size(); i++) {
	const MCParticleFormat& gen = gens.at(i);
	if (1<=gen.pdgid()&&gen.pdgid()<=4&&(gen.mothers()).at(0)->pdgid()==1000021) 
	  p_gluinos.push_back((gen.mothers()).at(0));
	if (-4<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)->pdgid()==1000021) 
	  p_gluinos.push_back((gen.mothers()).at(0));
  }
  //for (const auto &gen : gens) {
  //	if (1<=gen.pdgid()&&gen.pdgid()<=4&&(gen.mothers()).at(0)->pdgid()==1000021) p_gluinos.push_back((gen.mothers()).at(0));
  //	if (-4<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)->pdgid()==1000021) p_gluinos.push_back((gen.mothers()).at(0));
  //}

  sort(p_gluinos.begin(), p_gluinos.end());
  vector<const MCParticleFormat*>::iterator last;
  last = unique(p_gluinos.begin(), p_gluinos.end());
  //auto last = unique(p_gluinos.begin(), p_gluinos.end());
  p_gluinos.erase(last, p_gluinos.end());
  
  // start matching
  bool matched;
  for (unsigned int i = 0; i < trips.size(); i++) {
	for (unsigned int j = 0; j < gens.size(); j++) {
	  const Triplet& trip = trips.at(i);
	  const MCParticleFormat& gen = gens.at(j);
	  if (1<=gen.pdgid()&&gen.pdgid()<=4&&((gen.mothers()).at(0)==p_gluinos.at(0))) {
		for (unsigned int k = 0; k < trip.size(); k++) {
		  const RecJetFormat* jet = trip.at(k);
		  matched = (jet->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets1.push_back(jet);
		}
	  }
	  else if (1<=gen.pdgid()&&gen.pdgid()<=4&&((gen.mothers()).at(0)==p_gluinos.at(1))) {
		for (unsigned int k = 0; k < trip.size(); k++) {
		  const RecJetFormat* jet = trip.at(k);
		  matched = (jet->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets2.push_back(jet);
		}
	  }
	  else if (-4<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)==p_gluinos.at(0)) {
		for (unsigned int k = 0; k < trip.size(); k++) {
		  const RecJetFormat* jet = trip.at(k);
		  matched = (jet->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets3.push_back(jet);
		}
	  }
	  else if (-4<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)==p_gluinos.at(1)) {
		for (unsigned int k = 0; k < trip.size(); k++) {
		  const RecJetFormat* jet = trip.at(k);
		  matched = (jet->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets3.push_back(jet);
		}
	  }
	}
  /*	  
  for (const auto &trip : trips) {
	for (const auto &gen : gens) {
	  if (1<=gen.pdgid()&&gen.pdgid()<=4&&((gen.mothers()).at(0)==p_gluinos.at(0))) {
		for (const auto &j : trip) {
		  matched = (j->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets1.push_back(j);
		}
	  }
	  else if (1<=gen.pdgid()&&gen.pdgid()<=4&&((gen.mothers()).at(0)==p_gluinos.at(1))) {
	    for (const auto &j : trip) {
		  matched = (j->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets2.push_back(j);
		}
	  }

	  else if (-4<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)==p_gluinos.at(0)) {
		for (const auto &j : trip) {
		  matched = (j->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets3.push_back(j);
		}
	  }
	  else if (-4<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)==p_gluinos.at(1)) {
	    for (const auto &j : trip) {
		  matched = (j->momentum()).DeltaR(gen.momentum()) < 0.3;
		  if (matched) matched_jets4.push_back(j);
		}
	  }
	}
	*/

	// remove double matching
	JetCollection::iterator last1, last2, last3, last4;
	sort(matched_jets1.begin(), matched_jets1.end());
	last1 = unique(matched_jets1.begin(), matched_jets1.end());
	matched_jets1.erase(last1, matched_jets1.end());

	sort(matched_jets2.begin(), matched_jets2.end());
	last2 = unique(matched_jets2.begin(), matched_jets2.end());
	matched_jets2.erase(last2, matched_jets2.end());

	sort(matched_jets3.begin(), matched_jets3.end());
    last3 = unique(matched_jets3.begin(), matched_jets3.end());
    matched_jets3.erase(last3, matched_jets3.end());

    sort(matched_jets4.begin(), matched_jets4.end());
    last4 = unique(matched_jets4.begin(), matched_jets4.end());
    matched_jets4.erase(last4, matched_jets4.end());

	if (matched_jets1.size() == 3) matched_trips.push_back({matched_jets1.at(0), matched_jets1.at(1), matched_jets1.at(2)});
	if (matched_jets2.size() == 3) matched_trips.push_back({matched_jets2.at(0), matched_jets2.at(1), matched_jets2.at(2)});
	if (matched_jets3.size() == 3) matched_trips.push_back({matched_jets3.at(0), matched_jets3.at(1), matched_jets3.at(2)});
	if (matched_jets4.size() == 3) matched_trips.push_back({matched_jets4.at(0), matched_jets4.at(1), matched_jets4.at(2)});
	
	// prepare for next iteration	
	matched_jets1.clear();
	matched_jets2.clear();
	matched_jets3.clear();
	matched_jets4.clear();
  }

  //if (matched_trips.size() > 2) cout << "WARNING: matched_trips.size() == " << matched_trips.size() << endl; 
  return matched_trips;
}

