#include "SampleAnalyzer/User/Analyzer/sfs_test.h"


using namespace MA5;
using namespace std;

// Overlap Removal
template<typename T1, typename T2> std::vector<const T1*>
  Removal(std::vector<const T1*> &v1, std::vector<const T2*> &v2,
  const double &drmin)
{
  // Determining with objects should be removed
  std::vector<bool> mask(v1.size(),false);
  for (unsigned int j=0;j<v1.size();j++)
    for (unsigned int i=0;i<v2.size();i++)
      if (v2[i]->dr(v1[j]) < drmin)
      {
        mask[j]=true;
        break;
      }

  // Building the cleaned container
  std::vector<const T1*> cleaned_v1;
  for (unsigned int i=0;i<v1.size();i++)
    if (!mask[i]) cleaned_v1.push_back(v1[i]);

  return cleaned_v1;
}
// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool sfs_test::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  cout << "BEGIN Initialization" << endl;
  // initialize variables, histos
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>    Analysis: ATLAS-SUSY-16-07                <>" << endmsg;
  INFO << "      <>             arXiv:1712.02332                 <>" << endmsg;
  INFO << "      <>             (multijet + MET)                 <>" << endmsg;
  INFO << "      <>   Recasters: G. Chalons & H. Reyes-Gonzales  <>" << endmsg;
  INFO << "      <>   Contact: fuks@lpthe.jussieu.fr             <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.6                <>" << endmsg;
  INFO << "      <>   For more information, see                  <>" << endmsg;
  INFO << "      <>   http://madanalysis.irmp.ucl.ac.be/wiki/    <>" << endmsg;
  INFO << "      <>   /PhysicsAnalysisDatabase                   <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

    // Initializing PhysicsService for MC
  PHYSICS->mcConfig().Reset();


  // definition of the multiparticle "hadronic"
  PHYSICS->mcConfig().AddHadronicId(-20543);
  PHYSICS->mcConfig().AddHadronicId(-20533);
  PHYSICS->mcConfig().AddHadronicId(-20523);
  PHYSICS->mcConfig().AddHadronicId(-20513);
  PHYSICS->mcConfig().AddHadronicId(-20433);
  PHYSICS->mcConfig().AddHadronicId(-20423);
  PHYSICS->mcConfig().AddHadronicId(-20413);
  PHYSICS->mcConfig().AddHadronicId(-20323);
  PHYSICS->mcConfig().AddHadronicId(-20313);
  PHYSICS->mcConfig().AddHadronicId(-20213);
  PHYSICS->mcConfig().AddHadronicId(-10543);
  PHYSICS->mcConfig().AddHadronicId(-10541);
  PHYSICS->mcConfig().AddHadronicId(-10533);
  PHYSICS->mcConfig().AddHadronicId(-10531);
  PHYSICS->mcConfig().AddHadronicId(-10523);
  PHYSICS->mcConfig().AddHadronicId(-10521);
  PHYSICS->mcConfig().AddHadronicId(-10513);
  PHYSICS->mcConfig().AddHadronicId(-10511);
  PHYSICS->mcConfig().AddHadronicId(-10433);
  PHYSICS->mcConfig().AddHadronicId(-10431);
  PHYSICS->mcConfig().AddHadronicId(-10423);
  PHYSICS->mcConfig().AddHadronicId(-10421);
  PHYSICS->mcConfig().AddHadronicId(-10413);
  PHYSICS->mcConfig().AddHadronicId(-10411);
  PHYSICS->mcConfig().AddHadronicId(-10323);
  PHYSICS->mcConfig().AddHadronicId(-10321);
  PHYSICS->mcConfig().AddHadronicId(-10313);
  PHYSICS->mcConfig().AddHadronicId(-10311);
  PHYSICS->mcConfig().AddHadronicId(-10213);
  PHYSICS->mcConfig().AddHadronicId(-10211);
  PHYSICS->mcConfig().AddHadronicId(-5554);
  PHYSICS->mcConfig().AddHadronicId(-5544);
  PHYSICS->mcConfig().AddHadronicId(-5542);
  PHYSICS->mcConfig().AddHadronicId(-5534);
  PHYSICS->mcConfig().AddHadronicId(-5532);
  PHYSICS->mcConfig().AddHadronicId(-5524);
  PHYSICS->mcConfig().AddHadronicId(-5522);
  PHYSICS->mcConfig().AddHadronicId(-5514);
  PHYSICS->mcConfig().AddHadronicId(-5512);
  PHYSICS->mcConfig().AddHadronicId(-5503);
  PHYSICS->mcConfig().AddHadronicId(-5444);
  PHYSICS->mcConfig().AddHadronicId(-5442);
  PHYSICS->mcConfig().AddHadronicId(-5434);
  PHYSICS->mcConfig().AddHadronicId(-5432);
  PHYSICS->mcConfig().AddHadronicId(-5424);
  PHYSICS->mcConfig().AddHadronicId(-5422);
  PHYSICS->mcConfig().AddHadronicId(-5414);
  PHYSICS->mcConfig().AddHadronicId(-5412);
  PHYSICS->mcConfig().AddHadronicId(-5403);
  PHYSICS->mcConfig().AddHadronicId(-5401);
  PHYSICS->mcConfig().AddHadronicId(-5342);
  PHYSICS->mcConfig().AddHadronicId(-5334);
  PHYSICS->mcConfig().AddHadronicId(-5332);
  PHYSICS->mcConfig().AddHadronicId(-5324);
  PHYSICS->mcConfig().AddHadronicId(-5322);
  PHYSICS->mcConfig().AddHadronicId(-5314);
  PHYSICS->mcConfig().AddHadronicId(-5312);
  PHYSICS->mcConfig().AddHadronicId(-5303);
  PHYSICS->mcConfig().AddHadronicId(-5301);
  PHYSICS->mcConfig().AddHadronicId(-5242);
  PHYSICS->mcConfig().AddHadronicId(-5232);
  PHYSICS->mcConfig().AddHadronicId(-5224);
  PHYSICS->mcConfig().AddHadronicId(-5222);
  PHYSICS->mcConfig().AddHadronicId(-5214);
  PHYSICS->mcConfig().AddHadronicId(-5212);
  PHYSICS->mcConfig().AddHadronicId(-5203);
  PHYSICS->mcConfig().AddHadronicId(-5201);
  PHYSICS->mcConfig().AddHadronicId(-5142);
  PHYSICS->mcConfig().AddHadronicId(-5132);
  PHYSICS->mcConfig().AddHadronicId(-5122);
  PHYSICS->mcConfig().AddHadronicId(-5114);
  PHYSICS->mcConfig().AddHadronicId(-5112);
  PHYSICS->mcConfig().AddHadronicId(-5103);
  PHYSICS->mcConfig().AddHadronicId(-5101);
  PHYSICS->mcConfig().AddHadronicId(-4444);
  PHYSICS->mcConfig().AddHadronicId(-4434);
  PHYSICS->mcConfig().AddHadronicId(-4432);
  PHYSICS->mcConfig().AddHadronicId(-4424);
  PHYSICS->mcConfig().AddHadronicId(-4422);
  PHYSICS->mcConfig().AddHadronicId(-4414);
  PHYSICS->mcConfig().AddHadronicId(-4412);
  PHYSICS->mcConfig().AddHadronicId(-4403);
  PHYSICS->mcConfig().AddHadronicId(-4334);
  PHYSICS->mcConfig().AddHadronicId(-4332);
  PHYSICS->mcConfig().AddHadronicId(-4324);
  PHYSICS->mcConfig().AddHadronicId(-4322);
  PHYSICS->mcConfig().AddHadronicId(-4314);
  PHYSICS->mcConfig().AddHadronicId(-4312);
  PHYSICS->mcConfig().AddHadronicId(-4303);
  PHYSICS->mcConfig().AddHadronicId(-4301);
  PHYSICS->mcConfig().AddHadronicId(-4232);
  PHYSICS->mcConfig().AddHadronicId(-4224);
  PHYSICS->mcConfig().AddHadronicId(-4222);
  PHYSICS->mcConfig().AddHadronicId(-4214);
  PHYSICS->mcConfig().AddHadronicId(-4212);
  PHYSICS->mcConfig().AddHadronicId(-4203);
  PHYSICS->mcConfig().AddHadronicId(-4201);
  PHYSICS->mcConfig().AddHadronicId(-4132);
  PHYSICS->mcConfig().AddHadronicId(-4122);
  PHYSICS->mcConfig().AddHadronicId(-4114);
  PHYSICS->mcConfig().AddHadronicId(-4112);
  PHYSICS->mcConfig().AddHadronicId(-4103);
  PHYSICS->mcConfig().AddHadronicId(-4101);
  PHYSICS->mcConfig().AddHadronicId(-3334);
  PHYSICS->mcConfig().AddHadronicId(-3324);
  PHYSICS->mcConfig().AddHadronicId(-3322);
  PHYSICS->mcConfig().AddHadronicId(-3314);
  PHYSICS->mcConfig().AddHadronicId(-3312);
  PHYSICS->mcConfig().AddHadronicId(-3303);
  PHYSICS->mcConfig().AddHadronicId(-3224);
  PHYSICS->mcConfig().AddHadronicId(-3222);
  PHYSICS->mcConfig().AddHadronicId(-3214);
  PHYSICS->mcConfig().AddHadronicId(-3212);
  PHYSICS->mcConfig().AddHadronicId(-3203);
  PHYSICS->mcConfig().AddHadronicId(-3201);
  PHYSICS->mcConfig().AddHadronicId(-3122);
  PHYSICS->mcConfig().AddHadronicId(-3114);
  PHYSICS->mcConfig().AddHadronicId(-3112);
  PHYSICS->mcConfig().AddHadronicId(-3103);
  PHYSICS->mcConfig().AddHadronicId(-3101);
  PHYSICS->mcConfig().AddHadronicId(-2224);
  PHYSICS->mcConfig().AddHadronicId(-2214);
  PHYSICS->mcConfig().AddHadronicId(-2212);
  PHYSICS->mcConfig().AddHadronicId(-2203);
  PHYSICS->mcConfig().AddHadronicId(-2114);
  PHYSICS->mcConfig().AddHadronicId(-2112);
  PHYSICS->mcConfig().AddHadronicId(-2103);
  PHYSICS->mcConfig().AddHadronicId(-2101);
  PHYSICS->mcConfig().AddHadronicId(-1114);
  PHYSICS->mcConfig().AddHadronicId(-1103);
  PHYSICS->mcConfig().AddHadronicId(-545);
  PHYSICS->mcConfig().AddHadronicId(-543);
  PHYSICS->mcConfig().AddHadronicId(-541);
  PHYSICS->mcConfig().AddHadronicId(-535);
  PHYSICS->mcConfig().AddHadronicId(-533);
  PHYSICS->mcConfig().AddHadronicId(-531);
  PHYSICS->mcConfig().AddHadronicId(-525);
  PHYSICS->mcConfig().AddHadronicId(-523);
  PHYSICS->mcConfig().AddHadronicId(-521);
  PHYSICS->mcConfig().AddHadronicId(-515);
  PHYSICS->mcConfig().AddHadronicId(-513);
  PHYSICS->mcConfig().AddHadronicId(-511);
  PHYSICS->mcConfig().AddHadronicId(-435);
  PHYSICS->mcConfig().AddHadronicId(-433);
  PHYSICS->mcConfig().AddHadronicId(-431);
  PHYSICS->mcConfig().AddHadronicId(-425);
  PHYSICS->mcConfig().AddHadronicId(-423);
  PHYSICS->mcConfig().AddHadronicId(-421);
  PHYSICS->mcConfig().AddHadronicId(-415);
  PHYSICS->mcConfig().AddHadronicId(-413);
  PHYSICS->mcConfig().AddHadronicId(-411);
  PHYSICS->mcConfig().AddHadronicId(-325);
  PHYSICS->mcConfig().AddHadronicId(-323);
  PHYSICS->mcConfig().AddHadronicId(-321);
  PHYSICS->mcConfig().AddHadronicId(-315);
  PHYSICS->mcConfig().AddHadronicId(-313);
  PHYSICS->mcConfig().AddHadronicId(-311);
  PHYSICS->mcConfig().AddHadronicId(-215);
  PHYSICS->mcConfig().AddHadronicId(-213);
  PHYSICS->mcConfig().AddHadronicId(-211);
  PHYSICS->mcConfig().AddHadronicId(111);
  PHYSICS->mcConfig().AddHadronicId(113);
  PHYSICS->mcConfig().AddHadronicId(115);
  PHYSICS->mcConfig().AddHadronicId(130);
  PHYSICS->mcConfig().AddHadronicId(211);
  PHYSICS->mcConfig().AddHadronicId(213);
  PHYSICS->mcConfig().AddHadronicId(215);
  PHYSICS->mcConfig().AddHadronicId(221);
  PHYSICS->mcConfig().AddHadronicId(223);
  PHYSICS->mcConfig().AddHadronicId(225);
  PHYSICS->mcConfig().AddHadronicId(310);
  PHYSICS->mcConfig().AddHadronicId(311);
  PHYSICS->mcConfig().AddHadronicId(313);
  PHYSICS->mcConfig().AddHadronicId(315);
  PHYSICS->mcConfig().AddHadronicId(321);
  PHYSICS->mcConfig().AddHadronicId(323);
  PHYSICS->mcConfig().AddHadronicId(325);
  PHYSICS->mcConfig().AddHadronicId(331);
  PHYSICS->mcConfig().AddHadronicId(333);
  PHYSICS->mcConfig().AddHadronicId(335);
  PHYSICS->mcConfig().AddHadronicId(411);
  PHYSICS->mcConfig().AddHadronicId(413);
  PHYSICS->mcConfig().AddHadronicId(415);
  PHYSICS->mcConfig().AddHadronicId(421);
  PHYSICS->mcConfig().AddHadronicId(423);
  PHYSICS->mcConfig().AddHadronicId(425);
  PHYSICS->mcConfig().AddHadronicId(431);
  PHYSICS->mcConfig().AddHadronicId(433);
  PHYSICS->mcConfig().AddHadronicId(435);
  PHYSICS->mcConfig().AddHadronicId(441);
  PHYSICS->mcConfig().AddHadronicId(443);
  PHYSICS->mcConfig().AddHadronicId(445);
  PHYSICS->mcConfig().AddHadronicId(511);
  PHYSICS->mcConfig().AddHadronicId(513);
  PHYSICS->mcConfig().AddHadronicId(515);
  PHYSICS->mcConfig().AddHadronicId(521);
  PHYSICS->mcConfig().AddHadronicId(523);
  PHYSICS->mcConfig().AddHadronicId(525);
  PHYSICS->mcConfig().AddHadronicId(531);
  PHYSICS->mcConfig().AddHadronicId(533);
  PHYSICS->mcConfig().AddHadronicId(535);
  PHYSICS->mcConfig().AddHadronicId(541);
  PHYSICS->mcConfig().AddHadronicId(543);
  PHYSICS->mcConfig().AddHadronicId(545);
  PHYSICS->mcConfig().AddHadronicId(551);
  PHYSICS->mcConfig().AddHadronicId(553);
  PHYSICS->mcConfig().AddHadronicId(555);
  PHYSICS->mcConfig().AddHadronicId(1103);
  PHYSICS->mcConfig().AddHadronicId(1114);
  PHYSICS->mcConfig().AddHadronicId(2101);
  PHYSICS->mcConfig().AddHadronicId(2103);
  PHYSICS->mcConfig().AddHadronicId(2112);
  PHYSICS->mcConfig().AddHadronicId(2114);
  PHYSICS->mcConfig().AddHadronicId(2203);
  PHYSICS->mcConfig().AddHadronicId(2212);
  PHYSICS->mcConfig().AddHadronicId(2214);
  PHYSICS->mcConfig().AddHadronicId(2224);
  PHYSICS->mcConfig().AddHadronicId(3101);
  PHYSICS->mcConfig().AddHadronicId(3103);
  PHYSICS->mcConfig().AddHadronicId(3112);
  PHYSICS->mcConfig().AddHadronicId(3114);
  PHYSICS->mcConfig().AddHadronicId(3122);
  PHYSICS->mcConfig().AddHadronicId(3201);
  PHYSICS->mcConfig().AddHadronicId(3203);
  PHYSICS->mcConfig().AddHadronicId(3212);
  PHYSICS->mcConfig().AddHadronicId(3214);
  PHYSICS->mcConfig().AddHadronicId(3222);
  PHYSICS->mcConfig().AddHadronicId(3224);
  PHYSICS->mcConfig().AddHadronicId(3303);
  PHYSICS->mcConfig().AddHadronicId(3312);
  PHYSICS->mcConfig().AddHadronicId(3314);
  PHYSICS->mcConfig().AddHadronicId(3322);
  PHYSICS->mcConfig().AddHadronicId(3324);
  PHYSICS->mcConfig().AddHadronicId(3334);
  PHYSICS->mcConfig().AddHadronicId(4101);
  PHYSICS->mcConfig().AddHadronicId(4103);
  PHYSICS->mcConfig().AddHadronicId(4112);
  PHYSICS->mcConfig().AddHadronicId(4114);
  PHYSICS->mcConfig().AddHadronicId(4122);
  PHYSICS->mcConfig().AddHadronicId(4132);
  PHYSICS->mcConfig().AddHadronicId(4201);
  PHYSICS->mcConfig().AddHadronicId(4203);
  PHYSICS->mcConfig().AddHadronicId(4212);
  PHYSICS->mcConfig().AddHadronicId(4214);
  PHYSICS->mcConfig().AddHadronicId(4222);
  PHYSICS->mcConfig().AddHadronicId(4224);
  PHYSICS->mcConfig().AddHadronicId(4232);
  PHYSICS->mcConfig().AddHadronicId(4301);
  PHYSICS->mcConfig().AddHadronicId(4303);
  PHYSICS->mcConfig().AddHadronicId(4312);
  PHYSICS->mcConfig().AddHadronicId(4314);
  PHYSICS->mcConfig().AddHadronicId(4322);
  PHYSICS->mcConfig().AddHadronicId(4324);
  PHYSICS->mcConfig().AddHadronicId(4332);
  PHYSICS->mcConfig().AddHadronicId(4334);
  PHYSICS->mcConfig().AddHadronicId(4403);
  PHYSICS->mcConfig().AddHadronicId(4412);
  PHYSICS->mcConfig().AddHadronicId(4414);
  PHYSICS->mcConfig().AddHadronicId(4422);
  PHYSICS->mcConfig().AddHadronicId(4424);
  PHYSICS->mcConfig().AddHadronicId(4432);
  PHYSICS->mcConfig().AddHadronicId(4434);
  PHYSICS->mcConfig().AddHadronicId(4444);
  PHYSICS->mcConfig().AddHadronicId(5101);
  PHYSICS->mcConfig().AddHadronicId(5103);
  PHYSICS->mcConfig().AddHadronicId(5112);
  PHYSICS->mcConfig().AddHadronicId(5114);
  PHYSICS->mcConfig().AddHadronicId(5122);
  PHYSICS->mcConfig().AddHadronicId(5132);
  PHYSICS->mcConfig().AddHadronicId(5142);
  PHYSICS->mcConfig().AddHadronicId(5201);
  PHYSICS->mcConfig().AddHadronicId(5203);
  PHYSICS->mcConfig().AddHadronicId(5212);
  PHYSICS->mcConfig().AddHadronicId(5214);
  PHYSICS->mcConfig().AddHadronicId(5222);
  PHYSICS->mcConfig().AddHadronicId(5224);
  PHYSICS->mcConfig().AddHadronicId(5232);
  PHYSICS->mcConfig().AddHadronicId(5242);
  PHYSICS->mcConfig().AddHadronicId(5301);
  PHYSICS->mcConfig().AddHadronicId(5303);
  PHYSICS->mcConfig().AddHadronicId(5312);
  PHYSICS->mcConfig().AddHadronicId(5314);
  PHYSICS->mcConfig().AddHadronicId(5322);
  PHYSICS->mcConfig().AddHadronicId(5324);
  PHYSICS->mcConfig().AddHadronicId(5332);
  PHYSICS->mcConfig().AddHadronicId(5334);
  PHYSICS->mcConfig().AddHadronicId(5342);
  PHYSICS->mcConfig().AddHadronicId(5401);
  PHYSICS->mcConfig().AddHadronicId(5403);
  PHYSICS->mcConfig().AddHadronicId(5412);
  PHYSICS->mcConfig().AddHadronicId(5414);
  PHYSICS->mcConfig().AddHadronicId(5422);
  PHYSICS->mcConfig().AddHadronicId(5424);
  PHYSICS->mcConfig().AddHadronicId(5432);
  PHYSICS->mcConfig().AddHadronicId(5434);
  PHYSICS->mcConfig().AddHadronicId(5442);
  PHYSICS->mcConfig().AddHadronicId(5444);
  PHYSICS->mcConfig().AddHadronicId(5503);
  PHYSICS->mcConfig().AddHadronicId(5512);
  PHYSICS->mcConfig().AddHadronicId(5514);
  PHYSICS->mcConfig().AddHadronicId(5522);
  PHYSICS->mcConfig().AddHadronicId(5524);
  PHYSICS->mcConfig().AddHadronicId(5532);
  PHYSICS->mcConfig().AddHadronicId(5534);
  PHYSICS->mcConfig().AddHadronicId(5542);
  PHYSICS->mcConfig().AddHadronicId(5544);
  PHYSICS->mcConfig().AddHadronicId(5554);
  PHYSICS->mcConfig().AddHadronicId(10111);
  PHYSICS->mcConfig().AddHadronicId(10113);
  PHYSICS->mcConfig().AddHadronicId(10211);
  PHYSICS->mcConfig().AddHadronicId(10213);
  PHYSICS->mcConfig().AddHadronicId(10221);
  PHYSICS->mcConfig().AddHadronicId(10223);
  PHYSICS->mcConfig().AddHadronicId(10311);
  PHYSICS->mcConfig().AddHadronicId(10313);
  PHYSICS->mcConfig().AddHadronicId(10321);
  PHYSICS->mcConfig().AddHadronicId(10323);
  PHYSICS->mcConfig().AddHadronicId(10331);
  PHYSICS->mcConfig().AddHadronicId(10333);
  PHYSICS->mcConfig().AddHadronicId(10411);
  PHYSICS->mcConfig().AddHadronicId(10413);
  PHYSICS->mcConfig().AddHadronicId(10421);
  PHYSICS->mcConfig().AddHadronicId(10423);
  PHYSICS->mcConfig().AddHadronicId(10431);
  PHYSICS->mcConfig().AddHadronicId(10433);
  PHYSICS->mcConfig().AddHadronicId(10441);
  PHYSICS->mcConfig().AddHadronicId(10443);
  PHYSICS->mcConfig().AddHadronicId(10511);
  PHYSICS->mcConfig().AddHadronicId(10513);
  PHYSICS->mcConfig().AddHadronicId(10521);
  PHYSICS->mcConfig().AddHadronicId(10523);
  PHYSICS->mcConfig().AddHadronicId(10531);
  PHYSICS->mcConfig().AddHadronicId(10533);
  PHYSICS->mcConfig().AddHadronicId(10541);
  PHYSICS->mcConfig().AddHadronicId(10543);
  PHYSICS->mcConfig().AddHadronicId(10551);
  PHYSICS->mcConfig().AddHadronicId(10553);
  PHYSICS->mcConfig().AddHadronicId(20113);
  PHYSICS->mcConfig().AddHadronicId(20213);
  PHYSICS->mcConfig().AddHadronicId(20223);
  PHYSICS->mcConfig().AddHadronicId(20313);
  PHYSICS->mcConfig().AddHadronicId(20323);
  PHYSICS->mcConfig().AddHadronicId(20333);
  PHYSICS->mcConfig().AddHadronicId(20413);
  PHYSICS->mcConfig().AddHadronicId(20423);
  PHYSICS->mcConfig().AddHadronicId(20433);
  PHYSICS->mcConfig().AddHadronicId(20443);
  PHYSICS->mcConfig().AddHadronicId(20513);
  PHYSICS->mcConfig().AddHadronicId(20523);
  PHYSICS->mcConfig().AddHadronicId(20533);
  PHYSICS->mcConfig().AddHadronicId(20543);
  PHYSICS->mcConfig().AddHadronicId(20553);
  PHYSICS->mcConfig().AddHadronicId(100443);
  PHYSICS->mcConfig().AddHadronicId(100553);
  PHYSICS->mcConfig().AddHadronicId(9900440);
  PHYSICS->mcConfig().AddHadronicId(9900441);
  PHYSICS->mcConfig().AddHadronicId(9900443);
  PHYSICS->mcConfig().AddHadronicId(9900551);
  PHYSICS->mcConfig().AddHadronicId(9900553);
  PHYSICS->mcConfig().AddHadronicId(9910441);
  PHYSICS->mcConfig().AddHadronicId(9910551);

  // definition of the multiparticle "invisible"
  PHYSICS->mcConfig().AddInvisibleId(-16);
  PHYSICS->mcConfig().AddInvisibleId(-14);
  PHYSICS->mcConfig().AddInvisibleId(-12);
  PHYSICS->mcConfig().AddInvisibleId(12);
  PHYSICS->mcConfig().AddInvisibleId(14);
  PHYSICS->mcConfig().AddInvisibleId(16);
  PHYSICS->mcConfig().AddInvisibleId(1000022);
  PHYSICS->mcConfig().AddInvisibleId(1000039);

  // Initializing PhysicsService for RECO
  PHYSICS->recConfig().Reset();

  
  // Declaration of the signal regions (SR)
  Manager()->AddRegionSelection("2j_Meff_1200");
  Manager()->AddRegionSelection("2j_Meff_1600");
  Manager()->AddRegionSelection("2j_Meff_2000");
  Manager()->AddRegionSelection("2j_Meff_2400");
  Manager()->AddRegionSelection("2j_Meff_2800");
  Manager()->AddRegionSelection("2j_Meff_3600");
  Manager()->AddRegionSelection("2j_Meff_2100");
  Manager()->AddRegionSelection("3j_Meff_1300");
  Manager()->AddRegionSelection("4j_Meff_1000");
  Manager()->AddRegionSelection("4j_Meff_1400");
  Manager()->AddRegionSelection("4j_Meff_1800");
  Manager()->AddRegionSelection("4j_Meff_2200");
  Manager()->AddRegionSelection("4j_Meff_2600");
  Manager()->AddRegionSelection("4j_Meff_3000");
  Manager()->AddRegionSelection("5j_Meff_1700");
  Manager()->AddRegionSelection("5j_Meff_1600");
  Manager()->AddRegionSelection("5j_Meff_2000");
  Manager()->AddRegionSelection("5j_Meff_2600");
  Manager()->AddRegionSelection("6j_Meff_1200");
  Manager()->AddRegionSelection("6j_Meff_1800");
  Manager()->AddRegionSelection("6j_Meff_2200");
  Manager()->AddRegionSelection("6j_Meff_2600");
//   Manager()->AddRegionSelection("2jB_Meff_1600");
//   Manager()->AddRegionSelection("2jB_Meff_2400");
  
  
  //Preselection Cuts
  Manager()->AddCut("Preselection cuts");
  
  // Declaration of the jet multiplicity cuts
//   std::string SR_2j[]={"2j_Meff_1200","2j_Meff_1600","2j_Meff_2000","2j_Meff_2400","2j_Meff_2800","2j_Meff_3600","2j_Meff_2100"};
  std::string SR_4j[]={"4j_Meff_1000","4j_Meff_1400","4j_Meff_1800","4j_Meff_2200","4j_Meff_2600","4j_Meff_3000"};
  std::string SR_5j[]={"5j_Meff_1700","5j_Meff_1600","5j_Meff_2000","5j_Meff_2600"};
  std::string SR_6j[]={"6j_Meff_1200","6j_Meff_1800","6j_Meff_2200","6j_Meff_2600"};
  Manager()->AddCut("Njets>=2");
  Manager()->AddCut("Njets>=3","3j_Meff_1300");
  Manager()->AddCut("Njets>=4",SR_4j);
  Manager()->AddCut("Njets>=5",SR_5j);
  Manager()->AddCut("Njets>=6",SR_6j);
  
  // Declaration of the MET-jet separation cuts
  std::string DphijMET_lt3_04[] = {"2j_Meff_2100","3j_Meff_1300","4j_Meff_1000","4j_Meff_1400","4j_Meff_1800","4j_Meff_2200","4j_Meff_2600","4j_Meff_3000","5j_Meff_1600","5j_Meff_1700","5j_Meff_2000","6j_Meff_1200","6j_Meff_1800","6j_Meff_2200","6j_Meff_2600"};
  std::string DphijMET_lt3_08[] = {"2j_Meff_1200","2j_Meff_1600","2j_Meff_2000","2j_Meff_2400","2j_Meff_2800","2j_Meff_3600","5j_Meff_2600"};
  
  
  
  Manager()->AddCut("Dphi(j1,j2,(j3),MET)min > 0.4",DphijMET_lt3_04);
  Manager()->AddCut("Dphi(j1,j2,(j3),MET)min > 0.8",DphijMET_lt3_08);
  
//   std::string DphijMET_gt3_02[] = {"2j_Meff_2100","3j_Meff_1300","5j_Meff_1700","5j_Meff_1600","6j_Meff_1200","6j_Meff_1800","6j_Meff_2200","6j_Meff_2600"};
  std::string DphijMET_gt3_02[] = {"2j_Meff_2100","3j_Meff_1300","5j_Meff_1700","6j_Meff_1200","6j_Meff_1800","6j_Meff_2200","6j_Meff_2600"};
  std::string DphijMET_gt3_04[] ={"2j_Meff_1200","2j_Meff_1600","2j_Meff_2000","2j_Meff_2400","2j_Meff_2800","2j_Meff_3600","4j_Meff_1000","4j_Meff_1400","4j_Meff_1800","4j_Meff_2200","4j_Meff_2600","4j_Meff_3000","5j_Meff_2000","5j_Meff_2600"};
  
  
  Manager()->AddCut("Dphi(>j3,MET)min > 0.2",DphijMET_gt3_02);
  Manager()->AddCut("Dphi(>j3,MET)min > 0.4",DphijMET_gt3_04);
  
  // Declaration of the jet-pt cuts

  std::string ptjcut_350[] = {"2j_Meff_2000","2j_Meff_2400","2j_Meff_2800","2j_Meff_3600"};
  std::string ptj1cut_700[] = {"3j_Meff_1300","5j_Meff_1700"};
  
  Manager()->AddCut("pT(j1) > 250 GeV","2j_Meff_1200");
  Manager()->AddCut("pT(j1) > 300 GeV","2j_Meff_1600");
  Manager()->AddCut("pT(j1) > 350 GeV",ptjcut_350);
  Manager()->AddCut("pT(j1) > 600 GeV","2j_Meff_2100");
  Manager()->AddCut("pT(j1) > 700 GeV",ptj1cut_700);
  
  std::string ptj2cut_50[] = {"2j_Meff_2100","3j_Meff_1300"};
  Manager()->AddCut("pT(j2) > 250 GeV","2j_Meff_1200");
  Manager()->AddCut("pT(j2) > 300 GeV","2j_Meff_1600");
  Manager()->AddCut("pT(j2) > 350 GeV",ptjcut_350);
  Manager()->AddCut("pT(j2) > 50 GeV",ptj2cut_50);
//   Manager()->AddCut("pT(j2) > 50 GeV","2j_Meff_2100");
  
  Manager()->AddCut("pT(j3) > 50 GeV","3j_Meff_1300");
  
  std::string ptj4cut_100[] = {"4j_Meff_1000","4j_Meff_1400","4j_Meff_1800","4j_Meff_2200"};
  std::string ptj4cut_150[] = {"4j_Meff_2600","4j_Meff_3000"};
  Manager()->AddCut("pT(j4) > 100 GeV",ptj4cut_100);
  Manager()->AddCut("pT(j4) > 150 GeV",ptj4cut_150);
  Manager()->AddCut("pT(j4) > 50 GeV","5j_Meff_1700");
  
  Manager()->AddCut("pT(j5) > 50 GeV","5j_Meff_1700");
  
  std::string ptj6cut_100[] = {"6j_Meff_1800","6j_Meff_2200","6j_Meff_2600"};
  
//   Manager()->AddCut("pT(j6) > 50 GeV","6j_Meff_1200");
  Manager()->AddCut("pT(j6) > 100 GeV",ptj6cut_100);
  
  // Declaration of the eta cuts on the jets
  
  std::string etajcut_12_SR2j[] = {"2j_Meff_1600","2j_Meff_2000","2j_Meff_2400","2j_Meff_2800"};
  std::string etajcut_20_SR4j[] = {"4j_Meff_1400","4j_Meff_1800","4j_Meff_2200","4j_Meff_2600","4j_Meff_3000"};
  std::string etajcut_20_SR6j[]={"6j_Meff_1200","6j_Meff_1800"};
  
  Manager()->AddCut("eta(jets) < 0.8","2j_Meff_1200");
  Manager()->AddCut("eta(jets) < 1.2 SR2j",etajcut_12_SR2j);
  Manager()->AddCut("eta(jets) < 1.2 SR4j","4j_Meff_1000");
  Manager()->AddCut("eta(jets) < 2.0 SR4j",etajcut_20_SR4j);
  Manager()->AddCut("eta(jets) < 2.0 SR6j",etajcut_20_SR6j);
  
  // Declaration of the Aplanarity cuts
  std::string Aplanarity_04[] = {"4j_Meff_1000","4j_Meff_1400","4j_Meff_1800","4j_Meff_2200","4j_Meff_2600","4j_Meff_3000","6j_Meff_1800"};
  std::string Aplanarity_08[] = {"5j_Meff_1600","6j_Meff_2200","6j_Meff_2600"};
  
  Manager()->AddCut("lam3 > 0.04",Aplanarity_04);
  Manager()->AddCut("lam3 > 0.08",Aplanarity_08);
  
  // Declaration of the MET-to-HT/Meff ratio cuts
  
  std::string METoHT_18[] = {"2j_Meff_1600","2j_Meff_2000","2j_Meff_2400","2j_Meff_2800","2j_Meff_3600","5j_Meff_2600"};
 
  
  Manager()->AddCut("METtoHT > 14 sqrt(GeV)","2j_Meff_1200");
  Manager()->AddCut("METtoHT > 15 sqrt(GeV)","5j_Meff_2000");
  Manager()->AddCut("METtoHT > 16 sqrt(GeV)","3j_Meff_1300");
  Manager()->AddCut("METtoHT > 18 sqrt(GeV)",METoHT_18);
  Manager()->AddCut("METtoHT > 26 sqrt(GeV)","2j_Meff_2100");

  
  std::string METoMeff_02_SR4j[] = {"4j_Meff_2600","4j_Meff_3000"};
  std::string METoMeff_02_SR6j[] = {"6j_Meff_1800","6j_Meff_2200"};
  std::string METoMeff_025_SR4j[] = {"4j_Meff_1400","4j_Meff_1800","4j_Meff_2200"};
  
  Manager()->AddCut("METtoMeff(4) > 0.30","4j_Meff_1000");
  Manager()->AddCut("METtoMeff(4) > 0.25",METoMeff_025_SR4j);
  Manager()->AddCut("METtoMeff(4) > 0.20",METoMeff_02_SR4j);
  
  Manager()->AddCut("METtoMeff(5) > 0.30","5j_Meff_1700");
  Manager()->AddCut("METtoMeff(5) > 0.15","5j_Meff_1600");
  
  Manager()->AddCut("METtoMeff(6) > 0.15","6j_Meff_2600");
  Manager()->AddCut("METtoMeff(6) > 0.20",METoMeff_02_SR6j);
  Manager()->AddCut("METtoMeff(6) > 0.25","6j_Meff_1200");
  
  
  
  //Declaration of the cuts on Meff
  std::string Meff_1200[]={"2j_Meff_1200","6j_Meff_1200"};
  std::string Meff_1600[]={"2j_Meff_1600","5j_Meff_1600"};
  std::string Meff_1800[]={"4j_Meff_1800","6j_Meff_1800"};
  std::string Meff_2000[]={"2j_Meff_2000","5j_Meff_2000"};
  std::string Meff_2200[]={"4j_Meff_2200","6j_Meff_2200"};
  std::string Meff_2600[]={"4j_Meff_2600","5j_Meff_2600","6j_Meff_2600"};
  
  Manager()->AddCut("Meff > 1000 GeV","4j_Meff_1000");
  Manager()->AddCut("Meff > 1200 GeV",Meff_1200);
  Manager()->AddCut("Meff > 1300 GeV","3j_Meff_1300");
  Manager()->AddCut("Meff > 1400 GeV","4j_Meff_1400");
  Manager()->AddCut("Meff > 1600 GeV",Meff_1600);
  Manager()->AddCut("Meff > 1700 GeV","5j_Meff_1700");
  Manager()->AddCut("Meff > 1800 GeV",Meff_1800);
  Manager()->AddCut("Meff > 2000 GeV",Meff_2000);
  Manager()->AddCut("Meff > 2100 GeV","2j_Meff_2100");
  Manager()->AddCut("Meff > 2200 GeV",Meff_2200);
  Manager()->AddCut("Meff > 2400 GeV","2j_Meff_2400");
  Manager()->AddCut("Meff > 2600 GeV",Meff_2600);
  Manager()->AddCut("Meff > 2800 GeV","2j_Meff_2800");
  Manager()->AddCut("Meff > 3000 GeV","4j_Meff_3000");
  Manager()->AddCut("Meff > 3600 GeV","2j_Meff_3600");
  
  
  cout << "END   Initialization" << endl;
  
  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void sfs_test::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
unsigned int Nevents = 0;

bool sfs_test::Execute(SampleFormat& sample, const EventFormat& event)
{
  Nevents = Nevents + 1;
//   cout << " N° event = " << Nevents << endl;
  // Event weight
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
  {
    //////WARNING << "Found one event with a zero weight. Skipping...\n";
    return false;
  }
  Manager()->InitializeForNewEvent(myEventWeight);
  
  
  // The event loop start here
  if(event.rec()!=0)
  {
  
   // Containers
    std::vector<const RecLeptonFormat*> Electrons, Muons;
    std::vector<const RecJetFormat*> Jets, SignalJets;
 
    // Electrons
    for(unsigned int e=0; e<event.rec()->electrons().size(); e++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[e]);
      if(CurrentElectron->pt()>7. && fabs(CurrentElectron->eta())<2.47)
        Electrons.push_back(CurrentElectron);
    }
    SORTER->sort(Electrons);
    
    // Muons
    for(unsigned int mu=0; mu<event.rec()->muons().size(); mu++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[mu]);
      if(CurrentMuon->pt()>7. && fabs(CurrentMuon->eta())<2.7)
        Muons.push_back(CurrentMuon);
    }
    
    // Jets
    for(unsigned int j=0; j<event.rec()->jets().size(); j++)
    {
      const RecJetFormat *CurrentJet = &(event.rec()->jets()[j]);
      if(CurrentJet->pt()>20. && fabs(CurrentJet->eta())<2.8)
        Jets.push_back(CurrentJet);
    }
      
    //Overlap removal
    Jets = Removal(Jets, Electrons,  0.2);
    Electrons = Removal(Electrons, Jets,  0.4);
    Muons = Removal(Muons, Jets,  0.4);

    // MET
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();
    
    // SR jets, meff and HT, MET/sqrt(HT), Njets
    double HT=0.;
    for(unsigned int j=0; j<Jets.size(); j++)
    {
      if(Jets[j]->pt()>50.)
        SignalJets.push_back(Jets[j]);
      HT+=Jets[j]->pt();
    }
    SORTER->sort(SignalJets);
    double Meff = MET + HT;
    double METtoHT = MET/sqrt(HT);
    unsigned int NJets = SignalJets.size();
    
    // Calculation of the separation between the MET and the jets, as well as meffNj
    double dphij_1to3=1.e9, dphij_gt3=1.e9;
    double Meff4j=MET, Meff5j=MET, Meff6j=MET;
    for (unsigned int i=0; i<NJets; i++)
    {
      // Observables
      double mydphi = SignalJets[i]->dphi_0_pi(pTmiss);
      double mypt = SignalJets[i]->pt();
      // dphi(j,met)
      if(i<3 && mydphi<dphij_1to3) dphij_1to3=mydphi;
      else if(mydphi<dphij_gt3) dphij_gt3=mydphi;
      // non-inclusive meff
      if(i<4) Meff4j+=mypt;
      if(i<5) Meff5j+=mypt;
      if(i<6) Meff6j+=mypt;
    }
    double METtoMeff4 = MET/Meff4j;
    double METtoMeff5 = MET/Meff5j;
    double METtoMeff6 = MET/Meff6j;
    
    
    // Construction of the sphericity tensor, calculation of the aplanarity
    // using the Cardano algorithm
    double S12=0., S31=0., S23=0., S11=0., S22=0., S33=0., Stot=0.;
    for (unsigned int i=0; i<NJets; i++)
    {
      S11+=SignalJets[i]->px()*SignalJets[i]->px();
      S12+=SignalJets[i]->px()*SignalJets[i]->py();
      S22+=SignalJets[i]->py()*SignalJets[i]->py();
      S23+=SignalJets[i]->py()*SignalJets[i]->pz();
      S31+=SignalJets[i]->pz()*SignalJets[i]->px();
      S33+=SignalJets[i]->pz()*SignalJets[i]->pz();
      Stot+=SignalJets[i]->p()*SignalJets[i]->p();
    }
    S11=S11/Stot; S12=S12/Stot; S22=S22/Stot; S23=S23/Stot; S31=S31/Stot; S33=S33/Stot;
    double Sii = S11+S22+S33;
    double C0 = S11*S23*S23 + S22*S31*S31 + S33*S12*S12 - S11*S22*S33 - 2.*S31*S12*S23;
    double C1 = S11*S22 + S22*S33 + S11*S33 - S12*S12 - S23*S23 - S31*S31;
    double P = Sii*Sii - 3.*C1;
    double Q = Sii*(P-1.5*C1) - 13.5*C0;
    double phi = atan2(sqrt(fabs(27.*(C1*C1/4.*(P-C1) + C0*(Q+6.75*C0)))),Q)/3.;
    double cth = sqrt(fabs(P))*cos(phi);
    double sth = sqrt(fabs(P))*sin(phi)/sqrt(3.);
    double a1 = (Sii-cth)/3.+sth;
    double a2 = (Sii-cth)/3.-sth;
    double a3 = (Sii-cth)/3.+cth;
    double lam3 = 1.5*std::min(std::min(a1,a2),a3);
  

   
   //Preselection cuts
  bool IsMET = (MET>250.);
  bool IsLeptons = ((Electrons.size()+Muons.size())==0);
  bool IspTj1 = false;
  bool IsMeff = false;
  bool IsNJets = false;
  
  if(NJets>0)
  {
  IspTj1 = (SignalJets[0]->pt()>200.);
  IsMeff = (Meff>800.);
  IsNJets = (NJets>=2);
  }
  
  
  
  if(!Manager()->ApplyCut(IsMET && IspTj1 && IsMeff && IsLeptons,"Preselection cuts")) return true;
  if(!Manager()->ApplyCut(IsNJets,"Njets>=2")) return true;
  
  // Jet multiplicity
    if(!Manager()->ApplyCut(3<=NJets,"Njets>=3")) return true;
    if(!Manager()->ApplyCut(4<=NJets,"Njets>=4")) return true;
    if(!Manager()->ApplyCut(5<=NJets,"Njets>=5")) return true;
    if(!Manager()->ApplyCut(6<=NJets,"Njets>=6")) return true;
  
  // (MET,jet) separation
    if(!Manager()->ApplyCut(dphij_1to3>0.8,"Dphi(j1,j2,(j3),MET)min > 0.8")) return true;

    if(!Manager()->ApplyCut(dphij_1to3>0.4,"Dphi(j1,j2,(j3),MET)min > 0.4")) return true;

    if(!Manager()->ApplyCut(dphij_gt3>0.2,"Dphi(>j3,MET)min > 0.2")) return true;

    if(!Manager()->ApplyCut(dphij_gt3>0.4,"Dphi(>j3,MET)min > 0.4")) return true;

    

  // Jet pt thresholds

  if(!Manager()->ApplyCut(SignalJets[0]->pt()>250.,"pT(j1) > 250 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[0]->pt()>300.,"pT(j1) > 300 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[0]->pt()>350.,"pT(j1) > 350 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[0]->pt()>600.,"pT(j1) > 600 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[0]->pt()>700.,"pT(j1) > 700 GeV")) return true;

  if(!Manager()->ApplyCut(SignalJets[1]->pt()>50.,"pT(j2) > 50 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[1]->pt()>250.,"pT(j2) > 250 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[1]->pt()>300.,"pT(j2) > 300 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[1]->pt()>350.,"pT(j2) > 350 GeV")) return true;

  if(NJets>2)
  if(!Manager()->ApplyCut(SignalJets[2]->pt()>50.,"pT(j3) > 50 GeV")) return true;

  if(NJets>3) { 
  if(!Manager()->ApplyCut(SignalJets[3]->pt()>100.,"pT(j4) > 100 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[3]->pt()>150.,"pT(j4) > 150 GeV")) return true;
  }
  

  if(NJets>4) {
  if(!Manager()->ApplyCut(SignalJets[3]->pt()>50.,"pT(j4) > 50 GeV")) return true;
  if(!Manager()->ApplyCut(SignalJets[4]->pt()>50.,"pT(j5) > 50 GeV")) return true;
  }

  if(NJets>5) {

  if(!Manager()->ApplyCut(100.<SignalJets[5]->pt(),"pT(j6) > 100 GeV")) return true;
  }
  
  //eta cuts

  if(!Manager()->ApplyCut(fabs(SignalJets[0]->eta())<0.8 && fabs(SignalJets[1]->eta())<0.8,"eta(jets) < 0.8")) return true;
  
  if(!Manager()->ApplyCut(fabs(SignalJets[0]->eta())<1.2 && fabs(SignalJets[1]->eta())<1.2,"eta(jets) < 1.2 SR2j")) return true;
  
  if(NJets>3){
  if(!Manager()->ApplyCut(fabs(SignalJets[0]->eta())<1.2 && fabs(SignalJets[1]->eta())<1.2 && fabs(SignalJets[2]->eta())<1.2 && fabs(SignalJets[3]->eta())<1.2,"eta(jets) < 1.2 SR4j")) return true;    
  if(!Manager()->ApplyCut(fabs(SignalJets[0]->eta())<2.0 && fabs(SignalJets[1]->eta())<2.0 && fabs(SignalJets[2]->eta())<2.0 && fabs(SignalJets[3]->eta())<2.0,"eta(jets) < 2.0 SR4j")) return true;
  }
  if(NJets>5)
  if(!Manager()->ApplyCut(fabs(SignalJets[0]->eta())<2.0 && fabs(SignalJets[1]->eta())<2.0 && fabs(SignalJets[2]->eta())<2.0 && fabs(SignalJets[3]->eta())<2.0 && fabs(SignalJets[4]->eta())<2.0 && fabs(SignalJets[5]->eta())<2.0,"eta(jets) < 2.0 SR6j")) return true;
  
  //Aplanarity cuts
  if(NJets>3)
  {
  if(!Manager()->ApplyCut(lam3>0.04,"lam3 > 0.04")) return true;
  if(!Manager()->ApplyCut(lam3>0.08,"lam3 > 0.08")) return true;
  }
  
  
  // MET-to-HT/eff ratio cuts
  if(NJets>3)
  {
  if(!Manager()->ApplyCut(METtoMeff4>0.30,"METtoMeff(4) > 0.30")) return true;
  if(!Manager()->ApplyCut(METtoMeff4>0.25,"METtoMeff(4) > 0.25")) return true;
  if(!Manager()->ApplyCut(METtoMeff4>0.20,"METtoMeff(4) > 0.20")) return true;
  }
  if(NJets>4)
  {
  if(!Manager()->ApplyCut(METtoMeff5>0.30,"METtoMeff(5) > 0.30")) return true;
  if(!Manager()->ApplyCut(METtoMeff5>0.15,"METtoMeff(5) > 0.15")) return true;
  }
  
  if(NJets>5)
  {
  if(!Manager()->ApplyCut(METtoMeff6>0.15,"METtoMeff(6) > 0.15")) return true;
  if(!Manager()->ApplyCut(METtoMeff6>0.20,"METtoMeff(6) > 0.20")) return true;
  if(!Manager()->ApplyCut(METtoMeff6>0.25,"METtoMeff(6) > 0.25")) return true;
  
  }

  if(!Manager()->ApplyCut(METtoHT > 14.,"METtoHT > 14 sqrt(GeV)")) return true;
  if(!Manager()->ApplyCut(METtoHT > 15.,"METtoHT > 15 sqrt(GeV)")) return true;
  if(!Manager()->ApplyCut(METtoHT > 16.,"METtoHT > 16 sqrt(GeV)")) return true;
  if(!Manager()->ApplyCut(METtoHT > 18.,"METtoHT > 18 sqrt(GeV)")) return true;
  if(!Manager()->ApplyCut(METtoHT > 26.,"METtoHT > 26 sqrt(GeV)")) return true;
  
  
  
  //Meff inclusive cuts
  if(!Manager()->ApplyCut(Meff>1000.,"Meff > 1000 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>1200.,"Meff > 1200 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>1300.,"Meff > 1300 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>1400.,"Meff > 1400 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>1600.,"Meff > 1600 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>1700.,"Meff > 1700 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>1800.,"Meff > 1800 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>2000.,"Meff > 2000 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>2100.,"Meff > 2100 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>2200.,"Meff > 2200 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>2400.,"Meff > 2400 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>2600.,"Meff > 2600 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>2800.,"Meff > 2800 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>3000.,"Meff > 3000 GeV")) return true;
  if(!Manager()->ApplyCut(Meff>3600.,"Meff > 3600 GeV")) return true;
  
  
      
  }
   
  
  return true;
}


