#ifndef analysis_cms_sus_14_001_toptag_h
#define analysis_cus_14_001_TopTag_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
  class cms_sus_14_001_toptag : public AnalyzerBase
  {
    INIT_ANALYSIS(cms_sus_14_001_toptag,"cms_sus_14_001_toptag")

      public:
    virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
    virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
    virtual bool Execute(SampleFormat& sample, const EventFormat& event);

  private:

//    TFile* fNew;

//    TH1F* hLepIso;
//    TH1F* hLepSumPt;
//    TH1F* hLepPt;
//    TH1F* hMet;
//    TH1F* hMt2;
//    TH1F* hMt2blob;
//    TH1F* hMtRsys;
//    TH1F* hMt3jet;

//    double mtop;
//    double mW;
    double Rmin;
    double Rmax;
//    double isoCut;
//    double JEscale;
//    double isoCutEl;
//    double isoCutMu;
  };
}

#endif
