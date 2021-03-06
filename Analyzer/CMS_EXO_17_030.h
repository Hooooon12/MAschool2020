#ifndef analysis_CMS_EXO_17_030_h
#define analysis_CMS_EXO_17_030_h

#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"
#include <string>
#include <TString.h>
#include <vector>
#include <array>

namespace MA5
{
  typedef std::vector<const RecJetFormat*> JetCollection;
  typedef std::array<const RecJetFormat*, 3> Triplet;
  typedef std::pair<Triplet, Triplet> TripletPair;
  typedef std::vector<TripletPair> PairCollection;
  typedef std::vector<Triplet> TripletCollection;

  class CMS_EXO_17_030 : public AnalyzerBase	{                                                
    INIT_ANALYSIS(CMS_EXO_17_030,"CMS_EXO_17_030")
  
  public:
	virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
	virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
	virtual bool Execute(SampleFormat& sample, const EventFormat& event);
  
  private:
    std::vector<std::string> bins_SR1, bins_SR2, bins_SR3, bins_SR4;
    std::vector<std::string> cuts_SR1, cuts_SR2, cuts_SR3, cuts_SR4;
  	const unsigned int nBins_SR1 = 30; 
	const unsigned int binsize_SR1 = 7;
	const unsigned int firstBin_SR1 = 196;

   	const unsigned int nBins_SR2 = 32; 
	const unsigned int binsize_SR2 = 10;
	const unsigned int firstBin_SR2 = 390;

  	const unsigned int nBins_SR3 = 17; 
	const unsigned int binsize_SR3 = 30;
	const unsigned int firstBin_SR3 = 690;

  	const unsigned int nBins_SR4 = 20;
	const unsigned int binsize_SR4 = 40;
	const unsigned int firstBin_SR4 = 1200;

	JetCollection jetSelection(const EventFormat& event,const double &ptCut, const double &etaCut);
    TripletCollection pairSelection(const PairCollection &pairs, const double &asymmCut);
    TripletCollection deltaSelection(const TripletCollection &trips, const double &deltaCut);
    TripletCollection mds32Selection(const TripletCollection &trips, const double &mdsCut);
    TripletCollection GenMatchedTriplets(const EventFormat& event, const JetCollection &jetcoll);
    TripletCollection GenMatchedTriplets( const EventFormat& event, const TripletCollection &trips);

    PairCollection makePairCollection(const JetCollection &jetcoll);
   
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
  };
}

#endif
