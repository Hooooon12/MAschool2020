#ifndef analysis_atlas_exot_2015_03_h
#define analysis_atlas_exot_2015_03_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class atlas_exot_2015_03 : public AnalyzerBase
{
  INIT_ANALYSIS(atlas_exot_2015_03,"atlas_exot_2015_03")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:


};
}

#endif
