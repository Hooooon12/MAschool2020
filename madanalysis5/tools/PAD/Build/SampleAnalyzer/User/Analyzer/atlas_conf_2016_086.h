#ifndef analysis_atlas_conf_2016_086_h
#define analysis_atlas_conf_2016_086_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class atlas_conf_2016_086 : public AnalyzerBase
{
  INIT_ANALYSIS(atlas_conf_2016_086,"atlas_conf_2016_086")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
};
}

#endif