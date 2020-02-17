#include "SampleAnalyzer/User/Analyzer/cms_b2g_12_022.h"
#include <TCanvas.h>

using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_b2g_12_022::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: CMS-B2G-12-022                <>" << endmsg;
  INFO << "        <>              (Monotops)                    <>" << endmsg;
  INFO << "        <>    Recasted by: J. Guo, E. Conte & B. Fuks <>" << endmsg;
  INFO << "        <>    Contact: Jun.Guo@iphc.cnrs.fr           <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.3             <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/ <>" << endmsg;
  INFO << "        <>    /PublicAnalysisDatabase                 <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  // This analysis has one signal region

  Manager()->AddRegionSelection("S0b");
  Manager()->AddRegionSelection("S1b");

  // initialize variables, histos

  // Signal regions cuts
  Manager()->AddCut("Lepton veto");              // 1.
  Manager()->AddCut("Jet 1");                    // 2.
  Manager()->AddCut("Jet 2");                    // 3.
  Manager()->AddCut("Jet 3");                    // 4.
  Manager()->AddCut("Veto Jet 4");               // 5.
  Manager()->AddCut("M3j<250");                  // 6.
  Manager()->AddCut("MET>250.");                 // 7.
  Manager()->AddCut("MET>350.");                 // 7.
  Manager()->AddCut("0 b-tag","S0b");            // 8.
  Manager()->AddCut("1 b-tag","S1b");            // 9.

  return true;
}

// Finalize
// function called one time at the end of the analysis
void cms_b2g_12_022::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

bool cms_b2g_12_022::Execute(SampleFormat& sample, const EventFormat& event)
{
  // unchange -> initialization of the weight
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
  {
    //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
    return false;
  }
  Manager()->InitializeForNewEvent(myEventWeight);

  // The loop start
  if (event.rec()==0) return true;
  // Defining the containers
  vector<const RecJetFormat*> SignalJets,SignalBJets;
  vector<const RecLeptonFormat*>SignalMuons,SignalElectrons;

  // The MET
  MALorentzVector pTmiss = event.rec()->MET().momentum();
  double MET = pTmiss.Pt();

  //jets with pt>35, |eta| <2.4
  unsigned int nb=0;
  for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++)
  {
    const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
    if ( CurrentJet->pt() > 35.0 && fabs(CurrentJet->eta()<2.4))
    {
      SignalJets.push_back(CurrentJet);
      if(CurrentJet->btag()) nb++;
    }
  }
  SORTER->sort(SignalJets, PTordering);

  // Electron with pt > 20, |eta|<2.5 (excluding 1.44<|eta|<1.57) and Irel < 0.2
  for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++)
  {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ie]);
      double eta  = fabs(CurrentElectron->eta());
      double pt   = CurrentElectron->pt();
      double Irel = PHYSICS->Isol->tracker->sumIsolation(CurrentElectron,event.rec(),0.3,0.)/pt;
      if(CurrentElectron->pt()>20.0 && eta<2.5 && !(eta<1.57 && eta>1.44) && Irel<0.2)
        SignalElectrons.push_back(CurrentElectron);
  }

  // Muons with pT>10 |eta|<2.4
  for(unsigned int im=0; im<event.rec()->muons().size(); im++)
  {
    const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[im]);
    double pt   = CurrentMuon->pt();
    double eta  = fabs(CurrentMuon->eta());
    double Irel = PHYSICS->Isol->tracker->sumIsolation(CurrentMuon,event.rec(),0.4,0.)/pt;
    if(pt>10. && eta<2.4 && Irel<0.2)
      SignalMuons.push_back(CurrentMuon);
  }

  // The selections.

  // Lepton veto
  if(!Manager()->ApplyCut(SignalMuons.size()==0 && SignalElectrons.size()==0,"Lepton veto"))
    return true;

  // Jet 1 selection
  if(!Manager()->ApplyCut(SignalJets.size()>0 && SignalJets[0]->pt()>60.,"Jet 1"))
    return true;

  // Jet 2 selection
  if(!Manager()->ApplyCut(SignalJets.size()>1 && SignalJets[1]->pt()>60.,"Jet 2"))
    return true;

  // Jet 3 selection
  if(!Manager()->ApplyCut(SignalJets.size()>2 && SignalJets[2]->pt()>40.,"Jet 3"))
    return true;

  // Veto jet 4
  if(!Manager()->ApplyCut(SignalJets.size()==3,"Veto Jet 4")) return true;

  // Invariant mass of the top system
  MALorentzVector ljets = SignalJets[0]->momentum()+SignalJets[1]->momentum()+SignalJets[2]->momentum();
  double inv_mass = ljets.M();
  if(!Manager()->ApplyCut(inv_mass<250.,"M3j<250")) return true;

  // MET cut
  if(!Manager()->ApplyCut(MET>250,"MET>250.")) return true;
  if(!Manager()->ApplyCut(MET>350,"MET>350.")) return true;

  // btags
  if(!Manager()->ApplyCut(nb==0,"0 b-tag")) return true;
  if(!Manager()->ApplyCut(nb==1,"1 b-tag")) return true;

  return true;

}

