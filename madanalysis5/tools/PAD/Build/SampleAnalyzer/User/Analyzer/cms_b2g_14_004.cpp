#include "SampleAnalyzer/User/Analyzer/cms_b2g_14_004.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_b2g_14_004::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: CMS-B2G-14-004, arXiv:1504.03198  <>" << endmsg;
  INFO << "        <>            (top pairs, single lepton)        <>" << endmsg;
  INFO << "        <>  Recasted by: B. Fuks, A. Martini            <>" << endmsg;
  INFO << "        <>  Contact: fuks@lpthe.jussieu.fr              <>" << endmsg;
  INFO << "        <>           antony.martini@uclouvain.be        <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.3                 <>" << endmsg;
  INFO << "        <>  For more information, see                   <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  // Declare all the different signal regions in the analysis
  Manager()->AddRegionSelection("control region 1");
  Manager()->AddRegionSelection("control region 2");
  Manager()->AddRegionSelection("signal region");

  // Declare all preselection cuts used in the analysis.
  Manager()->AddCut("trigger");
  Manager()->AddCut("1 candidate lepton");
  Manager()->AddCut("3+ central jets");

  string CR1_AND_SR[] = {"control region 1","signal region"};
  Manager()->AddCut("1+ b-tagged jet",CR1_AND_SR);
  Manager()->AddCut("0 b-tagged jet","control region 2");

  Manager()->AddCut("MET > 160 GeV");

  // Other cuts
  Manager()->AddCut("MT > 160 GeV");
  Manager()->AddCut("MET > 320 GeV","signal region");
  Manager()->AddCut("MT2W > 200 GeV","signal region");
  Manager()->AddCut("min dphi(MET, j1 or j2) > 1.2","signal region");


  // Declare all histograms to be produced by the analysis.
  Manager()->AddHisto("MET",8,160,480,"signal region"); // Fig.3 top left
  Manager()->AddHisto("MT",9,0,360,"signal region"); // Fig.3 top right
  Manager()->AddHisto("MT2W",8,80,400,"signal region"); // Fig.3 bottom left
  Manager()->AddHisto("min dphi(MET, j1 or j2)",8,0,3.2,"signal region"); // Fig.3 bottom right

  Manager()->AddHisto("MET after CR1 cuts",8,160,480, "control region 1"); // Fig.4 top left
  Manager()->AddHisto("MT after CR1 cuts",10,160,560, "control region 1"); // Fig.4 top right
  Manager()->AddHisto("MT2W after CR1 cuts",11,80,520, "control region 1"); // Fig.4 bottom left
  Manager()->AddHisto("min dphi(MET, j1 or j2) after CR1 cuts",16,0,3.2, "control region 1"); // Fig.4 bottom right

  Manager()->AddHisto("MET after CR2 cuts",8,160,480, "control region 2"); // Fig.5 top left
  Manager()->AddHisto("MT after CR2 cuts",10,160,560, "control region 2"); // Fig.5 top right
  Manager()->AddHisto("MT2W after CR2 cuts",11,80,520, "control region 2"); // Fig.5 bottom left
  Manager()->AddHisto("min dphi(MET, j1 or j2) after CR2 cuts",16,0,3.2, "control region 2"); // Fig.5 bottom right

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_b2g_14_004::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_b2g_14_004::Execute(SampleFormat& sample, const EventFormat& event)
{
  if (event.rec()!=0)
  {
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Book-keeping with the event weight; no need to modify this.
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

    // first declare the empty containers:
    vector<const RecLeptonFormat*>  SignalElectrons, SignalMuons, TriggerElectrons, TriggerMuons;
    vector<const RecJetFormat*> myJets;

    // fill the lepton containers
    for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ii]);
      double pt = CurrentElectron->pt();
      double abseta = fabs(CurrentElectron->eta());
      double Riso = PHYSICS->Isol->eflow->relIsolation(CurrentElectron,event.rec(),0.3,0.,IsolationEFlow::ALL_COMPONENTS);

      if(pt>30. && abseta<2.5 && !(abseta>1.44 && abseta<1.57) && Riso<0.1)
        SignalElectrons.push_back(CurrentElectron);
      if(pt>27.)
        TriggerElectrons.push_back(CurrentElectron);
    }
    for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
      double pt = CurrentMuon->pt();
      double abseta = fabs(CurrentMuon->eta());
      double Riso = PHYSICS->Isol->eflow->relIsolation(CurrentMuon,event.rec(),0.4,0.,IsolationEFlow::ALL_COMPONENTS);

      if(pt>30. && abseta<2.1 && Riso<0.12)
        SignalMuons.push_back(CurrentMuon);
      if(pt>24.)
        TriggerMuons.push_back(CurrentMuon);
    }

    // Single lepton triggers
    double ProbaToFail = 1.;

    // single electron trigger
    for(unsigned int ii=0; ii<TriggerElectrons.size(); ii++)
    {
      double pt = TriggerElectrons[ii]->pt();
      double abseta = fabs(TriggerElectrons[ii]->eta());
      double CurEff;

      if(pt < 26.) {
        if(abseta < 1.5) CurEff = 0.0;
        else CurEff = 0.03;
      } else if(pt < 28.) {
        if(abseta < 1.5) CurEff = 0.07;
        else CurEff = 0.22;
      } else if(pt < 30.) {
        if(abseta < 1.5) CurEff = 0.57;
        else CurEff = 0.52;
      } else if(pt < 32.) {
        if(abseta < 1.5) CurEff = 0.85;
        else CurEff = 0.65;
      } else if(pt < 34.) {
        if(abseta < 1.5) CurEff = 0.88;
        else CurEff = 0.70;
      } else if(pt < 36.) {
        if(abseta < 1.5) CurEff = 0.89;
        else CurEff = 0.72;
      } else if(pt < 38.) {
        if(abseta < 1.5) CurEff = 0.91;
        else CurEff = 0.74;
      } else if(pt < 40.) {
        if(abseta < 1.5) CurEff = 0.92;
        else CurEff = 0.75;
      } else if(pt < 50.) {
        if(abseta < 1.5) CurEff = 0.94;
        else CurEff = 0.77;
      } else if(pt < 60.) {
        if(abseta < 1.5) CurEff = 0.95;
        else CurEff = 0.79;
      } else if(pt < 80.) {
        if(abseta < 1.5) CurEff = 0.96;
        else CurEff = 0.79;
      } else if(pt < 100.) {
        if(abseta < 1.5) CurEff = 0.96;
        else CurEff = 0.80;
      } else if(pt < 150.) {
        if(abseta < 1.5) CurEff = 0.97;
        else CurEff = 0.82;
      } else if(pt < 200.) {
        if(abseta < 1.5) CurEff = 0.97;
        else CurEff = 0.83;
      } else {
        if(abseta < 1.5) CurEff = 0.97;
        else CurEff = 0.85;
      }
      ProbaToFail *= 1.-CurEff;
    }
    // single muon trigger
    for(unsigned int ii=0; ii<TriggerMuons.size(); ii++)
    {
      double pt = TriggerMuons[ii]->pt();
      double abseta = fabs(TriggerMuons[ii]->eta());
      double CurEff;

      if(pt < 24.) {
        if(abseta < 0.8) CurEff = 0.02;
        else if(abseta < 1.5) CurEff = 0.05;
        else CurEff = 0.10;
      } else if(pt < 26.) {
        if(abseta < 0.8) CurEff = 0.87;
        else if(abseta < 1.5) CurEff = 0.78;
        else CurEff = 0.76;
      } else if(pt < 28.) {
        if(abseta < 0.8) CurEff = 0.90;
        else if(abseta < 1.5) CurEff = 0.80;
        else CurEff = 0.78;
      } else if(pt < 30.) {
        if(abseta < 0.8) CurEff = 0.91;
        else if(abseta < 1.5) CurEff = 0.81;
        else CurEff = 0.79;
      } else if(pt < 32.) {
        if(abseta < 0.8) CurEff = 0.91;
        else if(abseta < 1.5) CurEff = 0.82;
        else CurEff = 0.80;
      } else if(pt < 34.) {
        if(abseta < 0.8) CurEff = 0.92;
        else if(abseta < 1.5) CurEff = 0.82;
        else CurEff = 0.81;
      } else if(pt < 36.) {
        if(abseta < 0.8) CurEff = 0.93;
        else if(abseta < 1.5) CurEff = 0.82;
        else CurEff = 0.81;
      } else if(pt < 38.) {
        if(abseta < 0.8) CurEff = 0.93;
        else if(abseta < 1.5) CurEff = 0.83;
        else CurEff = 0.82;
      } else if(pt < 40.) {
        if(abseta < 0.8) CurEff = 0.93;
        else if(abseta < 1.5) CurEff = 0.83;
        else CurEff = 0.82;
      } else if(pt < 50.) {
        if(abseta < 0.8) CurEff = 0.94;
        else if(abseta < 1.5) CurEff = 0.84;
        else CurEff = 0.83;
      } else if(pt < 60.) {
        if(abseta < 0.8) CurEff = 0.95;
        else if(abseta < 1.5) CurEff = 0.84;
        else CurEff = 0.83;
      } else if(pt < 80.) {
        if(abseta < 0.8) CurEff = 0.95;
        else if(abseta < 1.5) CurEff = 0.84;
        else CurEff = 0.84;
      } else if(pt < 100.) {
        if(abseta < 0.8) CurEff = 0.94;
        else if(abseta < 1.5) CurEff = 0.84;
        else CurEff =   0.84;
      } else if(pt < 150.) {
        if(abseta < 0.8) CurEff = 0.94;
        else if(abseta < 1.5) CurEff = 0.84;
        else CurEff = 0.84;
      } else if(pt < 200.) {
        if(abseta < 0.8) CurEff = 0.93;
        else if(abseta < 1.5) CurEff = 0.83;
        else CurEff = 0.82;
      } else {
        if(abseta < 0.8) CurEff = 0.92;
        else if(abseta < 1.5) CurEff = 0.83;
        else CurEff = 0.83;
      }

      ProbaToFail *= 1.-CurEff;
    }

    // update the weight for this event
    myEventWeight *= (1.-ProbaToFail);
    Manager()->SetCurrentEventWeight(myEventWeight);
    Manager()->ApplyCut(true, "trigger");

    // fill the jets container (jets need pt > 30 GeV and |eta| < 4.0)
    unsigned int Nbtag = 0;
    for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
    {
      const RecJetFormat *CurrentJet = &(event.rec()->jets()[ii]);
      double pt = CurrentJet->pt();
      double abseta = fabs(CurrentJet->eta());
      if(pt>30. && abseta<4.0)
      {
        myJets.push_back(CurrentJet);
        if(CurrentJet->btag())
          Nbtag++;
      }
    }
    SORTER->sort(myJets);
    myJets = PHYSICS->Isol->JetCleaning(myJets, SignalElectrons, 0.4);
    myJets = PHYSICS->Isol->JetCleaning(myJets, SignalMuons,     0.4);


    // missing transverse momentum:
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();

    // applying identification-only weights obtained from CMS
    double Proba0lep = 1.;
    for(unsigned int ii=0; ii<SignalElectrons.size(); ii++)
    {
      double pt = SignalElectrons[ii]->pt();
      double CurEff;

      if(pt < 30.) CurEff = 0.78;
      else if(pt < 40.) CurEff = 0.84;
      else CurEff = 0.87;

      Proba0lep *= 1.-CurEff;
    }

    for(unsigned int ii=0; ii<SignalMuons.size(); ii++)
    {
      double pt = SignalMuons[ii]->pt();
      double CurEff;

      if(pt < 200.) CurEff = 0.95;
      else if(pt < 300.) CurEff = 0.90;
      else CurEff = 0.80;

      Proba0lep *= 1.-CurEff;
    }

    myEventWeight *= (1.-Proba0lep);
    Manager()->SetCurrentEventWeight(myEventWeight);

    // exactly one isolated lepton
    if(!Manager()->ApplyCut((SignalElectrons.size() + SignalMuons.size()) == 1,
                            "1 candidate lepton"))
      return true;

    // identify THE signal lepton
    const RecLeptonFormat* SignalLepton;
    bool is_e; // true: e, false: mu
    if(SignalElectrons.size() == 1 && SignalMuons.size() == 0)
      is_e = true;
    else if(SignalElectrons.size() == 0 && SignalMuons.size() == 1)
      is_e = false;
    else
    {
      ERROR << "Again no isolated lepton found (we must have one at this stage)"
            << endmsg;
      exit(1);
    }
    if(is_e) SignalLepton = SignalElectrons[0];
    else SignalLepton = SignalMuons[0];

    // The next cut: at least 3 jets with pT > 30 GeV and |eta| < 4.0
    if(!Manager()->ApplyCut((myJets.size()>=3),"3+ central jets"))
      return true;

    // The next cut: MET > 160.
    if(!Manager()->ApplyCut((MET > 160.),"MET > 160 GeV"))
      return true;

    // b-tags
    if(!Manager()->ApplyCut(Nbtag>0,"1+ b-tagged jet"))
      return true;
    if(!Manager()->ApplyCut(Nbtag==0,"0 b-tagged jet"))
      return true;

    // MT: the transverse mass of the signal lepton and the missing pT
    double MT = SignalLepton->mt_met(pTmiss);
    double mt2w = PHYSICS->Transverse->MT2W(myJets,SignalLepton,event.rec()->MET());
    double MinDeltaPhiJetMET = min(myJets[0]->dphi_0_pi(pTmiss),
                                   myJets[1]->dphi_0_pi(pTmiss));

    // Histograms for the SR
    if(MT>160. && mt2w>200. && MinDeltaPhiJetMET>1.2)
      Manager()->FillHisto("MET",MET);
    if(MET>320. && mt2w>200. && MinDeltaPhiJetMET>1.2)
      Manager()->FillHisto("MT",MT);
    if(MT>160. && MET>320. && MinDeltaPhiJetMET>1.2)
      Manager()->FillHisto("MT2W",mt2w);
    if(MT>160. && MET>320. && mt2w>200.)
      Manager()->FillHisto("min dphi(MET, j1 or j2)", MinDeltaPhiJetMET);

    // MT cut
    if(!Manager()->ApplyCut((MT > 160.),"MT > 160 GeV"))
      return true;

    // Hisograms for the CRS
    Manager()->FillHisto("MET after CR1 cuts", MET);
    Manager()->FillHisto("MT after CR1 cuts", MT);
    Manager()->FillHisto("MT2W after CR1 cuts", mt2w);
    Manager()->FillHisto("min dphi(MET, j1 or j2) after CR1 cuts", MinDeltaPhiJetMET);

    Manager()->FillHisto("MET after CR2 cuts", MET);
    Manager()->FillHisto("MT after CR2 cuts", MT);
    Manager()->FillHisto("MT2W after CR2 cuts", mt2w);
    Manager()->FillHisto("min dphi(MET, j1 or j2) after CR2 cuts", MinDeltaPhiJetMET);

    // The last cuts
    if(!Manager()->ApplyCut((MET > 320.),"MET > 320 GeV"))
      return true;
    if(!Manager()->ApplyCut((mt2w > 200.),"MT2W > 200 GeV"))
      return true;
    if(!Manager()->ApplyCut((MinDeltaPhiJetMET>1.2),"min dphi(MET, j1 or j2) > 1.2"))
      return true;
  }

  // nothing more to do in the execute function:
  return true;

}
