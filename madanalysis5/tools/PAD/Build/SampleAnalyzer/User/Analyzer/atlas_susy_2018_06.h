#ifndef analysis_atlas_susy_2018_06_h
#define analysis_atlas_susy_2018_06_h

#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"
// #include "SampleAnalyzer/interfaces/root/RootMainHeaders.h"

namespace MA5
{
class atlas_susy_2018_06 : public AnalyzerBase
{
  INIT_ANALYSIS(atlas_susy_2018_06,"atlas_susy_2018_06")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

//  TH1F* plot_test1;
//  TH1F* plot_test2;
//  TH1F* plot_test3;
//  TH1F* plot_test4;
//  TH1F* plot_test5;
//  TH1F* plot_test6;
//  TH1F* plot_test7;
//  TH1F* plot_test8;

 private:
};
}

#endif
