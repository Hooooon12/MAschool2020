#include "SampleAnalyzer/User/Analyzer/cms_sus_13_012.h"
using namespace MA5;
using namespace std;

// Define =====================================================
// =====some utilities to be used in the analysis ======
// ========================================================

double calcSumPt(const RecLeptonFormat* mylepton, double coneSize)
{
  double sumPt_ = 0;
  for(unsigned int c=0; c<mylepton->isolCones().size(); c++)
    {
      if(!(fabs(mylepton->isolCones()[c].deltaR() - coneSize)<0.0001)) continue;
      sumPt_ = mylepton->isolCones()[c].sumPT();
    }
  return sumPt_;
}


// ===============================================================
// Initialize =====================================================
// function called one time at the beginning of the analysis ======
// ===============================================================
bool cms_sus_13_012::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  cout << "========================================\n";
  cout << "Analysis: CMS-SUS-13-012, arXiv:1402.4770 "
       << "(HT + MHT)\n";
  cout << "Written with MA5 version 1.1.10\n";
  cout << "Authors: S. Bein \n";
  cout << "Contact e-mails: sbein@gmail.com\n";
  cout << "DOI: xx.yyyy/zzz\n";
  cout << "Please cite arXiv.YYMM.NNNN\n"; //TODO: add arXiv ref
  cout << "========================================\n";

  cout << "BEGIN Initialization" << endl; 
  // =====Declare the 36 signal regions in this analysis=====
  Manager()->AddRegionSelection("Njets3-5, HT500-800, MHT200-300");
  Manager()->AddRegionSelection("Njets3-5, HT500-800, MHT300-450");
  Manager()->AddRegionSelection("Njets3-5, HT500-800, MHT450-600");
  Manager()->AddRegionSelection("Njets3-5, HT500-800, MHT>600");
  Manager()->AddRegionSelection("Njets3-5, HT800-1000, MHT200-300");
  Manager()->AddRegionSelection("Njets3-5, HT800-1000, MHT300-450");
  Manager()->AddRegionSelection("Njets3-5, HT800-1000, MHT450-600");
  Manager()->AddRegionSelection("Njets3-5, HT800-1000, MHT>600");
  Manager()->AddRegionSelection("Njets3-5, HT1000-1250, MHT200-300");
  Manager()->AddRegionSelection("Njets3-5, HT1000-1250, MHT300-450");
  Manager()->AddRegionSelection("Njets3-5, HT1000-1250, MHT450-600");
  Manager()->AddRegionSelection("Njets3-5, HT1000-1250, MHT>600");
  Manager()->AddRegionSelection("Njets3-5, HT1250-1500, MHT200-300");
  Manager()->AddRegionSelection("Njets3-5, HT1250-1500, MHT300-450");
  Manager()->AddRegionSelection("Njets3-5, HT1250-1500, MHT>450");
  Manager()->AddRegionSelection("Njets3-5, HT>1500, MHT200-300");
  Manager()->AddRegionSelection("Njets3-5, HT>1500, MHT>300");
  Manager()->AddRegionSelection("Njets6-7, HT500-800, MHT200-300");
  Manager()->AddRegionSelection("Njets6-7, HT500-800, MHT300-450");//hi
  Manager()->AddRegionSelection("Njets6-7, HT500-800, MHT>450");
  Manager()->AddRegionSelection("Njets6-7, HT800-1000, MHT200-300");
  Manager()->AddRegionSelection("Njets6-7, HT800-1000, MHT300-450");
  Manager()->AddRegionSelection("Njets6-7, HT800-1000, MHT>450");
  Manager()->AddRegionSelection("Njets6-7, HT1000-1250, MHT200-300");
  Manager()->AddRegionSelection("Njets6-7, HT1000-1250, MHT300-450");
  Manager()->AddRegionSelection("Njets6-7, HT1000-1250, MHT>450");
  Manager()->AddRegionSelection("Njets6-7, HT1250-1500, MHT200-300");
  Manager()->AddRegionSelection("Njets6-7, HT1250-1500, MHT300-450");
  Manager()->AddRegionSelection("Njets6-7, HT1250-1500, MHT>450");
  Manager()->AddRegionSelection("Njets6-7, HT>1500, MHT200-300");
  Manager()->AddRegionSelection("Njets6-7, HT>1500, MHT>300");
  Manager()->AddRegionSelection("Njets>7, HT500-800, MHT>200");
  Manager()->AddRegionSelection("Njets>7, HT800-1000, MHT>200");
  Manager()->AddRegionSelection("Njets>7, HT1000-1250, MHT>200");
  Manager()->AddRegionSelection("Njets>7, HT1250-1500, MHT>200");
  Manager()->AddRegionSelection("Njets>7, HT>1500, MHT>200");

  //Declare the baseline selection cuts
  Manager()->AddCut("No Lepton");
  Manager()->AddCut("Njets>2");
  Manager()->AddCut("HT>500");
  Manager()->AddCut("MHT>200");
  Manager()->AddCut("MinDeltaPhi");


  
  //Declare the SR-defining cuts
  string SR_Njets3to5[] = 
    {
      "Njets3-5, HT500-800, MHT200-300",
      "Njets3-5, HT500-800, MHT300-450",
      "Njets3-5, HT500-800, MHT450-600",
      "Njets3-5, HT500-800, MHT>600",
      "Njets3-5, HT800-1000, MHT200-300",
      "Njets3-5, HT800-1000, MHT300-450",
      "Njets3-5, HT800-1000, MHT450-600",
      "Njets3-5, HT800-1000, MHT>600",
      "Njets3-5, HT1000-1250, MHT200-300",
      "Njets3-5, HT1000-1250, MHT300-450",
      "Njets3-5, HT1000-1250, MHT450-600",
      "Njets3-5, HT1000-1250, MHT>600",
      "Njets3-5, HT1250-1500, MHT200-300",
      "Njets3-5, HT1250-1500, MHT300-450",
      "Njets3-5, HT1250-1500, MHT>450",
      "Njets3-5, HT>1500, MHT200-300",
      "Njets3-5, HT>1500, MHT>300"
    };
  Manager()->AddCut("NJets3-5",SR_Njets3to5);
  string SR_Njets6to7[] = 
    {
      "Njets6-7, HT500-800, MHT200-300",
      "Njets6-7, HT500-800, MHT300-450",
      "Njets6-7, HT500-800, MHT>450",
      "Njets6-7, HT800-1000, MHT200-300",
      "Njets6-7, HT800-1000, MHT300-450",
      "Njets6-7, HT800-1000, MHT>450",
      "Njets6-7, HT1000-1250, MHT200-300",
      "Njets6-7, HT1000-1250, MHT300-450",
      "Njets6-7, HT1000-1250, MHT>450",
      "Njets6-7, HT1250-1500, MHT200-300",
      "Njets6-7, HT1250-1500, MHT300-450",
      "Njets6-7, HT1250-1500, MHT>450",
      "Njets6-7, HT>1500, MHT200-300",
      "Njets6-7, HT>1500, MHT>300"
    };
  Manager()->AddCut("NJets6-7",SR_Njets6to7);
  string SR_Njets8toInf[] = 
    {
      "Njets>7, HT500-800, MHT>200",
      "Njets>7, HT800-1000, MHT>200",
      "Njets>7, HT1000-1250, MHT>200",
      "Njets>7, HT1250-1500, MHT>200",
      "Njets>7, HT>1500, MHT>200"
    };
  Manager()->AddCut("NJets>7",SR_Njets8toInf);

  string SR_HT500to800[] = 
    {
      "Njets3-5, HT500-800, MHT200-300",
      "Njets3-5, HT500-800, MHT300-450",
      "Njets3-5, HT500-800, MHT450-600",
      "Njets3-5, HT500-800, MHT>600",
      "Njets6-7, HT500-800, MHT200-300",
      "Njets6-7, HT500-800, MHT300-450",
      "Njets6-7, HT500-800, MHT>450",
      "Njets>7, HT500-800, MHT>200"
    };
  Manager()->AddCut("HT500-800",SR_HT500to800);
  string SR_HT800to1000[] = 
    {
      "Njets3-5, HT800-1000, MHT200-300",
      "Njets3-5, HT800-1000, MHT300-450",
      "Njets3-5, HT800-1000, MHT450-600",
      "Njets3-5, HT800-1000, MHT>600",
      "Njets6-7, HT800-1000, MHT200-300",
      "Njets6-7, HT800-1000, MHT300-450",
      "Njets6-7, HT800-1000, MHT>450",
      "Njets>7, HT800-1000, MHT>200"
    };
  Manager()->AddCut("HT800-1000", SR_HT800to1000);
  string SR_HT1000to1250[] = 
    {
      "Njets3-5, HT1000-1250, MHT200-300",
      "Njets3-5, HT1000-1250, MHT300-450",
      "Njets3-5, HT1000-1250, MHT450-600",
      "Njets3-5, HT1000-1250, MHT>600",
      "Njets6-7, HT1000-1250, MHT200-300",
      "Njets6-7, HT1000-1250, MHT300-450",
      "Njets6-7, HT1000-1250, MHT>450",
      "Njets>7, HT1000-1250, MHT>200"
    };
  Manager()->AddCut("HT1000-1250", SR_HT1000to1250);
  string SR_HT1250to1500[] = 
    {
      "Njets3-5, HT1250-1500, MHT200-300",
      "Njets3-5, HT1250-1500, MHT300-450",
      "Njets3-5, HT1250-1500, MHT>450",
      "Njets6-7, HT1250-1500, MHT200-300",
      "Njets6-7, HT1250-1500, MHT300-450",
      "Njets6-7, HT1250-1500, MHT>450",
      "Njets>7, HT1250-1500, MHT>200"
    };
  Manager()->AddCut("HT1250-1500", SR_HT1250to1500);
  string SR_HT1500toInf[] = 
    {
      "Njets3-5, HT>1500, MHT200-300",
      "Njets3-5, HT>1500, MHT>300",
      "Njets6-7, HT>1500, MHT200-300",
      "Njets6-7, HT>1500, MHT>300",
      "Njets>7, HT>1500, MHT>200"
    };
  Manager()->AddCut("HT>1500", SR_HT1500toInf);

  string SR_MHT200to300[] = 
    {
      "Njets3-5, HT500-800, MHT200-300",
      "Njets3-5, HT800-1000, MHT200-300",
      "Njets3-5, HT1000-1250, MHT200-300",
      "Njets3-5, HT1250-1500, MHT200-300",
      "Njets3-5, HT>1500, MHT200-300",
      "Njets6-7, HT500-800, MHT200-300",
      "Njets6-7, HT800-1000, MHT200-300",
      "Njets6-7, HT1000-1250, MHT200-300",
      "Njets6-7, HT1250-1500, MHT200-300",
      "Njets6-7, HT>1500, MHT200-300"
    };
  Manager()->AddCut("MHT200-300",SR_MHT200to300);

  string SR_MHT300to450[] = 
    {
      "Njets3-5, HT500-800, MHT300-450",
      "Njets3-5, HT800-1000, MHT300-450",
      "Njets3-5, HT1000-1250, MHT300-450",
      "Njets3-5, HT1250-1500, MHT300-450",
      "Njets6-7, HT500-800, MHT300-450",
      "Njets6-7, HT800-1000, MHT300-450",
      "Njets6-7, HT1000-1250, MHT300-450",
      "Njets6-7, HT1250-1500, MHT300-450"
    };
  Manager()->AddCut("MHT300-450",SR_MHT300to450);

  string SR_MHT450to600[] = 
    {
      "Njets3-5, HT500-800, MHT450-600",
      "Njets3-5, HT800-1000, MHT450-600",
      "Njets3-5, HT1000-1250, MHT450-600"
    };
  Manager()->AddCut("MHT450-600",SR_MHT450to600);

  string SR_MHT600toInf[] = 
    {
      "Njets3-5, HT500-800, MHT>600",
      "Njets3-5, HT800-1000, MHT>600",
      "Njets3-5, HT1000-1250, MHT>600"
    };
  Manager()->AddCut("MHT>600",SR_MHT600toInf);

  string SR_MHT450toInf[] = 
    {
      "Njets3-5, HT1250-1500, MHT>450",
      "Njets6-7, HT500-800, MHT>450",
      "Njets6-7, HT800-1000, MHT>450",
      "Njets6-7, HT1000-1250, MHT>450",
      "Njets6-7, HT1250-1500, MHT>450",
    };
  Manager()->AddCut("MHT>450", SR_MHT450toInf);

  string SR_MHT300toInf[] = 
    {
      "Njets3-5, HT>1500, MHT>300",
      "Njets6-7, HT>1500, MHT>300"
    };
  Manager()->AddCut("MHT>300", SR_MHT300toInf);

  string SR_MHT200toInf[] = 
    {
      "Njets>7, HT500-800, MHT>200",
      "Njets>7, HT800-1000, MHT>200",
      "Njets>7, HT1000-1250, MHT>200",
      "Njets>7, HT1250-1500, MHT>200",
      "Njets>7, HT>1500, MHT>200"      
    };
  Manager()->AddCut("MHT>200again", SR_MHT200toInf);



  //histogram
  Manager()->AddHisto("NJets_METCleaning",16,-0.5,15.5);
  Manager()->AddHisto("NJets_NoLepton",16,-0.5,15.5);
  Manager()->AddHisto("NJets_NJets>2",16,-0.5,15.5);
  Manager()->AddHisto("NJets_HT>500",16,-0.5,15.5);
  Manager()->AddHisto("NJets_MHT>200",16,-0.5,15.5);
  Manager()->AddHisto("NJets_MinDeltaPhi",16,-0.5,15.5);

  Manager()->AddHisto("HT_METCleaning",40,0,4000);
  Manager()->AddHisto("HT_NoLepton",40,0,4000);
  Manager()->AddHisto("HT_NJets>2",40,0,4000);
  Manager()->AddHisto("HT_HT>500",40,0,4000);
  Manager()->AddHisto("HT_MHT>200",40,0,4000);
  Manager()->AddHisto("HT_MinDeltaPhi",40,0,4000);

  Manager()->AddHisto("MHT_METCleaning",30,0,1500);
  Manager()->AddHisto("MHT_NoLepton",30,0,1500);
  Manager()->AddHisto("MHT_NJets>2",30,0,1500);
  Manager()->AddHisto("MHT_HT>500",30,0,1500);
  Manager()->AddHisto("MHT_MHT>200",30,0,1500);
  Manager()->AddHisto("MHT_MinDeltaPhi",30,0,1500);



  Manager()->AddHisto("HT_BL+NJets>7",40,0,4000);
  Manager()->AddHisto("NJets_BL+HT>1250",16,-0.5,15.5);

  cout << "END   Initialization" << endl;
  
  return true;
}

// ==========================================================
// Finalize ==================================================                  
// function called one time at the end of the analysis =======
// ==========================================================
void cms_sus_13_012::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  cout << "not really doing anything"<<endl;//could save histos here, where's this done?
  cout << "END   Finalization" << endl;
  return;
}


// ====================================================
// Execute =============================================
// function called each time one event is read =========
// ====================================================
bool cms_sus_13_012::Execute(SampleFormat& sample, const EventFormat& event)
{
  double JEscale = 1;
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
    {
      INFO << "Found one event with a zero weight. Skipping...\n";
      return false;
    }
  Manager()->InitializeForNewEvent(myEventWeight);

  if (event.rec()!=0)
    {
      // ==========================================
      // Define collections of objects =============
    // ==========================================

    // =====first declare the empty containers:=====
    vector<const RecLeptonFormat*> isoElectron, isoMuon;
    vector<const RecJetFormat*> looseJet, tightJet;


     // =====fill the electrons container:=====
    for(unsigned int e=0; e<event.rec()->electrons().size(); e++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[e]);
      double pt = CurrentElectron->momentum().Pt();
      if(!(pt>10)) continue;
      double eta = CurrentElectron->momentum().Eta();
      if(!(fabs(eta)<2.4)) continue;
      double sumpt = calcSumPt(CurrentElectron, 0.3);
      if(!(sumpt/pt < 0.2)) continue;
      isoElectron.push_back(CurrentElectron);
    }

    // =====fill the muons container:=====
    for(unsigned int m=0; m<event.rec()->muons().size(); m++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[m]);
      double pt = CurrentMuon->momentum().Pt();
      if(!(pt>10)) continue;
      double eta = CurrentMuon->momentum().Eta();
      if(!(fabs(eta)<2.4)) continue;
      double sumpt = calcSumPt(CurrentMuon, 0.4);
      if(!(sumpt/pt < 0.15)) continue;
      isoMuon.push_back(CurrentMuon);
    }

    // =====fill the jet containers and order=====
    for(unsigned int j=0; j<event.rec()->jets().size(); j++)
    {
      const RecJetFormat *CurrentJet = &(event.rec()->jets()[j]);
      double pt = JEscale*CurrentJet->momentum().Pt();
      double eta = CurrentJet->momentum().Eta();
      if(!(pt > 30 && fabs(eta) < 5))continue;
      looseJet.push_back(CurrentJet);
      if(!(pt>50. && fabs(eta) < 2.5))continue;
      tightJet.push_back(CurrentJet);
    }
    SORTER->sort(looseJet);
    SORTER->sort(tightJet);

    // =====Get the missing ET=====
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();

    // =====Calculate the HT=====
    double HT = 0;
    for(unsigned int j = 0; j < tightJet.size(); j++)
      {
	HT += JEscale*tightJet[j]->momentum().Pt();
      }

    // =====Calculate the missing HT=====
    double MHT = 0;
    MALorentzVector MHT_vec = MALorentzVector();
    MALorentzVector CurrentJet;
    for(unsigned int j = 0; j < looseJet.size(); j++)
      {
	CurrentJet.SetPtEtaPhiE
	  (looseJet[j]->momentum().Pt()*JEscale, looseJet[j]->momentum().Eta(), 
	   looseJet[j]->momentum().Phi(), looseJet[j]->momentum().E()*JEscale);
	MHT_vec -= CurrentJet;
      }
    MHT = MHT_vec.Pt();
    int NJets = tightJet.size();


    // ==========================================
    // Apply the "baseline selection" cuts =======
    // ==========================================

  
    // =====Before Any Cuts=====
    Manager()->FillHisto("NJets_METCleaning",      NJets);
    Manager()->FillHisto("HT_METCleaning",            HT);
    Manager()->FillHisto("MHT_METCleaning",          MHT);

    // =====Apply no-lepton cut========
    if(!Manager()->ApplyCut((isoElectron.size()+isoMuon.size() == 0),"No Lepton")) return true;
    Manager()->FillHisto("NJets_NoLepton",         NJets);
    Manager()->FillHisto("HT_NoLepton",               HT);
    Manager()->FillHisto("MHT_NoLepton",             MHT);

    // =====Apply NJets jut============
    if(!Manager()->ApplyCut((tightJet.size() > 2),"Njets>2")) return true; 
    Manager()->FillHisto("NJets_NJets>2",          NJets);
    Manager()->FillHisto("HT_NJets>2",                HT);
    Manager()->FillHisto("MHT_NJets>2",              MHT);

    // =====Apply HT500 cut============
    if(!Manager()->ApplyCut((HT > 500),"HT>500")) return true;
    Manager()->FillHisto("NJets_HT>500",           NJets);
    Manager()->FillHisto("HT_HT>500",                 HT);
    Manager()->FillHisto("MHT_HT>500",               MHT);

    // =====Apply MHT200 cut===========
    if(!Manager()->ApplyCut((MHT > 200),"MHT>200")) return true;
    Manager()->FillHisto("NJets_MHT>200",          NJets);
    Manager()->FillHisto("HT_MHT>200",                HT);
    Manager()->FillHisto("MHT_MHT>200",              MHT);

    // =====Calculate the deltaPhi(jet(1,2,3), MHT)=====
    MALorentzVector jet1 = MALorentzVector();
    jet1.SetPtEtaPhiE
      (tightJet[0]->momentum().Pt(), tightJet[0]->momentum().Eta(), 
       tightJet[0]->momentum().Phi(), tightJet[0]->momentum().E());
    MALorentzVector jet2 = MALorentzVector();
    jet2.SetPtEtaPhiE
      (tightJet[1]->momentum().Pt(), tightJet[1]->momentum().Eta(), 
       tightJet[1]->momentum().Phi(), tightJet[1]->momentum().E());
    MALorentzVector jet3 = MALorentzVector();
    jet3.SetPtEtaPhiE
      (tightJet[2]->momentum().Pt(), tightJet[2]->momentum().Eta(), 
       tightJet[2]->momentum().Phi(), tightJet[2]->momentum().E());
    double dPhi1 = fabs(MHT_vec.DeltaPhi(jet1));
    double dPhi2 = fabs(MHT_vec.DeltaPhi(jet2));
    double dPhi3 = fabs(MHT_vec.DeltaPhi(jet3));

    // =====Apply min dPhi cut======
    if(!Manager()->ApplyCut( dPhi1>0.5 && dPhi2>0.5 && dPhi3>0.3,"MinDeltaPhi")) return true;
    Manager()->FillHisto("NJets_MinDeltaPhi",          NJets);
    Manager()->FillHisto("HT_MinDeltaPhi",                HT);
    Manager()->FillHisto("MHT_MinDeltaPhi",              MHT);



    // ==========================================
    // Fill Histograms for extra checking =======
    // ==========================================
    if(HT>1250) Manager()->FillHisto("NJets_BL+HT>1250",  NJets);
    if(NJets>7) Manager()->FillHisto("HT_BL+NJets>7",        HT);


    
    // ==========================================
    // Apply the Signal Region - dependent cuts =======
    // ==========================================
    Manager()->ApplyCut(3 <= NJets && NJets <=5, "NJets3-5");
    Manager()->ApplyCut(6 <= NJets && NJets <=7, "NJets6-7");
    Manager()->ApplyCut(8 <= NJets, "NJets>7");
    Manager()->ApplyCut(500 <= HT && HT < 800, "HT500-800");
    Manager()->ApplyCut(800 <= HT && HT < 1000, "HT800-1000");
    Manager()->ApplyCut(1000 <= HT && HT < 1250, "HT1000-1250");
    Manager()->ApplyCut(1250 <= HT && HT < 1500, "HT1250-1500");
    Manager()->ApplyCut(1500 <= HT, "HT>1500");
    Manager()->ApplyCut(200 <= MHT, "MHT>200again");
    Manager()->ApplyCut(200 <= MHT && MHT < 300, "MHT200-300");
    Manager()->ApplyCut(300 <= MHT, "MHT>300");
    Manager()->ApplyCut(300 <= MHT && MHT < 450, "MHT300-450");
    Manager()->ApplyCut(450 <= MHT, "MHT>450");
    Manager()->ApplyCut(450 <= MHT && MHT < 600, "MHT450-600");
    Manager()->ApplyCut(600 <= MHT, "MHT>600");

    // =====finished=====
    return true;
  }
}

