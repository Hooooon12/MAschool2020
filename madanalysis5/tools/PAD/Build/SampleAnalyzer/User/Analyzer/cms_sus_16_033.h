#ifndef analysis_cms_sus_16_033_h
#define analysis_cms_sus_16_033_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class cms_sus_16_033 : public AnalyzerBase
{
  INIT_ANALYSIS(cms_sus_16_033,"cms_sus_16_033")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
  // Overlap removal
  template<typename T1, typename T2> std::vector<const T1*> Removal(std::vector<const T1*>&, std::vector<const T2*>&, const double &);
  template<typename T1> std::vector<const T1*> Removal(std::vector<const T1*>&, const double &);

  // This function returns the DeltaR depending on the pT of the lepton considered
  // required for selecting isolated leptons
  double Determine_DeltaR(const RecLeptonFormat*);
};
}

#endif
