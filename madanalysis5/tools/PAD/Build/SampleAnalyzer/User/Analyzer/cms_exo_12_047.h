#ifndef cms_exo_12_047_h
#define cms_exo_12_047_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class cms_exo_12_047 : public AnalyzerBase
{
  INIT_ANALYSIS(cms_exo_12_047,"cms_exo_12_047")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:

};
}

#endif
