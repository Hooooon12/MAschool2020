#ifndef analysis_CMS_EXO_17_030_h
#define analysis_CMS_EXO_17_030_h

#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"
#include <vector>
#include <array>
#include <TFile.h>
#include <TTree.h>
#include <TH1D.h>

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
    MALorentzVector getMomentum(Triplet trip);
    double getMass(Triplet trip);
    double dalitz32(Triplet t, int idx1, int idx2);
    double mds32(Triplet t);
    double dalitz63(JetCollection, int, int, int);
    double massAsymm(TripletPair);
    double delta(Triplet);
    double mds6332(JetCollection jets);
    double compareMass(Triplet, double);
    Triplet chooseSigTrip(TripletCollection, double);

    TFile* fOut;
    TTree* tSr[4];
    TH1D*  cutFlow_Evt[4];
    TH1D*  cutFlow_TripletPair[4];
    TH1D*  cutFlow_Triplet[4];
    std::vector<double> triplet_pt[4];
    std::vector<double> triplet_eta[4];
    std::vector<double> triplet_phi[4];
    std::vector<double> triplet_mass[4];
  };
}

#endif
