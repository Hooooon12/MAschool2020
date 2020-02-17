#ifndef analysis_sfs_test_h
#define analysis_sfs_test_h

#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"
#include "new_tagger.h"
#include "new_smearer_reco.h"
namespace MA5
{
class sfs_test : public AnalyzerBase
{
  INIT_ANALYSIS(sfs_test,"sfs_test")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
};
}

#endif
