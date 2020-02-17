#include "SampleAnalyzer/User/Analyzer/atlas_susy_2014_10.h"
using namespace MA5;
using namespace std;

#define PROD_FIG8 0 // 0: normal mode
                    // 1: produce histograms for comparison with Fig. 8 of paper 

template<typename T1> void OverlapRmvPT(std::vector<const T1*> &, const double &);
template<typename T1, typename T2> void OverlapRmv(std::vector<const T1*> &,
  std::vector<const T2*>, const double &);

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_susy_2014_10::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // General information on the implementers
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: ATLAS-SUSY-2014-10              <>" << endmsg;
  INFO << "        <>            arXiv:1503.03290                <>" << endmsg;
  INFO << "        <>            (2 leptons + >= 2 jets + MET)   <>" << endmsg;
  INFO << "        <>  Recasted by: B. Dumont                    <>" << endmsg;
  INFO << "        <>  Contact: dumont@lpsc.in2p3.fr             <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11            <>" << endmsg;
  INFO << "        <>  For more information, see                 <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;


  // definition of the signal regions
  // below-Z means 20 < mll < 80 GeV
  // above-Z means mll > 110 GeV

  // on-Z regions
  Manager()->AddRegionSelection("Z ee");
  Manager()->AddRegionSelection("Z mumu");
  // off-Z regions
  Manager()->AddRegionSelection("below-Z-2j-bveto ee");
  Manager()->AddRegionSelection("below-Z-2j-bveto mumu");
  Manager()->AddRegionSelection("above-Z-2j-bveto ee");
  Manager()->AddRegionSelection("above-Z-2j-bveto mumu");
  Manager()->AddRegionSelection("below-Z-2j-btag ee");
  Manager()->AddRegionSelection("below-Z-2j-btag mumu");
  Manager()->AddRegionSelection("above-Z-2j-btag ee");
  Manager()->AddRegionSelection("above-Z-2j-btag mumu");
  Manager()->AddRegionSelection("below-Z-4j-bveto ee");
  Manager()->AddRegionSelection("below-Z-4j-bveto mumu");
  Manager()->AddRegionSelection("above-Z-4j-bveto ee");
  Manager()->AddRegionSelection("above-Z-4j-bveto mumu");
  Manager()->AddRegionSelection("below-Z-4j-btag ee");
  Manager()->AddRegionSelection("below-Z-4j-btag mumu");
  Manager()->AddRegionSelection("above-Z-4j-btag ee");
  Manager()->AddRegionSelection("above-Z-4j-btag mumu");
  Manager()->AddRegionSelection("below-Z-loose ee");
  Manager()->AddRegionSelection("below-Z-loose mumu");
  Manager()->AddRegionSelection("above-Z-loose ee");
  Manager()->AddRegionSelection("above-Z-loose mumu");

  // Definition of the cuts
  std::string SRZ[] = {"Z ee", "Z mumu"};
  std::string SRge4jets[] = {"below-Z-4j-bveto ee", "below-Z-4j-bveto mumu",
                             "above-Z-4j-bveto ee", "above-Z-4j-bveto mumu",
                             "below-Z-4j-btag ee", "below-Z-4j-btag mumu",
                             "above-Z-4j-btag ee", "above-Z-4j-btag mumu"};
  std::string SRloose[] = {"below-Z-loose ee", "below-Z-loose mumu",
                           "above-Z-loose ee", "above-Z-loose mumu"};
  std::string SRMET200[] = {"below-Z-2j-bveto ee", "below-Z-2j-bveto mumu",
                            "above-Z-2j-bveto ee", "above-Z-2j-bveto mumu",
                            "below-Z-2j-btag ee", "below-Z-2j-btag mumu",
                            "above-Z-2j-btag ee", "above-Z-2j-btag mumu",
                            "below-Z-4j-bveto ee", "below-Z-4j-bveto mumu",
                            "above-Z-4j-bveto ee", "above-Z-4j-bveto mumu",
                            "below-Z-4j-btag ee", "below-Z-4j-btag mumu",
                            "above-Z-4j-btag ee", "above-Z-4j-btag mumu"};
  std::string SR0bjet[] = {"below-Z-2j-bveto ee", "below-Z-2j-bveto mumu",
                           "above-Z-2j-bveto ee", "above-Z-2j-bveto mumu",
                           "below-Z-4j-bveto ee", "below-Z-4j-bveto mumu",
                           "above-Z-4j-bveto ee", "above-Z-4j-bveto mumu"};
  std::string SRge1bjet[] = {"below-Z-2j-btag ee", "below-Z-2j-btag mumu",
                             "above-Z-2j-btag ee", "above-Z-2j-btag mumu",
                             "below-Z-4j-btag ee", "below-Z-4j-btag mumu",
                             "above-Z-4j-btag ee", "above-Z-4j-btag mumu"};
  std::string SRbelowZ[] = {"below-Z-2j-bveto ee", "below-Z-2j-bveto mumu",
                            "below-Z-2j-btag ee", "below-Z-2j-btag mumu",
                            "below-Z-4j-bveto ee", "below-Z-4j-bveto mumu",
                            "below-Z-4j-btag ee", "below-Z-4j-btag mumu",
                            "below-Z-loose ee", "below-Z-loose mumu"};
  std::string SRaboveZ[] = {"above-Z-2j-bveto ee", "above-Z-2j-bveto mumu",
                            "above-Z-2j-btag ee", "above-Z-2j-btag mumu",
                            "above-Z-4j-bveto ee", "above-Z-4j-bveto mumu",
                            "above-Z-4j-btag ee", "above-Z-4j-btag mumu",
                            "above-Z-loose ee", "above-Z-loose mumu"};
  std::string SRoffZ[] = {"below-Z-2j-bveto ee", "below-Z-2j-bveto mumu",
                          "below-Z-2j-btag ee", "below-Z-2j-btag mumu",
                          "below-Z-4j-bveto ee", "below-Z-4j-bveto mumu",
                          "below-Z-4j-btag ee", "below-Z-4j-btag mumu",
                          "below-Z-loose ee", "below-Z-loose mumu",
                          "above-Z-2j-bveto ee", "above-Z-2j-bveto mumu",
                          "above-Z-2j-btag ee", "above-Z-2j-btag mumu",
                          "above-Z-4j-bveto ee", "above-Z-4j-bveto mumu",
                          "above-Z-4j-btag ee", "above-Z-4j-btag mumu",
                          "above-Z-loose ee", "above-Z-loose mumu"};

  std::string SRee[] = {"Z ee",
                        "below-Z-2j-bveto ee", "below-Z-2j-btag ee",
                        "below-Z-4j-bveto ee", "below-Z-4j-btag ee",
                        "below-Z-loose ee", "above-Z-2j-bveto ee",
                        "above-Z-2j-btag ee", "above-Z-4j-bveto ee",
                        "above-Z-4j-btag ee", "above-Z-loose ee"};
  std::string SRmumu[] = {"Z mumu",
                          "below-Z-2j-bveto mumu", "below-Z-2j-btag mumu",
                          "below-Z-4j-bveto mumu", "below-Z-4j-btag mumu",
                          "below-Z-loose mumu", "above-Z-2j-bveto mumu",
                          "above-Z-2j-btag mumu", "above-Z-4j-bveto mumu",
                          "above-Z-4j-btag mumu", "above-Z-loose mumu"};

  Manager()->AddCut("2 OS ee", SRee);
  Manager()->AddCut("2 OS mumu", SRmumu);

  Manager()->AddCut("pT 2nd lep", SRoffZ);

  Manager()->AddCut("njets >= 2");
  Manager()->AddCut("electron crack veto", SRee);

  Manager()->AddCut("mll > 15 GeV", SRZ);
  Manager()->AddCut("mll > 20 GeV", SRoffZ);

  Manager()->AddCut("njets >= 4", SRge4jets);

  Manager()->AddCut("Delta phi(jet1,MET)", SRZ); // dphi > 0.4 cut leading jet
  Manager()->AddCut("Delta phi(jet2,MET)", SRZ); // dphi > 0.4 cut 2nd jet
  Manager()->AddCut("Z window", SRZ); // 81 < mll < 101 GeV
  Manager()->AddCut("HT > 600 GeV", SRZ);
  Manager()->AddCut("MET > 225 GeV", SRZ);

  Manager()->AddCut("MET > 200 GeV", SRMET200);
  Manager()->AddCut("MET-loose", SRloose); // > (150,100) GeV
                                           // depending if (2,>=3) jets

  Manager()->AddCut("nbjets = 0", SR0bjet);
  Manager()->AddCut("nbjets >= 1", SRge1bjet);

  Manager()->AddCut("below-Z", SRbelowZ); // mll < 80 GeV
  Manager()->AddCut("above-Z", SRaboveZ); // mll > 110 GeV

  // finally, definition of histograms
  // they are all available on
  // https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2014-10/
  
  // for this first set of histograms: to be filled after all cuts
  Manager()->AddHisto("mll Zee", 8, 81, 101, "Z ee"); // Fig. 6a
  Manager()->AddHisto("mll Zmumu", 8, 81, 101, "Z mumu"); // Fig. 6b

  Manager()->AddHisto("MET Zee", 11, 225, 500, "Z ee"); // Fig. 6c
  Manager()->AddHisto("MET Zmumu", 11, 225, 500, "Z mumu"); // Fig. 6d

  Manager()->AddHisto("HT Zee", 9, 600, 1500, "Z ee"); // Fig. 7a
  Manager()->AddHisto("HT Zmumu", 9, 600, 1500, "Z mumu"); // Fig. 7b

  Manager()->AddHisto("njets Zee", 8, 1.5, 9.5, "Z ee"); // Fig. 7c
  Manager()->AddHisto("njets Zmumu", 8, 1.5, 9.5, "Z mumu"); // Fig. 7d

  // for the four following histograms: no cut on deltaphi(jets,MET)
  // need to set PROD_FIG8 to 1 to produce these
  Manager()->AddHisto("Delta phi(jet1,MET) Zee", 9, 0, M_PI, "Z ee"); // Fig. 8a
  Manager()->AddHisto("Delta phi(jet1,MET) Zmumu", 9, 0, M_PI, "Z mumu"); // Fig. 8b

  Manager()->AddHisto("Delta phi(jet2,MET) Zee", 9, 0, M_PI, "Z ee"); // Fig. 8c
  Manager()->AddHisto("Delta phi(jet2,MET) Zmumu", 9, 0, M_PI, "Z mumu"); // Fig. 8d

  // we define the following histos as belonging to the "below-Z" SR
  // but actually below-Z or above-Z makes no difference as we fill the histo
  // before the main mll cut
  Manager()->AddHisto("mll loose ee", 28, 20, 300, "below-Z-loose ee"); // Fig. 9a
  Manager()->AddHisto("mll loose mumu", 28, 20, 300, "below-Z-loose mumu"); // Fig. 9b

  Manager()->AddHisto("mll 2j-bveto ee", 10, 20, 320, "below-Z-2j-bveto ee"); // Fig. 9c
  Manager()->AddHisto("mll 2j-bveto mumu", 10, 20, 320, "below-Z-2j-bveto mumu"); // Fig. 9d

  Manager()->AddHisto("mll 4j-bveto ee", 10, 20, 320, "below-Z-4j-bveto ee"); // Fig. 9e
  Manager()->AddHisto("mll 4j-bveto mumu", 10, 20, 320, "below-Z-4j-bveto mumu"); // Fig. 9f

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2014_10::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  return;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2014_10::Execute(SampleFormat& sample, const EventFormat& event)
{
  if(event.rec()!=0)
  {
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Book-keeping with the event weight: do not modify this
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    double myEventWeight;
    if(Configuration().IsNoEventWeight()) myEventWeight=1.;
    else if(event.mc()->weight()!=0.) myEventWeight = event.mc()->weight();
    else
    {
      //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
      return false;
    }
    Manager()->InitializeForNewEvent(myEventWeight);

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Object definitions
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    // Declaration of all containers
    std::vector<const RecLeptonFormat*> baseElectrons, baseMuons;
    std::vector<const RecJetFormat*> baseJets;
    std::vector<const RecLeptonFormat*> sigElectrons, sigMuons, sigLeptons;
    std::vector<const RecJetFormat*> sigJets;


    // baseline electrons
    for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ii]);
      double pt = CurrentElectron->pt();
      double abseta = fabs(CurrentElectron->eta());

      if(pt > 10. && abseta < 2.47) // case of |eta| in [1.37,1.52]
                                    // treated below (see electron crack veto)
        baseElectrons.push_back(CurrentElectron);
    }

    // baseline muons
    for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
      double pt = CurrentMuon->pt();
      double abseta = fabs(CurrentMuon->eta());

      if(pt > 10. && abseta < 2.4)
        baseMuons.push_back(CurrentMuon);
    }

    // baseline jets (anti-kt, r=0.4)
    for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
    {
      const RecJetFormat *CurrentJet = &(event.rec()->jets()[ii]);
      double pt = CurrentJet->pt();
      double abseta = fabs(CurrentJet->eta());

      if(pt > 20. && abseta < 4.5)
        baseJets.push_back(CurrentJet);
    }

    // overlap removal
    OverlapRmvPT(baseElectrons,0.05);
    OverlapRmv(baseJets,baseElectrons,0.2);
    OverlapRmv(baseElectrons,baseJets,0.4);
    OverlapRmv(baseMuons,baseJets,0.4);
    OverlapRmv(baseElectrons,baseMuons,0.01);

    // after overlap removal: define signal objects
    // signal electrons
    for(unsigned int ii=0; ii<baseElectrons.size(); ii++)
    {
      const RecLeptonFormat *CurrentElectron = baseElectrons[ii];
      double pt = CurrentElectron->pt();

      for(unsigned int jj=0; jj<CurrentElectron->isolCones().size(); jj++)
        if(pt < 25.)
        {
          if(fabs(CurrentElectron->isolCones()[jj].deltaR() - 0.3) < 0.001)
            if(CurrentElectron->isolCones()[jj].sumPT()/pt<0.16)
            {
              sigElectrons.push_back(CurrentElectron);
              sigLeptons.push_back(CurrentElectron);
            }
        }
        else
        {
          if(fabs(CurrentElectron->isolCones()[jj].deltaR() - 0.2) < 0.001)
            if(CurrentElectron->isolCones()[jj].sumPT()/pt<0.10)
            {
              sigElectrons.push_back(CurrentElectron);
              sigLeptons.push_back(CurrentElectron);
            }
        }
    }

    // "signal electrons with ET < 25 GeV must additionally satisfy [...]
    // the ``tight'' selection criteria": not implemented

    // signal muons
    for(unsigned int ii=0; ii<baseMuons.size(); ii++)
    {
      const RecLeptonFormat *CurrentMuon = baseMuons[ii];
      double pt = CurrentMuon->pt();

      for(unsigned int jj=0; jj<CurrentMuon->isolCones().size(); jj++)
        if(pt < 25.)
        {
          if(fabs(CurrentMuon->isolCones()[jj].deltaR() - 0.3) < 0.001)
            if(CurrentMuon->isolCones()[jj].sumPT()/pt<0.12)
            {
              sigMuons.push_back(CurrentMuon);
              sigLeptons.push_back(CurrentMuon);
            }
        }
        else
        {
          if(fabs(CurrentMuon->isolCones()[jj].deltaR() - 0.2) < 0.001)
            if(CurrentMuon->isolCones()[jj].sumPT()<1.8)
            {
              sigMuons.push_back(CurrentMuon);
              sigLeptons.push_back(CurrentMuon);
            }
        }
    }

    // signal jets
    for(unsigned int ii=0; ii<baseJets.size(); ii++)
    {
      const RecJetFormat *CurrentJet = baseJets[ii];
      double pt = CurrentJet->pt();
      double abseta = fabs(CurrentJet->eta());

      if(pt > 35. && abseta < 2.5)
        sigJets.push_back(CurrentJet);
    }

    SORTER->sort(sigElectrons);
    SORTER->sort(sigMuons);
    SORTER->sort(sigLeptons);
    SORTER->sort(sigJets);

    // select two highest-pT leptons
    bool atleasttwolep = (sigLeptons.size() >= 2 &&
                          (sigElectrons.size() >= 2 || sigMuons.size() >= 2));
    bool elecpair = false;
    bool muonpair = false;
    bool OScond = false;
    bool leadpTlepcond = false;

    if(atleasttwolep)
    {
      if(sigElectrons.size() >= 2 && sigMuons.size() < 2)
      {
        if(sigMuons.size() == 0 || sigMuons[0]->pt() < sigElectrons[1]->pt())
          elecpair = true;
      }
      else if(sigMuons.size() >= 2 && sigElectrons.size() < 2)
      {
        if(sigElectrons.size() == 0 || sigElectrons[0]->pt() < sigMuons[1]->pt())
          muonpair = true;
      }
      else
      {
        // there are >=2 electrons and >=2 muons; need to check pT ordering
        if(sigElectrons[1]->pt() > sigMuons[0]->pt())
          elecpair = true;
        else if(sigMuons[1]->pt() > sigElectrons[0]->pt())
          muonpair = true;
      }

      OScond = sigLeptons[0]->charge() != sigLeptons[1]->charge();
      leadpTlepcond = sigLeptons[0]->pt() > 25.;

      // trigger efficiency
      if(elecpair)
        myEventWeight *= 0.935;
      else if(muonpair)
        myEventWeight *= 0.81;
      Manager()->SetCurrentEventWeight(myEventWeight);
    }

    if(!Manager()->ApplyCut(elecpair && OScond && leadpTlepcond, "2 OS ee"))
      return true;
    if(!Manager()->ApplyCut(muonpair && OScond && leadpTlepcond, "2 OS mumu"))
      return true;
    if(!Manager()->ApplyCut(sigLeptons[1]->pt() > 20., "pT 2nd lep"))
      return true;

    unsigned int njets = sigJets.size();
    if(!Manager()->ApplyCut(njets > 1, "njets >= 2"))
      return true;

    // electron crack veto
    bool crackveto = true;
    if(elecpair)
    {
      double abseta1 = fabs(sigElectrons[0]->eta());
      double abseta2 = fabs(sigElectrons[1]->eta());
      crackveto = (abseta1 < 1.37 || abseta1 > 1.52) &&
                  (abseta2 < 1.37 || abseta2 > 1.52);
    }
    if(!Manager()->ApplyCut(crackveto, "electron crack veto"))
      return true;

    // mll
    double mll = (sigLeptons[0]->momentum() + sigLeptons[1]->momentum()).M();

    // preselection of mll
    if(!Manager()->ApplyCut(mll > 15., "mll > 15 GeV"))
      return true;
    if(!Manager()->ApplyCut(mll > 20., "mll > 20 GeV"))
      return true;

    MALorentzVector p_met = event.rec()->MET().momentum();

    // Delta phi(jet12, MET)
    double dphi1 = 0.;
    double dphi2 = 0.;
    if(njets > 1)
    {
      dphi1 = fabs(sigJets[0]->momentum().DeltaPhi(p_met));
      dphi2 = fabs(sigJets[1]->momentum().DeltaPhi(p_met));
    }

    if(PROD_FIG8 == 0)
    {
      if(!Manager()->ApplyCut(dphi1 > 0.4, "Delta phi(jet1,MET)"))
        return true;
      if(!Manager()->ApplyCut(dphi2 > 0.4, "Delta phi(jet2,MET)"))
        return true;
    }
    else
    {
      if(!Manager()->ApplyCut(true, "Delta phi(jet1,MET)"))
        return true;
      if(!Manager()->ApplyCut(true, "Delta phi(jet2,MET)"))
        return true;
    }


    if(!Manager()->ApplyCut(mll > 81. && mll < 101., "Z window"))
      return true;

    // HT = sum pTsignaljets + pTlepton1 + pTlepton2
    double HT = 0.;
    for(unsigned int ii=0; ii<njets; ii++)
    {
      HT += sigJets[ii]->pt();
    }
    HT += sigLeptons[0]->pt() + sigLeptons[1]->pt();

    if(!Manager()->ApplyCut(HT > 600., "HT > 600 GeV"))
      return true;

    if(!Manager()->ApplyCut(njets > 3, "njets >= 4"))
      return true;

    // MET
    double MET = p_met.Pt();

    double METloosemin;
    if(njets == 2)
      METloosemin = 150.;
    else
      METloosemin = 100.;

    if(!Manager()->ApplyCut(MET > METloosemin, "MET-loose")) // SR Z
      return true;
    if(!Manager()->ApplyCut(MET > 200., "MET > 200 GeV")) // SR 2j & 4j
      return true;
    if(!Manager()->ApplyCut(MET > 225., "MET > 225 GeV")) // SR Z
      return true;

    // b-tagging
    double nbjets = 0;
    for(unsigned int ii=0; ii<njets; ii++)
    {
      if(sigJets[ii]->btag())
        nbjets += 1;
    }

    if(!Manager()->ApplyCut(nbjets == 0, "nbjets = 0"))
      return true;
    if(!Manager()->ApplyCut(nbjets > 0, "nbjets >= 1"))
      return true;

    Manager()->FillHisto("mll loose ee", mll);
    Manager()->FillHisto("mll loose mumu", mll);
    Manager()->FillHisto("mll 2j-bveto ee", mll);
    Manager()->FillHisto("mll 2j-bveto mumu", mll);
    Manager()->FillHisto("mll 4j-bveto ee", mll);
    Manager()->FillHisto("mll 4j-bveto mumu", mll);

    // final mll selecton for off-Z cases
    if(!Manager()->ApplyCut(mll < 80., "below-Z"))
      return true;
    if(!Manager()->ApplyCut(mll > 110., "above-Z"))
      return true;

    // fill histograms
    Manager()->FillHisto("mll Zee", mll);
    Manager()->FillHisto("mll Zmumu", mll);
    Manager()->FillHisto("MET Zee", MET);
    Manager()->FillHisto("MET Zmumu", MET);
    Manager()->FillHisto("HT Zee", HT);
    Manager()->FillHisto("HT Zmumu", HT);
    Manager()->FillHisto("njets Zee", njets);
    Manager()->FillHisto("njets Zmumu", njets);

    // need to set PROD_FIG8 to 1 to produce the following histograms correctly
    Manager()->FillHisto("Delta phi(jet1,MET) Zee", dphi1);
    Manager()->FillHisto("Delta phi(jet1,MET) Zmumu", dphi1);
    Manager()->FillHisto("Delta phi(jet2,MET) Zee", dphi2);
    Manager()->FillHisto("Delta phi(jet2,MET) Zmumu", dphi2);

  }
  return true;
}

// remove the object with the smallest pT if overlap
template<typename T1> void OverlapRmvPT(std::vector<const T1*> &v1, const double &DR)
{
  for(int i=v1.size()-1; i>=0; i--)
    for(int j=i-1; j>=0; j--)
      if(v1[i]->dr(v1[j]) < DR)
      {
        if(v1[i]->pt() < v1[j]->pt()) v1.erase(v1.begin()+i);
        else
        {
          v1.erase(v1.begin()+j);
          i--;
        }
        break;
      }
  return;
}

// remove object v1 if overlap
template<typename T1, typename T2> void OverlapRmv(std::vector<const T1*> &v1,
  std::vector<const T2*> v2, const double &dr)
{
  for(int i=v1.size()-1; i>=0; i--)
    for(unsigned int j=0; j<v2.size(); j++)
      if(v1[i]->dr(v2[j])<dr)
      {
        v1.erase(v1.begin()+i);
        break;
      }
  return;
}

