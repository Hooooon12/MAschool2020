#include "SampleAnalyzer/User/Analyzer/user.h"
using namespace MA5;

MAbool user::Initialize(const MA5::Configuration& cfg,
                      const std::map<std::string,std::string>& parameters)
{
  // Initializing PhysicsService for MC
  PHYSICS->mcConfig().Reset();

  // definition of the multiparticle "hadronic"
  PHYSICS->mcConfig().AddHadronicId(-5);
  PHYSICS->mcConfig().AddHadronicId(-4);
  PHYSICS->mcConfig().AddHadronicId(-3);
  PHYSICS->mcConfig().AddHadronicId(-2);
  PHYSICS->mcConfig().AddHadronicId(-1);
  PHYSICS->mcConfig().AddHadronicId(1);
  PHYSICS->mcConfig().AddHadronicId(2);
  PHYSICS->mcConfig().AddHadronicId(3);
  PHYSICS->mcConfig().AddHadronicId(4);
  PHYSICS->mcConfig().AddHadronicId(5);
  PHYSICS->mcConfig().AddHadronicId(21);

  // definition of the multiparticle "invisible"
  PHYSICS->mcConfig().AddInvisibleId(-16);
  PHYSICS->mcConfig().AddInvisibleId(-14);
  PHYSICS->mcConfig().AddInvisibleId(-12);
  PHYSICS->mcConfig().AddInvisibleId(12);
  PHYSICS->mcConfig().AddInvisibleId(14);
  PHYSICS->mcConfig().AddInvisibleId(16);
  PHYSICS->mcConfig().AddInvisibleId(1000022);

  // ===== Signal region ===== //
  Manager()->AddRegionSelection("myregion");

  // ===== Selections ===== //
  Manager()->AddCut("1_PT ( mu ) < 40.0");

  // ===== Histograms ===== //
  Manager()->AddHisto("1_PT", 100,0.0,1000.0);
  Manager()->AddHisto("2_PT", 100,0.0,1000.0);

  // No problem during initialization
  return true;
}

MAbool user::Execute(SampleFormat& sample, const EventFormat& event)
{
  MAfloat32 __event_weight__ = 1.0;
  if (weighted_events_ && event.mc()!=0) __event_weight__ = event.mc()->weight();

  if (sample.mc()!=0) sample.mc()->addWeightedEvents(__event_weight__);
  Manager()->InitializeForNewEvent(__event_weight__);

  // Clearing particle containers
  {
      _P_muPTorderingfinalstate_REG_.clear();
  }

  // Filling particle containers
  {
    for (MAuint32 i=0;i<event.mc()->particles().size();i++)
    {
      if (isP__muPTorderingfinalstate((&(event.mc()->particles()[i])))) _P_muPTorderingfinalstate_REG_.push_back(&(event.mc()->particles()[i]));
    }
  }

  // Sorting particles
  // Histogram number 1
  //   * Plot: PT ( mu ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_muPTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("1_PT", _P_muPTorderingfinalstate_REG_[ind[0]]->pt());
    }
  }
  }

  // Event selection number 1
  //   * Cut: reject PT ( mu ) < 40.0, regions = []
  {
    std::vector<MAbool> filter(1,false);
    {
    {
      MAuint32 ind[1];
      for (ind[0]=0;ind[0]<_P_muPTorderingfinalstate_REG_.size();ind[0]++)
      {
        if (_P_muPTorderingfinalstate_REG_[ind[0]]->pt()<40.0) {filter[0]=true; break;}
      }
    }
    }
    MAbool filter_global = (filter[0]);
    if(!Manager()->ApplyCut(!filter_global, "1_PT ( mu ) < 40.0")) return true;
  }

  // Histogram number 2
  //   * Plot: PT ( mu ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_muPTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("2_PT", _P_muPTorderingfinalstate_REG_[ind[0]]->pt());
    }
  }
  }

  return true;
}

void user::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}
