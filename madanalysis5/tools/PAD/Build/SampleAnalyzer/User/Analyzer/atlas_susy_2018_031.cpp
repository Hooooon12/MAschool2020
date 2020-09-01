#include "SampleAnalyzer/User/Analyzer/atlas_susy_2018_031.h"
using namespace MA5;
using namespace std;

template<typename T1, typename T2> std::vector<const T1*>
  Removal(std::vector<const T1*>&, std::vector<const T2*>&, const double &);
// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_susy_2018_031::Initialize(const MA5::Configuration& cfg, 
                                     const std::map<std::string,std::string>& parameters)
{
  INFO << "    <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "    <>    Analysis: ATLAS SUSY 2018 031                                 <>" << endmsg;
  INFO << "    <>    Higgs, sbottom, Bjets + MET @ 13 TeV, 139 fb^-1               <>" << endmsg;
  INFO << "    <>    arXiv:1908.03122                                              <>" << endmsg;
  INFO << "    <>    Recasted by : J.Y. Araz                                       <>" << endmsg;
  INFO << "    <>    Contact     : jack.araz@concordia.ca                          <>" << endmsg;
  INFO << "    <>    Based on MadAnalysis 5 v1.8 and above                         <>" << endmsg;
  INFO << "    <>    For more information, see                                     <>" << endmsg;
  INFO << "    <>    http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase <>" << endmsg;
  INFO << "    <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // ========================= //
  // ===== Signal region ===== //
  // ========================= //

  Manager()->AddRegionSelection("SRA");
  Manager()->AddRegionSelection("SRA_L");
  Manager()->AddRegionSelection("SRA_M");
  Manager()->AddRegionSelection("SRA_H");

  Manager()->AddRegionSelection("SRB");

  Manager()->AddRegionSelection("SRC");
  Manager()->AddRegionSelection("SRC_22");
  Manager()->AddRegionSelection("SRC_24");
  Manager()->AddRegionSelection("SRC_26");
  Manager()->AddRegionSelection("SRC_28");

  std::string SRA[]   = {"SRA","SRA_L","SRA_M","SRA_H"};
  std::string SRC[]   = {"SRC","SRC_22","SRC_24","SRC_26","SRC_28"};
  std::string SRABC[] = {"SRA","SRA_L","SRA_M","SRA_H","SRB",
                         "SRC","SRC_22","SRC_24","SRC_26","SRC_28"};
  std::string SRAB[]  = {"SRA","SRA_L","SRA_M","SRA_H","SRB"};
  std::string SRAB1[] = {"SRA","SRB"};

  // ====================== //
  // ===== Selections ===== //
  // ====================== //

  // Common selections
  Manager()->AddCut("$\\slashed{E}_T$ trigger",       SRABC);
  Manager()->AddCut("$N_{lep} = 0$",                  SRABC);

  Manager()->AddCut("$N_{j} \\geq 6$",                SRA);
  Manager()->AddCut("$N_{j} \\geq 5$",                "SRB");
  Manager()->AddCut("$N_{j} \\geq 4$",                SRC);

  Manager()->AddCut("$N_{b} \\geq 4$",                SRAB);
  Manager()->AddCut("$N_{b} \\geq 3$",                SRC);

  Manager()->AddCut("$\\slashed{E}_T > 350$",         SRAB);
  Manager()->AddCut("$\\slashed{E}_T > 250$",         SRC);

  Manager()->AddCut("$min(\\Delta\\phi(j_{1-4},\\slashed{E}_T))>0.4$ [rad]",SRABC);

  Manager()->AddCut("$\\tau^h$ veto",                 SRAB);

  // SRA selections
  Manager()->AddCut("$p^{b_1}_T > 200$ [GeV]",        SRA);
  Manager()->AddCut("$\\Delta R_{max}(b,b)>2.5$",     SRA);
  Manager()->AddCut("$\\Delta R_{max-min}(b,b)<2.5$", SRA);
  Manager()->AddCut("$m(h_{cand})>80$ [GeV]",         SRA);

  // SRB selections
  Manager()->AddCut("$m(h_{cand1},h_{cand2})_{avg}\\in[75,175]$ [GeV]", "SRB");
  Manager()->AddCut("Leading jet non-b-tagged",                         "SRB");
  Manager()->AddCut("$p^{j_1}_T > 350$ [GeV]",                          "SRB");
  Manager()->AddCut("$|\\Delta\\phi(j_{1},\\slashed{E}_T)|>2.8$ [rad]", "SRB");

  Manager()->AddCut("$m_{eff} > 1$ [TeV]",            SRAB1);

  Manager()->AddCut("$m_{eff} \\in [1,1.5]$ [TeV]",   "SRA_L");
  Manager()->AddCut("$m_{eff} \\in [1.5,2]$ [TeV]",   "SRA_M");
  Manager()->AddCut("$m_{eff} > 2$ [TeV]",            "SRA_H");

  // SRC selections
  Manager()->AddCut("$\\slashed{E}_T$ Sig. $>22$",          "SRC");
  Manager()->AddCut("$\\slashed{E}_T$ Sig. $\\in [22,24]$", "SRC_22");
  Manager()->AddCut("$\\slashed{E}_T$ Sig. $\\in [24,26]$", "SRC_24");
  Manager()->AddCut("$\\slashed{E}_T$ Sig. $\\in [26,28]$", "SRC_26");
  Manager()->AddCut("$\\slashed{E}_T$ Sig. $>28$",          "SRC_28");

  // ====================== //
  // ===== Histograms ===== //
  // ====================== //

  Manager()->AddHisto("SRA_Meff",  11,800.0,3000., "SRA");
  Manager()->AddHisto("SRA_Mh",    12,0.0,480.,    "SRA");

  Manager()->AddHisto("SRB_PTj1",  9,50.0,950.,    "SRB");
  Manager()->AddHisto("SRB_MhAvg", 16,50.0,450.,   "SRB");

  Manager()->AddHisto("SRC_MET",   13,200.0,1500., "SRC");
  Manager()->AddHisto("SRC_Sig",   19,17.0,36.,    "SRC");

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2018_031::Finalize(const SampleFormat& summary, 
                                   const std::vector<SampleFormat>& files){}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2018_031::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Event weight
  MAdouble64 EvWeight;
  if(Configuration().IsNoEventWeight()) EvWeight=1.;
  else if(event.mc()->weight()!=0.) EvWeight=event.mc()->weight();
  else { return false;}
  Manager()->InitializeForNewEvent(EvWeight);
  // Empty event
  if (event.rec()==0) {return true;}
  event_num++;
  std::vector<const RecJetFormat*>    BaseJets,  SignalBJets,   SignalnonBJets, SignalJets;
  std::vector<const RecLeptonFormat*> BaseMuons, BaseElectrons, SignalMuons,    SignalElectrons;
  std::vector<const RecTauFormat*>    SignalTaus;
  DEBUG << "============== Event " << event_num << endmsg;
  // Jets
  for(MAuint32 ij=0; ij<event.rec()->jets().size(); ij++)
  {
    const RecJetFormat *CurrentJet = &(event.rec()->jets()[ij]);
    if ( CurrentJet->pt() > 20.0 && CurrentJet->abseta() < 4.8)
    {
       BaseJets.push_back(CurrentJet);
    }
  }

  // Taus
  // Candidates (tau) are identified as jets which have |eta| < 2.5 and 
  // less than five inner detector tracks of pT > 500 MeV.
  for(MAuint32 ij=0; ij<event.rec()->taus().size(); ij++)
  {
    const RecTauFormat *CurrentTau = &(event.rec()->taus()[ij]);
    if ( CurrentTau->pt() > 0.5 && CurrentTau->abseta()<2.5)
    {
       SignalTaus.push_back(CurrentTau);
    }
  }

  // Electron with pT > 4.5 GeV & eta < 2.47
  for(MAuint32 ie=0; ie<event.rec()->electrons().size(); ie++)
  {
    const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ie]);
    if( CurrentElectron->pt()>4.5 && CurrentElectron->abseta() < 2.47)
      BaseElectrons.push_back(CurrentElectron);
  }

  // Muons with pT > 4 GeV & eta < 2.5
  for(MAuint32 im=0; im<event.rec()->muons().size(); im++)
  {
    const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[im]);
    if( CurrentMuon->pt()>4. && CurrentMuon->abseta() < 2.5)
      BaseMuons.push_back(CurrentMuon);
  }

  // Lepton-jet overlap removal
  BaseJets        = Removal(BaseJets,      BaseElectrons, 0.2);
  BaseElectrons   = Removal(BaseElectrons, BaseJets,      0.4);
  SignalMuons     = Removal(BaseMuons,     BaseJets,      0.4);

  // Select signal jets and bjets from basejets
  MAdouble64 HT = 0.0;
  for (MAuint32 i=0; i<BaseJets.size(); i++)
  {
    if ( BaseJets[i]->pt() > 30.0 && BaseJets[i]->abseta() < 2.8)
    {
      SignalJets.push_back(BaseJets[i]);
      HT += BaseJets[i]->pt();
      if(!BaseJets[i]->btag())
      {
        SignalnonBJets.push_back(BaseJets[i]);
      } else if ( BaseJets[i]->abseta() < 2.5 && BaseJets[i]->btag())
        {
          SignalBJets.push_back(BaseJets[i]);
        }
    }
  }

  // Select signal electrons and muons from base electrons and muons
  MAdouble64 LeadLepPt = 0.0;
  for (MAuint32 i=0; i<BaseElectrons.size(); i++)
  {
    if ( BaseElectrons[i]->pt() > 20.0 && BaseElectrons[i]->abseta()<2.47)
      {
        SignalElectrons.push_back(BaseElectrons[i]);
        if (BaseElectrons[i]->pt() > LeadLepPt)
          LeadLepPt = BaseElectrons[i]->pt();
      }
  }

  for (MAuint32 i=0; i<BaseMuons.size(); i++)
  {
    if ( BaseMuons[i]->pt() > 20.0 && BaseMuons[i]->abseta()<2.5)
      {
        SignalMuons.push_back(BaseMuons[i]);
        if (BaseMuons[i]->pt() > LeadLepPt)
          LeadLepPt = BaseMuons[i]->pt();
      }
  }
  
//TrkMiss
  MALorentzVector TrkMiss;
  for(MAuint32 i=0; i<event.rec()->tracks().size(); i++)
  {
    const RecTrackFormat *CurrentTrack = &(event.rec()->tracks()[i]);
    TrkMiss -= CurrentTrack->momentum();
  }


  DEBUG << "    * Event reconstructed properly..." << endmsg;
  // The MET & Meff
  MALorentzVector pTmiss = event.rec()->MET().momentum();
  MAdouble64 MET         = pTmiss.Pt();
  MAdouble64 Meff        = HT + MET;

  // Ordering everything
  SORTER->sort(SignalJets,      PTordering);
  SORTER->sort(SignalBJets,     PTordering);
  SORTER->sort(SignalnonBJets,  PTordering);
  SORTER->sort(SignalMuons,     PTordering);
  SORTER->sort(SignalElectrons, PTordering);

  MAint32  nBaselineLeptons = BaseMuons.size() + BaseElectrons.size();
  MAuint32 nJets            = SignalJets.size();
  MAint32  nbJets           = SignalBJets.size();
//  MAint32 nLeptons         = SignalMuons.size() + SignalElectrons.size();
  MAbool  nonBLead         = false;

  if(SignalnonBJets.size() > 0 && nbJets > 0)
  {
    if (SignalnonBJets[0]->pt() > SignalBJets[0]->pt()) 
    {
      nonBLead = true;
    }
      else nonBLead = false;
  }

  //minDPhis
  MAdouble64 minDPhiJMET_4 = 99.;
  MAdouble64 DPhiJMET_1    = 99.;
  for (MAuint32 i=0; i<4; i++)
  {
    if (nJets >= i+1)
    {
      MAdouble64 DPhi = SignalJets[i]->dphi_0_pi(pTmiss);
      if (DPhi < minDPhiJMET_4) minDPhiJMET_4 = DPhi;
    }
  }
  if (nJets > 0) DPhiJMET_1 = SignalJets[0]->dphi_0_pi(pTmiss);

  MAdouble64 minDPhiTauMet = 99.;
  for (MAuint32 i=0; i<SignalTaus.size(); i++)
  {
    MAdouble64 DPhi = SignalTaus[i]->dphi_0_pi(pTmiss);
    if (DPhi < minDPhiTauMet) minDPhiTauMet = DPhi;
  }
  DEBUG << "    * Starting cut-flow..." << endmsg;
  // Need to be figured out:
  if (!Manager()->ApplyCut(TrkMiss.Pt()>0.5 && minDPhiTauMet>1.0471976, "$\\slashed{E}_T$ trigger")) return true;
  
  if (!Manager()->ApplyCut(nBaselineLeptons == 0, "$N_{lep} = 0$")) return true;

  if (!Manager()->ApplyCut(nJets >= 6, "$N_{j} \\geq 6$")) return true;
  if (!Manager()->ApplyCut(nJets >= 5, "$N_{j} \\geq 5$")) return true;
  if (!Manager()->ApplyCut(nJets >= 4, "$N_{j} \\geq 4$")) return true;
  
  if (!Manager()->ApplyCut(nbJets >= 4, "$N_{b} \\geq 4$")) return true;
  if (!Manager()->ApplyCut(nbJets >= 3, "$N_{b} \\geq 3$")) return true;

  Manager()->FillHisto("SRC_MET",   MET);
  if (!Manager()->ApplyCut(MET > 350.0, "$\\slashed{E}_T > 350$")) return true;
  if (!Manager()->ApplyCut(MET > 250.0, "$\\slashed{E}_T > 250$")) return true;

  if (!Manager()->ApplyCut(minDPhiJMET_4 > 0.4, "$min(\\Delta\\phi(j_{1-4},\\slashed{E}_T))>0.4$ [rad]")) return true;

  MAdouble64 METtoHT = 0.;
  if (MET > 0. && HT > 0.) METtoHT = MET/sqrt(HT);

  Manager()->FillHisto("SRC_Sig",   METtoHT);
  if (!Manager()->ApplyCut(METtoHT>22.0,                   "$\\slashed{E}_T$ Sig. $>22$")) return true;
  if (!Manager()->ApplyCut(METtoHT>=22.0 && METtoHT<=24.0, "$\\slashed{E}_T$ Sig. $\\in [22,24]$")) return true;
  if (!Manager()->ApplyCut(METtoHT>=24.0 && METtoHT<=26.0, "$\\slashed{E}_T$ Sig. $\\in [24,26]$")) return true;
  if (!Manager()->ApplyCut(METtoHT>=26.0 && METtoHT<=28.0, "$\\slashed{E}_T$ Sig. $\\in [26,28]$")) return true;
  if (!Manager()->ApplyCut(METtoHT > 28.0,                 "$\\slashed{E}_T$ Sig. $>28$")) return true;


  // Tau veto is wrong!!!
  if (!Manager()->ApplyCut(SignalTaus.size()==0, "$\\tau^h$ veto")) return true;

  if (!Manager()->ApplyCut(SignalBJets[0]->pt() > 200.0, "$p^{b_1}_T > 200$ [GeV]")) return true;

  // =============================== //
  // ===== Max - Min Algorithm ===== //
  // =============================== //

  MAdouble64 maxDR     = 0.;
  MAdouble64 maxmin_M  = -99.;
  MAdouble64 max_M     = -99.;
  MAdouble64 max_avg_M = -99.;
  MAuint32   imax      = -1;
  MAuint32   jmax      = -1;
  MAdouble64 maxminDR  = 99.;
  MAdouble64 maxmaxDR  = -1.;
  MAuint32   imin      = -1;
  MAuint32   jmin      = -1;
  MAuint32   imaxmax   = -1;
  MAuint32   jmaxmax   = -1;
  DEBUG << "    * Starting Min-Max Algorithm..." << endmsg;
  std::vector< std::vector<double> > DR_matrix;
  for(MAuint32 i=0; i<SignalBJets.size(); i++)
  {
    std::vector<MAdouble64> temp; 
    for(MAuint32 j=0; j<=i; j++)
    {
      MAdouble64 DR = SignalBJets[i]->dr(SignalBJets[j]);
      if (i !=j)
      {
        if (DR>maxDR) 
        {
          maxDR = DR;
          imax  = i; 
          jmax  = j;
        }
      }
      temp.push_back(DR);
    }
    DR_matrix.push_back(temp);
  }

  max_M = (SignalBJets[imax]->momentum()+SignalBJets[jmax]->momentum()).M();

  for(MAuint32 i=0; i<SignalBJets.size(); i++)
  {
    for(MAuint32 j=0; j<=i; j++)
    {
      if (i != j)
      {
        MAdouble64 DR = DR_matrix[i][j];
        if (i != imax && j != jmax && DR > maxmaxDR)
        {
          imaxmax = i; 
          jmaxmax = j;
        }
        if (i != imax && j != jmax && DR < maxminDR)
        {
          maxminDR = DR;
          imin     = i;
          jmin     = j;
        }
      }
    }
  }

  MAdouble64 maxmax_M = 0.;

  if (SignalBJets.size() >= imaxmax && SignalBJets.size() >= jmaxmax && imaxmax >= 0 && jmaxmax >= 0)
    maxmax_M = (SignalBJets[imaxmax]->momentum() + SignalBJets[jmaxmax]->momentum()).M();
  if (max_M > 0. && maxmax_M > 0.)
    max_avg_M           = (max_M+maxmax_M)/2.0;
  if (SignalBJets.size() >= imin && SignalBJets.size() >= jmin && imin >= 0 && jmin >= 0)
    maxmin_M            = (SignalBJets[imin]->momentum() + SignalBJets[jmin]->momentum()).M();
  if (!Manager()->ApplyCut(maxDR > 2.5,     "$\\Delta R_{max}(b,b)>2.5$")) return true;
  if (!Manager()->ApplyCut(maxminDR < 2.5,  "$\\Delta R_{max-min}(b,b)<2.5$")) return true;

  Manager()->FillHisto("SRA_Mh",   maxmin_M);
  if (!Manager()->ApplyCut(maxmin_M > 80.0, "$m(h_{cand})>80$ [GeV]")) return true;

  Manager()->FillHisto("SRB_MhAvg",   max_avg_M);
  if (!Manager()->ApplyCut(max_avg_M > 175.0 && max_avg_M < 75.0, 
                           "$m(h_{cand1},h_{cand2})_{avg}\\in[75,175]$ [GeV]")) return true;
  if (!Manager()->ApplyCut(nonBLead, "Leading jet non-b-tagged")) return true;

  Manager()->FillHisto("SRB_PTj1",   SignalJets[0]->pt());
  if (!Manager()->ApplyCut(SignalJets[0]->pt()>350.0, "$p^{j_1}_T > 350$ [GeV]")) return true;
  if (!Manager()->ApplyCut(DPhiJMET_1>2.8, "$|\\Delta\\phi(j_{1},\\slashed{E}_T)|>2.8$ [rad]")) return true;
  
  Manager()->FillHisto("SRA_Meff",   Meff);
  if (!Manager()->ApplyCut(Meff>1000.0,                  "$m_{eff} > 1$ [TeV]")) return true;
  if (!Manager()->ApplyCut(Meff>=1000.0 && Meff<=1500.0, "$m_{eff} \\in [1,1.5]$ [TeV]")) return true;
  if (!Manager()->ApplyCut(Meff>=1500.0 && Meff<=2000.0, "$m_{eff} \\in [1.5,2]$ [TeV]")) return true;
  if (!Manager()->ApplyCut(Meff>2000.0,                  "$m_{eff} > 2$ [TeV]")) return true;
  DEBUG << "    * All cuts applied properly..." << endmsg;
  return true;
}

// Overlap Removal
template<typename T1, typename T2> std::vector<const T1*>
  Removal(std::vector<const T1*> &v1, std::vector<const T2*> &v2,
  const MAdouble64 &drmin)
{
  // Determining with objects should be removed
  std::vector<bool> mask(v1.size(),false);
  for (MAuint32 j=0;j<v1.size();j++)
    for (MAuint32 i=0;i<v2.size();i++)
      if (v2[i]->dr(v1[j]) < drmin)
      {
        mask[j]=true;
        break;
      }

  // Building the cleaned container
  std::vector<const T1*> cleaned_v1;
  for (MAuint32 i=0;i<v1.size();i++)
    if (!mask[i]) cleaned_v1.push_back(v1[i]);

  return cleaned_v1;
}