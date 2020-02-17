#include "SampleAnalyzer/User/Analyzer/cms_sus_14_001_monojet.h"
using namespace MA5;
using namespace std;



// Following function returns sum of pT of tracks inside a given isolation cone
double getIsoSumPt(const RecLeptonFormat* mylepton, double coneSize)
{
  double sumPt_ = 0;
  for(unsigned int c=0; c<mylepton->isolCones().size(); c++)
    {
      if(!(fabs(mylepton->isolCones()[c].deltaR() - coneSize)<0.0001)) continue;
      sumPt_ = mylepton->isolCones()[c].sumPT();
    }
  return sumPt_;
}


// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_sus_14_001_monojet::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  cout << "========================================\n";
  cout << "Compressed stop search in monojet channel:\n";
  cout << "CMS-SUS-14-001 (monojet), arXiv:1503.08037 \n";
  cout << "Written with MA5 version v1.1.11_patch1b\n";
  cout << "Authors: Shubham Pandey, Seema Sharma \n";
  cout << "Contact e-mails: shubham.pandey@students.iiserpune.ac.in, seema.sharma@cern.ch \n";
  cout << "DOI: xx.yyyy/zzz\n";
  cout << "========================================\n";

  cout << "BEGIN Initialization" << endl;

  //-----------------------------------------------------------------------------
  // Declare 7 search regions used in analysis
  //-----------------------------------------------------------------------------
  cout << "Declaring seven search regions: " << endl;
  cout <<"pT(jet1) > 250 GeV \n" << "pT(jet1) > 300 GeV \n"
       <<"pT(jet1) > 350 GeV \n" << "pT(jet1) > 400 GeV \n"
       <<"pT(jet1) > 450 GeV \n" << "pT(jet1) > 500 GeV \n"
       <<"pT(jet1) > 550 GeV \n"
       << endl;

  Manager()->AddRegionSelection("pT(j1) Greater than 250");
  Manager()->AddRegionSelection("pT(j1) Greater than 300");
  Manager()->AddRegionSelection("pT(j1) Greater than 350");
  Manager()->AddRegionSelection("pT(j1) Greater than 400");
  Manager()->AddRegionSelection("pT(j1) Greater than 450");
  Manager()->AddRegionSelection("pT(j1) Greater than 500");
  Manager()->AddRegionSelection("pT(j1) Greater than 550");
  

  //-----------------------------------------------------------------------------
  // Declare Baseline selection cuts common to all search regions
  //-----------------------------------------------------------------------------
  cout << "Declaring baseline selections common to all search regions \n"
       << "(i)   MET > 200 GeV \n"    << "(ii)  pT leading jet (pT(j1)) > 110 GeV \n"
       << "(iii) No. of jets < 3 \n" << "(iv)  deltaPhi (jet1, jet2) < 2.5 \n"
       << "(v)   Veto events with isolated muons or electrons \n"
       << "(vi)  Veto events with a tau lepton \n"
       << "(vii) MET > 250 GeV to define search regions \n"
       << endl;

  Manager()->AddCut("EventCleaning");
  Manager()->AddCut("MET>200");
  Manager()->AddCut("NoisyEvents");
  Manager()->AddCut("pT(j1)>110");
  Manager()->AddCut("Njets<3");
  Manager()->AddCut("delphi<2.5");
  Manager()->AddCut("LeptonVeto");
  Manager()->AddCut("TauVeto");
  Manager()->AddCut("MET>250");
  
  // Declare the SR-defining cuts
  string SR_pTj1gt250[] = {"pT(j1) Greater than 250"};
  string SR_pTj1gt300[] = {"pT(j1) Greater than 300"};
  string SR_pTj1gt350[] = {"pT(j1) Greater than 350"};
  string SR_pTj1gt400[] = {"pT(j1) Greater than 400"};
  string SR_pTj1gt450[] = {"pT(j1) Greater than 450"};
  string SR_pTj1gt500[] = {"pT(j1) Greater than 500"};
  string SR_pTj1gt550[] = {"pT(j1) Greater than 550"};

  //Declare Selection region cuts
  Manager()->AddCut("pT(j1)>250", SR_pTj1gt250);
  Manager()->AddCut("pT(j1)>300", SR_pTj1gt300);
  Manager()->AddCut("pT(j1)>350", SR_pTj1gt350);
  Manager()->AddCut("pT(j1)>400", SR_pTj1gt400);
  Manager()->AddCut("pT(j1)>450", SR_pTj1gt450);
  Manager()->AddCut("pT(j1)>500", SR_pTj1gt500);
  Manager()->AddCut("pT(j1)>550", SR_pTj1gt550);


  //======Declare histograms=====
  Manager()->AddHisto("MET_EventCleaning",50,0,1000);
  Manager()->AddHisto("MET_MET200",50,0,1000);
  Manager()->AddHisto("MET_pTj1110",50,0,1000);
  Manager()->AddHisto("MET_NJetsLT3",50,0,1000);
  Manager()->AddHisto("MET_delphiLT2.5",50,0,1000);
  Manager()->AddHisto("MET_LeptonVeto",50,0,1000);
  Manager()->AddHisto("MET_TauVeto",40,0,1000);

  Manager()->AddHisto("MET_MET250_pTj1250",40,0,1000);
  Manager()->AddHisto("Njets_MET250_pTj1250",10,0,10);
  Manager()->AddHisto("Ptj1_MET250_pTj1250",40,0,1000);
  Manager()->AddHisto("Ptj2_MET250_pTj1250",40,0,1000);
  Manager()->AddHisto("Phij1_MET250_pTj1250",80,-4.0,4.0);
  Manager()->AddHisto("Phij2_MET250_pTj1250",80,-4.0,4.0);
  Manager()->AddHisto("Etaj1_MET250_pTj1250",36,-3.6,3.6);
  Manager()->AddHisto("Etaj2_MET250_pTj1250",52,-5.2,5.2);
  Manager()->AddHisto("dPhi_Jet1_Jet2_MET250_pTj1250",35,0,3.5);

  cout << "END   Initialization" << endl;
  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_sus_14_001_monojet::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  cout << "END   Finalization" << endl;

  return;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_sus_14_001_monojet::Execute(SampleFormat& sample, const EventFormat& event)
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
      vector<const RecTauFormat*> isoTau;
      vector<const RecJetFormat*> tightjets, loosejets;

      // =====fill the electrons container:=====
      for(unsigned int e=0; e<event.rec()->electrons().size(); e++)
	{
	  const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[e]);
	  double pt = CurrentElectron->momentum().Pt();
	  if(!(pt>10)) continue;
	  double eta = CurrentElectron->momentum().Eta();
	  if(!( (fabs(eta)<1.44) || (fabs(eta)>1.56 && fabs(eta)<2.5) ) ) continue;
	  double sumpt = getIsoSumPt(CurrentElectron, 0.4);
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
	  double sumpt = getIsoSumPt(CurrentMuon, 0.4);
	  if(!(sumpt/pt < 0.2)) continue;
	  isoMuon.push_back(CurrentMuon);
	}

      
      // =====fill the tau container:=====
      for(unsigned int m=0; m<event.rec()->taus().size(); m++)
	{
	  const RecTauFormat *CurrentTau = &(event.rec()->taus()[m]);
	  double pt = CurrentTau->momentum().Pt();
	  if(!(pt>20)) continue;
	  double eta = CurrentTau->momentum().Eta();
	  if(!(fabs(eta)<2.3)) continue;
	  isoTau.push_back(CurrentTau);
	}
      
      
      // =====fill the jet containers and order=====
      for(unsigned int j=0; j<event.rec()->jets().size(); j++)
	{
	  const RecJetFormat *CurrentJet = &(event.rec()->jets()[j]);
	  double pt = JEscale*CurrentJet->momentum().Pt();
	  double eta = CurrentJet->momentum().Eta();
	  if(!(pt > 60 && fabs(eta) < 4.5))continue;
	  loosejets.push_back(CurrentJet);
	  if(!(pt > 110 && fabs(eta) < 2.4))continue;
	  tightjets.push_back(CurrentJet);
	}
      SORTER->sort(tightjets);
      SORTER->sort(loosejets);
      
      //=====Get the missing ET=====
      MALorentzVector pTmiss = event.rec()->MET().momentum();
      double MET = pTmiss.Pt();

      //=====Get pT of leading jet (j1) ======
      double pT_tightjet = 0;
      if(tightjets.size() > 0){
	pT_tightjet = tightjets[0]->momentum().Pt(); 
      }

      // =====Get Number of looser jets (Njets)===
      int Njets = loosejets.size();

      // =======Apply EventCleaning cut (does nothing) =====
      if(!Manager()->ApplyCut((MET > 0.0), "EventCleaning")) return true;
      Manager()->FillHisto("MET_EventCleaning", MET);      

      // =======Apply MET(or Missing pT) > 200 GeV cut=====
      if(!Manager()->ApplyCut((MET > 200), "MET>200")) return true; 
      Manager()->FillHisto("MET_MET200", MET);
      
      // ======Apply NoisyEvents Cut (does nothing) ===========
      if(!Manager()->ApplyCut((MET > 0.0), "NoisyEvents")) return true;

      // ======pT of leading tight jet > 110 GeV=======
      if(!Manager()->ApplyCut((pT_tightjet > 110), "pT(j1)>110")) return true;
      Manager()->FillHisto("MET_pTj1110", MET);

      // =====Apply NJets < 3 cut =======
      if(!Manager()->ApplyCut((loosejets.size() < 3), "Njets<3")) return true;
      Manager()->FillHisto("MET_NJetsLT3", MET);

      // =====Calculate deltaPhi between two jets with highest pT ===
      float delphi = 0.0;
      if(Njets > 1)
	delphi = fabs(loosejets[0]->momentum().DeltaPhi(loosejets[1]->momentum()));
      
      // =========Apply dPhi(j1,j2) < 2.5 cut ==========
      if(!Manager()->ApplyCut((delphi < 2.5), "delphi<2.5")) return true;
      Manager()->FillHisto("MET_delphiLT2.5", MET);


      // =======Apply electron or muon veto =========
      int LeptonSize = isoElectron.size() + isoMuon.size();
      if(!Manager()->ApplyCut((LeptonSize == 0), "LeptonVeto")) return true;
      Manager()->FillHisto("MET_LeptonVeto", MET);
      
      // =======Apply tau veto =========
      if(!Manager()->ApplyCut((isoTau.size() == 0), "TauVeto")) return true;
      Manager()->FillHisto("MET_TauVeto", MET);

      
      // =======Apply MET(or Missing pT) > 250 GeV cut=====
      // ==== common to all search regions =====
      if(!Manager()->ApplyCut((MET > 250), "MET>250")) return true; 
      
      //===================================
      // Apply the signal region cut ======
      //===================================

      //=== Fill some histograms corresponding to first search region
      if(pT_tightjet > 250) {
	Manager()->FillHisto("MET_MET250_pTj1250",MET);
	Manager()->FillHisto("Njets_MET250_pTj1250",Njets);
	Manager()->FillHisto("Ptj1_MET250_pTj1250", loosejets[0]->momentum().Pt());
	Manager()->FillHisto("Phij1_MET250_pTj1250", loosejets[0]->momentum().Phi());
	Manager()->FillHisto("Etaj1_MET250_pTj1250", loosejets[0]->momentum().Eta());
	if(Njets > 1) {
	  Manager()->FillHisto("Ptj2_MET250_pTj1250", loosejets[1]->momentum().Pt());
	  Manager()->FillHisto("Phij2_MET250_pTj1250", loosejets[1]->momentum().Phi());
	  Manager()->FillHisto("Etaj2_MET250_pTj1250", loosejets[1]->momentum().Eta());
	  Manager()->FillHisto("dPhi_Jet1_Jet2_MET250_pTj1250", delphi);
	}
      }

      // Apply search region selections (statistically non-exclusive)
      Manager()->ApplyCut((pT_tightjet > 250), "pT(j1)>250");
      Manager()->ApplyCut((pT_tightjet > 300), "pT(j1)>300");
      Manager()->ApplyCut((pT_tightjet > 350), "pT(j1)>350");
      Manager()->ApplyCut((pT_tightjet > 400), "pT(j1)>400");
      Manager()->ApplyCut((pT_tightjet > 450), "pT(j1)>450");
      Manager()->ApplyCut((pT_tightjet > 500), "pT(j1)>500");
      Manager()->ApplyCut((pT_tightjet > 550), "pT(j1)>550");
      
      //===================
      // Finish ==========
      //==================
    }

  return true;
}

