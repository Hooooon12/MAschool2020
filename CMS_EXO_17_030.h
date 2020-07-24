#ifndef analysis_CMS_EXO_17_030_h
#define analysis_CMS_EXO_17_030_h

#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"
#include <vector>
#include <array>
#include <TFile.h>
#include <TTree.h>
#include <TH1D.h>
#include <TString.h>

namespace MA5
{
  typedef std::vector<const RecJetFormat*> JetCollection;
  typedef std::array<const RecJetFormat*, 3> Triplet;
  typedef std::pair<Triplet, Triplet> TripletPair;
  typedef std::vector<TripletPair> PairCollection;
  typedef std::vector<Triplet> TripletCollection;  
  class CMS_EXO_17_030 : public AnalyzerBase	{                                                
    INIT_ANALYSIS(CMS_EXO_17_030,"CMS_EXO_17_030"  )
  
  public:
	virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
	virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
	virtual bool Execute(SampleFormat& sample, const EventFormat& event);
  
  private:
	int SR = 0;
	bool trigGen = false;
	JetCollection jetSelection(const EventFormat& event,const double &ptCut, const double &etaCut);
    TripletCollection pairSelection(const PairCollection &pairs, const double &asymmCut);
    TripletCollection deltaSelection(const TripletCollection &trips, const double &deltaCut);
    TripletCollection mds32Selection(const TripletCollection &trips, const double &mdsCut);
    TripletCollection GenMatchedTriplets(const EventFormat& event, const JetCollection &jetcoll);
    TripletCollection GenMatchedTriplets( const EventFormat& event, const TripletCollection &trips);

    PairCollection makePairCollection(const JetCollection &jetcoll);
    PairCollection MassAsymSelection(const PairCollection &pairs, const double &asymmCut);
   
    // kinematic variables
    MALorentzVector momentum(const Triplet &trip);
    double HT(const JetCollection &jetcoll);
    double mass(const Triplet &triplet);
    double dalitz32(const Triplet &triplet, const int &idx1, const int &idx2);
    double mds32(const Triplet &triplet);
    double dalitz6332(const JetCollection &jetcoll, const int &idx1, const int &idx2, const int &idx3);
    double mds6332(const JetCollection &jetcoll);
    double massAsymm(const TripletPair &pair);
    double delta(const Triplet &triplet);

	// histograms to validate cuts
	TFile* f;
	TH1D* cutflow_event[4];
	TH1D* cutflow_pair[4];
	TH1D* cutflow_triplet[4];
	TH1D* h_mass[4];
	//TH1D* h_mds6332[4];
	//TH1D* h_massAsymm[4];
	TH1D* h_mds32[4];
	TH1D* h_delta[4];
  };
}

#endif
