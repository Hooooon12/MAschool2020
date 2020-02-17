#include "SampleAnalyzer/User/Analyzer/cms_exo_16_022.h"
#include "SampleAnalyzer/User/Analyzer/cms_top_17_009.h"
#include "SampleAnalyzer/User/Analyzer/cms_sus_17_001.h"
#include "SampleAnalyzer/User/Analyzer/cms_sus_16_052.h"
#include "SampleAnalyzer/User/Analyzer/cms_sus_16_039.h"
#include "SampleAnalyzer/User/Analyzer/cms_sus_16_033.h"
#include "SampleAnalyzer/User/Analyzer/cms_exo_16_012.h"
#include "SampleAnalyzer/User/Analyzer/cms_exo_16_010.h"
#include "SampleAnalyzer/User/Analyzer/cms_exo_12_048.h"
#include "SampleAnalyzer/User/Analyzer/cms_exo_12_047.h"
#include "SampleAnalyzer/User/Analyzer/cms_b2g_14_004.h"
#include "SampleAnalyzer/User/Analyzer/cms_b2g_12_022.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2018_031.h"
#include "SampleAnalyzer/User/Analyzer/atlas_conf_2019_040.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2015_06.h"
#include "SampleAnalyzer/User/Analyzer/atlas_exot_2015_03.h"
#include "SampleAnalyzer/User/Analyzer/atlas_conf_2016_086.h"
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2016_07.h"
#include "SampleAnalyzer/User/Analyzer/atlas_exot_2016_32.h"
#include "SampleAnalyzer/User/Analyzer/atlas_exot_2016_25.h"
#include "SampleAnalyzer/User/Analyzer/atlas_exot_2016_27.h"
#include "SampleAnalyzer/User/Analyzer/atlas_exot_2014_06.h"
#include "SampleAnalyzer/User/Analyzer/cms_b2g_12_012.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerManager.h"
#include "SampleAnalyzer/Commons/Service/LogStream.h"

// -----------------------------------------------------------------------------
// BuildTable
// -----------------------------------------------------------------------------
void BuildUserTable(MA5::AnalyzerManager& manager)
{
  using namespace MA5;
  manager.Add("cms_b2g_12_012",new cms_b2g_12_012);
  manager.Add("atlas_exot_2014_06",new atlas_exot_2014_06);
  manager.Add("atlas_exot_2016_27",new atlas_exot_2016_27);
  manager.Add("atlas_exot_2016_25",new atlas_exot_2016_25);
  manager.Add("atlas_exot_2016_32",new atlas_exot_2016_32);
  manager.Add("atlas_susy_2016_07",new atlas_susy_2016_07);
  manager.Add("atlas_conf_2016_086",new atlas_conf_2016_086);
  manager.Add("atlas_exot_2015_03",new atlas_exot_2015_03);
  manager.Add("atlas_susy_2015_06",new atlas_susy_2015_06);
  manager.Add("atlas_conf_2019_040",new atlas_conf_2019_040);
  manager.Add("atlas_susy_2018_031",new atlas_susy_2018_031);
  manager.Add("cms_b2g_12_022",new cms_b2g_12_022);
  manager.Add("cms_b2g_14_004",new cms_b2g_14_004);
  manager.Add("cms_exo_12_047",new cms_exo_12_047);
  manager.Add("cms_exo_12_048",new cms_exo_12_048);
  manager.Add("cms_exo_16_010",new cms_exo_16_010);
  manager.Add("cms_exo_16_012",new cms_exo_16_012);
  manager.Add("cms_sus_16_033",new cms_sus_16_033);
  manager.Add("cms_sus_16_039",new cms_sus_16_039);
  manager.Add("cms_sus_16_052",new cms_sus_16_052);
  manager.Add("cms_sus_17_001",new cms_sus_17_001);
  manager.Add("cms_top_17_009",new cms_top_17_009);
  manager.Add("cms_exo_16_022",new cms_exo_16_022);
}
