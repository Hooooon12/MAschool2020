#include "SampleAnalyzer/User/Analyzer/cms_sus_14_001_toptag.h"
#include "SampleAnalyzer/User/Analyzer/cms_sus_14_001_monojet.h"
#include "SampleAnalyzer/User/Analyzer/cms_sus_13_016.h"
#include "SampleAnalyzer/User/Analyzer/cms_sus_13_012.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_05.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2014_10.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_21.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_11.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_04.h"
#include "SampleAnalyzer/User/Analyzer/atlas_higg_2013_03.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_02.h"
#include "SampleAnalyzer/User/Analyzer/cms_sus_13_011.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerManager.h"
#include "SampleAnalyzer/Commons/Service/LogStream.h"

// -----------------------------------------------------------------------------
// BuildTable
// -----------------------------------------------------------------------------
void BuildUserTable(MA5::AnalyzerManager& manager)
{
  using namespace MA5;
  manager.Add("cms_sus_13_011",new cms_sus_13_011);
  manager.Add("atlas_susy_2013_02",new atlas_susy_2013_02);
  manager.Add("atlas_higg_2013_03",new atlas_higg_2013_03);
  manager.Add("atlas_susy_2013_04",new atlas_susy_2013_04);
  manager.Add("atlas_susy_2013_11",new atlas_susy_2013_11);
  manager.Add("atlas_susy_2013_21",new atlas_susy_2013_21);
  manager.Add("atlas_susy_2014_10",new atlas_susy_2014_10);
  manager.Add("atlas_susy_2013_05",new atlas_susy_2013_05);
  manager.Add("cms_sus_13_012",new cms_sus_13_012);
  manager.Add("cms_sus_13_016",new cms_sus_13_016);
  manager.Add("cms_sus_14_001_monojet",new cms_sus_14_001_monojet);
  manager.Add("cms_sus_14_001_toptag",new cms_sus_14_001_toptag);
}
