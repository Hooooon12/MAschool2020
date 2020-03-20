#ifndef analysis_CMS_EXO_17_030_h
#define analysis_CMS_EXO_17_030_h

#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"
#include <vector>
#include <array>
#include <TFile.h>
#include <TTree.h>
#include <TH1D.h>
#include <TH2D.h>
namespace MA5
{
  typedef std::vector<const RecJetFormat*> JetCollection;
  typedef std::array<const RecJetFormat*, 3> Triplet;
  typedef std::pair<Triplet, Triplet> TripletPair;
  typedef std::vector<TripletPair> PairCollection;
  typedef std::vector<Triplet> TripletCollection;  
  class CMS_EXO_17_030 : public AnalyzerBase       
  {                                                
    INIT_ANALYSIS(CMS_EXO_17_030,"CMS_EXO_17_030"  )
  
   public:
    virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
    virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
    virtual bool Execute(SampleFormat& sample, const EventFormat& event);
  
   private:
    JetCollection jetSelection( const EventFormat& event, double );
    double getHT( JetCollection );
    TripletCollection pairSelection( PairCollection, double );
    TripletCollection deltaSelection( TripletCollection, double );
    TripletCollection mds32Selection( TripletCollection, double ); 

    PairCollection makePairCollection(JetCollection);
    PairCollection passAmTripPairs( PairCollection, double);
    MALorentzVector getMomentum(Triplet trip);
    double getMass(Triplet);
    double dalitz32(Triplet t, int idx1, int idx2);
    double mds32(Triplet t);
    double dalitz63(JetCollection, int, int, int);
    double massAsymm(TripletPair);
    double delta(Triplet);
	double GetMass(Triplet);
	double GetHT(Triplet);
    double mds6332(JetCollection jets);
    double compareMass(Triplet, double);
    Triplet chooseSigTrip(TripletCollection, double);
	double mass12(Triplet);
	double mass23(Triplet);

    TFile* fOut;
    TTree* tSr[4];
    TH1D*  cutFlow_Evt[4];
    TH1D*  cutFlow_TripletPair[4];
    TH1D*  cutFlow_Triplet[4];
    TH1D*  trips_num_init[4];
    TH1D*  trips_num_Am[4];
    TH1D*  trips_num_Delta[4];
    TH1D*  trips_num_MDS32[4];
    TH1D*  Am_before[4];
    TH1D*  Am_after[4];
    TH1D*  Delta_before[4];
    TH1D*  Delta_after[4];
    TH1D*  MDS32_before[4];
    TH1D*  MDS32_after[4];
    TH1D*  MDS6332_before[4];
    TH1D*  MDS6332_after[4];
    TH1D*  Njets[4];
    //TH1D*  jet_pt[4][10];
    TH1D*  jet_pt_1[4];
    TH1D*  jet_pt_2[4];
    TH1D*  jet_pt_3[4];
    TH1D*  jet_pt_4[4];
    TH1D*  jet_pt_5[4];
    TH1D*  jet_pt_6[4];
    TH1D*  jet_pt_7[4];
    TH1D*  jet_pt_8[4];
    TH1D*  jet_pt_9[4];
    TH1D*  jet_pt_10[4];
	TH2D*  Mass_HT_beforeDelta[4];
	TH2D*  Mass_HT_afterDelta[4];

    std::vector<double> triplet_pt[4];
    std::vector<double> triplet_eta[4];
    std::vector<double> triplet_phi[4];
    std::vector<double> triplet_mass[4];
  };
}

#endif
