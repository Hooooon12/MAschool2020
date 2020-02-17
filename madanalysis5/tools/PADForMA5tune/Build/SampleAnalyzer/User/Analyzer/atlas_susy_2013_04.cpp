#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_04.h"

using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_susy_2013_04::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: ATLAS-SUSY-2013-04              <>" << endmsg;
  INFO << "        <>            arXiv:1308.1841                 <>" << endmsg;
  INFO << "        <>            (ATLAS multijet + missing E_T)  <>" << endmsg;
  INFO << "        <>  Recasted by: M.Blanke, B.Fuks, I.Galon    <>" << endmsg;
  INFO << "        <>  Contact: monika.blanke@cern.ch            <>" << endmsg;
  INFO << "        <>           benjamin.fuks@cern.ch            <>" << endmsg;
  INFO << "        <>           iftah@tx.technion.ac.il          <>" << endmsg;
  INFO << "        <>           gilad.perez.cern.ch              <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.12            <>" << endmsg;
  INFO << "        <>  DOI: xx.yyyy/zzz                          <>" << endmsg;
  INFO << "        <>  Please cite arXiv.YYMM.NNNN               <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Signal region declarations
  Manager()->AddRegionSelection("8j50, 0 bjet");
  Manager()->AddRegionSelection("8j50, 1 bjet");
  Manager()->AddRegionSelection("8j50, >=2 bjets");
  Manager()->AddRegionSelection("9j50, 0 bjet");
  Manager()->AddRegionSelection("9j50, 1 bjet");
  Manager()->AddRegionSelection("9j50, >=2 bjets");
  Manager()->AddRegionSelection(">=10j50");
  Manager()->AddRegionSelection("7j80, 0 bjet");
  Manager()->AddRegionSelection("7j80, 1 bjet");
  Manager()->AddRegionSelection("7j80, >=2 bjets");
  Manager()->AddRegionSelection(">=8j80, 0 bjet");
  Manager()->AddRegionSelection(">=8j80, 1 bjet");
  Manager()->AddRegionSelection(">=8j80, >=2 bjets");

  // Cut declarations for the multi-jet + flavor stream
  Manager()->AddCut("6 jets");
  Manager()->AddCut("Lepton veto");


  std::string SR8j50Cut[] = {"8j50, 0 bjet", "8j50, 1 bjet", "8j50, >=2 bjets"};
  Manager()->AddCut("8 jets with pT > 50, eta < 2",SR8j50Cut);

  std::string SR9j50Cut[] = {"9j50, 0 bjet", "9j50, 1 bjet", "9j50, >=2 bjets"};
  Manager()->AddCut("9 jets with pT > 50, eta < 2",SR9j50Cut);

  Manager()->AddCut(">=10 jets with pT > 50, eta < 2", ">=10j50");

  std::string SR7j80Cut[] = {"7j80, 0 bjet", "7j80, 1 bjet", "7j80, >=2 bjets"};
  Manager()->AddCut("7 jets with pT > 80, eta < 2",SR7j80Cut);

  std::string SR8j80Cut[] = {">=8j80, 0 bjet", ">=8j80, 1 bjet", ">=8j80, >=2 bjets"};
  Manager()->AddCut(">=8 jets with pT > 80, eta < 2",SR8j80Cut);

  Manager()->AddCut("MET/sqrt(HT) > 4GeV^1/2");

  std::string zerobtagCut[] = {"8j50, 0 bjet", "9j50, 0 bjet","7j80, 0 bjet", ">=8j80, 0 bjet"};
  Manager()->AddCut("0 bjet with pT > 40, eta < 2.5",zerobtagCut);

  std::string onebtagCut[] = {"8j50, 1 bjet", "9j50, 1 bjet", "7j80, 1 bjet", ">=8j80, 1 bjet"};
  Manager()->AddCut("1 bjet with pT > 40, eta < 2.5",onebtagCut);

  std::string atleast2btagCut[] = {"8j50, >=2 bjets", "9j50, >=2 bjets", "7j80, >=2 bjets", ">=8j80, >=2 bjets"};
  Manager()->AddCut(">=2 bjets with pT > 40, eta < 2.5",atleast2btagCut);


  // Histogram declaration (the benchmark used in the figure is not available)
//  Manager()->AddHisto("MET/sqrt(HT) in 8j50, 0 bjet",32,0,16,"8j50, 0 bjet"); // Fig. 5a
//  Manager()->AddHisto("MET/sqrt(HT) in 9j50, 0 bjet",32,0,16,"9j50, 0 bjet"); // Fig. 5b
//  Manager()->AddHisto("MET/sqrt(HT) in 8j50, 1 bjet",32,0,16,"8j50, 1 bjet"); // Fig. 5c
//  Manager()->AddHisto("MET/sqrt(HT) in 9j50, 1 bjet",32,0,16,"9j50, 1 bjet"); // Fig. 5d
//  Manager()->AddHisto("MET/sqrt(HT) in 8j50, >=2 bjets",32,0,16,"8j50, >=2 bjets"); // Fig. 5e
//  Manager()->AddHisto("MET/sqrt(HT) in 9j50, >=2 bjets",32,0,16,"9j50, >=2 bjets"); // Fig. 5f
//  Manager()->AddHisto("MET/sqrt(HT) in >=10j50",32,0,16,">=10j50"); // Fig. 6
//  Manager()->AddHisto("MET/sqrt(HT) in 7j80, 0 bjet",32,0,16,"7j80, 0 bjet"); // Fig. 7a
//  Manager()->AddHisto("MET/sqrt(HT) in 8j80, 0 bjet",32,0,16,">=8j80, 0 bjet"); // Fig. 7b
//  Manager()->AddHisto("MET/sqrt(HT) in 7j80, 1 bjet",32,0,16,"7j80, 1 bjet"); // Fig. 7c
//  Manager()->AddHisto("MET/sqrt(HT) in 8j80, 1 bjet",32,0,16,">=8j80, 1 bjet"); // Fig. 7d
//  Manager()->AddHisto("MET/sqrt(HT) in 7j80, >=2 bjets",32,0,16,"7j80, >=2 bjets"); // Fig. 7e
//  Manager()->AddHisto("MET/sqrt(HT) in 8j80, >=2 bjets",32,0,16,">=8j80, >=2 bjets"); // Fig. 7f

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2013_04::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files) {}


// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2013_04::Execute(SampleFormat& sample, const EventFormat& event)
{
  if (event.rec()!=0)
  {
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Initialization for the current event
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    double myEventWeight;
    if(Configuration().IsNoEventWeight()) myEventWeight=1.;
    else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
    else
    {
      //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
      return false;
    }
    Manager()->InitializeForNewEvent(myEventWeight);

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Collect the different kinds of object we're interested in into containers
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    std::vector<const RecJetFormat*> myJets, myHardJets, myVeryHardJets, myBJets;
    std::vector<const RecLeptonFormat*> myLeptons;

    // Very loose electrons
    std::vector<const RecLeptonFormat*> LooseElectrons;
    for (unsigned int i=0;i<event.rec()->electrons().size();i++)
    {
      const RecLeptonFormat *lep = &(event.rec()->electrons()[i]);
      double pt = lep->pt();
      if(pt<5.) continue;
      for(unsigned int j=0; j<lep->isolCones().size(); j++)
        if(fabs(lep->isolCones()[j].deltaR() - 0.2) < 0.001)
          if(lep->isolCones()[j].sumET()/pt<0.2)
             LooseElectrons.push_back(lep);
    }

    // Getting the jet collection
    std::vector<const RecJetFormat*> CleanedJets;
    std::vector<bool> mask(event.rec()->jets().size(),false);
    for (unsigned int i=0;i<event.rec()->jets().size();i++)
      if (event.rec()->jets()[i].pt()<0.5) mask[i]=true;
    for (unsigned int i=0;i<LooseElectrons.size();i++)
    {
      if (LooseElectrons[i]==0) continue;
      if (LooseElectrons[i]->pt()<1e-6) continue;
      int jet_index=-1;
      double deltaR_min=0;
      for (unsigned int j=0;j<event.rec()->jets().size();j++)
      {
        const RecJetFormat& jet = event.rec()->jets()[j];
        if (mask[j]) continue;
        double dr = LooseElectrons[i]->momentum().DeltaR(jet.momentum());
        if (dr>0.2) continue;
        if (jet_index==-1 || dr<deltaR_min)
          { deltaR_min=dr; jet_index=j; }
      }
      if (jet_index!=-1) mask[jet_index]=true;
    }
    for (unsigned int i=0;i<event.rec()->jets().size();i++)
      if (!mask[i]) CleanedJets.push_back(&event.rec()->jets()[i]);

    // Overlap removal between the leptons and the jets (cleaning the leptons)
    for(int i=LooseElectrons.size()-1; i>=0; i--)
      for(unsigned int j=0; j<CleanedJets.size(); j++)
        if(LooseElectrons[i]->dr(CleanedJets[j])<0.4)
        {
          LooseElectrons.erase(LooseElectrons.begin()+i);
          break;
        }

    // Computation of the HT variable
    double HT = 0.;
    unsigned int TriggerJets=0;
    for(unsigned int i=0; i<CleanedJets.size(); i++)
    {
      const RecJetFormat *CurrentJet = CleanedJets[i];
      double pt = CurrentJet->pt();
      double Et = CurrentJet->et();
      double eta = fabs(CurrentJet->eta());
      if(pt>20. && eta<2.8)
      {
        myJets.push_back(CurrentJet);
        if(Et>45.) TriggerJets++;
        if(pt>40.) HT+=pt;
        if(pt>50. && eta<2.)
        {
           myHardJets.push_back(CurrentJet);
           if(pt>80.) myVeryHardJets.push_back(CurrentJet);
        }
        if(pt>40. && eta<2.5 && CurrentJet->btag()) myBJets.push_back(CurrentJet);
      }
    }

    // electrons
    for(unsigned int i=0; i<LooseElectrons.size(); i++)
    {
      const RecLeptonFormat *CurrentElectron = LooseElectrons[i];
      double pt = CurrentElectron->pt();
      double eta = fabs(CurrentElectron->eta());
      if(pt>10. && eta<2.47) myLeptons.push_back(CurrentElectron);
    }

    // muons
    for(unsigned int i=0; i<event.rec()->muons().size(); i++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[i]);
      double pt = CurrentMuon->pt();
      double eta = fabs(CurrentMuon->eta());
      if(pt>10. && eta<2.5) myLeptons.push_back(CurrentMuon);
    }

    // Overlap removal between the leptons and the jets (cleaning the leptons)
    for(int i=myLeptons.size()-1; i>=0; i--)
      for(unsigned int j=0; j<CleanedJets.size(); j++)
        if(myLeptons[i]->dr(CleanedJets[j])<0.4)
        {
          myLeptons.erase(myLeptons.begin()+i);
          break;
        }


    // Cut-0: 6 jets
    if(!Manager()->ApplyCut(TriggerJets>=6,"6 jets"))
      return true;

    // Cut-1: lepton veto
    if(!Manager()->ApplyCut((myLeptons.size()==0),"Lepton veto"))
      return true;

    // missing transverse momentum:
    // We'll have to see whether the default definition of MET is sufficiently close...
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Signal region definitions
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Cut-2: at least 8 hard jets (subdivision into three regions to be further divided)
    unsigned int nhj = myHardJets.size();
    if(!Manager()->ApplyCut(nhj==8,"8 jets with pT > 50, eta < 2"))
      return true;
    if(!Manager()->ApplyCut(nhj==9,"9 jets with pT > 50, eta < 2"))
      return true;
    if(!Manager()->ApplyCut(nhj>=10,">=10 jets with pT > 50, eta < 2"))
      return true;

    // Cut-3: at least 7 very hard jets (subdivision into two regions to be further divided)
    unsigned int nvhj = myVeryHardJets.size();
    if(!Manager()->ApplyCut(nvhj==7,"7 jets with pT > 80, eta < 2"))
      return true;
    if(!Manager()->ApplyCut(nvhj>=8,">=8 jets with pT > 80, eta < 2"))
      return true;

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // MET/sqrt(HT) plots (cf. Fig 5 to 7) and cut
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    double METOverSqrtHT = MET/sqrt(HT);

    // Cut-4:  MET/sqrt(HT) > 4 GeV^1/2
    if(!Manager()->ApplyCut(METOverSqrtHT>4.,"MET/sqrt(HT) > 4GeV^1/2"))
      return true;

    // Cut-%: subdivisions when checking the number of b-tags
    unsigned int nb = myBJets.size();
    if(!Manager()->ApplyCut(nb==0,"0 bjet with pT > 40, eta < 2.5"))
      return true;
    if(!Manager()->ApplyCut(nb==1,"1 bjet with pT > 40, eta < 2.5"))
      return true;
    if(!Manager()->ApplyCut(nb>=2,">=2 bjets with pT > 40, eta < 2.5"))
      return true;

//    // Fig 5
//    Manager()->FillHisto("MET/sqrt(HT) in 8j50, 0 bjet", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 9j50, 0 bjet", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 8j50, 1 bjet", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 9j50, 1 bjet", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 8j50, >=2 bjets", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 9j50, >=2 bjets", METOverSqrtHT);
//
//    // Fig 6
//    Manager()->FillHisto("MET/sqrt(HT) in >=10j50", METOverSqrtHT);
//
//    // Fig 7
//    Manager()->FillHisto("MET/sqrt(HT) in 7j80, 0 bjet", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 8j80, 0 bjet", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 7j80, 1 bjet", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 8j80, 1 bjet", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 7j80, >=2 bjets", METOverSqrtHT);
//    Manager()->FillHisto("MET/sqrt(HT) in 8j80, >=2 bjets", METOverSqrtHT);



  }
  return true;
}

