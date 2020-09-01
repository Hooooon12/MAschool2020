#include "SampleAnalyzer/User/Analyzer/atlas_conf_2016_086.h"
using namespace MA5;

template<typename T1, typename T2> std::vector<const T1*>
  Removal(std::vector<const T1*>&, std::vector<const T2*>&, const double &);
// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_conf_2016_086::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: atlas_conf_2016_086           <>" << endmsg;
  INFO << "        <>    DM + bbar @ 13 TeV, 13.3 fb^-1          <>" << endmsg;
  INFO << "        <>    Recasted by: M. Zumbihl and B. Fuks     <>" << endmsg;
  INFO << "        <>    Contact: fuks@lpthe.jussieu.fr          <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.6 and above   <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // =====Declare the signal regions in this analysis=====
  Manager()->AddRegionSelection("SR");

  //============= Selection cuts=================//
  Manager()->AddCut("MET > 150 GeV");
  Manager()->AddCut("Nbjets = 2");
  Manager()->AddCut("Njets = 2-3");
  Manager()->AddCut("dphijmin > 0.4");
  Manager()->AddCut("Lepton veto");
  Manager()->AddCut("Hyperbolic 2D");
  Manager()->AddCut("dRmin > 2.8");
  Manager()->AddCut("b-separation");
  Manager()->AddCut("Imb(b1, b2) > 0.5");

  //Declare histograms

  Manager()->AddHisto("Imb(b1, b2)",8,0,1);
  Manager()->AddHisto("dRmin",9,0.5,4);

  //================================================
  return true;
}

// Finalize
// function called one time at the end of the analysis
void atlas_conf_2016_086::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

bool atlas_conf_2016_086::Execute(SampleFormat& sample, const EventFormat& event)
{
  
  // Event weight
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
  {
    //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
    return false;
  }
  Manager()->InitializeForNewEvent(myEventWeight);
  // Empty event
  if (event.rec()==0) {return true;}
  // Defining the containers
  std::vector<const RecJetFormat*> SignalLightJets, SignalBJets;
  std::vector<const RecLeptonFormat*> SignalMuons, SignalElectrons;

  // Jets
  for(unsigned int ij=0; ij<event.rec()->jets().size(); ij++)
  {
    const RecJetFormat *CurrentJet = &(event.rec()->jets()[ij]);
    if ( CurrentJet->pt() > 20.0 && fabs(CurrentJet->eta())<2.8)
    {
      if(CurrentJet->btag()) SignalBJets.push_back(CurrentJet);
      else SignalLightJets.push_back(CurrentJet);
    }
  }

  // Electron with pT > 7 GeV
  for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++)
  {
    const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ie]);
    if( CurrentElectron->pt()>7. && fabs(CurrentElectron->eta())<2.47)
      SignalElectrons.push_back(CurrentElectron);
  }

  // Muons with ET > 6 GeV
  for(unsigned int im=0; im<event.rec()->muons().size(); im++)
  {
    const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[im]);
    if( CurrentMuon->et()>6. && fabs(CurrentMuon->eta())<2.7)
      SignalMuons.push_back(CurrentMuon);
  }

  // Electron-muon overlap removal
  SignalElectrons = Removal(SignalElectrons, SignalMuons, 0.05);

  // Electron-jet overlap removal
  SignalLightJets =
    PHYSICS->Isol->JetCleaning(SignalLightJets, SignalElectrons, 0.2);
  std::vector<const RecJetFormat*> SignalJets;
  for (unsigned ii=0; ii < SignalLightJets.size(); ii++)
    SignalJets.push_back(SignalLightJets[ii]);
  for (unsigned ii=0; ii < SignalBJets.size(); ii++)
    SignalJets.push_back(SignalBJets[ii]);

  // Final lepton-jet removal
  SignalElectrons = Removal(SignalElectrons, SignalJets, 0.4);
  SignalMuons = Removal(SignalMuons, SignalJets, 0.4);

  // The MET
  MALorentzVector pTmiss = event.rec()->MET().momentum();
  double MET = pTmiss.Pt();

  // Ordering of the jets
  SORTER->sort(SignalJets, PTordering);
  SORTER->sort(SignalBJets, PTordering);

  // Cut-1 - MET > 150 GeV
  if(!Manager()->ApplyCut(MET > 150,"MET > 150 GeV")) return true;

  // Cut-2 - Nb == 2
  if(!Manager()->ApplyCut(SignalBJets.size() == 2 ,"Nbjets = 2")) return true;

  // Cut-3 - 3rd jet veto
  bool condc3 = true;
  if(SignalJets.size()>2 && SignalJets[2]->pt()>60) condc3 = false;
  if(!Manager()->ApplyCut(condc3,"Njets = 2-3")) return true;

  // Cut-4 - MET alignement
  double DeltaPhiJet=99999.;
  for(unsigned int ii=0; ii<SignalJets.size();ii++)
    if(SignalJets[ii]->dphi_0_pi(pTmiss)<DeltaPhiJet)
      DeltaPhiJet=SignalJets[ii]->dphi_0_pi(pTmiss);
  if(!Manager()->ApplyCut(DeltaPhiJet>0.4,"dphijmin > 0.4")) return true;

  // Cut-5 - Lepton veto
  unsigned int nlep = SignalElectrons.size() + SignalMuons.size();
  if(!Manager()->ApplyCut( nlep == 0, "Lepton veto")) return true;

  // Cut-6 - Hyperbolic requirement on the MET and the leading jet
  double pt1   = SignalJets[0]->pt();
  double ptb1 = SignalBJets[0]->pt();
  bool cond1 = pt1 > 100.;
  bool cond2 = ptb1 > 50.;
  bool cond3 = MET > ((150.*pt1 - 11700.)/(pt1-85.));
  if(!Manager()->ApplyCut(cond1 && cond2 && cond3,"Hyperbolic 2D")) return true;

  // Cut-7 - jet angular separation
  double DRmin=99999.;
  int nj = std::min(3, int(SignalJets.size()));
  for (unsigned int i=0; i<nj; i++)
    for (unsigned int j=i+1; j<nj; j++)

      /*double y1 = SignalJets[i]->y();
      double y2 = SignalJets[j]->y();
      double eta1 = SignalJets[i]->eta();
      double eta2 = SignalJets[j]->eta();
      double DR= sqrt(pow(y1-y2,2) + pow(eta1-eta2, 2));
      if(DR<DRmin) DRmin = DR;*/

      if(SignalJets[i]->dr(SignalJets[j])<DRmin){
        DRmin=SignalJets[i]->dr(SignalJets[j]);
      }
  Manager()->FillHisto("dRmin", DRmin);
  if(!Manager()->ApplyCut(DRmin>2.8, "dRmin > 2.8")) return true;

   // Cut-8 - b-jet separation
   double deta = fabs(SignalBJets[0]->eta() - SignalBJets[1]->eta());
   double dPhi = SignalBJets[0]->dphi_0_pi(SignalBJets[1]);
   if(!Manager()->ApplyCut((deta>0.5)&&(dPhi>2.2),"b-separation")) return true;

   // Cut-9 - transverse momentum imbalance between the 2 b-jets
   double ptb2 = SignalBJets[1]->pt();
   double imb = (ptb1 - ptb2)/(ptb1 + ptb2);
   Manager()->FillHisto("Imb(b1, b2)", imb);
   if (!Manager()->ApplyCut(imb>0.5, "Imb(b1, b2) > 0.5")) return true;

   return true;
}


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

