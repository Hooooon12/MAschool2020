#ifndef analysis_cms_sus_16_039_h
#define analysis_cms_sus_16_039_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class cms_sus_16_039 : public AnalyzerBase
{
  INIT_ANALYSIS(cms_sus_16_039,"cms_sus_16_039")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
  // -- user-defined functions -- //
  virtual bool isLooseLepton(const RecLeptonFormat*, const EventFormat&, const double &);
  virtual bool isIsolated(const RecLeptonFormat*, std::vector<const RecJetFormat*>, const EventFormat&, const double&, const double&, const double&);
};
}

#endif
