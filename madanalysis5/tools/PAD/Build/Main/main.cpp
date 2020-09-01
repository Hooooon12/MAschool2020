////////////////////////////////////////////////////////////////////////////////
//  
//  This file has been generated by MadAnalysis 5.
//  The MadAnalysis development team: <ma5team@iphc.cnrs.fr>
//                Eric Conte and Benjamin Fuks
//  Official website: <https://launchpad.net/madanalysis5>
//  
////////////////////////////////////////////////////////////////////////////////

// SampleHeader header
#include "SampleAnalyzer/Process/Core/SampleAnalyzer.h"
#include "SampleAnalyzer/User/Analyzer/analysisList.h"
using namespace MA5;

// -----------------------------------------------------------------------
// Info function
// -----------------------------------------------------------------------
int Info(SampleAnalyzer& manager)
{
  INFO << "BEGIN " << __FILE__ << endmsg;
  manager.AnalyzerList().Print();
  INFO << "END " << __FILE__ << endmsg;
  return 0;
}
// -----------------------------------------------------------------------
// main program
// -----------------------------------------------------------------------
int main(int argc, char *argv[])
{
  // Creating a manager
  SampleAnalyzer manager;
  BuildUserTable(manager.AnalyzerList());

  // Identifying --info argument
  if (argc==2)
  {
    std::string arg=argv[1];
    if (arg=="--info") return Info(manager);
  }

  // ---------------------------------------------------
  //                    INITIALIZATION
  // ---------------------------------------------------
  INFO << "    * Initializing all components" << endmsg;

  // Initializing the manager
  if (!manager.Initialize(argc,argv,"pdg.ma5")) return 1;

  // Creating data format for storing data
  EventFormat myEvent;
  std::vector<SampleFormat> mySamples;

  // Getting pointer to the analyzer
  std::map<std::string, std::string> prmcms_top_18_003;
  AnalyzerBase* analyzer_cms_top_18_003=
    manager.InitializeAnalyzer("cms_top_18_003","cms_top_18_003.saf",prmcms_top_18_003);
  if (analyzer_cms_top_18_003==0) return 1;

  std::map<std::string, std::string> prmcms_top_17_009;
  AnalyzerBase* analyzer_cms_top_17_009=
    manager.InitializeAnalyzer("cms_top_17_009","cms_top_17_009.saf",prmcms_top_17_009);
  if (analyzer_cms_top_17_009==0) return 1;

  std::map<std::string, std::string> prmcms_sus_17_001;
  AnalyzerBase* analyzer_cms_sus_17_001=
    manager.InitializeAnalyzer("cms_sus_17_001","cms_sus_17_001.saf",prmcms_sus_17_001);
  if (analyzer_cms_sus_17_001==0) return 1;

  std::map<std::string, std::string> prmcms_sus_16_052;
  AnalyzerBase* analyzer_cms_sus_16_052=
    manager.InitializeAnalyzer("cms_sus_16_052","cms_sus_16_052.saf",prmcms_sus_16_052);
  if (analyzer_cms_sus_16_052==0) return 1;

  std::map<std::string, std::string> prmcms_sus_16_048;
  AnalyzerBase* analyzer_cms_sus_16_048=
    manager.InitializeAnalyzer("cms_sus_16_048","cms_sus_16_048.saf",prmcms_sus_16_048);
  if (analyzer_cms_sus_16_048==0) return 1;

  std::map<std::string, std::string> prmcms_sus_16_039;
  AnalyzerBase* analyzer_cms_sus_16_039=
    manager.InitializeAnalyzer("cms_sus_16_039","cms_sus_16_039.saf",prmcms_sus_16_039);
  if (analyzer_cms_sus_16_039==0) return 1;

  std::map<std::string, std::string> prmcms_sus_16_033;
  AnalyzerBase* analyzer_cms_sus_16_033=
    manager.InitializeAnalyzer("cms_sus_16_033","cms_sus_16_033.saf",prmcms_sus_16_033);
  if (analyzer_cms_sus_16_033==0) return 1;

  std::map<std::string, std::string> prmcms_exo_16_022;
  AnalyzerBase* analyzer_cms_exo_16_022=
    manager.InitializeAnalyzer("cms_exo_16_022","cms_exo_16_022.saf",prmcms_exo_16_022);
  if (analyzer_cms_exo_16_022==0) return 1;

  std::map<std::string, std::string> prmcms_exo_16_012;
  AnalyzerBase* analyzer_cms_exo_16_012=
    manager.InitializeAnalyzer("cms_exo_16_012","cms_exo_16_012.saf",prmcms_exo_16_012);
  if (analyzer_cms_exo_16_012==0) return 1;

  std::map<std::string, std::string> prmcms_exo_16_010;
  AnalyzerBase* analyzer_cms_exo_16_010=
    manager.InitializeAnalyzer("cms_exo_16_010","cms_exo_16_010.saf",prmcms_exo_16_010);
  if (analyzer_cms_exo_16_010==0) return 1;

  std::map<std::string, std::string> prmcms_exo_12_048;
  AnalyzerBase* analyzer_cms_exo_12_048=
    manager.InitializeAnalyzer("cms_exo_12_048","cms_exo_12_048.saf",prmcms_exo_12_048);
  if (analyzer_cms_exo_12_048==0) return 1;

  std::map<std::string, std::string> prmcms_exo_12_047;
  AnalyzerBase* analyzer_cms_exo_12_047=
    manager.InitializeAnalyzer("cms_exo_12_047","cms_exo_12_047.saf",prmcms_exo_12_047);
  if (analyzer_cms_exo_12_047==0) return 1;

  std::map<std::string, std::string> prmcms_b2g_14_004;
  AnalyzerBase* analyzer_cms_b2g_14_004=
    manager.InitializeAnalyzer("cms_b2g_14_004","cms_b2g_14_004.saf",prmcms_b2g_14_004);
  if (analyzer_cms_b2g_14_004==0) return 1;

  std::map<std::string, std::string> prmcms_b2g_12_022;
  AnalyzerBase* analyzer_cms_b2g_12_022=
    manager.InitializeAnalyzer("cms_b2g_12_022","cms_b2g_12_022.saf",prmcms_b2g_12_022);
  if (analyzer_cms_b2g_12_022==0) return 1;

  std::map<std::string, std::string> prmatlas_susy_2019_08;
  AnalyzerBase* analyzer_atlas_susy_2019_08=
    manager.InitializeAnalyzer("atlas_susy_2019_08","atlas_susy_2019_08.saf",prmatlas_susy_2019_08);
  if (analyzer_atlas_susy_2019_08==0) return 1;

  std::map<std::string, std::string> prmatlas_susy_2018_031;
  AnalyzerBase* analyzer_atlas_susy_2018_031=
    manager.InitializeAnalyzer("atlas_susy_2018_031","atlas_susy_2018_031.saf",prmatlas_susy_2018_031);
  if (analyzer_atlas_susy_2018_031==0) return 1;

  std::map<std::string, std::string> prmatlas_susy_2018_06;
  AnalyzerBase* analyzer_atlas_susy_2018_06=
    manager.InitializeAnalyzer("atlas_susy_2018_06","atlas_susy_2018_06.saf",prmatlas_susy_2018_06);
  if (analyzer_atlas_susy_2018_06==0) return 1;

  std::map<std::string, std::string> prmatlas_conf_2019_040;
  AnalyzerBase* analyzer_atlas_conf_2019_040=
    manager.InitializeAnalyzer("atlas_conf_2019_040","atlas_conf_2019_040.saf",prmatlas_conf_2019_040);
  if (analyzer_atlas_conf_2019_040==0) return 1;

  std::map<std::string, std::string> prmatlas_susy_2015_06;
  AnalyzerBase* analyzer_atlas_susy_2015_06=
    manager.InitializeAnalyzer("atlas_susy_2015_06","atlas_susy_2015_06.saf",prmatlas_susy_2015_06);
  if (analyzer_atlas_susy_2015_06==0) return 1;

  std::map<std::string, std::string> prmatlas_exot_2015_03;
  AnalyzerBase* analyzer_atlas_exot_2015_03=
    manager.InitializeAnalyzer("atlas_exot_2015_03","atlas_exot_2015_03.saf",prmatlas_exot_2015_03);
  if (analyzer_atlas_exot_2015_03==0) return 1;

  std::map<std::string, std::string> prmatlas_conf_2016_086;
  AnalyzerBase* analyzer_atlas_conf_2016_086=
    manager.InitializeAnalyzer("atlas_conf_2016_086","atlas_conf_2016_086.saf",prmatlas_conf_2016_086);
  if (analyzer_atlas_conf_2016_086==0) return 1;

  std::map<std::string, std::string> prmatlas_susy_2016_07;
  AnalyzerBase* analyzer_atlas_susy_2016_07=
    manager.InitializeAnalyzer("atlas_susy_2016_07","atlas_susy_2016_07.saf",prmatlas_susy_2016_07);
  if (analyzer_atlas_susy_2016_07==0) return 1;

  std::map<std::string, std::string> prmatlas_exot_2018_30;
  AnalyzerBase* analyzer_atlas_exot_2018_30=
    manager.InitializeAnalyzer("atlas_exot_2018_30","atlas_exot_2018_30.saf",prmatlas_exot_2018_30);
  if (analyzer_atlas_exot_2018_30==0) return 1;

  std::map<std::string, std::string> prmatlas_exot_2016_32;
  AnalyzerBase* analyzer_atlas_exot_2016_32=
    manager.InitializeAnalyzer("atlas_exot_2016_32","atlas_exot_2016_32.saf",prmatlas_exot_2016_32);
  if (analyzer_atlas_exot_2016_32==0) return 1;

  std::map<std::string, std::string> prmatlas_exot_2016_25;
  AnalyzerBase* analyzer_atlas_exot_2016_25=
    manager.InitializeAnalyzer("atlas_exot_2016_25","atlas_exot_2016_25.saf",prmatlas_exot_2016_25);
  if (analyzer_atlas_exot_2016_25==0) return 1;

  std::map<std::string, std::string> prmatlas_exot_2016_27;
  AnalyzerBase* analyzer_atlas_exot_2016_27=
    manager.InitializeAnalyzer("atlas_exot_2016_27","atlas_exot_2016_27.saf",prmatlas_exot_2016_27);
  if (analyzer_atlas_exot_2016_27==0) return 1;

  std::map<std::string, std::string> prmatlas_exot_2014_06;
  AnalyzerBase* analyzer_atlas_exot_2014_06=
    manager.InitializeAnalyzer("atlas_exot_2014_06","atlas_exot_2014_06.saf",prmatlas_exot_2014_06);
  if (analyzer_atlas_exot_2014_06==0) return 1;

  std::map<std::string, std::string> parametersA1;
  AnalyzerBase* analyzer1 = 
      manager.InitializeAnalyzer("cms_b2g_12_012","cms_b2g_12_012.saf",parametersA1);
  if (analyzer1==0) return 1;

  // Post initialization (creates the new output directory structure)
  if(!manager.PostInitialize()) return 1;

  // ---------------------------------------------------
  //                      EXECUTION
  // ---------------------------------------------------
  INFO << "    * Running over files ..." << endmsg;

  // Loop over files
  while(1)
  {
    // Opening input file
    mySamples.push_back(SampleFormat());
    SampleFormat& mySample=mySamples.back();
    StatusCode::Type result1 = manager.NextFile(mySample);
    if (result1!=StatusCode::KEEP)
    {
      if (result1==StatusCode::SKIP) continue;
      else if (result1==StatusCode::FAILURE) {mySamples.pop_back(); break;}
    }
    
    // Loop over events
    while(1)
    {
      StatusCode::Type result2 = manager.NextEvent(mySample,myEvent);
      if (result2!=StatusCode::KEEP)
      {
        if (result2==StatusCode::SKIP) continue;
        else if (result2==StatusCode::FAILURE) break;
      }
          manager.UpdateProgressBar();
      if (!analyzer_cms_top_18_003->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_top_17_009->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_sus_17_001->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_sus_16_052->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_sus_16_048->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_sus_16_039->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_sus_16_033->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_exo_16_022->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_exo_16_012->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_exo_16_010->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_exo_12_048->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_exo_12_047->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_b2g_14_004->Execute(mySample,myEvent)) continue;
      if (!analyzer_cms_b2g_12_022->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_susy_2019_08->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_susy_2018_031->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_susy_2018_06->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_conf_2019_040->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_susy_2015_06->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_exot_2015_03->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_conf_2016_086->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_susy_2016_07->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_exot_2018_30->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_exot_2016_32->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_exot_2016_25->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_exot_2016_27->Execute(mySample,myEvent)) continue;
      if (!analyzer_atlas_exot_2014_06->Execute(mySample,myEvent)) continue;
      if (!analyzer1->Execute(mySample,myEvent)) continue;
    }
  }

  // ---------------------------------------------------
  //                     FINALIZATION
  // ---------------------------------------------------
  INFO << "    * Finalizing all components ..." << endmsg;

  // Finalizing all components
  manager.Finalize(mySamples,myEvent);
  return 0;
}
