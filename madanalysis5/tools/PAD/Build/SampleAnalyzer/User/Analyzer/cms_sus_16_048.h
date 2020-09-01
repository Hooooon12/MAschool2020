#ifndef analysis_cms_sus_16_048_h
#define analysis_cms_sus_16_048_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class cms_sus_16_048 : public AnalyzerBase
{
  INIT_ANALYSIS(cms_sus_16_048,"cms_sus_16_048")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
  template<typename T1, typename T2> std::vector<const T1*>
    Removal(std::vector<const T1*> &, std::vector<const T2*> &,
    const double &);
};
}

#endif
