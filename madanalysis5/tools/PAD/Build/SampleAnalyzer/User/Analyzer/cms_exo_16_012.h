#ifndef analysis_cms_exo_16_012_h
#define analysis_cms_exo_16_012_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class cms_exo_16_012 : public AnalyzerBase
{
  INIT_ANALYSIS(cms_exo_16_012,"cms_exo_16_012")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
// double Invariant_Mass(const RecPhotonFormat* jet1, const RecPhotonFormat* jet2);
 int AA,BB,CC,begin_before,begin_after;
};
}

#endif
