#define PI 3.1415926535897932384626433832795028841971693993751

#include "SampleAnalyzer/User/Analyzer/cms_sus_13_011.h"

// IMPORTANT!
// the following include statement is analysis specific (needed for calculating
// a chi^2). It requires MINUIT libraries. Therefore, the line
// LIBFLAGS += -lMinuit
// need to be added to the Makefile of the Build/ directory before compilation.
#include "TFitter.h"


using namespace MA5;
using namespace std;

// This is analysis specific (the minimization thing for calculating
// a chi^2). This should not be there in other analyses.
// (c++ sources below, at the end of this file).
static const float PDG_TOP_MASS = 173.5;
static const float PDG_W_MASS = 80.385;
double calculateChi2(std::vector<const RecJetFormat *>);


// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_sus_13_011::Initialize(const MA5::Configuration& cfg,
const map<string,string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: CMS-SUS-13-011, arXiv:1308.1586 <>" << endmsg;
  INFO << "        <>            (stop search, single lepton)    <>" << endmsg;
  INFO << "        <>  Recasted by: B.Dumont, B.Fuks & C.Wymant  <>" << endmsg;
  INFO << "        <>  Contact: dumont@lpsc.in2p3.fr             <>" << endmsg;
  INFO << "        <>           fuks@cern.ch                     <>" << endmsg;
  INFO << "        <>           wymant@lapth.cnrs.fr             <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11            <>" << endmsg;
  INFO << "        <>  For more information, see                 <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;


  // Declare all the different signal regions in the analysis, simply giving
  // them a name and telling RSManager they exist:
  Manager()->AddRegionSelection("Stop->T+neutralino, LowDeltaM, MET>150");
  Manager()->AddRegionSelection("Stop->T+neutralino, LowDeltaM, MET>200");
  Manager()->AddRegionSelection("Stop->T+neutralino, LowDeltaM, MET>250");
  Manager()->AddRegionSelection("Stop->T+neutralino, LowDeltaM, MET>300");
  Manager()->AddRegionSelection("Stop->T+neutralino, HighDeltaM, MET>150");
  Manager()->AddRegionSelection("Stop->T+neutralino, HighDeltaM, MET>200");
  Manager()->AddRegionSelection("Stop->T+neutralino, HighDeltaM, MET>250");
  Manager()->AddRegionSelection("Stop->T+neutralino, HighDeltaM, MET>300");
  Manager()->AddRegionSelection("Stop->b+chargino, LowDeltaM, MET>100");
  Manager()->AddRegionSelection("Stop->b+chargino, LowDeltaM, MET>150");
  Manager()->AddRegionSelection("Stop->b+chargino, LowDeltaM, MET>200");
  Manager()->AddRegionSelection("Stop->b+chargino, LowDeltaM, MET>250");
  Manager()->AddRegionSelection("Stop->b+chargino, HighDeltaM, MET>100");
  Manager()->AddRegionSelection("Stop->b+chargino, HighDeltaM, MET>150");
  Manager()->AddRegionSelection("Stop->b+chargino, HighDeltaM, MET>200");
  Manager()->AddRegionSelection("Stop->b+chargino, HighDeltaM, MET>250");

  // Declare all the cuts used in the analysis.
  // Note that the order in which you declare cuts defines the order in which 
  // they appear in the cut flow table. What you want this order to be is the
  // order in which the cuts are applied. It's therefore on you to declare cuts
  // in the order that they are applied, so as to have a sensible cut flow at
  // the end.
  // Cuts are declared with RSManager's AddCut method. A cut needs a (string)
  // name, and a set of signal regions which it applies to; if the latter is not
  // specified, i.e. AddCut is called with only a name as its argument, the cut
  // is taken to apply to *all* signal regions, i.e. it's a common cut, not a
  // region-specific cut. We do this here:
  Manager()->AddCut("ISR boost factor");
  Manager()->AddCut("trigger");
  Manager()->AddCut("1+ candidate lepton");
  Manager()->AddCut("4+ central jets");
  Manager()->AddCut("MET > 50 GeV");
  Manager()->AddCut("MET > 100 GeV");
  Manager()->AddCut("1+ b-tagged jet");
  Manager()->AddCut("veto isol lepton and track");
  Manager()->AddCut("No hadronic tau");
  Manager()->AddCut("dphi(MET, j1 or j2) > 0.8");

  string SRForChi2_5Cut[] = {"Stop->T+neutralino, LowDeltaM, MET>150",
    "Stop->T+neutralino, LowDeltaM, MET>200",
    "Stop->T+neutralino, LowDeltaM, MET>250",
    "Stop->T+neutralino, LowDeltaM, MET>300",
    "Stop->T+neutralino, HighDeltaM, MET>150",
    "Stop->T+neutralino, HighDeltaM, MET>200",
    "Stop->T+neutralino, HighDeltaM, MET>250",
    "Stop->T+neutralino, HighDeltaM, MET>300"};
  Manager()->AddCut("chi^2 < 5",SRForChi2_5Cut);

  Manager()->AddCut("MT > 120 GeV");


  // Some cuts, on the other hand, apply only to some of the regions and not all
  // of them. To declare such cuts, call the method AddCut with a second
  // argument - an array of strings - with each string corresponding to the name
  // of a signal region. This is what we do next.
  // (Note that we have declared all common cuts first, then all region-specific
  // cuts afterwards; we clarify that it doesn't need to be done like this -
  // that's just the order of the cuts in the experimental analysis we're
  // implementing here.)
  string SRForMet150Cut[] = {"Stop->b+chargino, LowDeltaM, MET>150",
    "Stop->b+chargino, HighDeltaM, MET>150",
    "Stop->T+neutralino, LowDeltaM, MET>150",
    "Stop->T+neutralino, HighDeltaM, MET>150"};
  Manager()->AddCut("MET > 150 GeV",SRForMet150Cut);

  string SRForMet200Cut[] = {"Stop->b+chargino, LowDeltaM, MET>200",
    "Stop->b+chargino, HighDeltaM, MET>200",
    "Stop->T+neutralino, LowDeltaM, MET>200",
    "Stop->T+neutralino, HighDeltaM, MET>200"};
  Manager()->AddCut("MET > 200 GeV",SRForMet200Cut);

  string SRForMet250Cut[] = {"Stop->b+chargino, LowDeltaM, MET>250",
    "Stop->b+chargino, HighDeltaM, MET>250",
    "Stop->T+neutralino, LowDeltaM, MET>250",
    "Stop->T+neutralino, HighDeltaM, MET>250"};
  Manager()->AddCut("MET > 250 GeV",SRForMet250Cut);

  string SRForMet300Cut[] = {"Stop->T+neutralino, LowDeltaM, MET>300",
    "Stop->T+neutralino, HighDeltaM, MET>300"};
  Manager()->AddCut("MET > 300 GeV",SRForMet300Cut);

  string SRForMT2W200Cut[] = {"Stop->b+chargino, HighDeltaM, MET>100",
    "Stop->b+chargino, HighDeltaM, MET>150",
    "Stop->b+chargino, HighDeltaM, MET>200",
    "Stop->b+chargino, HighDeltaM, MET>250",
    "Stop->T+neutralino, HighDeltaM, MET>150",
    "Stop->T+neutralino, HighDeltaM, MET>200",
    "Stop->T+neutralino, HighDeltaM, MET>250",
    "Stop->T+neutralino, HighDeltaM, MET>300"};
  Manager()->AddCut("MT2W > 200 GeV",SRForMT2W200Cut);

  string SRForHardbjet100Cut[] = {"Stop->b+chargino, HighDeltaM, MET>100",
    "Stop->b+chargino, HighDeltaM, MET>150",
    "Stop->b+chargino, HighDeltaM, MET>200",
    "Stop->b+chargino, HighDeltaM, MET>250"};
  Manager()->AddCut("Leading b-jet pT > 100 GeV",SRForHardbjet100Cut);

  // Declare all histograms to be produced by the analysis.
  // Each histo has a name, a number of bins, a lower bound to the binning range
  // and upper bound (to be given in that order to the AddHisto method).
  // The histograms are
  // associated with all the Signal regions. Otherwise, proceed as
  // for the cuts with an extra argument that is array of string names of signal
  // regions.
  Manager()->AddHisto("MT",10,0,300); // Fig. 2a
  Manager()->AddHisto("MET",10,100,350); // Fig. 2b
  Manager()->AddHisto("MT2W",17,75,500); // Fig. 2c
  Manager()->AddHisto("chi2",20,0,20); // Fig. 2d
  Manager()->AddHisto("HTratio",25,0,1); // Fig. 2e
  Manager()->AddHisto("pT(leading b-jet)",9,30,300); // Fig. 2g
  Manager()->AddHisto("pT(l)",8,20,100); // Fig. 2i
  Manager()->AddHisto("JetMETMindeltaPhi",15,0,PI); // Fig. 2f
  Manager()->AddHisto("deltaR(l, leading b-jet)",15,0,5); // Fig. 2h
  Manager()->AddHisto("MT2W after MT>120",17,75,500); // Fig. add 12
  Manager()->AddHisto("chi2 after MT>120",20,0,20); // Fig. add 14
  Manager()->AddHisto("HTratio after MT>120",25,0,1); // Fig. add 16
  Manager()->AddHisto("JetMETMindeltaPhi after MT>120",25,0,PI); // Fig. add 17
  Manager()->AddHisto("pT(leading b-jet) after MT>120",20,0,500); // Fig. add 13
  Manager()->AddHisto("deltaR(l, leading b-jet) after MT>120",20,0,5); // Fig.
                                                                       // add 15

  return true;
}





// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_sus_13_011::Finalize(const SampleFormat& summary,
const vector<SampleFormat>& files)
{
  // Feel free to add anything here which is not in the default output

  return;
}







// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_sus_13_011::Execute(SampleFormat& sample, const EventFormat& event)
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


    // ----
    // ISR boost factor, see Appendix B of arXiv:1308.1586
    // this is very specific to this analysis
    // ----

    double ISRweight = 1.0;

    if(event.mc()!=0)
    {
        EventFormat myEvent;
        myEvent = event;

        unsigned int n = event.mc()->particles().size();
        MALorentzVector sum_stop;

        for(unsigned int i=0; i<n; i++)
        {
          MCParticleFormat* prt = &myEvent.mc()->particles()[i];
          if(prt->pdgid() == 1000006)
          { // stop
            sum_stop += prt->momentum(); 
          }
          else if(prt->pdgid() == -1000006)
          { // anti-stop
            sum_stop += prt->momentum();
          }
        }
        
        if(sum_stop.Pt() <= 120.)
          ISRweight = 1.0;
        else if(sum_stop.Pt() <= 150.)
          ISRweight = 0.95;
        else if(sum_stop.Pt() <= 250.)
          ISRweight = 0.90;
        else
          ISRweight = 0.80;
    }
    else
    {
        // something is wrong with the sample---print error and exit the code
        ERROR << "No event.mc() has been found." << endmsg;
        exit(1);
    }
    
    myEventWeight *= ISRweight;
    // should be deactivated for comparison with CMS cutflow
    Manager()->SetCurrentEventWeight(myEventWeight);

    // We're ready to make our first cut.
    // The ApplyCut method takes two arguments: the first is a bool which is the
    // condition for passing (not failing) the cut, and the second is the name
    // you gave that cut when you declared it.
    // ApplyCut returns a bool: true if there is at least one signal region in
    // the analysis still passing all the cuts so far, and false if all signal
    // regions have failed the cuts so far. In the latter case, there's no point
    // continuing to analyse this event and we skip to the next one with the
    // command "return"; we do this each time we apply a cut.

    // The first cut: simply updating the cutflow given the weighting due to
    // the ISR boost factor

    Manager()->ApplyCut(true, "ISR boost factor");

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Collect the different kinds of object we're interested in into containers
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    // first declare the empty containers:
    vector<const RecLeptonFormat*> OtherLeptons;
    vector<const RecLeptonFormat*> SignalElectrons, SignalMuons;
    vector<const RecJetFormat*> myJets;
    vector<const RecTauFormat*> myTaus;
    vector<const RecTrackFormat*> myTracks;

    // fill the tracks container:
    for(unsigned int ii=0; ii<event.rec()->tracks().size(); ii++)
    {
      const RecTrackFormat *CurrentTrack = &(event.rec()->tracks()[ii]);
      double pt = CurrentTrack->pt();
      double abseta = fabs(CurrentTrack->eta());
      // |eta| < 2.1 not mentioned in the paper, but confirmed by Alessandro Gaz
      if(pt>10. && abseta<2.1)
        myTracks.push_back(CurrentTrack);
    }

    // Next deal with leptons.
    // To be considered in the analysis, electrons have to have |eta| < 1.4442
    // and pt > 5 GeV; muons |eta| < 2.1 and pt > 5 GeV. Thereafter we put in
    // one container all electrons with pt greater than 30 GeV
    // (SignalElectrons), in another container all muons with pt > 25 GeV
    // (SignalMuons), and put all that's left in another container
    // (OtherLeptons). Note the reason for defining containers in exactly
    // this way is highly specific to this analysis - the event is vetoed or
    // kept depending on the containers defined in this way.

    // fill the electrons container:
    for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ii]);
      double pt = CurrentElectron->pt();
      double abseta = fabs(CurrentElectron->eta());

      if     (pt<5.  || abseta>1.4442) {continue;}
      else if(pt>30.) 
      {
        SignalElectrons.push_back(CurrentElectron);
      }
      else {OtherLeptons.push_back(CurrentElectron);}
    }

    // fill the muons container:
    for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
      double pt = CurrentMuon->pt();
      double abseta = fabs(CurrentMuon->eta());
      if     (pt<5.  || abseta>2.1) {continue;}
      else if(pt>25.)
      {
        SignalMuons.push_back(CurrentMuon);
      }
      else {OtherLeptons.push_back(CurrentMuon);}
    }

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Now that we have filled the signal leptons container, we are in a
    // position to check the first cut: that there is at least one signal
    // lepton. (Note that you should always check cuts as soon as you can - if
    // you fail them, it's good to quit early to save CPU time.) However we are
    // going to adjust the weight of this event according to the probability
    // that it would pass the triggers, and we need to know the weight before
    // the first cut, in order to update the cut flow correctly.
    // So let's do that now!
    //
    // The event is triggered on a lepton. If there are truly N leptons,
    // the probability to fail the trigger is (1-efficiency)^N. This is
    // what we do here, modelling the pT and eta dependence of the efficiency
    // from CMS tables.
    // Instead of keeping/discarding the event based on the probability of
    // passing the trigger (i.e. comparing this probability to a random number
    // between 0 and 1), we always keep the event but multiply its weight by the
    // probability to pass the trigger: this improves the statistics obtained
    // for the sample analysed.

    double ProbaToFail = 1.;
    double CurEff;

    // single electron trigger
    for(unsigned int ii=0; ii<SignalElectrons.size(); ii++)
    {
      double pt = SignalElectrons[ii]->pt();
      double abseta = fabs(SignalElectrons[ii]->eta());

      // should be deactivated for comparison with CMS cutflow
      // if(pt > 27.) CurEff = 1.; else CurEff = 0.;

      if(pt < 24.) CurEff = 0.0;
      else if(pt < 26.) {
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
    for(unsigned int ii=0; ii<SignalMuons.size(); ii++)
    {
      double pt = SignalMuons[ii]->pt();
      double abseta = fabs(SignalMuons[ii]->eta());
      
      // should be deactivated for comparison with CMS cutflow
      // if(pt > 24.) CurEff = 1.; else CurEff = 0.;
      
      if(pt < 22.) CurEff = 0.0;
      else if(pt < 24.) {
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

    // update the weight for this event (and tell RSManager, which needs to know
    // for the cut flows)
    myEventWeight *= (1.-ProbaToFail);
    Manager()->SetCurrentEventWeight(myEventWeight);
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    Manager()->ApplyCut(true, "trigger");

    // fill the jets container (jets need pt > 30 GeV and |eta| < 2.4)
    for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
    {
      const RecJetFormat *CurrentJet = &(event.rec()->jets()[ii]);
      double pt = CurrentJet->pt();
      double abseta = fabs(CurrentJet->eta());
      if(pt>30. && abseta<2.4)
        myJets.push_back(CurrentJet);
    }

    // Order the jets by pT (if you want to order by something else, e.g. ET, E,
    // etc., add a second argument: ETordering, Eordering, etc.)
    SORTER->sort(myJets);

    // fill the taus container:
    // Note that taus are also included in the jet collection; in this analysis
    // this is irrelevant as we veto taus. If taus do not cause the event to be
    // vetoed, you may want to remove them from the jets container.
    // TODO: perhaps write code which removes taus from the jets container and
    // comment it out. We will see to that later.
    // If you care about taus, stay tuned for further developments (automatic
    // removal from the jet container).
    for(unsigned int ii=0; ii<event.rec()->taus().size(); ii++)
    {
      const RecTauFormat *CurrentTau = &(event.rec()->taus()[ii]);
      double pt = CurrentTau->pt();
      double abseta = fabs(CurrentTau->eta());
      if(pt>20. && abseta<2.4)
        myTaus.push_back(CurrentTau);
    }

    // missing transverse momentum:
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Isolation criteria
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    // lepton isolation: pTsum in a cone of Delta R = 0.3, excluding the lepton
    // itself, should be < min(5 GeV, 0.15*pT_lepton)
    // We remove from SignalElectrons and SignalMuons those leptons that are
    // not isolated, and put them in OtherLeptons, since their presence in the
    // event may yet cause a veto. 

    // Note that we start at the end of the container and iterate backwards
    // through it because we may *remove* elements from it as we go.
    // Note also that we use a signed int, as subtracting 1 from an unsigned
    // int that's currently equal to zero returns a huge number, not -1, which
    // fails to terminate the loop.
    for(int ii=SignalElectrons.size()-1; ii>=0; ii--)
    {
      for(unsigned int jj=0; jj<SignalElectrons[ii]->isolCones().size(); jj++)
      {
        if(fabs(SignalElectrons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        {
          if(SignalElectrons[ii]->isolCones()[jj].sumPT()
             > min(5.,.15*SignalElectrons[ii]->pt()))
          {
            OtherLeptons.push_back(SignalElectrons[ii]);
            SignalElectrons.erase(SignalElectrons.begin()+ii);
            break;
          }
        }
      }
    }
    for(int ii=SignalMuons.size()-1; ii>=0; ii--)
    {
      for(unsigned int jj=0; jj<SignalMuons[ii]->isolCones().size(); jj++)
      {
        if(fabs(SignalMuons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        {
          if(SignalMuons[ii]->isolCones()[jj].sumPT()
             > min(5.,.15*SignalMuons[ii]->pt()))
          {
            OtherLeptons.push_back(SignalMuons[ii]);
            SignalMuons.erase(SignalMuons.begin()+ii);
            break;
          }
        }
      }
    }

    // applying identification-only weights obtained from CMS
    double Proba0lep = 1.;

    for(unsigned int ii=0; ii<SignalElectrons.size(); ii++)
    {
      double pt = SignalElectrons[ii]->pt();

      if(pt < 30.) CurEff = 0.78;
      else if(pt < 40.) CurEff = 0.84;
      else CurEff = 0.87;

      Proba0lep *= 1.-CurEff;
    }

    for(unsigned int ii=0; ii<SignalMuons.size(); ii++)
    {
      double pt = SignalMuons[ii]->pt();

      if(pt < 200.) CurEff = 0.95;
      else if(pt < 300.) CurEff = 0.90;
      else CurEff = 0.80;

      Proba0lep *= 1.-CurEff;
    }

    myEventWeight *= (1.-Proba0lep);
    Manager()->SetCurrentEventWeight(myEventWeight);

    // at least one isolated lepton with pT > 30 (25) for e (mu)
    if(!Manager()->ApplyCut((SignalElectrons.size() + SignalMuons.size()) > 0,
                            "1+ candidate lepton"))
      return true;

    // The next cut: at least 4 jets with pT > 30 GeV and |eta| < 2.4
    // If no signal region is left passing cuts, we stop analysing this event.

    // Any jets overlapping (within deltaR = 0.4) with the signal lepton are 
    // discarded. (Note that in other analyses it's common to see electrons 
    // discarded if they're too close to jets; not here.)
    // Warning: again, we iterate through the container backwards.
    bool do_erase = false;
    for(int ii=myJets.size()-1; ii>=0; ii--)
    {
      for(unsigned int jj=0; jj<SignalElectrons.size(); jj++)
      {
        if(myJets[ii]->dr(SignalElectrons[jj]) < 0.4)
        {
          do_erase = true;
          break;
        }
      }
      for(unsigned int jj=0; jj<SignalMuons.size(); jj++)
      {
        if(myJets[ii]->dr(SignalMuons[jj]) < 0.4)
        {
          do_erase = true;
          break;
        }
      }
      if(do_erase)
      {
        myJets.erase(myJets.begin()+ii);
        do_erase = false;
      }
    }

    if(!Manager()->ApplyCut((myJets.size()>=4),"4+ central jets"))
      return true;

    if(!Manager()->ApplyCut((MET > 50.),"MET > 50 GeV"))
      return true;

    if(!Manager()->ApplyCut((MET > 100.),"MET > 100 GeV"))
      return true;

    // check for the presence of at least one b tag:
    bool AtLeast1btag = false;
    for(unsigned int ii=0; ii<myJets.size(); ii++)
    {
      if(myJets[ii]->btag())
      {
        // found one! quit the loop
        AtLeast1btag = true;
        break;
      }
    }
    // The next cut: at least one b tag
    // If no signal region is left passing cuts, we stop analysing this event.
    if(!Manager()->ApplyCut(AtLeast1btag,"1+ b-tagged jet"))
      return true;

    // check for the presence of a second isolated lepton:
    // Delta R = 0.3 is the correct value (0.4 in the paper is a mistake)
    int NumIsolatedLepton = 0;

    for(unsigned int ii=0; ii<SignalElectrons.size(); ii++)
    {
      for(unsigned int jj=0; jj<SignalElectrons[ii]->isolCones().size(); jj++)
      {
        if(fabs(SignalElectrons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        {
          if(SignalElectrons[ii]->isolCones()[jj].sumPT()
             < .20*SignalElectrons[ii]->pt())
          {
            ++NumIsolatedLepton;
            break;
          }
        }
      }
    }
    for(unsigned int ii=0; ii<SignalMuons.size(); ii++)
    {
      for(unsigned int jj=0; jj<SignalMuons[ii]->isolCones().size(); jj++)
      {
        if(fabs(SignalMuons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        {
          if(SignalMuons[ii]->isolCones()[jj].sumPT()
             < .20*SignalMuons[ii]->pt())
          {
            ++NumIsolatedLepton;
            break;
          }
        }
      }
    }
    for(unsigned int ii=0; ii<OtherLeptons.size(); ii++)
    {
      for(unsigned int jj=0; jj<OtherLeptons[ii]->isolCones().size(); jj++)
      {
        if(fabs(OtherLeptons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        {
          if(OtherLeptons[ii]->isolCones()[jj].sumPT()
             < .20*OtherLeptons[ii]->pt())
          {
            ++NumIsolatedLepton;
            break;
          }
        }
      }
    }

    if(NumIsolatedLepton == 0)
    {
      // this should not happen and means that there is a bug.
      ERROR << "No isolated lepton found (and we must have one at this stage)"
            << endmsg;
      exit(1);
    }

    // The next cut: demand no other isolated leptons
    // (note: it's not exactly the same criterion as exactly one signal lepton)
    // If no signal region is left passing cuts, we stop analysing this event.
    if(NumIsolatedLepton != 1) {
    if(!Manager()->ApplyCut(NumIsolatedLepton == 1,
                             "veto isol lepton and track"))
      return true;
    }

    // identify THE signal lepton
    bool is_e; // true: e, false: mu
    if(SignalElectrons.size() == 1 && SignalMuons.size() == 0)
    {
      is_e = true;
    }
    else if(SignalElectrons.size() == 0 && SignalMuons.size() == 1)
    {
      is_e = false;
    }
    else
    {
      ERROR << "Again no isolated lepton found (we must have one at this stage)"
            << endmsg;
      exit(1);
    }
    const RecLeptonFormat* SignalLepton;

    if(is_e) SignalLepton = SignalElectrons[0];
    else SignalLepton = SignalMuons[0];

    int LeptonCharge = SignalLepton->charge();

    // check for the presence of an isolated track of pT > 10 GeV with a charge
    // of opposite-sign (OS) to the signal lepton
    bool NoOtherIsolatedOSTrack = true;
    for(unsigned int ii=0; ii<myTracks.size(); ii++)
    {
      if(myTracks[ii]->charge()!=LeptonCharge)
      {
        for(unsigned int jj=0; jj<myTracks[ii]->isolCones().size(); jj++)
        {
          if(fabs(myTracks[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
          {
            if(myTracks[ii]->isolCones()[jj].sumPT()
               < .1*myTracks[ii]->pt())
            {
              // found one! quit the loop
              NoOtherIsolatedOSTrack = false;
              break;
            }
          }
        }
      }
    }

    // apply scale factor corresponding to the difference in isolation between
    // tracks method and CMS method using PF particles
    // obtain from the two cutflow tables (T2tt 650/50 and 250/50)
    myEventWeight *= 0.885;
    Manager()->SetCurrentEventWeight(myEventWeight);

    // The next cut: checking that there are no isolated tracks
    // If no signal region is left passing cuts, we stop analysing this event.
    if(!Manager()->ApplyCut(NoOtherIsolatedOSTrack,
                            "veto isol lepton and track"))
      return true;

    // The next cut: no jets tagged as hadronic taus
    // Note that (imperfect) tau tagging efficiency is dealt with at the Delphes
    // level, as is b-tagging efficiency. (So there's no need, for example, to
    // pretend b-jets are not b-jets if a random number in [0,1] is > 0.7.)
    // If no signal region is left passing cuts, we stop analysing this event.
    if(!Manager()->ApplyCut((myTaus.size()==0),"No hadronic tau"))
      return true;

    // This completes the set of cuts referred to as 'preselection' in the
    // experimental paper (even though there are still two more cuts to be
    // applied which affect all signal regions, and so are on the same footing
    // as preselection cuts). Most histograms are thus filled at this stage.

    // MT: the transverse mass of the signal lepton and the missing pT
    double MT = SignalLepton->mt_met(pTmiss);
    double mt2w = PHYSICS->Transverse->MT2W(myJets,
                                            SignalLepton,event.rec()->MET());

    // chi^2: we use the CMS (public) snippet of code
    double chi2 = calculateChi2(myJets);

    double MinDeltaPhiJetMET = min(myJets[0]->dphi_0_pi(pTmiss),
                                   myJets[1]->dphi_0_pi(pTmiss));

    // Calculate HT - here defined as the scalar sum of jet transverse energies
    // - for (a) all jets up to the maximum number considered, and (b) only 
    // those jets in the same hemisphere as the MET
    // (i.e. with DeltaPhi(MET,jet) < 90 degrees)
    // In some analyses, HT is calculated using only the N hardest jets, not all
    // of them. Here it's all of them.
    // Note that there is an HT method in the MA5 built-in library, summing 
    // over *all* hadronic objects, but this does not match the HT definition 
    // needed in this analysis (soft and very forward jets do not get counted as
    // jets).
    unsigned int NumJetsConsideredForHT = myJets.size();
    double HT = 0.;
    double HTsameHemisphere = 0.;
    for(unsigned int ii=0; ii<NumJetsConsideredForHT; ii++)
    {
      double Et = myJets[ii]->et();
      HT += Et;
      if (myJets[ii]->dphi_0_pi(pTmiss) < PI/2.)
        HTsameHemisphere += Et;
    }
    double HTratio = HTsameHemisphere / HT;

    // Jets are pT ordered, so start from the hardest and break when the first
    // b-tag (at least one must be present at this stage of the code) is found:
    double LeadingBjetpT = 0.;
    double deltaRb1l = 0.;
    for(unsigned int ii=0; ii<myJets.size(); ii++)
    {
      if (myJets[ii]->btag())
      {
        LeadingBjetpT = myJets[ii]->pt();
        deltaRb1l = myJets[ii]->dr(SignalLepton);
        break;
      }
    }

    // Fill histos with RSManager's FillHisto method; the arguments are the
    // string of one of the histos declared in Initialize, and the value to be
    // binned.
    Manager()->FillHisto("MT",      MT);
    Manager()->FillHisto("MET",     MET);
    Manager()->FillHisto("MT2W",    mt2w);
    Manager()->FillHisto("chi2",    chi2);
    Manager()->FillHisto("HTratio", HTratio);
    Manager()->FillHisto("JetMETMindeltaPhi", MinDeltaPhiJetMET);
    Manager()->FillHisto("pT(leading b-jet)", LeadingBjetpT);
    Manager()->FillHisto("deltaR(l, leading b-jet)", deltaRb1l);
    Manager()->FillHisto("pT(l)", SignalLepton->pt());

    // §§ this is where the MinDeltaPhiJetMET > 0.8 cuts should be when
    // comparing to the CMS cutflow

    // §§ this is where the chi2 < 5 cut should be when comparing to the
    // CMS cutflow

    // The next cut: the transverse mass is > 120 GeV
    // If no signal region is left passing cuts, we stop analysing this event.
    if(!Manager()->ApplyCut((MT > 120.),"MT > 120 GeV"))
      return true;

    // Some histos which are defined only after the previous cut:
    Manager()->FillHisto("MT2W after MT>120", mt2w);
    Manager()->FillHisto("chi2 after MT>120", chi2);
    Manager()->FillHisto("HTratio after MT>120", HTratio);
    Manager()->FillHisto("JetMETMindeltaPhi after MT>120", MinDeltaPhiJetMET);
    Manager()->FillHisto("pT(leading b-jet) after MT>120",LeadingBjetpT);
    Manager()->FillHisto("deltaR(l, leading b-jet) after MT>120",deltaRb1l);

    // The next cut: the delta-phi between the missing pT and each of the two
    // leading jets should be greater than 0.8.
    // If no signal region is left passing cuts, we stop analysing this event.
    if(!Manager()->ApplyCut((MinDeltaPhiJetMET>.8),"dphi(MET, j1 or j2) > 0.8"))
      return true;

    if(!Manager()->ApplyCut((chi2 < 5.),"chi^2 < 5"))
      return true;

    // §§ this is where the MT > 120 GeV cut should be when comparing to the
    // CMS cutflow

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Signal region definitions
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Now we're into the signal-region-specific cuts.
    // If no signal region is left passing cuts, we stop analysing this event.

    if(!Manager()->ApplyCut((MET > 150.),"MET > 150 GeV"))
      return true;
    if(!Manager()->ApplyCut((MET > 200.),"MET > 200 GeV"))
      return true;
    if(!Manager()->ApplyCut((MET > 250.),"MET > 250 GeV"))
      return true;
    if(!Manager()->ApplyCut((MET > 300.),"MET > 300 GeV"))
      return true;
    if(!Manager()->ApplyCut((mt2w > 200.),"MT2W > 200 GeV"))
      return true;
    if(!Manager()->ApplyCut((LeadingBjetpT > 100.),
                            "Leading b-jet pT > 100 GeV"))
      return true;
  }
  // nothing more to do in the execute function:
  return true;
}





float floatM2(const RecJetFormat* jj)
{
  return pow(float(jj->momentum().E()),2)
  - pow(float(jj->momentum().Px()),2)
  - pow(float(jj->momentum().Py()),2)
  - pow(float(jj->momentum().Pz()),2);
}
double floatM(const RecJetFormat* jj)
{
  return float(sqrt(floatM2(jj)));
}
//--------------------------------------------------------------------
double sigma(const RecJetFormat* jj)
{
  // return jj->momentum().Pt()*.10;
  return 0.10;
}
//--------------------------------------------------------------------
double fc2 (double c1, double m12, double m22, double m02)
{
  double a = m22;
  double b = (m02 - m12 - m22) * c1;
  double c = m12 * c1 * c1 - PDG_W_MASS * PDG_W_MASS;
  double num = -1. * b + sqrt(b * b - 4 * a * c);
  double den = 2. * a;
  return (num/den);
}
//--------------------------------------------------------------------
double fchi2 (double c1, double pt1, double sigma1, double pt2, double sigma2,
              double m12, double m22, double m02){
  double rat1 = pt1 * (1 - c1) / sigma1;
  double rat2 = pt2 * (1 - fc2(c1, m12, m22, m02)) / sigma2;

  return ( rat1 * rat1 + rat2 * rat2);
}
//--------------------------------------------------------------------
void minuitFunction(int&, double* , double &result, double par[], int)
{
  result=fchi2(par[0], par[1], par[2], par[3], par[4], par[5], par[6], par[7]);
}
//--------------------------------------------------------------------


// This function calculates the hadronic chi2 - SNT version
double calculateChi2(std::vector<const RecJetFormat *> myjets)
{
  //check at most first 6 jets
  int n_jets = myjets.size();
  if (n_jets>6) n_jets = 6;
  //consider at least 3 jets
  if (n_jets<3) return 999999.;

  std::vector<int> v_i, v_j;
  std::vector<double> v_k1, v_k2;
  for ( int i=0; i<n_jets; ++i )
    for ( int j=i+1; j<n_jets; ++j )
    {
      //  W
      MALorentzVector hadW = myjets[i]->momentum() + myjets[j]->momentum();

      //  W Mass Constraint.
      TFitter *minimizer = new TFitter();
      double p1 = -1;
      minimizer->ExecuteCommand("SET PRINTOUT", &p1, 1);
      minimizer->SetFCN(minuitFunction);
      minimizer->SetParameter(0 , "c1"     , 1.1             , 1 , 0 , 0);
      minimizer->SetParameter(1 , "pt1"    , 1.0             , 1 , 0 , 0);
      minimizer->SetParameter(2 , "sigma1" , sigma(myjets[i])  , 1 , 0 , 0);
      minimizer->SetParameter(3 , "pt2"    , 1.0             , 1 , 0 , 0);
      minimizer->SetParameter(4 , "sigma2" , sigma(myjets[j])  , 1 , 0 , 0);
      minimizer->SetParameter(5 , "m12"    , floatM2(myjets[i]) , 1 , 0 , 0);
      minimizer->SetParameter(6 , "m22"    , floatM2(myjets[j]) , 1 , 0 , 0);
      minimizer->SetParameter(7 , "m02"    , hadW.M2(), 1 , 0 , 0);
      for (unsigned int k = 1; k < 8; k++)
        minimizer->FixParameter(k);
      minimizer->ExecuteCommand("SIMPLEX", 0, 0);
      minimizer->ExecuteCommand("MIGRAD", 0, 0);

      double c1 = minimizer->GetParameter(0);
      if (c1!=c1) continue;
      double c2 = fc2(c1, floatM2(myjets[i]), floatM2(myjets[j]), hadW.M2());
      delete minimizer;

       // * W Mass check
       v_i.push_back(i);
       v_j.push_back(j);
       v_k1.push_back(c1);
       v_k2.push_back(c2);
    }

  //Apply b-consistency requirement
  int n_btag = 0;
  for( int i = 0 ; i < n_jets ; i++ )
    if(myjets[i]->btag()) n_btag++;
  double chi2min = 99999.;

  //consider b-jet in leading 3 jets
  for ( int b=0; b<n_jets; ++b )
  {
    //if not tagged, consider only 3 leading jets
    if( (!myjets[b]->btag()) && b>2 ) continue;

    //require b-tagging if have more than 1 b-tag
    if( n_btag>1 && (!myjets[b]->btag()) ) continue;

    for (unsigned int w = 0; w < v_i.size() ; ++w )
    {
      int i = v_i[w];
      int j = v_j[w];
      if ( i==b || j==b ) continue;
      //count number of b-tagged Ws
      int nwb = 0;
      if (myjets[i]->btag()) nwb++;
      if (myjets[j]->btag()) nwb++;
      //no btagged jets in W if have few btags
      if ( n_btag<3  && nwb>0 ) continue;
      //In 3 b-tag case, allow for 1 W jet to be tagged
      // If have more b-tags then btagging information not useful
      if ( n_btag==3 && nwb>1 ) continue;

      //  W Mass
      MALorentzVector hadW =myjets[i]->momentum() + myjets[j]->momentum();
      double c1 = v_k1[w];
      double c2 = v_k2[w];

      // Top Mass
      MALorentzVector hadT = (myjets[i]->momentum()*c1)+(myjets[j]->momentum()*c2)+myjets[b]->momentum();
      double sigma_w2 = pow(myjets[i]->momentum().Pt()*sigma(myjets[i]), 2)
        + pow(myjets[j]->momentum().Pt()*sigma(myjets[j]), 2);
      double smw2 = (1. + 2.*pow(hadW.Pt(),2)/hadW.M2())*sigma_w2;
      double sigma_t2 = pow(c1*myjets[i]->momentum().Pt()*sigma(myjets[i]),2)
        + pow(c2*myjets[j]->momentum().Pt()*sigma(myjets[j]),2)
        + pow(myjets[b]->momentum().Pt()*sigma(myjets[b]),2);
      double smtop2 = (1. + 2.*pow(hadT.Pt(),2))/hadT.M2()*sigma_t2;

      double c_chi2 = pow(hadT.M()-PDG_TOP_MASS, 2)/smtop2
        + pow(hadW.M()-PDG_W_MASS, 2)/smw2;
      if (c_chi2<chi2min) chi2min = c_chi2;
    }
  }
  return chi2min;
}



