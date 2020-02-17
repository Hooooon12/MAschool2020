#include "SampleAnalyzer/User/Analyzer/atlas_susy_2015_06.h"
using namespace MA5;

// Overlap removal
template<typename T1, typename T2> std::vector<const T1*> Removal(std::vector<const T1*>&,
  std::vector<const T2*>&, const double &);
template<typename T1> std::vector<const T1*> Removal(std::vector<const T1*>&, const double &);

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_susy_2015_06::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>   Analysis: ATLAS-CONF-2015-062              <>" << endmsg;
  INFO << "      <>             arXiv.1605.03814                 <>" << endmsg;
  INFO << "      <>             (multijet + MET)                 <>" << endmsg;
  INFO << "      <>   Recasters: S.Banerjee, B.Fuks & B.Zaldivar <>" << endmsg;
  INFO << "      <>   Contact: fuks@lpthe.jussieu.fr             <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.4                <>" << endmsg;
  INFO << "      <>   For more information, see                  <>" << endmsg;
  INFO << "      <>   http://madanalysis.irmp.ucl.ac.be/wiki/    <>" << endmsg;
  INFO << "      <>   /PhysicsAnalysisDatabase                   <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Declaration of the signal regions
  Manager()->AddRegionSelection("2jl");
  Manager()->AddRegionSelection("2jm");
  Manager()->AddRegionSelection("2jt");
  Manager()->AddRegionSelection("4jt");
  Manager()->AddRegionSelection("5j");
  Manager()->AddRegionSelection("6jm");
  Manager()->AddRegionSelection("6jt");

  // Declaration of the preselection cuts
  std::string sub2jm[]={"2jl", "2jt","4jt","5j","6jm","6jt"};
  Manager()->AddCut("Preselection-all", sub2jm);
  Manager()->AddCut("Preselection-2jm","2jm");

  // Declaration of the jet multiplicity cuts
  std::string SR_2j[]={"2jl", "2jt","2jm"};
  std::string SR_6j[]={"6jm","6jt"};
  Manager()->AddCut("Njets>=2",SR_2j);
  Manager()->AddCut("Njets>=4","4jt");
  Manager()->AddCut("Njets>=5","5j");
  Manager()->AddCut("Njets>=6",SR_6j);

  // Declaration of the MET-jet separation cuts
  std::string SR_DphiA_08[]={"2jl","2jt"};
  std::string SR_4j[]={"4jt","5j","6jm","6jt"};
  Manager()->AddCut("dphi-nj2",SR_DphiA_08);
  Manager()->AddCut("dphi-2jm","2jm");
  Manager()->AddCut("dphi-nj4",SR_4j);

  // Declaration of the jet-pt cuts
  Manager()->AddCut("pT2>50 GeV","2jm");
  Manager()->AddCut("pT2>100 GeV",SR_4j);
  Manager()->AddCut("pT2>200 GeV",SR_DphiA_08);
  Manager()->AddCut("pT4>100 GeV",SR_4j);

  // Declaration of the aplanarity cuts
  Manager()->AddCut("lam3>0.04",SR_4j);

  // Declaration of the MET-to-HT/Meff ratio cuts
  std::string SR_METoHT_15[]={"2jl","2jm"};
  Manager()->AddCut("METtoHT>15 sqrGeV",SR_METoHT_15);
  Manager()->AddCut("METtoHT>20 sqrGeV","2jt");
  Manager()->AddCut("METtoMeff4>0.20","4jt");
  Manager()->AddCut("METtoMeff5>0.25","5j");
  Manager()->AddCut("METtoMeff6>0.25","6jm");
  Manager()->AddCut("METtoMeff6>0.20","6jt");

  // Declaration of the cuts on Meff
  std::string SR_meff_1600[]={"2jm","5j","6jm"};
  std::string SR_meff_2000[]={"2jt","6jt"};
  Manager()->AddCut("Meff>1200 GeV","2jl");
  Manager()->AddCut("Meff>1600 GeV",SR_meff_1600);
  Manager()->AddCut("Meff>2000 GeV",SR_meff_2000);
  Manager()->AddCut("Meff>2200 GeV","4jt");



  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2015_06::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2015_06::Execute(SampleFormat& sample, const EventFormat& event)
{
  // Event weight
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
  {
    //WARNING << "Found one event with a zero weight. Skipping...\n";
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
      if(CurrentElectron->pt()>10. && fabs(CurrentElectron->eta())<2.47)
        Electrons.push_back(CurrentElectron);
    }
    SORTER->sort(Electrons);

    // Muons
    for(unsigned int mu=0; mu<event.rec()->muons().size(); mu++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[mu]);
      if(CurrentMuon->pt()>10. && fabs(CurrentMuon->eta())<2.7)
        Muons.push_back(CurrentMuon);
    }

    // Jets
    for(unsigned int j=0; j<event.rec()->jets().size(); j++)
    {
      const RecJetFormat *CurrentJet = &(event.rec()->jets()[j]);
      if(CurrentJet->pt()>20. && fabs(CurrentJet->eta())<2.8)
        Jets.push_back(CurrentJet);
    }

    // Overlap removal
    Jets      = Removal(Jets, Electrons,  0.2);
    Electrons = Removal(Electrons, Jets,  0.4);
    Electrons = Removal(Electrons, Muons, 0.05);
    Electrons = Removal(Electrons, 0.05);

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
      // non-onclusive meff
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

    // Preselection
    bool pre1 = ((Electrons.size()+Muons.size())==0);
    bool pre2a = false, pre2b=false;
    if(NJets>0)
    {
      pre2a = (SignalJets[0]->pt()>200.);
      pre2b = (SignalJets[0]->pt()>300.);
    }
    bool pre3 = (MET>200.);
    if(!Manager()->ApplyCut(pre1 && pre2a && pre3 ,"Preselection-all")) return true;
    if(!Manager()->ApplyCut(pre1 && pre2b && pre3 ,"Preselection-2jm")) return true;

    // Jet multiplicity
    if(!Manager()->ApplyCut(2<=NJets,"Njets>=2")) return true;
    if(!Manager()->ApplyCut(4<=NJets,"Njets>=4")) return true;
    if(!Manager()->ApplyCut(5<=NJets,"Njets>=5")) return true;
    if(!Manager()->ApplyCut(6<=NJets,"Njets>=6")) return true;

    // (MET,jet) separation
    if(!Manager()->ApplyCut(dphij_1to3>0.4,"dphi-2jm")) return true;
    if(!Manager()->ApplyCut(dphij_1to3>0.8,"dphi-nj2")) return true;
    if(!Manager()->ApplyCut(dphij_1to3>0.4 && dphij_gt3>0.2,"dphi-nj4")) return true;

    // Jet pt thresholds
    if(!Manager()->ApplyCut(50.<SignalJets[1]->pt(),"pT2>50 GeV")) return true;
    if(!Manager()->ApplyCut(100.<SignalJets[1]->pt(),"pT2>100 GeV")) return true;
    if(!Manager()->ApplyCut(200.<SignalJets[1]->pt(),"pT2>200 GeV")) return true;
    if(NJets>3)
      if(!Manager()->ApplyCut(100.<SignalJets[3]->pt(),"pT4>100 GeV")) return true;

    // Aplanarity cut
    if(NJets>3)
      if(!Manager()->ApplyCut(0.04<lam3,"lam3>0.04")) return true;

    // MET-to-HT/eff ratio
    if(!Manager()->ApplyCut(METtoHT > 15.   ,"METtoHT>15 sqrGeV")) return true;
    if(!Manager()->ApplyCut(METtoHT > 20.   ,"METtoHT>20 sqrGeV")) return true;
    if(NJets>3)
      if(!Manager()->ApplyCut(METtoMeff4>0.20,"METtoMeff4>0.20")) return true;
    if(NJets>4)
      if(!Manager()->ApplyCut(METtoMeff5>0.25,"METtoMeff5>0.25")) return true;
    if(NJets>5)
    {
      if(!Manager()->ApplyCut(METtoMeff6>0.25,"METtoMeff6>0.25")) return true;
      if(!Manager()->ApplyCut(METtoMeff6>0.20,"METtoMeff6>0.20")) return true;
    }

    // Meff inclusive cuts
    if(!Manager()->ApplyCut(Meff>1200.,"Meff>1200 GeV")) return true;
    if(!Manager()->ApplyCut(Meff>1600.,"Meff>1600 GeV")) return true;
    if(!Manager()->ApplyCut(Meff>2000.,"Meff>2000 GeV")) return true;
    if(!Manager()->ApplyCut(Meff>2200.,"Meff>2200 GeV")) return true;

  }
  return true;
}


// Overlap Removal
template<typename T1, typename T2> std::vector<const T1*> Removal(std::vector<const T1*> &v1,
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

template<typename T1> std::vector<const T1*> Removal(std::vector<const T1*> &v1,
  const double &drmin)
{
  // Determining with objects should be removed (objects are sorted)
  std::vector<bool> mask(v1.size(),false);
  for (unsigned int j=0;j<v1.size();j++)
    for (unsigned int i=j+1;i<v1.size();i++)
    {
      if (mask[i]) continue;
      if (v1[i]->dr(v1[j]) < drmin)
      {
        mask[i]=true;
        continue;
      }
    }

  // Building the cleaned container
  std::vector<const T1*> cleaned_v1;
  for (unsigned int i=0;i<v1.size();i++)
    if (!mask[i]) cleaned_v1.push_back(v1[i]);

  return cleaned_v1;
}



