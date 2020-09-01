#include "SampleAnalyzer/User/Analyzer/cms_sus_16_039.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_sus_16_039::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>   Analysis: CMS_SUS_16_039, arXiv:1709.05406 <>" << endmsg;
  INFO << "      <>             (multilepton LHC13, 35.9 fb^-1)  <>" << endmsg;
  INFO << "      <>   Recasted by: B. Fuks, S. Mondal            <>" << endmsg;
  INFO << "      <>   Contacts: fuks@lpthe.jussieu.fr            <>" << endmsg;
  INFO << "      <>             subhadeep.mondal@helsinki.fi     <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.6                <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // -- define signal regions -- //
  Manager()->AddRegionSelection("SRSS01_Njets0_MT0to100_PTll0to50_MET0to100");
  Manager()->AddRegionSelection("SRSS02_lPP_Njets0_MT0to100_PTll0to50_MET100to150");
  Manager()->AddRegionSelection("SRSS03_lMM_Njets0_MT0to100_PTll0to50_MET100to150");
  Manager()->AddRegionSelection("SRSS04_Njets0_MT0to100_PTll0to50_MET150to200");
  Manager()->AddRegionSelection("SRSS05_Njets0_MT0to100_PTll0to50_MET200toInf");
  Manager()->AddRegionSelection("SRSS06_Njets0_MT0to100_PTll50toInf_MET0to100");
  Manager()->AddRegionSelection("SRSS07_lPP_Njets0_MT0to100_PTll50toInf_MET100to150");
  Manager()->AddRegionSelection("SRSS08_lMM_Njets0_MT0to100_PTll50toInf_MET100to150");
  Manager()->AddRegionSelection("SRSS09_Njets0_MT0to100_PTll50toInf_MET150to200");
  Manager()->AddRegionSelection("SRSS10_Njets0_MT0to100_PTll50toInf_MET200toInf");
  Manager()->AddRegionSelection("SRSS11_Njets0_MT100toInf_MET0to100");
  Manager()->AddRegionSelection("SRSS12_lPP_Njets0_MT100toInf_MET100to150");
  Manager()->AddRegionSelection("SRSS13_lMM_Njets0_MT100toInf_MET100to150");
  Manager()->AddRegionSelection("SRSS14_Njets0_MT100toInf_MET150to200");
  Manager()->AddRegionSelection("SRSS15_Njets0_MT100toInf_MET200toInf");
  Manager()->AddRegionSelection("SRSS16_Njets1_MT0to100_PTll0to50_MET0to100");
  Manager()->AddRegionSelection("SRSS17_lPP_Njets1_MT0to100_PTll0to50_MET100to150");
  Manager()->AddRegionSelection("SRSS18_lMM_Njets1_MT0to100_PTll0to50_MET100to150");
  Manager()->AddRegionSelection("SRSS19_Njets1_MT0to100_PTll0to50_MET150to200");
  Manager()->AddRegionSelection("SRSS20_Njets1_MT0to100_PTll0to50_MET200toInf");
  Manager()->AddRegionSelection("SRSS21_Njets1_MT0to100_PTll50toInf_MET0to100");
  Manager()->AddRegionSelection("SRSS22_lPP_Njets1_MT0to100_PTll50toInf_MET100to150");
  Manager()->AddRegionSelection("SRSS23_lMM_Njets1_MT0to100_PTll50toInf_MET100to150");
  Manager()->AddRegionSelection("SRSS24_Njets1_MT0to100_PTll50toInf_MET150to200");
  Manager()->AddRegionSelection("SRSS25_Njets1_MT0to100_PTll50toInf_MET200toInf");
  Manager()->AddRegionSelection("SRSS26_Njets1_MT100toInf_MET0to100");
  Manager()->AddRegionSelection("SRSS27_lPP_Njets1_MT100toInf_MET100to150");
  Manager()->AddRegionSelection("SRSS28_lMM_Njets1_MT100toInf_MET100to150");
  Manager()->AddRegionSelection("SRSS29_Njets1_MT100toInf_MET150to200");
  Manager()->AddRegionSelection("SRSS30_Njets1_MT100toInf_MET200toInf");
  Manager()->AddRegionSelection("SRA01_Mll0to75_MT0to100_MET50to100");
  Manager()->AddRegionSelection("SRA02_Mll0to75_MT0to100_MET100to150");
  Manager()->AddRegionSelection("SRA03_Mll0to75_MT0to100_MET150to200");
  Manager()->AddRegionSelection("SRA04_Mll0to75_MT0to100_MET200to250");
  Manager()->AddRegionSelection("SRA05_Mll0to75_MT0to100_MET250toInf");
  Manager()->AddRegionSelection("SRA06_Mll0to75_MT100to160_MET50to100");
  Manager()->AddRegionSelection("SRA07_Mll0to75_MT100to160_MET100to150");
  Manager()->AddRegionSelection("SRA08_Mll0to75_MT100to160_MET150to200");
  Manager()->AddRegionSelection("SRA09_Mll0to75_MT100to160_MET200toInf");
  Manager()->AddRegionSelection("SRA10_Mll0to75_MT160toInf_MET50to100");
  Manager()->AddRegionSelection("SRA11_Mll0to75_MT160toInf_MET100to150");
  Manager()->AddRegionSelection("SRA12_Mll0to75_MT160toInf_MET150to200");
  Manager()->AddRegionSelection("SRA13_Mll0to75_MT160toInf_MET200to250");
  Manager()->AddRegionSelection("SRA14_Mll0to75_MT160toInf_MET250toInf");
  Manager()->AddRegionSelection("SRA15_Mll75to105_MT0to100_MET50to100");
  Manager()->AddRegionSelection("SRA16_Mll75to105_MT0to100_MET100to150");
  Manager()->AddRegionSelection("SRA17_Mll75to105_MT0to100_MET150to200");
  Manager()->AddRegionSelection("SRA18_Mll75to105_MT0to100_MET200to250");
  Manager()->AddRegionSelection("SRA19_Mll75to105_MT0to100_MET250to400");
  Manager()->AddRegionSelection("SRA20_Mll75to105_MT0to100_MET400to550");
  Manager()->AddRegionSelection("SRA21_Mll75to105_MT0to100_MET550toInf");
  Manager()->AddRegionSelection("SRA22_Mll75to105_MT100to160_MET50to100");
  Manager()->AddRegionSelection("SRA23_Mll75to105_MT100to160_MET100to150");
  Manager()->AddRegionSelection("SRA24_Mll75to105_MT100to160_MET150to200");
  Manager()->AddRegionSelection("SRA25_Mll75to105_MT100to160_MET200toInf");
  Manager()->AddRegionSelection("SRA26_Mll75to105_MT160toInf_MET50to100");
  Manager()->AddRegionSelection("SRA27_Mll75to105_MT160toInf_MET100to150");
  Manager()->AddRegionSelection("SRA28_Mll75to105_MT160toInf_MET150to200");
  Manager()->AddRegionSelection("SRA29_Mll75to105_MT160toInf_MET200to250");
  Manager()->AddRegionSelection("SRA30_Mll75to105_MT160toInf_MET250to400");
  Manager()->AddRegionSelection("SRA31_Mll75to105_MT160toInf_MET400toInf");
  Manager()->AddRegionSelection("SRA32_Mll105toInf_MT0to100_MET50to100");
  Manager()->AddRegionSelection("SRA33_Mll105toInf_MT0to100_MET100to150");
  Manager()->AddRegionSelection("SRA34_Mll105toInf_MT0to100_MET150to200");
  Manager()->AddRegionSelection("SRA35_Mll105toInf_MT0to100_MET200to250");
  Manager()->AddRegionSelection("SRA36_Mll105toInf_MT0to100_MET250toInf");
  Manager()->AddRegionSelection("SRA37_Mll105toInf_MT100to160_MET50to100");
  Manager()->AddRegionSelection("SRA38_Mll105toInf_MT100to160_MET100to150");
  Manager()->AddRegionSelection("SRA39_Mll105toInf_MT100to160_MET150to200");
  Manager()->AddRegionSelection("SRA40_Mll105toInf_MT100to160_MET200toInf");
  Manager()->AddRegionSelection("SRA41_Mll105toInf_MT160toInf_MET50to100");
  Manager()->AddRegionSelection("SRA42_Mll105toInf_MT160toInf_MET100to150");
  Manager()->AddRegionSelection("SRA43_Mll105toInf_MT160toInf_MET150to200");
  Manager()->AddRegionSelection("SRA44_Mll105toInf_MT160toInf_MET200toInf");
  Manager()->AddRegionSelection("SRB01_Mll0to100_MT0to120_MET50to100");
  Manager()->AddRegionSelection("SRB02_Mll0to100_MT0to120_MET100toInf");
  Manager()->AddRegionSelection("SRB03_Mll0to100_MT120toInf_MET50toInf");
  Manager()->AddRegionSelection("SRB04_Mll100toInf_MT0to120_MET50to100");
  Manager()->AddRegionSelection("SRB05_Mll100toInf_MT0to120_MET100toInf");
  Manager()->AddRegionSelection("SRB06_Mll100toInf_MT120toInf_MET50toInf");
  Manager()->AddRegionSelection("SRC01_Mll0to75_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRC02_Mll0to75_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRC03_Mll0to75_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRC04_Mll0to75_MT20to100_MET200to250");
  Manager()->AddRegionSelection("SRC05_Mll0to75_MT20to100_MET250toInf");
  Manager()->AddRegionSelection("SRC06_Mll75to105_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRC07_Mll75to105_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRC08_Mll75to105_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRC09_Mll75to105_MT20to100_MET200to300");
  Manager()->AddRegionSelection("SRC10_Mll75to105_MT20to100_MET300to400");
  Manager()->AddRegionSelection("SRC11_Mll75to105_MT20to100_MET400toInf");
  Manager()->AddRegionSelection("SRC12_Mll105toInf_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRC13_Mll105toInf_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRC14_Mll105toInf_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRC15_Mll105toInf_MT20to100_MET200to250");
  Manager()->AddRegionSelection("SRC16_Mll105toInf_MT20to100_MET250toInf");
  Manager()->AddRegionSelection("SRC17_Mll0to75or105toInf_MT2100toInf_MET50to200");
  Manager()->AddRegionSelection("SRC18_Mll0to75or105toInf_MT2100toInf_MET200toInf");
  Manager()->AddRegionSelection("SRD01_Mll0to60_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRD02_Mll0to60_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRD03_Mll0to60_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRD04_Mll0to60_MT20to100_MET200to250");
  Manager()->AddRegionSelection("SRD05_Mll0to60_MT20to100_MET250toInf");
  Manager()->AddRegionSelection("SRD06_Mll60to100_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRD07_Mll60to100_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRD08_Mll60to100_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRD09_Mll60to100_MT20to100_MET200to250");
  Manager()->AddRegionSelection("SRD10_Mll60to100_MT20to100_MET250toInf");
  Manager()->AddRegionSelection("SRD11_Mll100toInf_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRD12_Mll100toInf_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRD13_Mll100toInf_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRD14_Mll100toInf_MT20to100_MET200toInf");
  Manager()->AddRegionSelection("SRD15_Mll0toInf_MT2100toInf_MET50to200"); 
  Manager()->AddRegionSelection("SRD16_Mll0toInf_MT2100toInf_MET200toInf");
  Manager()->AddRegionSelection("SRE01_Mll0to60_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRE02_Mll0to60_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRE03_Mll0to60_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRE04_Mll0to60_MT20to100_MET200to250");
  Manager()->AddRegionSelection("SRE05_Mll0to60_MT20to100_MET250toInf");
  Manager()->AddRegionSelection("SRE06_Mll60to100_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRE07_Mll60to100_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRE08_Mll60to100_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRE09_Mll60to100_MT20to100_MET200to250");
  Manager()->AddRegionSelection("SRE10_Mll60to100_MT20to100_MET250toInf");
  Manager()->AddRegionSelection("SRE11_Mll100toInf_MT20to100_MET50toInf"); 
  Manager()->AddRegionSelection("SRE12_Mll0toInf_MT2100toInf_MET50toInf");
  Manager()->AddRegionSelection("SRF01_Mll0to100_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRF02_Mll0to100_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRF03_Mll0to100_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRF04_Mll0to100_MT20to100_MET200to250");
  Manager()->AddRegionSelection("SRF05_Mll0to100_MT20to100_MET250to300");
  Manager()->AddRegionSelection("SRF06_Mll0to100_MT20to100_MET300toInf");
  Manager()->AddRegionSelection("SRF07_Mll100toInf_MT20to100_MET50to100");
  Manager()->AddRegionSelection("SRF08_Mll100toInf_MT20to100_MET100to150");
  Manager()->AddRegionSelection("SRF09_Mll100toInf_MT20to100_MET150to200");
  Manager()->AddRegionSelection("SRF10_Mll100toInf_MT20to100_MET200toInf");
  Manager()->AddRegionSelection("SRF11_Mll0toInf_MT2100toInf_MET50to200"); 
  Manager()->AddRegionSelection("SRF12_Mll0toInf_MT2100toInf_MET200toInf");
  Manager()->AddRegionSelection("SRG01_MET0to50");
  Manager()->AddRegionSelection("SRG02_MET50to100");
  Manager()->AddRegionSelection("SRG03_MET100to150");
  Manager()->AddRegionSelection("SRG04_MET150to200");
  Manager()->AddRegionSelection("SRG05_MET200toInf");
  Manager()->AddRegionSelection("SRH01_MET0to50");
  Manager()->AddRegionSelection("SRH02_MET50to100");
  Manager()->AddRegionSelection("SRH03_MET100to150");
  Manager()->AddRegionSelection("SRH04_MET150toInf");
  Manager()->AddRegionSelection("SRI01_MET0to50");
  Manager()->AddRegionSelection("SRI02_MET50to100");
  Manager()->AddRegionSelection("SRI03_MET100to150");
  Manager()->AddRegionSelection("SRI04_MET150toInf");
  Manager()->AddRegionSelection("SRJ01_MET0to50");
  Manager()->AddRegionSelection("SRJ02_MET50to100");
  Manager()->AddRegionSelection("SRJ03_MET100to150");
  Manager()->AddRegionSelection("SRJ04_MET150toInf");
  Manager()->AddRegionSelection("SRK01_MET0to50");
  Manager()->AddRegionSelection("SRK02_MET50to100");
  Manager()->AddRegionSelection("SRK03_MET100toInf");

  std::string SRSS[] = {
  "SRSS01_Njets0_MT0to100_PTll0to50_MET0to100", "SRSS02_lPP_Njets0_MT0to100_PTll0to50_MET100to150",
  "SRSS03_lMM_Njets0_MT0to100_PTll0to50_MET100to150",  "SRSS04_Njets0_MT0to100_PTll0to50_MET150to200",
  "SRSS05_Njets0_MT0to100_PTll0to50_MET200toInf",  "SRSS06_Njets0_MT0to100_PTll50toInf_MET0to100",
  "SRSS07_lPP_Njets0_MT0to100_PTll50toInf_MET100to150",  "SRSS08_lMM_Njets0_MT0to100_PTll50toInf_MET100to150",
  "SRSS09_Njets0_MT0to100_PTll50toInf_MET150to200",  "SRSS10_Njets0_MT0to100_PTll50toInf_MET200toInf",
  "SRSS11_Njets0_MT100toInf_MET0to100",  "SRSS12_lPP_Njets0_MT100toInf_MET100to150",
  "SRSS13_lMM_Njets0_MT100toInf_MET100to150",  "SRSS14_Njets0_MT100toInf_MET150to200",
  "SRSS15_Njets0_MT100toInf_MET200toInf",  "SRSS16_Njets1_MT0to100_PTll0to50_MET0to100",
  "SRSS17_lPP_Njets1_MT0to100_PTll0to50_MET100to150",   "SRSS18_lMM_Njets1_MT0to100_PTll0to50_MET100to150",
  "SRSS19_Njets1_MT0to100_PTll0to50_MET150to200",  "SRSS20_Njets1_MT0to100_PTll0to50_MET200toInf",
  "SRSS21_Njets1_MT0to100_PTll50toInf_MET0to100",  "SRSS22_lPP_Njets1_MT0to100_PTll50toInf_MET100to150",
  "SRSS23_lMM_Njets1_MT0to100_PTll50toInf_MET100to150",  "SRSS24_Njets1_MT0to100_PTll50toInf_MET150to200",
  "SRSS25_Njets1_MT0to100_PTll50toInf_MET200toInf",  "SRSS26_Njets1_MT100toInf_MET0to100",
  "SRSS27_lPP_Njets1_MT100toInf_MET100to150",  "SRSS28_lMM_Njets1_MT100toInf_MET100to150",
  "SRSS29_Njets1_MT100toInf_MET150to200",  "SRSS30_Njets1_MT100toInf_MET200toInf" };

  std::string SRA[] = {"SRA01_Mll0to75_MT0to100_MET50to100", "SRA02_Mll0to75_MT0to100_MET100to150",
    "SRA03_Mll0to75_MT0to100_MET150to200", "SRA04_Mll0to75_MT0to100_MET200to250",
    "SRA05_Mll0to75_MT0to100_MET250toInf", "SRA06_Mll0to75_MT100to160_MET50to100",
    "SRA07_Mll0to75_MT100to160_MET100to150", "SRA08_Mll0to75_MT100to160_MET150to200",
    "SRA09_Mll0to75_MT100to160_MET200toInf", "SRA10_Mll0to75_MT160toInf_MET50to100",
    "SRA11_Mll0to75_MT160toInf_MET100to150", "SRA12_Mll0to75_MT160toInf_MET150to200",
    "SRA13_Mll0to75_MT160toInf_MET200to250", "SRA14_Mll0to75_MT160toInf_MET250toInf",
    "SRA15_Mll75to105_MT0to100_MET50to100", "SRA16_Mll75to105_MT0to100_MET100to150",
    "SRA17_Mll75to105_MT0to100_MET150to200", "SRA18_Mll75to105_MT0to100_MET200to250",
    "SRA19_Mll75to105_MT0to100_MET250to400", "SRA20_Mll75to105_MT0to100_MET400to550",
    "SRA21_Mll75to105_MT0to100_MET550toInf", "SRA22_Mll75to105_MT100to160_MET50to100",
    "SRA23_Mll75to105_MT100to160_MET100to150", "SRA24_Mll75to105_MT100to160_MET150to200",
    "SRA25_Mll75to105_MT100to160_MET200toInf", "SRA26_Mll75to105_MT160toInf_MET50to100",
    "SRA27_Mll75to105_MT160toInf_MET100to150", "SRA28_Mll75to105_MT160toInf_MET150to200",
    "SRA29_Mll75to105_MT160toInf_MET200to250", "SRA30_Mll75to105_MT160toInf_MET250to400",
    "SRA31_Mll75to105_MT160toInf_MET400toInf", "SRA32_Mll105toInf_MT0to100_MET50to100",
    "SRA33_Mll105toInf_MT0to100_MET100to150", "SRA34_Mll105toInf_MT0to100_MET150to200",
    "SRA35_Mll105toInf_MT0to100_MET200to250", "SRA36_Mll105toInf_MT0to100_MET250toInf",
    "SRA37_Mll105toInf_MT100to160_MET50to100", "SRA38_Mll105toInf_MT100to160_MET100to150",
    "SRA39_Mll105toInf_MT100to160_MET150to200", "SRA40_Mll105toInf_MT100to160_MET200toInf",
    "SRA41_Mll105toInf_MT160toInf_MET50to100", "SRA42_Mll105toInf_MT160toInf_MET100to150",
    "SRA43_Mll105toInf_MT160toInf_MET150to200", "SRA44_Mll105toInf_MT160toInf_MET200toInf" };

  std::string SRB[] = { "SRB01_Mll0to100_MT0to120_MET50to100", "SRB02_Mll0to100_MT0to120_MET100toInf",
    "SRB03_Mll0to100_MT120toInf_MET50toInf", "SRB04_Mll100toInf_MT0to120_MET50to100",
    "SRB05_Mll100toInf_MT0to120_MET100toInf", "SRB06_Mll100toInf_MT120toInf_MET50toInf"};

  std::string SRC[] = { "SRC01_Mll0to75_MT20to100_MET50to100", "SRC02_Mll0to75_MT20to100_MET100to150",
    "SRC03_Mll0to75_MT20to100_MET150to200",    "SRC04_Mll0to75_MT20to100_MET200to250",
    "SRC05_Mll0to75_MT20to100_MET250toInf",    "SRC06_Mll75to105_MT20to100_MET50to100",
    "SRC07_Mll75to105_MT20to100_MET100to150",  "SRC08_Mll75to105_MT20to100_MET150to200",
    "SRC09_Mll75to105_MT20to100_MET200to300",  "SRC10_Mll75to105_MT20to100_MET300to400",
    "SRC11_Mll75to105_MT20to100_MET400toInf",  "SRC12_Mll105toInf_MT20to100_MET50to100",
    "SRC13_Mll105toInf_MT20to100_MET100to150", "SRC14_Mll105toInf_MT20to100_MET150to200",
    "SRC15_Mll105toInf_MT20to100_MET200to250", "SRC16_Mll105toInf_MT20to100_MET250toInf",
    "SRC17_Mll0to75or105toInf_MT2100toInf_MET50to200", "SRC18_Mll0to75or105toInf_MT2100toInf_MET200toInf"};

  std::string SRD[] = { "SRD01_Mll0to60_MT20to100_MET50to100", "SRD02_Mll0to60_MT20to100_MET100to150",
    "SRD03_Mll0to60_MT20to100_MET150to200",    "SRD04_Mll0to60_MT20to100_MET200to250",
    "SRD05_Mll0to60_MT20to100_MET250toInf",    "SRD06_Mll60to100_MT20to100_MET50to100",
    "SRD07_Mll60to100_MT20to100_MET100to150",  "SRD08_Mll60to100_MT20to100_MET150to200",
    "SRD09_Mll60to100_MT20to100_MET200to250",  "SRD10_Mll60to100_MT20to100_MET250toInf",
    "SRD11_Mll100toInf_MT20to100_MET50to100",  "SRD12_Mll100toInf_MT20to100_MET100to150",
    "SRD13_Mll100toInf_MT20to100_MET150to200", "SRD14_Mll100toInf_MT20to100_MET200toInf",
    "SRD15_Mll0toInf_MT2100toInf_MET50to200",  "SRD16_Mll0toInf_MT2100toInf_MET200toInf"};

  std::string SRE[] = { "SRE01_Mll0to60_MT20to100_MET50to100", "SRE02_Mll0to60_MT20to100_MET100to150",
    "SRE03_Mll0to60_MT20to100_MET150to200",   "SRE04_Mll0to60_MT20to100_MET200to250",
    "SRE05_Mll0to60_MT20to100_MET250toInf",   "SRE06_Mll60to100_MT20to100_MET50to100",
    "SRE07_Mll60to100_MT20to100_MET100to150", "SRE08_Mll60to100_MT20to100_MET150to200",
    "SRE09_Mll60to100_MT20to100_MET200to250", "SRE10_Mll60to100_MT20to100_MET250toInf",
    "SRE11_Mll100toInf_MT20to100_MET50toInf", "SRE12_Mll0toInf_MT2100toInf_MET50toInf"};

  std::string SRF[] = {"SRF01_Mll0to100_MT20to100_MET50to100", "SRF02_Mll0to100_MT20to100_MET100to150",
    "SRF03_Mll0to100_MT20to100_MET150to200",   "SRF04_Mll0to100_MT20to100_MET200to250",
    "SRF05_Mll0to100_MT20to100_MET250to300",   "SRF06_Mll0to100_MT20to100_MET300toInf",
    "SRF07_Mll100toInf_MT20to100_MET50to100",  "SRF08_Mll100toInf_MT20to100_MET100to150",
    "SRF09_Mll100toInf_MT20to100_MET150to200", "SRF10_Mll100toInf_MT20to100_MET200toInf",
    "SRF11_Mll0toInf_MT2100toInf_MET50to200", "SRF12_Mll0toInf_MT2100toInf_MET200toInf"};

  std::string SR3l[] = {"SRA01_Mll0to75_MT0to100_MET50to100", "SRA02_Mll0to75_MT0to100_MET100to150",
    "SRA03_Mll0to75_MT0to100_MET150to200", "SRA04_Mll0to75_MT0to100_MET200to250",
    "SRA05_Mll0to75_MT0to100_MET250toInf", "SRA06_Mll0to75_MT100to160_MET50to100",
    "SRA07_Mll0to75_MT100to160_MET100to150", "SRA08_Mll0to75_MT100to160_MET150to200",
    "SRA09_Mll0to75_MT100to160_MET200toInf", "SRA10_Mll0to75_MT160toInf_MET50to100",
    "SRA11_Mll0to75_MT160toInf_MET100to150", "SRA12_Mll0to75_MT160toInf_MET150to200",
    "SRA13_Mll0to75_MT160toInf_MET200to250", "SRA14_Mll0to75_MT160toInf_MET250toInf",
    "SRA15_Mll75to105_MT0to100_MET50to100", "SRA16_Mll75to105_MT0to100_MET100to150",
    "SRA17_Mll75to105_MT0to100_MET150to200", "SRA18_Mll75to105_MT0to100_MET200to250",
    "SRA19_Mll75to105_MT0to100_MET250to400", "SRA20_Mll75to105_MT0to100_MET400to550",
    "SRA21_Mll75to105_MT0to100_MET550toInf", "SRA22_Mll75to105_MT100to160_MET50to100",
    "SRA23_Mll75to105_MT100to160_MET100to150", "SRA24_Mll75to105_MT100to160_MET150to200",
    "SRA25_Mll75to105_MT100to160_MET200toInf", "SRA26_Mll75to105_MT160toInf_MET50to100",
    "SRA27_Mll75to105_MT160toInf_MET100to150", "SRA28_Mll75to105_MT160toInf_MET150to200",
    "SRA29_Mll75to105_MT160toInf_MET200to250", "SRA30_Mll75to105_MT160toInf_MET250to400",
    "SRA31_Mll75to105_MT160toInf_MET400toInf", "SRA32_Mll105toInf_MT0to100_MET50to100",
    "SRA33_Mll105toInf_MT0to100_MET100to150", "SRA34_Mll105toInf_MT0to100_MET150to200",
    "SRA35_Mll105toInf_MT0to100_MET200to250", "SRA36_Mll105toInf_MT0to100_MET250toInf",
    "SRA37_Mll105toInf_MT100to160_MET50to100", "SRA38_Mll105toInf_MT100to160_MET100to150",
    "SRA39_Mll105toInf_MT100to160_MET150to200", "SRA40_Mll105toInf_MT100to160_MET200toInf",
    "SRA41_Mll105toInf_MT160toInf_MET50to100", "SRA42_Mll105toInf_MT160toInf_MET100to150",
    "SRA43_Mll105toInf_MT160toInf_MET150to200", "SRA44_Mll105toInf_MT160toInf_MET200toInf",
    "SRB01_Mll0to100_MT0to120_MET50to100", "SRB02_Mll0to100_MT0to120_MET100toInf",
    "SRB03_Mll0to100_MT120toInf_MET50toInf", "SRB04_Mll100toInf_MT0to120_MET50to100",
    "SRB05_Mll100toInf_MT0to120_MET100toInf", "SRB06_Mll100toInf_MT120toInf_MET50toInf",
    "SRC01_Mll0to75_MT20to100_MET50to100", "SRC02_Mll0to75_MT20to100_MET100to150",
    "SRC03_Mll0to75_MT20to100_MET150to200",    "SRC04_Mll0to75_MT20to100_MET200to250",
    "SRC05_Mll0to75_MT20to100_MET250toInf",    "SRC06_Mll75to105_MT20to100_MET50to100",
    "SRC07_Mll75to105_MT20to100_MET100to150",  "SRC08_Mll75to105_MT20to100_MET150to200",
    "SRC09_Mll75to105_MT20to100_MET200to300",  "SRC10_Mll75to105_MT20to100_MET300to400",
    "SRC11_Mll75to105_MT20to100_MET400toInf",  "SRC12_Mll105toInf_MT20to100_MET50to100",
    "SRC13_Mll105toInf_MT20to100_MET100to150", "SRC14_Mll105toInf_MT20to100_MET150to200",
    "SRC15_Mll105toInf_MT20to100_MET200to250", "SRC16_Mll105toInf_MT20to100_MET250toInf",
    "SRC17_Mll0to75or105toInf_MT2100toInf_MET50to200", "SRC18_Mll0to75or105toInf_MT2100toInf_MET200toInf",
    "SRD01_Mll0to60_MT20to100_MET50to100", "SRD02_Mll0to60_MT20to100_MET100to150",
    "SRD03_Mll0to60_MT20to100_MET150to200",    "SRD04_Mll0to60_MT20to100_MET200to250",
    "SRD05_Mll0to60_MT20to100_MET250toInf",    "SRD06_Mll60to100_MT20to100_MET50to100",
    "SRD07_Mll60to100_MT20to100_MET100to150",  "SRD08_Mll60to100_MT20to100_MET150to200",
    "SRD09_Mll60to100_MT20to100_MET200to250",  "SRD10_Mll60to100_MT20to100_MET250toInf",
    "SRD11_Mll100toInf_MT20to100_MET50to100",  "SRD12_Mll100toInf_MT20to100_MET100to150",
    "SRD13_Mll100toInf_MT20to100_MET150to200", "SRD14_Mll100toInf_MT20to100_MET200toInf",
    "SRD15_Mll0toInf_MT2100toInf_MET50to200",  "SRD16_Mll0toInf_MT2100toInf_MET200toInf",
    "SRE01_Mll0to60_MT20to100_MET50to100", "SRE02_Mll0to60_MT20to100_MET100to150",
    "SRE03_Mll0to60_MT20to100_MET150to200",   "SRE04_Mll0to60_MT20to100_MET200to250",
    "SRE05_Mll0to60_MT20to100_MET250toInf",   "SRE06_Mll60to100_MT20to100_MET50to100",
    "SRE07_Mll60to100_MT20to100_MET100to150", "SRE08_Mll60to100_MT20to100_MET150to200",
    "SRE09_Mll60to100_MT20to100_MET200to250", "SRE10_Mll60to100_MT20to100_MET250toInf",
    "SRE11_Mll100toInf_MT20to100_MET50toInf", "SRE12_Mll0toInf_MT2100toInf_MET50toInf",
    "SRF01_Mll0to100_MT20to100_MET50to100", "SRF02_Mll0to100_MT20to100_MET100to150",
    "SRF03_Mll0to100_MT20to100_MET150to200",   "SRF04_Mll0to100_MT20to100_MET200to250",
    "SRF05_Mll0to100_MT20to100_MET250to300",   "SRF06_Mll0to100_MT20to100_MET300toInf",
    "SRF07_Mll100toInf_MT20to100_MET50to100",  "SRF08_Mll100toInf_MT20to100_MET100to150",
    "SRF09_Mll100toInf_MT20to100_MET150to200", "SRF10_Mll100toInf_MT20to100_MET200toInf",
    "SRF11_Mll0toInf_MT2100toInf_MET50to200", "SRF12_Mll0toInf_MT2100toInf_MET200toInf"};

  std::string SRG[] = {"SRG01_MET0to50", "SRG02_MET50to100", "SRG03_MET100to150", "SRG04_MET150to200",
    "SRG05_MET200toInf" };

  std::string SRH[] = {"SRH01_MET0to50", "SRH02_MET50to100", "SRH03_MET100to150", "SRH04_MET150toInf" };

  std::string SRI[] = {"SRI01_MET0to50", "SRI02_MET50to100", "SRI03_MET100to150", "SRI04_MET150toInf" };

  std::string SRJ[] = {"SRJ01_MET0to50", "SRJ02_MET50to100", "SRJ03_MET100to150", "SRJ04_MET150toInf" };

  std::string SRK[] = {"SRK01_MET0to50", "SRK02_MET50to100", "SRK03_MET100toInf" };

  std::string SR4l[] = { "SRG01_MET0to50", "SRG02_MET50to100", "SRG03_MET100to150", "SRG04_MET150to200",
    "SRG05_MET200toInf" , "SRH01_MET0to50", "SRH02_MET50to100", "SRH03_MET100to150", "SRH04_MET150toInf",
    "SRI01_MET0to50", "SRI02_MET50to100", "SRI03_MET100to150", "SRI04_MET150toInf",
    "SRJ01_MET0to50", "SRJ02_MET50to100", "SRJ03_MET100to150", "SRJ04_MET150toInf",
    "SRK01_MET0to50", "SRK02_MET50to100", "SRK03_MET100toInf" };

  // Baseline cuts
  Manager()->AddCut("baseline_A", SRA);
  Manager()->AddCut("baseline_B", SRB);
  Manager()->AddCut("baseline_C", SRC);
  Manager()->AddCut("baseline_D", SRD);
  Manager()->AddCut("baseline_E", SRE);
  Manager()->AddCut("baseline_F", SRF);
  Manager()->AddCut("baseline_G", SRG);
  Manager()->AddCut("baseline_H", SRH);
  Manager()->AddCut("baseline_I", SRI);
  Manager()->AddCut("baseline_J", SRJ);
  Manager()->AddCut("baseline_K", SRK);

  // Lepton number (part of the baseline cuts)
  Manager()->AddCut("2 tight leptons", SRSS);
  Manager()->AddCut("3 tight leptons", SR3l);
  Manager()->AddCut("4 tight leptons", SR4l);

  // SS specific cuts
  std::string SS_plus[] = {
    "SRSS02_lPP_Njets0_MT0to100_PTll0to50_MET100to150", "SRSS07_lPP_Njets0_MT0to100_PTll50toInf_MET100to150",
    "SRSS12_lPP_Njets0_MT100toInf_MET100to150", "SRSS17_lPP_Njets1_MT0to100_PTll0to50_MET100to150",
    "SRSS22_lPP_Njets1_MT0to100_PTll50toInf_MET100to150", "SRSS27_lPP_Njets1_MT100toInf_MET100to150"};
  std::string SS_minus[] = {
    "SRSS03_lMM_Njets0_MT0to100_PTll0to50_MET100to150", "SRSS08_lMM_Njets0_MT0to100_PTll50toInf_MET100to150",
    "SRSS13_lMM_Njets0_MT100toInf_MET100to150",  "SRSS18_lMM_Njets1_MT0to100_PTll0to50_MET100to150",
    "SRSS23_lMM_Njets1_MT0to100_PTll50toInf_MET100to150", "SRSS28_lMM_Njets1_MT100toInf_MET100to150"};

  Manager()->AddCut("Same sign", SRSS);
  Manager()->AddCut("Same sign++", SS_plus);
  Manager()->AddCut("Same sign--", SS_minus);

  // vetos
  Manager()->AddCut("3rd lepton veto", SRSS);
  Manager()->AddCut("4th lepton veto", SR3l);
  Manager()->AddCut("low-mass veto");
  Manager()->AddCut("conversion veto",SR3l);
  Manager()->AddCut("b-jet veto");

  // Baseline MET cut
  Manager()->AddCut("base_met");

  // NJet cuts
  std::string SR_Njets0[] =  {
     "SRSS02_lPP_Njets0_MT0to100_PTll0to50_MET100to150",
     "SRSS03_lMM_Njets0_MT0to100_PTll0to50_MET100to150",  "SRSS04_Njets0_MT0to100_PTll0to50_MET150to200",
     "SRSS05_Njets0_MT0to100_PTll0to50_MET200toInf",  "SRSS06_Njets0_MT0to100_PTll50toInf_MET0to100",
     "SRSS07_lPP_Njets0_MT0to100_PTll50toInf_MET100to150",  "SRSS08_lMM_Njets0_MT0to100_PTll50toInf_MET100to150",
     "SRSS09_Njets0_MT0to100_PTll50toInf_MET150to200",  "SRSS10_Njets0_MT0to100_PTll50toInf_MET200toInf",
     "SRSS11_Njets0_MT100toInf_MET0to100",  "SRSS12_lPP_Njets0_MT100toInf_MET100to150",
     "SRSS13_lMM_Njets0_MT100toInf_MET100to150",  "SRSS14_Njets0_MT100toInf_MET150to200",
     "SRSS15_Njets0_MT100toInf_MET200toInf" };
  std::string SR_Njets1[] =  {"SRSS16_Njets1_MT0to100_PTll0to50_MET0to100",
     "SRSS17_lPP_Njets1_MT0to100_PTll0to50_MET100to150",   "SRSS18_lMM_Njets1_MT0to100_PTll0to50_MET100to150",
     "SRSS19_Njets1_MT0to100_PTll0to50_MET150to200",  "SRSS20_Njets1_MT0to100_PTll0to50_MET200toInf",
     "SRSS21_Njets1_MT0to100_PTll50toInf_MET0to100",  "SRSS22_lPP_Njets1_MT0to100_PTll50toInf_MET100to150",
     "SRSS23_lMM_Njets1_MT0to100_PTll50toInf_MET100to150",  "SRSS24_Njets1_MT0to100_PTll50toInf_MET150to200",
     "SRSS25_Njets1_MT0to100_PTll50toInf_MET200toInf",  "SRSS26_Njets1_MT100toInf_MET0to100",
     "SRSS27_lPP_Njets1_MT100toInf_MET100to150",  "SRSS28_lMM_Njets1_MT100toInf_MET100to150",
     "SRSS29_Njets1_MT100toInf_MET150to200",  "SRSS30_Njets1_MT100toInf_MET200toInf" };

  Manager()->AddCut("Njets40 = 0/1", "SRSS01_Njets0_MT0to100_PTll0to50_MET0to100" );
  Manager()->AddCut("Njets40 = 0", SR_Njets0 );
  Manager()->AddCut("Njets40 = 1", SR_Njets1 );

  // MT cuts
  std::string SR_MT0to100[] = {
     "SRSS01_Njets0_MT0to100_PTll0to50_MET0to100",          "SRSS02_lPP_Njets0_MT0to100_PTll0to50_MET100to150",
     "SRSS03_lMM_Njets0_MT0to100_PTll0to50_MET100to150",    "SRSS04_Njets0_MT0to100_PTll0to50_MET150to200",
     "SRSS05_Njets0_MT0to100_PTll0to50_MET200toInf",        "SRSS06_Njets0_MT0to100_PTll50toInf_MET0to100",
     "SRSS07_lPP_Njets0_MT0to100_PTll50toInf_MET100to150",  "SRSS08_lMM_Njets0_MT0to100_PTll50toInf_MET100to150",
     "SRSS09_Njets0_MT0to100_PTll50toInf_MET150to200",      "SRSS10_Njets0_MT0to100_PTll50toInf_MET200toInf",
     "SRSS16_Njets1_MT0to100_PTll0to50_MET0to100",
     "SRSS17_lPP_Njets1_MT0to100_PTll0to50_MET100to150",    "SRSS18_lMM_Njets1_MT0to100_PTll0to50_MET100to150",
     "SRSS19_Njets1_MT0to100_PTll0to50_MET150to200",        "SRSS20_Njets1_MT0to100_PTll0to50_MET200toInf",
     "SRSS21_Njets1_MT0to100_PTll50toInf_MET0to100",        "SRSS22_lPP_Njets1_MT0to100_PTll50toInf_MET100to150",
     "SRSS23_lMM_Njets1_MT0to100_PTll50toInf_MET100to150",  "SRSS24_Njets1_MT0to100_PTll50toInf_MET150to200",
     "SRSS25_Njets1_MT0to100_PTll50toInf_MET200toInf",      
     "SRA02_Mll0to75_MT0to100_MET100to150",                 "SRA03_Mll0to75_MT0to100_MET150to200",
     "SRA04_Mll0to75_MT0to100_MET200to250",                 "SRA05_Mll0to75_MT0to100_MET250toInf",
     "SRA15_Mll75to105_MT0to100_MET50to100",                "SRA16_Mll75to105_MT0to100_MET100to150",
     "SRA17_Mll75to105_MT0to100_MET150to200",               "SRA18_Mll75to105_MT0to100_MET200to250",
     "SRA19_Mll75to105_MT0to100_MET250to400",               "SRA20_Mll75to105_MT0to100_MET400to550",
     "SRA21_Mll75to105_MT0to100_MET550toInf",               "SRA32_Mll105toInf_MT0to100_MET50to100",
     "SRA33_Mll105toInf_MT0to100_MET100to150",              "SRA34_Mll105toInf_MT0to100_MET150to200",
     "SRA35_Mll105toInf_MT0to100_MET200to250",              "SRA36_Mll105toInf_MT0to100_MET250toInf"};
  std::string SR_MT0to120[] = { "SRB01_Mll0to100_MT0to120_MET50to100", "SRB02_Mll0to100_MT0to120_MET100toInf",
      "SRB04_Mll100toInf_MT0to120_MET50to100", "SRB05_Mll100toInf_MT0to120_MET100toInf" };
  std::string SR_MT100to160[] = {"SRA06_Mll0to75_MT100to160_MET50to100",
      "SRA07_Mll0to75_MT100to160_MET100to150", "SRA08_Mll0to75_MT100to160_MET150to200",
      "SRA09_Mll0to75_MT100to160_MET200toInf", "SRA22_Mll75to105_MT100to160_MET50to100",
      "SRA23_Mll75to105_MT100to160_MET100to150", "SRA24_Mll75to105_MT100to160_MET150to200",
      "SRA25_Mll75to105_MT100to160_MET200toInf", "SRA37_Mll105toInf_MT100to160_MET50to100",
      "SRA38_Mll105toInf_MT100to160_MET100to150",  "SRA39_Mll105toInf_MT100to160_MET150to200",
      "SRA40_Mll105toInf_MT100to160_MET200toInf" };
  std::string SR_MT100toInf[] = {"SRA01_Mll0to75_MT0to100_MET50to100",
     "SRSS11_Njets0_MT100toInf_MET0to100",  "SRSS12_lPP_Njets0_MT100toInf_MET100to150",
     "SRSS13_lMM_Njets0_MT100toInf_MET100to150",  "SRSS14_Njets0_MT100toInf_MET150to200",
     "SRSS15_Njets0_MT100toInf_MET200toInf",  "SRSS26_Njets1_MT100toInf_MET0to100",
     "SRSS27_lPP_Njets1_MT100toInf_MET100to150",  "SRSS28_lMM_Njets1_MT100toInf_MET100to150",
     "SRSS29_Njets1_MT100toInf_MET150to200",  "SRSS30_Njets1_MT100toInf_MET200toInf" };
  std::string SR_MT120toInf[] = { "SRB03_Mll0to100_MT120toInf_MET50toInf",
      "SRB06_Mll100toInf_MT120toInf_MET50toInf" };
  std::string SR_MT160toInf[] = {  "SRA10_Mll0to75_MT160toInf_MET50to100",
      "SRA11_Mll0to75_MT160toInf_MET100to150", "SRA12_Mll0to75_MT160toInf_MET150to200",
      "SRA13_Mll0to75_MT160toInf_MET200to250", "SRA14_Mll0to75_MT160toInf_MET250toInf",
      "SRA26_Mll75to105_MT160toInf_MET50to100",
      "SRA27_Mll75to105_MT160toInf_MET100to150", "SRA28_Mll75to105_MT160toInf_MET150to200",
      "SRA29_Mll75to105_MT160toInf_MET200to250", "SRA30_Mll75to105_MT160toInf_MET250to400",
      "SRA31_Mll75to105_MT160toInf_MET400toInf", "SRA41_Mll105toInf_MT160toInf_MET50to100",
      "SRA42_Mll105toInf_MT160toInf_MET100to150",
      "SRA43_Mll105toInf_MT160toInf_MET150to200", "SRA44_Mll105toInf_MT160toInf_MET200toInf" };

  Manager()->AddCut("MT < 100 GeV", SR_MT0to100 );
  Manager()->AddCut("MT > 100 GeV", SR_MT100toInf );
  Manager()->AddCut("0 < MT < 120 GeV", SR_MT0to120 );
  Manager()->AddCut("100 < MT < 160 GeV", SR_MT100to160 );
  Manager()->AddCut("MT > 120 GeV", SR_MT120toInf );
  Manager()->AddCut("MT > 160 GeV", SR_MT160toInf );

  // PTll cuts
  std::string SR_PTll0to50[] =  {
     "SRSS02_lPP_Njets0_MT0to100_PTll0to50_MET100to150",
     "SRSS03_lMM_Njets0_MT0to100_PTll0to50_MET100to150",  "SRSS04_Njets0_MT0to100_PTll0to50_MET150to200",
     "SRSS05_Njets0_MT0to100_PTll0to50_MET200toInf","SRSS16_Njets1_MT0to100_PTll0to50_MET0to100",
     "SRSS17_lPP_Njets1_MT0to100_PTll0to50_MET100to150",   "SRSS18_lMM_Njets1_MT0to100_PTll0to50_MET100to150",
     "SRSS19_Njets1_MT0to100_PTll0to50_MET150to200",  "SRSS20_Njets1_MT0to100_PTll0to50_MET200toInf" };
  std::string SR_PTll50toInf[] =  {"SRSS06_Njets0_MT0to100_PTll50toInf_MET0to100",
     "SRSS07_lPP_Njets0_MT0to100_PTll50toInf_MET100to150",  "SRSS08_lMM_Njets0_MT0to100_PTll50toInf_MET100to150",
     "SRSS09_Njets0_MT0to100_PTll50toInf_MET150to200",  "SRSS10_Njets0_MT0to100_PTll50toInf_MET200toInf",
     "SRSS21_Njets1_MT0to100_PTll50toInf_MET0to100",  "SRSS22_lPP_Njets1_MT0to100_PTll50toInf_MET100to150",
     "SRSS23_lMM_Njets1_MT0to100_PTll50toInf_MET100to150",  "SRSS24_Njets1_MT0to100_PTll50toInf_MET150to200",
     "SRSS25_Njets1_MT0to100_PTll50toInf_MET200toInf" };

  Manager()->AddCut("PTll < 50", SR_PTll0to50 );
  Manager()->AddCut("PTll > 50", SR_PTll50toInf );
  Manager()->AddCut("PTll > 100", "SRSS01_Njets0_MT0to100_PTll0to50_MET0to100" );

  // MET cuts
  std::string SR_MET0to50[] =  {"SRG01_MET0to50", "SRH01_MET0to50", "SRI01_MET0to50", 
                                  "SRJ01_MET0to50", "SRK01_MET0to50" };
  std::string SR_MET0to100[] = {"SRSS01_Njets0_MT0to100_PTll0to50_MET0to100",
     "SRSS06_Njets0_MT0to100_PTll50toInf_MET0to100", "SRSS11_Njets0_MT100toInf_MET0to100",
     "SRSS16_Njets1_MT0to100_PTll0to50_MET0to100", "SRSS21_Njets1_MT0to100_PTll50toInf_MET0to100",
     "SRSS26_Njets1_MT100toInf_MET0to100"};
  std::string SR_MET50to100[] =  {
     "SRA06_Mll0to75_MT100to160_MET50to100",
     "SRA10_Mll0to75_MT160toInf_MET50to100", "SRA15_Mll75to105_MT0to100_MET50to100",
     "SRA22_Mll75to105_MT100to160_MET50to100","SRA26_Mll75to105_MT160toInf_MET50to100",
     "SRA32_Mll105toInf_MT0to100_MET50to100", "SRA37_Mll105toInf_MT100to160_MET50to100",
     "SRA41_Mll105toInf_MT160toInf_MET50to100",
     "SRB01_Mll0to100_MT0to120_MET50to100", "SRB04_Mll100toInf_MT0to120_MET50to100",
     "SRC01_Mll0to75_MT20to100_MET50to100", "SRC06_Mll75to105_MT20to100_MET50to100",
     "SRC12_Mll105toInf_MT20to100_MET50to100", "SRD01_Mll0to60_MT20to100_MET50to100",
     "SRD06_Mll60to100_MT20to100_MET50to100", "SRD11_Mll100toInf_MT20to100_MET50to100",
     "SRE01_Mll0to60_MT20to100_MET50to100", "SRE06_Mll60to100_MT20to100_MET50to100",
     "SRF01_Mll0to100_MT20to100_MET50to100", "SRF07_Mll100toInf_MT20to100_MET50to100",
     "SRG02_MET50to100", "SRH02_MET50to100", "SRI02_MET50to100", "SRJ02_MET50to100", "SRK02_MET50to100"};
  std::string SR_MET100to150[] = {
     "SRSS02_lPP_Njets0_MT0to100_PTll0to50_MET100to150", "SRSS03_lMM_Njets0_MT0to100_PTll0to50_MET100to150",
     "SRSS07_lPP_Njets0_MT0to100_PTll50toInf_MET100to150", "SRSS08_lMM_Njets0_MT0to100_PTll50toInf_MET100to150",
     "SRSS12_lPP_Njets0_MT100toInf_MET100to150", "SRSS13_lMM_Njets0_MT100toInf_MET100to150",
     "SRSS17_lPP_Njets1_MT0to100_PTll0to50_MET100to150",   "SRSS18_lMM_Njets1_MT0to100_PTll0to50_MET100to150",
     "SRSS22_lPP_Njets1_MT0to100_PTll50toInf_MET100to150", "SRSS23_lMM_Njets1_MT0to100_PTll50toInf_MET100to150", 
     "SRSS27_lPP_Njets1_MT100toInf_MET100to150",  "SRSS28_lMM_Njets1_MT100toInf_MET100to150",
     "SRA02_Mll0to75_MT0to100_MET100to150", "SRA07_Mll0to75_MT100to160_MET100to150",
     "SRA11_Mll0to75_MT160toInf_MET100to150", "SRA16_Mll75to105_MT0to100_MET100to150",
     "SRA23_Mll75to105_MT100to160_MET100to150", "SRA27_Mll75to105_MT160toInf_MET100to150",
     "SRA33_Mll105toInf_MT0to100_MET100to150", "SRA38_Mll105toInf_MT100to160_MET100to150",
     "SRA42_Mll105toInf_MT160toInf_MET100to150",
     "SRC02_Mll0to75_MT20to100_MET100to150", "SRC07_Mll75to105_MT20to100_MET100to150",
     "SRC13_Mll105toInf_MT20to100_MET100to150", "SRD02_Mll0to60_MT20to100_MET100to150",
     "SRD07_Mll60to100_MT20to100_MET100to150", "SRD12_Mll100toInf_MT20to100_MET100to150",
     "SRE02_Mll0to60_MT20to100_MET100to150", "SRE07_Mll60to100_MT20to100_MET100to150",
     "SRF02_Mll0to100_MT20to100_MET100to150","SRF08_Mll100toInf_MT20to100_MET100to150",
     "SRG03_MET100to150", "SRH03_MET100to150", "SRI03_MET100to150", "SRJ03_MET100to150"  };
  std::string SR_MET150to200[] = {
     "SRSS04_Njets0_MT0to100_PTll0to50_MET150to200", "SRSS09_Njets0_MT0to100_PTll50toInf_MET150to200",
     "SRSS14_Njets0_MT100toInf_MET150to200", "SRSS19_Njets1_MT0to100_PTll0to50_MET150to200",
     "SRSS24_Njets1_MT0to100_PTll50toInf_MET150to200", "SRSS29_Njets1_MT100toInf_MET150to200",
     "SRA03_Mll0to75_MT0to100_MET150to200", "SRA08_Mll0to75_MT100to160_MET150to200",
     "SRA12_Mll0to75_MT160toInf_MET150to200", "SRA17_Mll75to105_MT0to100_MET150to200",
     "SRA24_Mll75to105_MT100to160_MET150to200", "SRA28_Mll75to105_MT160toInf_MET150to200",
     "SRA34_Mll105toInf_MT0to100_MET150to200", "SRA39_Mll105toInf_MT100to160_MET150to200",
     "SRA43_Mll105toInf_MT160toInf_MET150to200",
     "SRC03_Mll0to75_MT20to100_MET150to200", "SRC08_Mll75to105_MT20to100_MET150to200",
     "SRC14_Mll105toInf_MT20to100_MET150to200", "SRD03_Mll0to60_MT20to100_MET150to200",
     "SRD08_Mll60to100_MT20to100_MET150to200", "SRD13_Mll100toInf_MT20to100_MET150to200",
     "SRE03_Mll0to60_MT20to100_MET150to200", "SRE08_Mll60to100_MT20to100_MET150to200",
     "SRF03_Mll0to100_MT20to100_MET150to200", "SRF09_Mll100toInf_MT20to100_MET150to200","SRG04_MET150to200"};
  std::string SR_MET200to250[] = {
     "SRA04_Mll0to75_MT0to100_MET200to250", "SRA13_Mll0to75_MT160toInf_MET200to250",
     "SRA18_Mll75to105_MT0to100_MET200to250", "SRA29_Mll75to105_MT160toInf_MET200to250",
     "SRA35_Mll105toInf_MT0to100_MET200to250", "SRC04_Mll0to75_MT20to100_MET200to250",
     "SRC15_Mll105toInf_MT20to100_MET200to250",
     "SRD04_Mll0to60_MT20to100_MET200to250", "SRD09_Mll60to100_MT20to100_MET200to250",
     "SRE04_Mll0to60_MT20to100_MET200to250", "SRE09_Mll60to100_MT20to100_MET200to250",
     "SRF04_Mll0to100_MT20to100_MET200to250"};
  std::string SR_MET250to400[] = {
     "SRA19_Mll75to105_MT0to100_MET250to400", "SRA30_Mll75to105_MT160toInf_MET250to400" };
  std::string SR_MET50to200[] =  {"SRC17_Mll0to75or105toInf_MT2100toInf_MET50to200",
     "SRD15_Mll0toInf_MT2100toInf_MET50to200","SRF11_Mll0toInf_MT2100toInf_MET50to200" };
  std::string SR_MET100toInf[] = {
     "SRB02_Mll0to100_MT0to120_MET100toInf", "SRB05_Mll100toInf_MT0to120_MET100toInf", "SRK03_MET100toInf" };
  std::string SR_MET150toInf[] = {"SRH04_MET150toInf", "SRI04_MET150toInf", "SRJ04_MET150toInf" };
  std::string SR_MET200toInf[] = {
     "SRSS05_Njets0_MT0to100_PTll0to50_MET200toInf", "SRSS10_Njets0_MT0to100_PTll50toInf_MET200toInf",
     "SRSS15_Njets0_MT100toInf_MET200toInf", "SRSS20_Njets1_MT0to100_PTll0to50_MET200toInf",
     "SRSS25_Njets1_MT0to100_PTll50toInf_MET200toInf", "SRSS30_Njets1_MT100toInf_MET200toInf",
     "SRA09_Mll0to75_MT100to160_MET200toInf", "SRA25_Mll75to105_MT100to160_MET200toInf", 
     "SRA40_Mll105toInf_MT100to160_MET200toInf", "SRA44_Mll105toInf_MT160toInf_MET200toInf",
     "SRC18_Mll0to75or105toInf_MT2100toInf_MET200toInf",
     "SRD14_Mll100toInf_MT20to100_MET200toInf", "SRD16_Mll0toInf_MT2100toInf_MET200toInf",
     "SRF10_Mll100toInf_MT20to100_MET200toInf", "SRF12_Mll0toInf_MT2100toInf_MET200toInf", "SRG05_MET200toInf" };
  std::string SR_MET250toInf[] = {
     "SRA05_Mll0to75_MT0to100_MET250toInf", "SRA14_Mll0to75_MT160toInf_MET250toInf",
     "SRA36_Mll105toInf_MT0to100_MET250toInf",
     "SRC05_Mll0to75_MT20to100_MET250toInf", "SRC16_Mll105toInf_MT20to100_MET250toInf",
     "SRD05_Mll0to60_MT20to100_MET250toInf", "SRD10_Mll60to100_MT20to100_MET250toInf",
     "SRE05_Mll0to60_MT20to100_MET250toInf", "SRE10_Mll60to100_MT20to100_MET250toInf"};
  std::string SR_MET400toInf[] = {
     "SRA31_Mll75to105_MT160toInf_MET400toInf", "SRC11_Mll75to105_MT20to100_MET400toInf" };

  Manager()->AddCut("MET < 50 GeV", SR_MET0to50 );
  Manager()->AddCut("MET < 100 GeV", SR_MET0to100 );
  Manager()->AddCut("50 < MET < 100 GeV", SR_MET50to100 );
  Manager()->AddCut("100 < MET < 150 GeV", SR_MET100to150 );
  Manager()->AddCut("150 < MET < 200 GeV", SR_MET150to200 );
  Manager()->AddCut("200 < MET < 250 GeV", SR_MET200to250 );
  Manager()->AddCut("250 < MET < 400 GeV", SR_MET250to400 );
  Manager()->AddCut("250 < MET < 300 GeV", "SRF05_Mll0to100_MT20to100_MET250to300" );
  Manager()->AddCut("200 < MET < 300 GeV", "SRC09_Mll75to105_MT20to100_MET200to300" );
  Manager()->AddCut("300 < MET < 400 GeV", "SRC10_Mll75to105_MT20to100_MET300to400" );
  Manager()->AddCut("400 < MET < 550 GeV", "SRA20_Mll75to105_MT0to100_MET400to550" );
  Manager()->AddCut("50 < MET < 200 GeV", SR_MET50to200 );
  Manager()->AddCut("MET > 100 GeV", SR_MET100toInf );
  Manager()->AddCut("MET > 150 GeV", SR_MET150toInf );
  Manager()->AddCut("MET >= 200 GeV", SR_MET200toInf );
  Manager()->AddCut("MET >= 250 GeV", SR_MET250toInf );
  Manager()->AddCut("MET >= 300 GeV", "SRF06_Mll0to100_MT20to100_MET300toInf" );
  Manager()->AddCut("MET >= 400 GeV", SR_MET400toInf );
  Manager()->AddCut("MET >= 550 GeV", "SRA21_Mll75to105_MT0to100_MET550toInf" );

  // MT2
  std::string SR_MT20to100[] = {"SRC01_Mll0to75_MT20to100_MET50to100", "SRC02_Mll0to75_MT20to100_MET100to150",
     "SRC03_Mll0to75_MT20to100_MET150to200", "SRC04_Mll0to75_MT20to100_MET200to250",
     "SRC05_Mll0to75_MT20to100_MET250toInf", "SRC06_Mll75to105_MT20to100_MET50to100",
     "SRC07_Mll75to105_MT20to100_MET100to150", "SRC08_Mll75to105_MT20to100_MET150to200",
     "SRC09_Mll75to105_MT20to100_MET200to300", "SRC10_Mll75to105_MT20to100_MET300to400",
     "SRC11_Mll75to105_MT20to100_MET400toInf", "SRC12_Mll105toInf_MT20to100_MET50to100",
     "SRC13_Mll105toInf_MT20to100_MET100to150", "SRC14_Mll105toInf_MT20to100_MET150to200",
     "SRC15_Mll105toInf_MT20to100_MET200to250", "SRC16_Mll105toInf_MT20to100_MET250toInf",
     "SRD01_Mll0to60_MT20to100_MET50to100", "SRD02_Mll0to60_MT20to100_MET100to150",
     "SRD03_Mll0to60_MT20to100_MET150to200", "SRD04_Mll0to60_MT20to100_MET200to250",
     "SRD05_Mll0to60_MT20to100_MET250toInf", "SRD06_Mll60to100_MT20to100_MET50to100",
     "SRD07_Mll60to100_MT20to100_MET100to150", "SRD08_Mll60to100_MT20to100_MET150to200",
     "SRD09_Mll60to100_MT20to100_MET200to250", "SRD10_Mll60to100_MT20to100_MET250toInf",
     "SRD11_Mll100toInf_MT20to100_MET50to100", "SRD12_Mll100toInf_MT20to100_MET100to150",
     "SRD13_Mll100toInf_MT20to100_MET150to200", "SRD14_Mll100toInf_MT20to100_MET200toInf",
     "SRE01_Mll0to60_MT20to100_MET50to100", "SRE02_Mll0to60_MT20to100_MET100to150",
     "SRE03_Mll0to60_MT20to100_MET150to200", "SRE04_Mll0to60_MT20to100_MET200to250",
     "SRE05_Mll0to60_MT20to100_MET250toInf", "SRE06_Mll60to100_MT20to100_MET50to100",
     "SRE07_Mll60to100_MT20to100_MET100to150", "SRE08_Mll60to100_MT20to100_MET150to200",
     "SRE09_Mll60to100_MT20to100_MET200to250", "SRE10_Mll60to100_MT20to100_MET250toInf",
     "SRE11_Mll100toInf_MT20to100_MET50toInf", "SRF01_Mll0to100_MT20to100_MET50to100",
     "SRF02_Mll0to100_MT20to100_MET100to150", "SRF03_Mll0to100_MT20to100_MET150to200",
     "SRF04_Mll0to100_MT20to100_MET200to250", "SRF05_Mll0to100_MT20to100_MET250to300",
     "SRF06_Mll0to100_MT20to100_MET300toInf", "SRF07_Mll100toInf_MT20to100_MET50to100",
     "SRF08_Mll100toInf_MT20to100_MET100to150", "SRF09_Mll100toInf_MT20to100_MET150to200",
     "SRF10_Mll100toInf_MT20to100_MET200toInf"};
  std::string SR_MT2100toInf[] = {"SRC17_Mll0to75or105toInf_MT2100toInf_MET50to200",
     "SRC18_Mll0to75or105toInf_MT2100toInf_MET200toInf", "SRD15_Mll0toInf_MT2100toInf_MET50to200",
     "SRD16_Mll0toInf_MT2100toInf_MET200toInf", "SRE12_Mll0toInf_MT2100toInf_MET50toInf",
     "SRF11_Mll0toInf_MT2100toInf_MET50to200", "SRF12_Mll0toInf_MT2100toInf_MET200toInf" };

  Manager()->AddCut("0 < MT2 < 100 GeV", SR_MT20to100 );
  Manager()->AddCut("MT2 >= 100 GeV", SR_MT2100toInf );

  // Mll cuts
  std::string SR_Mll0to100[] =   {"SRB01_Mll0to100_MT0to120_MET50to100", "SRB02_Mll0to100_MT0to120_MET100toInf",
     "SRB03_Mll0to100_MT120toInf_MET50toInf", "SRF01_Mll0to100_MT20to100_MET50to100",
     "SRF02_Mll0to100_MT20to100_MET100to150", "SRF03_Mll0to100_MT20to100_MET150to200",
     "SRF04_Mll0to100_MT20to100_MET200to250", "SRF05_Mll0to100_MT20to100_MET250to300",
     "SRF06_Mll0to100_MT20to100_MET300toInf" };
  std::string SR_Mll100toInf[] = {
     "SRB04_Mll100toInf_MT0to120_MET50to100", "SRB05_Mll100toInf_MT0to120_MET100toInf",
     "SRB06_Mll100toInf_MT120toInf_MET50toInf", "SRD11_Mll100toInf_MT20to100_MET50to100",
     "SRD12_Mll100toInf_MT20to100_MET100to150", "SRD13_Mll100toInf_MT20to100_MET150to200",
     "SRD14_Mll100toInf_MT20to100_MET200toInf", "SRE11_Mll100toInf_MT20to100_MET50toInf",
     "SRF07_Mll100toInf_MT20to100_MET50to100", "SRF08_Mll100toInf_MT20to100_MET100to150",
     "SRF09_Mll100toInf_MT20to100_MET150to200", "SRF10_Mll100toInf_MT20to100_MET200toInf"};
  std::string SR_OnZ[] =         {
     "SRA15_Mll75to105_MT0to100_MET50to100", "SRA16_Mll75to105_MT0to100_MET100to150",
     "SRA17_Mll75to105_MT0to100_MET150to200", "SRA18_Mll75to105_MT0to100_MET200to250",
     "SRA19_Mll75to105_MT0to100_MET250to400", "SRA20_Mll75to105_MT0to100_MET400to550",
     "SRA21_Mll75to105_MT0to100_MET550toInf", "SRA22_Mll75to105_MT100to160_MET50to100",
     "SRA23_Mll75to105_MT100to160_MET100to150", "SRA24_Mll75to105_MT100to160_MET150to200",
     "SRA25_Mll75to105_MT100to160_MET200toInf", "SRA26_Mll75to105_MT160toInf_MET50to100",
     "SRA27_Mll75to105_MT160toInf_MET100to150", "SRA28_Mll75to105_MT160toInf_MET150to200",
     "SRA29_Mll75to105_MT160toInf_MET200to250", "SRA30_Mll75to105_MT160toInf_MET250to400",
     "SRA31_Mll75to105_MT160toInf_MET400toInf",     "SRC06_Mll75to105_MT20to100_MET50to100",
     "SRC07_Mll75to105_MT20to100_MET100to150",
     "SRC08_Mll75to105_MT20to100_MET150to200", "SRC09_Mll75to105_MT20to100_MET200to300",
     "SRC10_Mll75to105_MT20to100_MET300to400", "SRC11_Mll75to105_MT20to100_MET400toInf" };
  std::string SR_Mll0to75[] =    {
     "SRA02_Mll0to75_MT0to100_MET100to150",
     "SRA03_Mll0to75_MT0to100_MET150to200", "SRA04_Mll0to75_MT0to100_MET200to250",
     "SRA05_Mll0to75_MT0to100_MET250toInf", "SRA06_Mll0to75_MT100to160_MET50to100",
     "SRA07_Mll0to75_MT100to160_MET100to150", "SRA08_Mll0to75_MT100to160_MET150to200",
     "SRA09_Mll0to75_MT100to160_MET200toInf", "SRA10_Mll0to75_MT160toInf_MET50to100",
     "SRA11_Mll0to75_MT160toInf_MET100to150", "SRA12_Mll0to75_MT160toInf_MET150to200",
     "SRA13_Mll0to75_MT160toInf_MET200to250", "SRA14_Mll0to75_MT160toInf_MET250toInf",
     "SRC01_Mll0to75_MT20to100_MET50to100", "SRC02_Mll0to75_MT20to100_MET100to150",
     "SRC03_Mll0to75_MT20to100_MET150to200", "SRC04_Mll0to75_MT20to100_MET200to250",
     "SRC05_Mll0to75_MT20to100_MET250toInf" };
  std::string SR_Mll105toInf[] = {
     "SRA32_Mll105toInf_MT0to100_MET50to100",
     "SRA33_Mll105toInf_MT0to100_MET100to150", "SRA34_Mll105toInf_MT0to100_MET150to200",
     "SRA35_Mll105toInf_MT0to100_MET200to250", "SRA36_Mll105toInf_MT0to100_MET250toInf",
     "SRA37_Mll105toInf_MT100to160_MET50to100", "SRA38_Mll105toInf_MT100to160_MET100to150",
     "SRA39_Mll105toInf_MT100to160_MET150to200", "SRA40_Mll105toInf_MT100to160_MET200toInf",
     "SRA41_Mll105toInf_MT160toInf_MET50to100", "SRA42_Mll105toInf_MT160toInf_MET100to150",
     "SRA43_Mll105toInf_MT160toInf_MET150to200", "SRA44_Mll105toInf_MT160toInf_MET200toInf",
     "SRC12_Mll105toInf_MT20to100_MET50to100","SRC13_Mll105toInf_MT20to100_MET100to150",
     "SRC14_Mll105toInf_MT20to100_MET150to200", "SRC15_Mll105toInf_MT20to100_MET200to250",
     "SRC16_Mll105toInf_MT20to100_MET250toInf" };
  std::string SR_OffZ[] =        {"SRC17_Mll0to75or105toInf_MT2100toInf_MET50to200",
     "SRC18_Mll0to75or105toInf_MT2100toInf_MET200toInf" };
  std::string SR_Mll0to60[] =    {"SRD01_Mll0to60_MT20to100_MET50to100", "SRD02_Mll0to60_MT20to100_MET100to150",
     "SRD03_Mll0to60_MT20to100_MET150to200", "SRD04_Mll0to60_MT20to100_MET200to250",
     "SRD05_Mll0to60_MT20to100_MET250toInf", "SRE01_Mll0to60_MT20to100_MET50to100",
     "SRE02_Mll0to60_MT20to100_MET100to150", "SRE03_Mll0to60_MT20to100_MET150to200",
     "SRE04_Mll0to60_MT20to100_MET200to250", "SRE05_Mll0to60_MT20to100_MET250toInf" };
  std::string SR_Mll60to100[] =  {
     "SRD06_Mll60to100_MT20to100_MET50to100", "SRD07_Mll60to100_MT20to100_MET100to150",
     "SRD08_Mll60to100_MT20to100_MET150to200", "SRD09_Mll60to100_MT20to100_MET200to250",
     "SRD10_Mll60to100_MT20to100_MET250toInf", "SRE06_Mll60to100_MT20to100_MET50to100",
     "SRE07_Mll60to100_MT20to100_MET100to150", "SRE08_Mll60to100_MT20to100_MET150to200",
     "SRE09_Mll60to100_MT20to100_MET200to250", "SRE10_Mll60to100_MT20to100_MET250toInf" };

  Manager()->AddCut("0 < Mll < 100 GeV", SR_Mll0to100 );
  Manager()->AddCut("Mll >= 100 GeV", SR_Mll100toInf );
  Manager()->AddCut("Mll < 60 GeV", SR_Mll0to60 );
  Manager()->AddCut("Mll < 75 GeV", SR_Mll0to75 );
  Manager()->AddCut("Mll > 75 GeV", "SRA01_Mll0to75_MT0to100_MET50to100" );
  Manager()->AddCut("60 <= Mll < 100 GeV", SR_Mll60to100 );
  Manager()->AddCut("Mll >= 105 GeV", SR_Mll105toInf );
  Manager()->AddCut("on-Z", SR_OnZ );
  Manager()->AddCut("off-Z", SR_OffZ );

  // -- histograms
//  Manager()->AddHisto("MT2", 30, 0, 300, "SRC18_Mll0to75or105toInf_MT2100toInf_MET200toInf" );
//  Manager()->AddHisto("MET", 10, 50, 300, "SRF12_Mll0toInf_MT2100toInf_MET200toInf");

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_sus_16_039::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_sus_16_039::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Security for empty events
  if (event.rec()==0) return true;

  // Event weight
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight = event.mc()->weight();
  else return false;
  Manager()->InitializeForNewEvent(myEventWeight);

  // Loose leptons
  std::vector<const RecLeptonFormat*> LooseLeptons;
  for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
  {
    const RecLeptonFormat *myElec = &(event.rec()->electrons()[ii]);
    double pt = myElec->pt();
    if(isLooseLepton(myElec, event, 2.5) && pt > 7.)
      LooseLeptons.push_back(myElec);
  }
  for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
  {
    const RecLeptonFormat *myMuon = &(event.rec()->muons()[ii]);
    double pt = myMuon->pt();
    if(isLooseLepton(myMuon, event, 2.4) && pt > 5.)
      LooseLeptons.push_back(myMuon);
  }

  // -- baseline jets (anti-kt, r=0.4 simulated @ Delphes) -- //
  unsigned int nbjets = 0, njets=0;
  double HT=0.;
  std::vector<const RecJetFormat*> IsoJets;
  for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
  {
    const RecJetFormat * myJet = &(event.rec()->jets()[ii]);
    double eta = std::abs(myJet->eta());
    double pt = myJet->pt();
    bool iso = true, isL = false;
    for (unsigned int jj=0; jj<LooseLeptons.size(); jj++)
    {
      if(myJet->dr(LooseLeptons[jj])<0.1) { isL = true;  break; }
      if(myJet->dr(LooseLeptons[jj])<0.4) { iso = false; break; }
    }
    if(!iso && !isL && pt>5.) IsoJets.push_back(myJet);
    else if(!isL && eta<2.4 && iso)
    {
      if(pt>25. && myJet->btag()) nbjets++;
      if(pt>40.) { njets++; HT+=myJet->pt(); }
    }
  }
  // tau selection
  std::vector<const RecTauFormat*> SignalTaus;
  for(unsigned int ii=0; ii<event.rec()->taus().size(); ii++)
  {
    const RecTauFormat *CurrentTau = &(event.rec()->taus()[ii]);
    double pt = CurrentTau->pt();
    double abseta = abs(CurrentTau->eta());
    double iso_var = PHYSICS->Isol->eflow->sumIsolation(CurrentTau,
      event.rec(),0.5,0.,IsolationEFlow::ALL_COMPONENTS);
    bool iso= true;
    for (unsigned int jj=0; jj<LooseLeptons.size(); jj++)
      if(CurrentTau->dr(LooseLeptons[jj])<0.4) { iso = false; break; }
    if(pt>20.0 && abseta<2.3 && iso_var< 0.20*pt && iso)
        SignalTaus.push_back(CurrentTau);
  }
  unsigned int ntau = SignalTaus.size();

  //  -- Signal lepton selection -- //
  std::vector<const RecLeptonFormat*> SignalLeptons;
  for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
  {
    const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ii]);
    double abseta = std::abs(CurrentElectron->eta());
    double pt = CurrentElectron->pt();
    bool isIso =  isIsolated(CurrentElectron,IsoJets,event,0.12,0.76,7.2);
    double eta_thr = 2.5;
    if(ntau==2) eta_thr=2.1;
    if(abseta<eta_thr && isIso && pt>10.) SignalLeptons.push_back(CurrentElectron);
  }
  unsigned int ne = SignalLeptons.size();
  for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
  {
    const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
    double abseta = std::abs(CurrentMuon->eta());
    double pt = CurrentMuon->pt();
    bool isIso =  isIsolated(CurrentMuon,IsoJets,event,0.16,0.69,6.0);
    double eta_thr = 2.4;
    if(ntau==2) eta_thr=2.1;
    if(abseta<eta_thr && isIso && pt>10.) SignalLeptons.push_back(CurrentMuon);
  }
  SORTER->sort(SignalLeptons);
  unsigned int nl = SignalLeptons.size();
  unsigned int nmu = nl-ne;

  //Missing Transverse Energy
  double MET = event.rec()->MET().pt();

  // -------- //
  // BASELINE //
  // -------- //
  // -- MET --
  bool met_cut = false;
  if(MET>50.) met_cut = true;

  //--dilepton --//
  bool is_SS=false, ptl1=false, ptl2=false;
  double ptll=1e+09;
  if(nl==2 && ntau==0)
  {
    if( (SignalLeptons[0]->isElectron() && SignalLeptons[0]->pt()>25.) ||
        (SignalLeptons[0]->isMuon()     && SignalLeptons[0]->pt()>20.) )  ptl1=true;
    if( (SignalLeptons[1]->isElectron() && SignalLeptons[1]->pt()>15.) || SignalLeptons[1]->isMuon() )
      ptl2=true;
    if(SignalLeptons[0]->charge()==SignalLeptons[1]->charge()) is_SS = true;
    if(MET<60.) met_cut = false;
    ptll = (SignalLeptons[0]->momentum()+SignalLeptons[1]->momentum()).Pt();
  }

  // -- trileptonic pt's --
  if( (nl+ntau)>=3 && ntau<=2)
  {
    double thr1_e=25.,thr1_mu=20.;
    if(nmu==1  && SignalLeptons[0]->isMuon()) thr1_mu=25.;
    if(ntau==2 && SignalLeptons[0]->isMuon()) {thr1_mu=25.; ptl2=true;}
    else if(ntau==2) {thr1_e=30; ptl2=true;}
    if( (SignalLeptons[0]->isElectron() && SignalLeptons[0]->pt()>thr1_e) ||
        (SignalLeptons[0]->isMuon()     && SignalLeptons[0]->pt()>thr1_mu) )
      ptl1=true;
    if(ntau<2)
      if( (SignalLeptons[1]->isElectron() && SignalLeptons[1]->pt()>15.) || (SignalLeptons[1]->isMuon()) )
        ptl2=true;
  }

  // Loose OSSF pair with M < 12 GeV
  bool looseOSSF = false, looseZ=false;
  for(unsigned int ii=0; ii<LooseLeptons.size();ii++)
    for(unsigned int jj=ii+1; jj<LooseLeptons.size();jj++)
    {
       if( (LooseLeptons[ii]->charge()!=LooseLeptons[jj]->charge()) &&
           (LooseLeptons[ii]->isElectron()==LooseLeptons[jj]->isElectron()) )
       {
         if( (LooseLeptons[ii]->momentum()+LooseLeptons[jj]->momentum()).M()<12.)
            { looseOSSF = true; break; }
         if( std::abs((LooseLeptons[ii]->momentum()+LooseLeptons[jj]->momentum()).M()-91.)<15.)
            looseZ = true;
       }
    }

  // Number of particles
  unsigned int nep=0, nem=0, nmp=0, nmm=0,ntp=0,ntm=0;
  for(unsigned int ii=0; ii<SignalLeptons.size();ii++)
  {
    if(SignalLeptons[ii]->charge()>0 && SignalLeptons[ii]->isElectron()) nep++;
    if(SignalLeptons[ii]->charge()>0 && SignalLeptons[ii]->isMuon()) nmp++;
    if(SignalLeptons[ii]->charge()<0 && SignalLeptons[ii]->isElectron()) nem++;
    if(SignalLeptons[ii]->charge()<0 && SignalLeptons[ii]->isMuon()) nmm++;
  }
  for (unsigned int ii=0; ii<SignalTaus.size();ii++)
  {
    if(SignalTaus[ii]->charge()<0) ntm++;
    else if(SignalTaus[ii]->charge()>0) ntp++;
  }
  unsigned int nOSSF = std::min(nem,nep) + std::min(nmm,nmp) + std::min(ntm,ntp);

  // Calculation of mll, MT and MT2
  bool OSSF=false;
  double mll=1e09, MT=1e+09, MT2=1e+09;
  if(nl==2 && ntau==0)
  {
    for(unsigned int ii=0; ii<SignalLeptons.size();ii++)
    {
      double tmp_MT = SignalLeptons[ii]->mt_met(event.rec()->MET().momentum());
      if(tmp_MT<MT) MT = tmp_MT;
    }
  }
  else if(nl==3 && ntau==0)
  {
    for(unsigned int ii=0; ii<SignalLeptons.size();ii++)
      for(unsigned int jj=ii+1; jj<SignalLeptons.size();jj++)
        if( (SignalLeptons[ii]->charge()!=SignalLeptons[jj]->charge()) &&
             (SignalLeptons[ii]->isElectron()==SignalLeptons[jj]->isElectron()) )
        {
           OSSF = true;
           double tmp_mll = (SignalLeptons[ii]->momentum()+SignalLeptons[jj]->momentum()).M();
           if ( std::abs(tmp_mll-91.)<std::abs(mll-91.) )
           {
             mll=tmp_mll;
             for(unsigned int kk=0; kk<SignalLeptons.size();kk++)
               if(kk!=ii && kk!=jj)
                 MT = SignalLeptons[kk]->mt_met(event.rec()->MET().momentum());
           }
        }
    if(!OSSF)
    {
      for(unsigned int ii=0; ii<SignalLeptons.size();ii++)
        for(unsigned int jj=ii+1; jj<SignalLeptons.size();jj++)
          if(SignalLeptons[ii]->charge()!=SignalLeptons[jj]->charge())
          {
             double tmp_mll = (SignalLeptons[ii]->momentum()+SignalLeptons[jj]->momentum()).M();
             if ( std::abs(tmp_mll-50.)<std::abs(mll-50.) )
             {
               mll=tmp_mll;
               for(unsigned int kk=0; kk<SignalLeptons.size();kk++)
                 if(kk!=ii && kk!=jj)
                   MT = SignalLeptons[kk]->mt_met(event.rec()->MET().momentum());
             }
          }
    }
    if(mll==1e09 && MT==1e+09)
    {
      mll=0.;
      for(unsigned int kk=0; kk<SignalLeptons.size();kk++)
      {
        double tmp_MT = SignalLeptons[kk]->mt_met(event.rec()->MET().momentum());
        if(tmp_MT<MT) MT = tmp_MT;
      }
    }
  }
  else if(nl==2 && ntau==1)
  {
    if( (SignalLeptons[0]->charge()!=SignalLeptons[1]->charge()) &&
        (SignalLeptons[0]->isElectron()==SignalLeptons[1]->isElectron()) )
    {
      OSSF = true;
      mll = (SignalLeptons[0]->momentum()+SignalLeptons[1]->momentum()).M();
      MT2 = PHYSICS->Transverse->MT2(SignalLeptons[0],SignalLeptons[1],event.rec()->MET(),0.);
    }
    if(!OSSF)
    {
      if(SignalLeptons[0]->charge()!=SignalLeptons[1]->charge())
      {
        mll = (SignalLeptons[0]->momentum()+SignalLeptons[1]->momentum()).M();
        MT2 = PHYSICS->Transverse->MT2(SignalLeptons[0],SignalLeptons[1],event.rec()->MET(),0.);
      }
      double dum=0.;
      for(unsigned int ii=0; ii<SignalLeptons.size();ii++)
        if(SignalLeptons[ii]->charge()!=SignalTaus[0]->charge())
        {
           double tmp_mll = (SignalLeptons[ii]->momentum()+SignalTaus[0]->momentum()).M();
           if ( std::abs(tmp_mll-60.)<std::abs(mll-50.-dum*10.) )
           {
              dum=1.; mll=tmp_mll;
              MT2 = PHYSICS->Transverse->MT2(SignalLeptons[ii],SignalTaus[0],event.rec()->MET(),0.);
           }
        }
    }
    if(mll==1e09 && MT2==1e+09)
    {
      mll=0.;
      MT2 = PHYSICS->Transverse->MT2(SignalLeptons[0],SignalTaus[0],event.rec()->MET(),0.);
    }
  }
  else if (nl==1 && ntau==2)
  {
    mll = (SignalTaus[0]->momentum()+SignalTaus[1]->momentum()).M();
    MT2 = PHYSICS->Transverse->MT2(SignalLeptons[0],SignalTaus[0],event.rec()->MET(),0.);
  }

  // Conversions
  bool conversion=false;
  if( (nl+ntau)==3 && (std::min(nem,nep) + std::min(nmm,nmp))>0)
  {
    double tmpmll=0.;
    if(nl==3)
      tmpmll=(SignalLeptons[0]->momentum()+SignalLeptons[1]->momentum()+SignalLeptons[2]->momentum()).M();
    else if(nl==2)
      tmpmll=(SignalLeptons[0]->momentum()+SignalLeptons[1]->momentum()+SignalTaus[0]->momentum()).M();
    if( tmpmll>76. && tmpmll < 106. ) conversion=true;
  }

  // Baseline SR //
  bool base_A = nl==3 && ntau==0 && OSSF;
  bool base_B = nl==3 && ntau==0 && !OSSF;
  bool base_C = ntau==1 && OSSF;
  bool base_D = ntau==1 && !OSSF && mll!=0.;
  bool base_E = ntau==1 && !OSSF && mll==0.;
  bool base_F = ntau==2;
  bool base_G = ntau==0 && nOSSF>=2;
  bool base_H = ntau==0 && nOSSF< 2;
  bool base_I = ntau==1;
  bool base_J = ntau==2 && nOSSF>=2;
  bool base_K = ntau==2 && nOSSF< 2;
  if(!Manager()->ApplyCut(base_A, "baseline_A")) return true;
  if(!Manager()->ApplyCut(base_B, "baseline_B")) return true;
  if(!Manager()->ApplyCut(base_C, "baseline_C")) return true;
  if(!Manager()->ApplyCut(base_D, "baseline_D")) return true;
  if(!Manager()->ApplyCut(base_E, "baseline_E")) return true;
  if(!Manager()->ApplyCut(base_F, "baseline_F")) return true;
  if(!Manager()->ApplyCut(base_G, "baseline_G")) return true;
  if(!Manager()->ApplyCut(base_H, "baseline_H")) return true;
  if(!Manager()->ApplyCut(base_I, "baseline_I")) return true;
  if(!Manager()->ApplyCut(base_J, "baseline_J")) return true;
  if(!Manager()->ApplyCut(base_K, "baseline_K")) return true;

  // baseline nlepton and ntau cuts
  if(!Manager()->ApplyCut(nl>=2 && ptl1 && ptl2, "2 tight leptons")) return true;
  if(!Manager()->ApplyCut((nl+ntau)>=3 && ntau<=2 && ptl1 && ptl2, "3 tight leptons")) return true;
  if(!Manager()->ApplyCut((nl+ntau)>=4 && ntau<=2 && ptl1 && ptl2, "4 tight leptons")) return true;

  // other baseline cuts (SS)
  if(!Manager()->ApplyCut(is_SS && !looseZ, "Same sign")) return true;
  if(!Manager()->ApplyCut(SignalLeptons[0]->charge()>0, "Same sign++")) return true;
  if(!Manager()->ApplyCut(SignalLeptons[0]->charge()<0, "Same sign--")) return true;

  // vetos
  if(!Manager()->ApplyCut(nl==2 && ntau==0, "3rd lepton veto")) return true;
  if(!Manager()->ApplyCut((nl+ntau)==3, "4th lepton veto")) return true;
  if(!Manager()->ApplyCut(!looseOSSF, "low-mass veto")) return true;
  if(!Manager()->ApplyCut(!conversion, "conversion veto")) return true;
  if(!Manager()->ApplyCut(nbjets==0, "b-jet veto")) return true;

  // baseline met cut
  if(!Manager()->ApplyCut(met_cut, "base_met")) return true;

  // Filling histograms //
//  Manager()->FillHisto("MT2", MT2 );
//  Manager()->FillHisto("MET", MET );

  // Region definitions //
  if(!Manager()->ApplyCut(njets==0 || njets==1, "Njets40 = 0/1")) return true;
  if(!Manager()->ApplyCut(njets==0, "Njets40 = 0")) return true;
  if(!Manager()->ApplyCut(njets==1, "Njets40 = 1")) return true;

  if(!Manager()->ApplyCut(MT < 100, "MT < 100 GeV")) return true;
  if(!Manager()->ApplyCut(MT > 100, "MT > 100 GeV")) return true;
  if(!Manager()->ApplyCut(MT < 120, "0 < MT < 120 GeV")) return true;
  if(!Manager()->ApplyCut(MT > 100 && MT < 160, "100 < MT < 160 GeV")) return true;
  if(!Manager()->ApplyCut(MT > 120, "MT > 120 GeV")) return true;
  if(!Manager()->ApplyCut(MT > 160, "MT > 160 GeV")) return true;

  if(!Manager()->ApplyCut(ptll < 50., "PTll < 50")) return true;
  if(!Manager()->ApplyCut(ptll > 50., "PTll > 50")) return true;
  if(!Manager()->ApplyCut(ptll > 100., "PTll > 100")) return true;

  if(!Manager()->ApplyCut(MET < 50 , "MET < 50 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 50 && MET < 100, "50 < MET < 100 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 100 && MET < 150, "100 < MET < 150 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 150 && MET < 200, "150 < MET < 200 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 200 && MET < 250, "200 < MET < 250 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 250 && MET < 300, "250 < MET < 300 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 250 && MET < 400, "250 < MET < 400 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 400 && MET < 550, "400 < MET < 550 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 200 && MET < 300, "200 < MET < 300 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 300 && MET < 400, "300 < MET < 400 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 50 && MET < 200, "50 < MET < 200 GeV")) return true;
  if(!Manager()->ApplyCut(MET < 100, "MET < 100 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 100, "MET > 100 GeV")) return true;
  if(!Manager()->ApplyCut(MET > 150, "MET > 150 GeV")) return true;
  if(!Manager()->ApplyCut(MET >= 200, "MET >= 200 GeV")) return true;
  if(!Manager()->ApplyCut(MET >= 250, "MET >= 250 GeV")) return true;
  if(!Manager()->ApplyCut(MET >= 300, "MET >= 300 GeV")) return true;
  if(!Manager()->ApplyCut(MET >= 400, "MET >= 400 GeV")) return true;
  if(!Manager()->ApplyCut(MET >= 550, "MET >= 550 GeV")) return true;

  if(!Manager()->ApplyCut(MT2 < 100, "0 < MT2 < 100 GeV")) return true;
  if(!Manager()->ApplyCut(MT2 >= 100, "MT2 >= 100 GeV")) return true;

  if(!Manager()->ApplyCut(mll < 100, "0 < Mll < 100 GeV")) return true;
  if(!Manager()->ApplyCut(mll >= 100, "Mll >= 100 GeV")) return true;
  if(!Manager()->ApplyCut(mll > 75, "Mll > 75 GeV")) return true;
  if(!Manager()->ApplyCut(mll > 75 && mll < 105, "on-Z")) return true;
  if(!Manager()->ApplyCut(mll < 75 || mll >= 105, "off-Z")) return true;
  if(!Manager()->ApplyCut(mll < 60, "Mll < 60 GeV")) return true;
  if(!Manager()->ApplyCut(mll < 75, "Mll < 75 GeV")) return true;
  if(!Manager()->ApplyCut(mll >= 60 && mll < 100, "60 <= Mll < 100 GeV")) return true;
  if(!Manager()->ApplyCut(mll >= 105, "Mll >= 105 GeV")) return true;


  return true;
}


// -----------------------------------------------------------------------------
// User-defined methods
// -----------------------------------------------------------------------------
bool cms_sus_16_039::isLooseLepton(const RecLeptonFormat* Lep, const EventFormat& event, const double &etaTH)
{
  double eta = std::fabs(Lep->eta());
  double pt = Lep->pt();
  double DR = 10./std::min(std::max(pt,50.),200.);
  double imini = (PHYSICS->Isol->eflow->sumIsolation(Lep,
    event.rec(),DR,0.,IsolationEFlow::ALL_COMPONENTS))/pt;

  if( eta<etaTH && imini<0.4) return true;

  return false;
}

bool cms_sus_16_039::isIsolated(const RecLeptonFormat* Lep,
   std::vector<const RecJetFormat*> IsoJets, const EventFormat& event,
   const double &I1, const double &I2, const double &I3)
{
  double pt  = Lep->pt();
  // I1
  double DR = 10./std::min(std::max(pt,50.),200.);
  double imini = (PHYSICS->Isol->eflow->sumIsolation(Lep,
     event.rec(),DR,0.,IsolationEFlow::ALL_COMPONENTS))/pt;
  // Closest jet
  unsigned int ijet=9999;
  double drmin=1e+09;
  for(unsigned int ii=0; ii<IsoJets.size(); ii++)
    if(Lep->dr(IsoJets[ii])<drmin) { drmin=Lep->dr(IsoJets[ii]); ijet=ii; }
  // I2
  double ptratio=1.;
  if (ijet!=9999)  ptratio = pt/IsoJets[ijet]->pt();
  // I3
  double ptrel = 0.;
  if (ijet!=9999)
  {
     MAVector3 axis(IsoJets[ijet]->momentum().Vect() - Lep->momentum().Vect());
     ptrel = (axis.Cross(Lep->momentum().Vect())).Mag()/axis.Mag();
  }
  // output
  if (imini<I1 && (ptratio>I2 || ptrel>I3)) return true;
  return false;
}
