#ifndef analysis_atlas_susy_2013_11_h
#define analysis_atlas_susy_2013_11_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class atlas_susy_2013_11 : public AnalyzerBase
{
  INIT_ANALYSIS(atlas_susy_2013_11,"atlas_susy_2013_11")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
};
}

#endif
