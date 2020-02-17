#ifndef analysis_atlas_susy_2018_031_h
#define analysis_atlas_susy_2018_031_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class atlas_susy_2018_031 : public AnalyzerBase
{
  INIT_ANALYSIS(atlas_susy_2018_031,"atlas_susy_2018_031")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
   MAint32 event_num = 0;
};
}

#endif
