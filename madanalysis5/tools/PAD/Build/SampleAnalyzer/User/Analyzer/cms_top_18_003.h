#ifndef analysis_cms_top_18_003_h
#define analysis_cms_top_18_003_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class cms_top_18_003 : public AnalyzerBase
{
  INIT_ANALYSIS(cms_top_18_003,"cms_top_18_003")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

  // -- user-defined functions -- //
  bool IsLooseLepton(const RecLeptonFormat*, const EventFormat&,const double &, const double &);
  bool IsIsolated(const RecLeptonFormat*, std::vector<const RecJetFormat*>,const EventFormat&, const double&, const double&, const double&);


 private:
};
}

#endif
