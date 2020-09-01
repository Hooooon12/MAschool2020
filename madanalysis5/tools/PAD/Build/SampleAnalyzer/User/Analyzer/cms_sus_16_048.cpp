#include "SampleAnalyzer/User/Analyzer/cms_sus_16_048.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_sus_16_048::Initialize(const MA5::Configuration& cfg,
   const std::map<std::string,std::string>& parameters)
{
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>   Analysis: CMS_SUS_16_048, arXiv:1801.01846 <>" << endmsg;
  INFO << "      <>             (soft dilepton LHC13, 35.9 fb^-1)<>" << endmsg;
  INFO << "      <>   Recasted by: B. Fuks                       <>" << endmsg;
  INFO << "      <>   Contacts: fuks@lpthe.jussieu.fr            <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.8                <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Signal regions
  Manager()->AddRegionSelection("Ewkino_lowMET_M_4to9");
  Manager()->AddRegionSelection("Ewkino_lowMET_M_10to20");
  Manager()->AddRegionSelection("Ewkino_lowMET_M_20to30");
  Manager()->AddRegionSelection("Ewkino_lowMET_M_30to50");
  Manager()->AddRegionSelection("Ewkino_medMET_M_4to9");
  Manager()->AddRegionSelection("Ewkino_medMET_M_10to20");
  Manager()->AddRegionSelection("Ewkino_medMET_M_20to30");
  Manager()->AddRegionSelection("Ewkino_medMET_M_30to50");
  Manager()->AddRegionSelection("Ewkino_highMET_M_4to9");
  Manager()->AddRegionSelection("Ewkino_highMET_M_10to20");
  Manager()->AddRegionSelection("Ewkino_highMET_M_20to30");
  Manager()->AddRegionSelection("Ewkino_highMET_M_30to50");

  Manager()->AddRegionSelection("stop_lowMET_PT_5to12");
  Manager()->AddRegionSelection("stop_lowMET_PT_12to20");
  Manager()->AddRegionSelection("stop_lowMET_PT_20to30");
  Manager()->AddRegionSelection("stop_medMET_PT_5to12");
  Manager()->AddRegionSelection("stop_medMET_PT_12to20");
  Manager()->AddRegionSelection("stop_medMET_PT_20to30");
  Manager()->AddRegionSelection("stop_highMET_PT_5to12");
  Manager()->AddRegionSelection("stop_highMET_PT_12to20");
  Manager()->AddRegionSelection("stop_highMET_PT_20to30");

  // Preselection cuts
  std::string ewkinos[] = {"Ewkino_lowMET_M_4to9", "Ewkino_lowMET_M_10to20",
   "Ewkino_lowMET_M_20to30", "Ewkino_lowMET_M_30to50", "Ewkino_medMET_M_4to9",
   "Ewkino_medMET_M_10to20", "Ewkino_medMET_M_20to30", "Ewkino_medMET_M_30to50",
   "Ewkino_highMET_M_4to9", "Ewkino_highMET_M_10to20","Ewkino_highMET_M_20to30",
   "Ewkino_highMET_M_30to50"};
  std::string non_stpHM[] = {"Ewkino_lowMET_M_4to9", "Ewkino_lowMET_M_10to20",
   "Ewkino_lowMET_M_20to30", "Ewkino_lowMET_M_30to50", "Ewkino_medMET_M_4to9",
   "Ewkino_medMET_M_10to20", "Ewkino_medMET_M_20to30", "Ewkino_medMET_M_30to50",
   "Ewkino_highMET_M_4to9", "Ewkino_highMET_M_10to20","Ewkino_highMET_M_20to30",
   "Ewkino_highMET_M_30to50", "stop_lowMET_PT_5to12","stop_lowMET_PT_12to20",
   "stop_lowMET_PT_20to30", "stop_medMET_PT_5to12", "stop_medMET_PT_12to20",
   "stop_medMET_PT_20to30"};
  std::string lowMET[] = {"Ewkino_lowMET_M_4to9", "Ewkino_lowMET_M_10to20",
   "Ewkino_lowMET_M_20to30", "Ewkino_lowMET_M_30to50", "stop_lowMET_PT_5to12",
   "stop_lowMET_PT_12to20", "stop_lowMET_PT_20to30"};
  Manager()->AddCut("Lepton_1_init");
  Manager()->AddCut("Lepton_1");
  Manager()->AddCut("Lepton_2");
  Manager()->AddCut("Lepton_2_nonStopHM", non_stpHM);
  Manager()->AddCut("Dimuon",lowMET);
  Manager()->AddCut("SameFlavour",ewkinos);
  Manager()->AddCut("OSdilepton");
  Manager()->AddCut("pt(ll)");
  Manager()->AddCut("M(ll)_bounds", ewkinos);
  Manager()->AddCut("M(ll)_hadronic_veto", ewkinos);

  // MET cuts
  std::string ewk_medMET[] = {"Ewkino_medMET_M_4to9", "Ewkino_medMET_M_10to20",
   "Ewkino_medMET_M_20to30", "Ewkino_medMET_M_30to50"};
  std::string ewk_highMET[] = {"Ewkino_highMET_M_4to9",
   "Ewkino_highMET_M_10to20","Ewkino_highMET_M_20to30",
   "Ewkino_highMET_M_30to50"};
  std::string stp_medMET[] = {"stop_medMET_PT_5to12", "stop_medMET_PT_12to20",
   "stop_medMET_PT_20to30"};
  std::string stp_highMET[] = {"stop_highMET_PT_5to12", "stop_highMET_PT_12to20",
   "stop_highMET_PT_20to30"};
  Manager()->AddCut("MET");
  Manager()->AddCut("lowMET",lowMET);
  Manager()->AddCut("MET_corrected");
  Manager()->AddCut("lowMET_corrected",lowMET);
  Manager()->AddCut("ewk_medMET", ewk_medMET);
  Manager()->AddCut("ewk_highMET",ewk_highMET);
  Manager()->AddCut("stp_medMET", stp_medMET);
  Manager()->AddCut("stp_highMET",stp_highMET);

  // Follow up preselection
  Manager()->AddCut("ISR_jet");
  Manager()->AddCut("HT");
  Manager()->AddCut("MET/HT");
  Manager()->AddCut("b-veto");
  Manager()->AddCut("Mtautau");
  Manager()->AddCut("MT_MET",ewkinos);

  // Mll cuts
  std::string MLL4_9[] = {"Ewkino_lowMET_M_4to9", "Ewkino_medMET_M_4to9",
    "Ewkino_highMET_M_4to9"};
  std::string MLL10_20[] = {"Ewkino_lowMET_M_10to20", "Ewkino_medMET_M_10to20",
    "Ewkino_highMET_M_10to20"};
  std::string MLL20_30[] = {"Ewkino_lowMET_M_20to30", "Ewkino_medMET_M_20to30",
    "Ewkino_highMET_M_20to30"};
  std::string MLL30_50[] = {"Ewkino_lowMET_M_30to50", "Ewkino_medMET_M_30to50",
    "Ewkino_highMET_M_30to50"};
  Manager()->AddCut("MLL4_9",MLL4_9);
  Manager()->AddCut("MLL10_20",MLL10_20);
  Manager()->AddCut("MLL20_30",MLL20_30);
  Manager()->AddCut("MLL30_50",MLL30_50);

  // PT(lepton1)
  std::string PTL5_12[] = {"stop_lowMET_PT_5to12", "stop_medMET_PT_5to12",
   "stop_highMET_PT_5to12"};
  std::string PTL12_20[] = {"stop_lowMET_PT_12to20", "stop_medMET_PT_12to20",
    "stop_highMET_PT_12to20"};
  std::string PTL20_30[] = {"stop_lowMET_PT_20to30", "stop_medMET_PT_20to30",
   "stop_highMET_PT_20to30"};
  Manager()->AddCut("PTL5_12", PTL5_12);
  Manager()->AddCut("PTL12_20",PTL12_20);
  Manager()->AddCut("PTL20_30",PTL20_30);


  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_sus_16_048::Finalize(const SampleFormat& summary,
  const std::vector<SampleFormat>& files)
{
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_sus_16_048::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Security for empty events
  if (event.rec()==0) return true;

  // Event weight
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight = event.mc()->weight();
  else return false;
  Manager()->InitializeForNewEvent(myEventWeight);

  // Leptons
  std::vector<const RecLeptonFormat*> Leptons;
  for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
  {
    const RecLeptonFormat *myElec = &(event.rec()->electrons()[ii]);
    if(myElec->pt()<5. || myElec->abseta()>2.5) continue;
    Leptons.push_back(myElec);
  }
  for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
  {
    const RecLeptonFormat *myMuon = &(event.rec()->muons()[ii]);
    if(myMuon->pt()<3.5 || myMuon->abseta()>2.4) continue;
    Leptons.push_back(myMuon);
  }
  SORTER->sort(Leptons);
  unsigned int Nl = Leptons.size();
  if(!Manager()->ApplyCut((event.rec()->electrons().size()+event.rec()->muons().size())>0, "Lepton_1_init")) return true;

  // Jets
  std::vector<const RecJetFormat*> SignalJets;
  for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
  {
    const RecJetFormat * myJet = &(event.rec()->jets()[ii]);
    if(myJet->pt()<25. || myJet->abseta()>2.4) continue;
    SignalJets.push_back(myJet);
  }
  SignalJets = PHYSICS->Isol->JetCleaning(SignalJets, Leptons, 0.2);
  double HT=0.;
  unsigned int Nb=0, Nj = SignalJets.size();
  for(unsigned int ii=0; ii<SignalJets.size(); ii++)
  {
    HT+=SignalJets[ii]->pt();
    if(SignalJets[ii]->btag()) Nb++;
  }

  // Requirement on the first lepton
  bool firstlpt = (Nl>=1) && (Leptons[0]->pt()>5.) && (Leptons[0]->pt()<30.);
  if(!Manager()->ApplyCut(firstlpt, "Lepton_1")) return true;

  // Requirement on the second lepton
  bool seclpt_general   = (Nl>=2) && (Leptons[1]->pt()<30.);
  if(!Manager()->ApplyCut(seclpt_general,   "Lepton_2")) return true;
  bool seclpt_non_stpHM = (Leptons[1]->pt()>5.);
  if(!Manager()->ApplyCut(seclpt_non_stpHM, "Lepton_2_nonStopHM")) return true;

  // 1 OS dilepton / flavour requirements
  bool osdilep = (Nl==2) && (Leptons[0]->charge()*Leptons[1]->charge()<0);
  bool is_SF     = (Leptons[0]->isMuon()==Leptons[1]->isMuon());
  bool is_dimuon = is_SF && Leptons[0]->isMuon();
  if(!Manager()->ApplyCut(is_dimuon, "Dimuon")) return true;
  if(!Manager()->ApplyCut(is_SF, "SameFlavour")) return true;
  if(!Manager()->ApplyCut(osdilep, "OSdilepton")) return true;

  // Missing Transverse Energy
  MALorentzVector ptmiss  = event.rec()->MET().momentum();
  double MET     = ptmiss.Pt();
  double MET_cor = (ptmiss + Leptons[0]->momentum()+Leptons[1]->momentum()).Pt();

  // PT(ll) and Mll
  double ptll = (Leptons[0]->momentum()+Leptons[1]->momentum()).Pt();
  double mll = (Leptons[0]->momentum()+Leptons[1]->momentum()).M();
  bool mll_lims = is_SF && (mll>4.) && (mll<50.);
  bool mll_veto = is_SF && ((mll<9.) || (mll>10.5));
  if(!Manager()->ApplyCut(ptll>3., "pt(ll)")) return true;
  if(!Manager()->ApplyCut(mll_lims, "M(ll)_bounds")) return true;
  if(!Manager()->ApplyCut(mll_veto, "M(ll)_hadronic_veto")) return true;

  // MET cut
  if(!Manager()->ApplyCut(MET>125., "MET")) return true;
  if(!Manager()->ApplyCut(is_dimuon && MET<200., "lowMET")) return true;
  // Trigger efficiency
  if(is_dimuon && MET < 200.)
    { Manager()->SetCurrentEventWeight(0.65*myEventWeight); }
  // Corrected MET cuts
  if(!Manager()->ApplyCut(is_dimuon && MET_cor>125., "MET_corrected")) return true;
  if(!Manager()->ApplyCut(is_dimuon && MET_cor<200., "lowMET_corrected"))
    return true;
  if(!Manager()->ApplyCut(MET>200. && MET<250., "ewk_medMET")) return true;
  if(!Manager()->ApplyCut(MET>200. && MET<300., "stp_medMET")) return true;
  if(!Manager()->ApplyCut(MET>250., "ewk_highMET")) return true;
  if(!Manager()->ApplyCut(MET>300., "stp_highMET")) return true;

  // ISR jet
  if(!Manager()->ApplyCut(Nj>0, "ISR_jet")) return true;
  if(!Manager()->ApplyCut(HT>100., "HT")) return true;

  // MET to HT
  if(!Manager()->ApplyCut(MET/HT<1.4 && MET/HT>0.6, "MET/HT")) return true;

  // b-veto
  if(!Manager()->ApplyCut(Nb==0, "b-veto")) return true;

  // M(tau tau)
  double AA = -(ptmiss.Px()*Leptons[1]->py() - ptmiss.Py()*Leptons[1]->px())/
        (Leptons[0]->py()*Leptons[1]->px() - Leptons[0]->px()*Leptons[1]->py());
  double BB = (ptmiss.Px()*Leptons[0]->py() - ptmiss.Py()*Leptons[0]->px())/
        (Leptons[0]->py()*Leptons[1]->px() - Leptons[0]->px()*Leptons[1]->py());
  double mtautau = ((AA+1.)*Leptons[0]->momentum() + (BB+1.)*Leptons[1]->momentum()).M();
  if(!Manager()->ApplyCut(mtautau<0. || mtautau>160., "Mtautau")) return true;

  // MT(li, met)
  double mt1 = sqrt(2.*Leptons[0]->pt()*MET*(1.-cos(Leptons[0]->dphi_0_pi(ptmiss))));
  double mt2 = sqrt(2.*Leptons[1]->pt()*MET*(1.-cos(Leptons[1]->dphi_0_pi(ptmiss))));
  if(!Manager()->ApplyCut(std::max(mt1,mt2)<70., "MT_MET")) return true;

  // Mll
  if(!Manager()->ApplyCut(mll<9., "MLL4_9")) return true;
  if(!Manager()->ApplyCut(mll>10.5 && mll<20., "MLL10_20")) return true;
  if(!Manager()->ApplyCut(mll>20.  && mll<30., "MLL20_30")) return true;
  if(!Manager()->ApplyCut(mll>30., "MLL30_50")) return true;

  // pt(l1)
  double pt1=Leptons[0]->pt();
  if(!Manager()->ApplyCut(pt1<12., "PTL5_12")) return true;
  if(!Manager()->ApplyCut(pt1>12. && pt1<20., "PTL12_20")) return true;
  if(!Manager()->ApplyCut(pt1>20. && pt1<30., "PTL20_30")) return true;

  // exit
  return true;
}

// Overlap Removal
template<typename T1, typename T2> std::vector<const T1*> cms_sus_16_048::Removal(std::vector<const T1*> &v1,
  std::vector<const T2*> &v2, const double &drmin)
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

