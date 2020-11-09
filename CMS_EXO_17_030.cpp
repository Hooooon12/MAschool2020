#include "SampleAnalyzer/User/Analyzer/CMS_EXO_17_030.h"
#define CMS_EXO_17_030_PID 1000021
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool CMS_EXO_17_030::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
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
  
  // Initial setting for the mother particle
  WARNING << "Triplets will be matched to the particle with PID " << CMS_EXO_17_030_PID << endmsg;
  WARNING << "Change CMS_EXO_17_030_PID for your triplets" << endmsg;

  // Declaration of the signal regions (SR)
  Manager()->AddRegionSelection("Mg_200to400");
  Manager()->AddRegionSelection("Mg_400to700");
  Manager()->AddRegionSelection("Mg_700to1200");
  Manager()->AddRegionSelection("Mg_1200to2000");
  Manager()->AddRegionSelection("Mass_200to300");
  Manager()->AddRegionSelection("Mass_300to400");
  Manager()->AddRegionSelection("Mass_400to500");
  Manager()->AddRegionSelection("Mass_500to600");
  Manager()->AddRegionSelection("Mass_600to700");
  Manager()->AddRegionSelection("Mass_700to800");
  Manager()->AddRegionSelection("Mass_800to900");
  Manager()->AddRegionSelection("Mass_900to1000");
  Manager()->AddRegionSelection("Mass_1000to1100");
  Manager()->AddRegionSelection("Mass_1100to1200");
  Manager()->AddRegionSelection("Mass_1200to1300");
  Manager()->AddRegionSelection("Mass_1300to1400");
  Manager()->AddRegionSelection("Mass_1400to1500");
  Manager()->AddRegionSelection("Mass_1500to1600");
  Manager()->AddRegionSelection("Mass_1600to1700");
  Manager()->AddRegionSelection("Mass_1700to1800");
  Manager()->AddRegionSelection("Mass_1800to1900");
  Manager()->AddRegionSelection("Mass_1900to2000");
  
  // Signal Region Partitions
  std::string All_Region[] = {
	// Signal regions
	"Mg_200to400", "Mg_400to700", "Mg_700to1200", "Mg_1200to2000",
	// Mass partition 1
	"Mass_200to300", "Mass_300to400",
	// Mass partition 2
	"Mass_400to500", "Mass_500to600", "Mass_600to700",
	// Mass partition 3
	"Mass_700to800", "Mass_800to900", "Mass_900to1000" ,"Mass_1000to1100" ,"Mass_1100to1200", 
	// Mass partition 4
	"Mass_1200to1300", "Mass_1300to1400", "Mass_1400to1500", "Mass_1500to1600", "Mass_1600to1700", "Mass_1700to1800", "Mass_1800to1900", "Mass_1900to2000"
  };

  std::string Low_Mass_Region[] = {
	"Mg_200to400", "Mg_400to700",
	"Mass_200to300", "Mass_300to400",
	"Mass_400to500", "Mass_500to600", "Mass_600to700"
  };
  std::string High_Mass_Region[] = {
	"Mg_700to1200", "Mg_1200to2000",
    "Mass_700to800", "Mass_800to900", "Mass_900to1000" ,"Mass_1000to1100" ,"Mass_1100to1200",
	"Mass_1200to1300", "Mass_1300to1400", "Mass_1400to1500", "Mass_1500to1600", "Mass_1600to1700", "Mass_1700to1800", "Mass_1800to1900", "Mass_1900to2000"
  };
  std::string SR1[] = {"Mg_200to400", "Mass_200to300", "Mass_300to400"};
  std::string SR2[] = {"Mg_400to700", "Mass_400to500", "Mass_500to600", "Mass_600to700"};
  std::string SR3[] = {"Mg_700to1200", "Mass_700to800", "Mass_800to900", "Mass_900to1000" ,"Mass_1000to1100" ,"Mass_1100to1200"};
  std::string SR4[] = {"Mg_1200to2000", "Mass_1200to1300", "Mass_1300to1400", "Mass_1400to1500", "Mass_1500to1600", "Mass_1600to1700", "Mass_1700to1800", "Mass_1800to1900", "Mass_1900to2000"};

    
  // Declaration of the preselection and HT cuts 
  Manager()->AddCut("ALL: Njets>=6", All_Region);

  Manager()->AddCut("LOW: preselection", Low_Mass_Region);
  Manager()->AddCut("HIGH: preselection", High_Mass_Region);

  Manager()->AddCut("LOW: HT > 650GeV", Low_Mass_Region);
  Manager()->AddCut("HIGH: HT > 900GeV", High_Mass_Region);
  
  // Declaration of the sixth jet-pt cut
  Manager()->AddCut("SR1: pt(j6) > 40GeV", SR1);
  Manager()->AddCut("SR2: pt(j6) > 50GeV", SR2);
  Manager()->AddCut("SR3: pt(j6) > 125GeV", SR3);
  Manager()->AddCut("SR4: pt(j6) > 175GeV", SR4);
  
  // Declaration of the D^2[6,3+3,2] cut
  Manager()->AddCut("SR1: D^2[6,3+3,2] < 1.25", SR1);
  Manager()->AddCut("SR2: D^2[6,3+3,2] < 1.0", SR2);
  Manager()->AddCut("SR3: D^2[6,3+3,2] < 0.9", SR3);
  Manager()->AddCut("SR4: D^2[6,3+3,2] < 0.75", SR4);
  
  // Declaration of the Am cut - TripletPair cut
  Manager()->AddCut("SR1: Am < 0.25", SR1);
  Manager()->AddCut("SR2: Am < 0.175", SR2);
  Manager()->AddCut("SR3: Am < 0.15", SR3);
  Manager()->AddCut("SR4: Am < 0.15", SR4);
  
  // Declaration of the Delta cut - Triplet cut
  Manager()->AddCut("SR1: Delta > 250GeV", SR1);
  Manager()->AddCut("SR2: Delta > 180GeV", SR2);
  Manager()->AddCut("SR3: Delta > 20GeV", SR3);
  Manager()->AddCut("SR4: Delta > -120GeV", SR4);
                    
  // Declaration of the D^2[3,2] cut - Triplet cut
  Manager()->AddCut("SR1: D^2[3,2] < 0.05", SR1);
  Manager()->AddCut("SR2: D^2[3,2] < 0.175", SR2);
  Manager()->AddCut("SR3: D^2[3,2] < 0.2", SR3);
  Manager()->AddCut("SR4: D^2[3,2] < 0.25", SR4);

  // mass partition
  Manager()->AddCut("SR1: 200 < M(jjj) < 300GeV", "Mass_200to300");
  Manager()->AddCut("SR1: 300 < M(jjj) < 400GeV", "Mass_300to400");
  Manager()->AddCut("SR2: 400 < M(jjj) < 500GeV", "Mass_400to500");
  Manager()->AddCut("SR2: 500 < M(jjj) < 600GeV", "Mass_500to600");
  Manager()->AddCut("SR2: 600 < M(jjj) < 700GeV", "Mass_600to700");
  Manager()->AddCut("SR3: 700 < M(jjj) < 800GeV", "Mass_700to800");
  Manager()->AddCut("SR3: 800 < M(jjj) < 900GeV", "Mass_800to900");
  Manager()->AddCut("SR3: 900 < M(jjj) < 1000GeV", "Mass_900to1000");
  Manager()->AddCut("SR3: 1000 < M(jjj) < 1100GeV", "Mass_1000to1100");
  Manager()->AddCut("SR3: 1100 < M(jjj) < 1200GeV", "Mass_1100to1200");
  Manager()->AddCut("SR4: 1200 < M(jjj) < 1300GeV", "Mass_1200to1300");
  Manager()->AddCut("SR4: 1300 < M(jjj) < 1400GeV", "Mass_1300to1400");
  Manager()->AddCut("SR4: 1400 < M(jjj) < 1500GeV", "Mass_1400to1500");
  Manager()->AddCut("SR4: 1500 < M(jjj) < 1600GeV", "Mass_1500to1600");
  Manager()->AddCut("SR4: 1600 < M(jjj) < 1700GeV", "Mass_1600to1700");
  Manager()->AddCut("SR4: 1700 < M(jjj) < 1800GeV", "Mass_1700to1800");
  Manager()->AddCut("SR4: 1800 < M(jjj) < 1900GeV", "Mass_1800to1900");
  Manager()->AddCut("SR4: 1900 < M(jjj) < 2000GeV", "Mass_1900to2000");


  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void CMS_EXO_17_030::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files) {}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool CMS_EXO_17_030::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Event weight
  double weight;
  if (Configuration().IsNoEventWeight()) weight = 1.;
  else if (event.mc()->weight() != 0.) weight = event.mc()->weight();
  else return false;
  
  const double nTrips = 20.;
  const int nRegions = 4;
  Manager()->InitializeForNewEvent(weight*nTrips);
  
  const double ptCut[] = {30, 30, 50, 50};
  const double HTcut[] = {650, 650, 900, 900};
  const double j6ptCut[] = {40, 50, 125, 175};
  const double mds6332Cut[] = {1.25, 1., 0.9, 0.75};
  const double asymmCut[] = {0.25, 0.175, 0.15, 0.15};
  const double deltaCut[] = {250, 180, 20, -120};
  const double mds32Cut[] = {0.05, 0.175, 0.2, 0.25};
  
  // The event loop start here
  if(event.rec() == 0) return true;
  
  // Select jets satisfying pt&eta cut
  const double etaCut = 2.4;
  const double basePtCut = 20.;
  JetCollection jets = jetSelection(event, basePtCut, etaCut);
  SORTER->sort(jets);
  
  // Nj cut for low and high mass regions
  if(!Manager()->ApplyCut(jets.size() >= 6, "ALL: Njets>=6")) return true;
 
  // confirm jet pt cut
  if(!Manager()->ApplyCut(jets.at(5)->pt() > ptCut[0], "LOW: preselection")) return true;
  if(!Manager()->ApplyCut(jets.at(5)->pt() > ptCut[2], "HIGH: preselection")) return true;
  
  // HT, j6pt cut
  double H_T = HT(jets);
  double j6pt = jets.at(5)->pt();

  // HT cut for low and high mass regions
  if(!Manager()->ApplyCut(H_T > HTcut[0], "LOW: HT > 650GeV")) return true;
  if(!Manager()->ApplyCut(H_T > HTcut[2], "HIGH: HT > 900GeV")) return true;

  // 6th Jet Pt cut for each regions
  if(!Manager()->ApplyCut(j6pt > j6ptCut[0], "SR1: pt(j6) > 40GeV") ) return true;
  if(!Manager()->ApplyCut(j6pt > j6ptCut[1], "SR2: pt(j6) > 50GeV") ) return true;
  if(!Manager()->ApplyCut(j6pt > j6ptCut[2], "SR3: pt(j6) > 125GeV")) return true;
  if(!Manager()->ApplyCut(j6pt > j6ptCut[3], "SR4: pt(j6) > 175GeV")) return true;
  
  // Mds6332 cut
  double evtMds6332 = mds6332(jets);
  
  if(!Manager()->ApplyCut(evtMds6332 < mds6332Cut[0], "SR1: D^2[6,3+3,2] < 1.25")) return true;
  if(!Manager()->ApplyCut(evtMds6332 < mds6332Cut[1], "SR2: D^2[6,3+3,2] < 1.0") ) return true;
  if(!Manager()->ApplyCut(evtMds6332 < mds6332Cut[2], "SR3: D^2[6,3+3,2] < 0.9") ) return true;
  if(!Manager()->ApplyCut(evtMds6332 < mds6332Cut[3], "SR4: D^2[6,3+3,2] < 0.75")) return true; 

  // Mass asymmetry cut
  PairCollection tripPairs = makePairCollection(jets);
  TripletCollection trips[nRegions];
  for (int i = 0; i < nRegions; i++) {
	trips[i] = pairSelection(tripPairs, asymmCut[i]);
	trips[i] = GenMatchedTriplets(event, trips[i]);
  }

  double nTrips_passAsymm[nRegions];
  for (int i = 0; i < nRegions; i++)
	nTrips_passAsymm[i] = trips[i].size();

  // starting to implement triplet size as weight
  Manager()->SetCurrentEventWeight(weight*nTrips_passAsymm[0]); 
  if(!Manager()->ApplyCut(trips[0].size() != 0, "SR1: Am < 0.25")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passAsymm[1]);
  if(!Manager()->ApplyCut(trips[1].size() != 0, "SR2: Am < 0.175")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passAsymm[2]);
  if(!Manager()->ApplyCut(trips[2].size() != 0, "SR3: Am < 0.15")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passAsymm[3]);
  Manager()->SetCurrentEventWeight(weight*trips[3].size());
  if(!Manager()->ApplyCut(trips[3].size() != 0, "SR4: Am < 0.15")) return true;

  // Delta cut
  double nTrips_passDelta[nRegions];
  for (int i = 0; i < nRegions; i++) {
	// select triplets
	trips[i] = deltaSelection(trips[i], deltaCut[i]);

	// update nTrips
	nTrips_passDelta[i] = trips[i].size();
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
  double nTrips_passMDS32[nRegions];
  for (int i = 0; i < nRegions; i++) {
	// select triplets
	trips[i] = mds32Selection(trips[i], mds32Cut[i]);
	
	// update nTrips
	nTrips_passMDS32[i] = trips[i].size();
  }
  
  Manager()->SetCurrentEventWeight(weight*nTrips_passMDS32[0]);
  if(!Manager()->ApplyCut(trips[0].size() != 0, "SR1: D^2[3,2] < 0.05")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passMDS32[1]);
  if(!Manager()->ApplyCut(trips[1].size() != 0, "SR2: D^2[3,2] < 0.175")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passMDS32[2]);
  if(!Manager()->ApplyCut(trips[2].size() != 0, "SR3: D^2[3,2] < 0.2")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_passMDS32[3]);
  if(!Manager()->ApplyCut(trips[3].size() != 0, "SR4: D^2[3,2] < 0.25")) return true;

  // 200to300 -> nTrips_massbin[2], 500to600 -> nTrips_massbin[5]
  int nTrips_massbin[20] = {0};
  for (unsigned int i = 0; i < trips[0].size(); i++) {
    int trip_mass = static_cast<int> (mass(trips[0].at(i)));
	int bin = trip_mass / 100;
	if (2 <= bin && bin < 4) 
	  nTrips_massbin[bin]++;
	else
	  continue;
  }
  for (unsigned int i = 0; i < trips[1].size(); i++) {
    int trip_mass = static_cast<int> (mass(trips[1].at(i)));
    int bin = trip_mass / 100;
    if (4 <= bin && bin < 7)
      nTrips_massbin[bin]++;
    else
      continue;
  }
  for (unsigned int i = 0; i < trips[2].size(); i++) {
    int trip_mass = static_cast<int> (mass(trips[2].at(i)));
    int bin = trip_mass / 100;
    if (7 <= bin && bin < 12)
      nTrips_massbin[bin]++;
    else
      continue;
  }
  for (unsigned int i = 0; i < trips[3].size(); i++) {
    int trip_mass = static_cast<int> (mass(trips[3].at(i)));
    int bin = trip_mass / 100;
    if (12 <= bin && bin < 20)
      nTrips_massbin[bin]++;
    else
      continue;
  }
  
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[2]);
  if(!Manager()->ApplyCut(nTrips_massbin[2] != 0, "SR1: 200 < M(jjj) < 300GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[3]);
  if(!Manager()->ApplyCut(nTrips_massbin[3] != 0, "SR1: 300 < M(jjj) < 400GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[4]);
  if(!Manager()->ApplyCut(nTrips_massbin[4] != 0, "SR2: 400 < M(jjj) < 500GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[5]);
  if(!Manager()->ApplyCut(nTrips_massbin[5] != 0, "SR2: 500 < M(jjj) < 600GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[6]);
  if(!Manager()->ApplyCut(nTrips_massbin[6] != 0, "SR2: 600 < M(jjj) < 700GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[7]);
  if(!Manager()->ApplyCut(nTrips_massbin[7] != 0, "SR3: 700 < M(jjj) < 800GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[8]);
  if(!Manager()->ApplyCut(nTrips_massbin[8] != 0, "SR3: 800 < M(jjj) < 900GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[9]);
  if(!Manager()->ApplyCut(nTrips_massbin[9] != 0, "SR3: 900 < M(jjj) < 1000GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[10]);
  if(!Manager()->ApplyCut(nTrips_massbin[10] != 0, "SR3: 1000 < M(jjj) < 1100GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[11]);
  if(!Manager()->ApplyCut(nTrips_massbin[11] != 0, "SR3: 1100 < M(jjj) < 1200GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[12]);
  if(!Manager()->ApplyCut(nTrips_massbin[12] != 0, "SR4: 1200 < M(jjj) < 1300GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[13]);
  if(!Manager()->ApplyCut(nTrips_massbin[13] != 0, "SR4: 1300 < M(jjj) < 1400GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[14]);
  if(!Manager()->ApplyCut(nTrips_massbin[14] != 0, "SR4: 1400 < M(jjj) < 1500GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[15]);
  if(!Manager()->ApplyCut(nTrips_massbin[15] != 0, "SR4: 1500 < M(jjj) < 1600GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[16]);
  if(!Manager()->ApplyCut(nTrips_massbin[16] != 0, "SR4: 1600 < M(jjj) < 1700GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[17]);
  if(!Manager()->ApplyCut(nTrips_massbin[17] != 0, "SR4: 1700 < M(jjj) < 1800GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[18]);
  if(!Manager()->ApplyCut(nTrips_massbin[18] != 0, "SR4: 1800 < M(jjj) < 1900GeV")) return true;
  Manager()->SetCurrentEventWeight(weight*nTrips_massbin[19]);
  if(!Manager()->ApplyCut(nTrips_massbin[19] != 0, "SR4: 1900 < M(jjj) < 2000GeV")) return true;
  

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

  return out;
}

TripletCollection CMS_EXO_17_030::deltaSelection(const TripletCollection &trips, const double &deltaCut) {
  TripletCollection out;

  for (unsigned int i = 0; i < trips.size(); i++) {
	const Triplet& this_trip = trips.at(i);
	if (delta(this_trip) > deltaCut)
	  out.push_back(this_trip);
  }
  
  return out;
}

TripletCollection CMS_EXO_17_030::mds32Selection(const TripletCollection &trips, const double &mdsCut) {
  TripletCollection out;

  for (unsigned int i = 0; i < trips.size(); i++) {
	const Triplet& this_trip = trips.at(i);
	if (mds32(this_trip) < mdsCut)
	  out.push_back(this_trip);
  }

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
	if (1<=gen.pdgid()&&gen.pdgid()<=4&&(gen.mothers()).at(0)->pdgid()==CMS_EXO_17_030_PID) 
	  p_gluinos.push_back((gen.mothers()).at(0));
	if (-4<=gen.pdgid()&&gen.pdgid()<=-1&&(gen.mothers()).at(0)->pdgid()==CMS_EXO_17_030_PID) 
	  p_gluinos.push_back((gen.mothers()).at(0));
  }
  
  sort(p_gluinos.begin(), p_gluinos.end());
  vector<const MCParticleFormat*>::iterator last;
  last = unique(p_gluinos.begin(), p_gluinos.end());
  p_gluinos.erase(last, p_gluinos.end());
  
  // start matching
  // triplets should be matched to the "same" mother gluino -> use the pointer comparision
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
		  if (matched) matched_jets4.push_back(jet);
		}
	  }
	   
	}
	
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
  
  return matched_trips;
}

