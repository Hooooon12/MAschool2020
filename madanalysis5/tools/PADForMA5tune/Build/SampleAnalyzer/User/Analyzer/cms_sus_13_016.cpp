#include "SampleAnalyzer/User/Analyzer/cms_sus_13_016.h"


using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_sus_13_016::Initialize(const MA5::Configuration& cfg,
const map<string,string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: CMS-SUS-13-016                  <>" << endmsg;
  INFO << "        <>            (stop search, OS leptons)       <>" << endmsg;
  INFO << "        <>  Recasted by: D.Sengupta                   <>" << endmsg;
  INFO << "        <>  Contact: dipan@lpsc.in2p3.fr              <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11            <>" << endmsg;
  INFO << "        <>  For more information, see                 <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

// For this analysis there is only one signal region for two different benchmark points.
// The first corresponds to m_{gluino}=1150, m_{LSP}=300 GeV,
// the second being m_{gluino}=1150, m_{LSP}=500 GeV
   Manager()->AddRegionSelection("Gluino->TT+neutralino");

  // Declare all the cuts used in the analysis.
  Manager()->AddCut("at least 2 leptons");
  Manager()->AddCut("at least 2 OS leptons");
  Manager()->AddCut("at least 2 jets");
  Manager()->AddCut("MET > 180 GeV");
  Manager()->AddCut("at least 5 jets");
  Manager()->AddCut("at least 3 b-tagged jets");
  Manager()->AddCut("Eta(Jet1) < 1");
  Manager()->AddCut("Eta(Jet2) < 1");


  // Declare all histograms to be produced by the analysis.
    Manager()->AddHisto("njet",15,0,15);
    Manager()->AddHisto("nbjet",10,0,10);
    Manager()->AddHisto("j1eta",10,-2.5,2.5);
    Manager()->AddHisto("j2eta",10,-2.5,2.5);
    Manager()->AddHisto("met",4,30,230);

  return true;
}





// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_sus_13_016::Finalize(const SampleFormat& summary,
const vector<SampleFormat>& files)
{
  return;
}



// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_sus_13_016::Execute(SampleFormat& sample, const EventFormat& event)
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
     vector<const RecLeptonFormat*> OtherLeptons,CurrentElectron,CurrentMuon; 
     vector<const RecLeptonFormat*>SignalLeptons, SignalElectrons, SignalMuons;
     vector<const RecJetFormat*> SignalJets,CurrentJet;
    
    // fill the electrons container:

// For the cms_sus_016 analysis we need the two leptons, either two muons 
// two electrons or a muon electron pair. For the double muon(electron) trigger with the leading muon(electron ) being > 17 GeV and. For the muon-electron trigger the threshold is 8 GeV (17 GeV) for the muon(electron). Events 
//are then required to have at least two opposite sign leptons with 20 GeV 
// and at least two jets  with 30 GeV

      for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
    {
      const RecJetFormat * CurrentJet = &(event.rec()->jets()[ii]);
      if ( CurrentJet->pt()   > 30. &&
      fabs(CurrentJet->eta()) < 2.4)
     SignalJets.push_back(CurrentJet);
    }




       for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
    {
      const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ii]);

      if  (CurrentElectron->pt()   > 20.  &&
      fabs(CurrentElectron->eta()) < 2.4)
        {
         SignalElectrons.push_back(CurrentElectron);
         SignalLeptons.push_back(CurrentElectron);
          }
    else {OtherLeptons.push_back(CurrentElectron);}
    }



    for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
      if  (CurrentMuon->pt()   > 20.  &&
      fabs(CurrentMuon->eta()) < 2.4)
        {
       SignalMuons.push_back(CurrentMuon);
       SignalLeptons.push_back(CurrentMuon);
         }
     else {OtherLeptons.push_back(CurrentMuon);}
    }

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


// We're ready to make our first cut.
// The first cut: checking that we have two leptons irrespective 
//        of charge


     if( !Manager()->ApplyCut(SignalLeptons.size() > 1,
     "at least 2 leptons"))
      return true;

// Isolation Criteria
// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
// Isolation criteria
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
   // lepton isolation: pTsum in a cone of Delta R = 0.3, excluding the lepton
   // itself, should be < min(5 GeV, 0.15*pT_lepton)


    for(int ii=SignalLeptons.size()-1; ii>=0; ii--)
    {
      for(unsigned int jj=0; jj<SignalLeptons[ii]->isolCones().size(); jj++)
      {
        if(fabs(SignalLeptons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        {
          if(SignalLeptons[ii]->isolCones()[jj].sumPT() > .20*SignalLeptons[ii]->pt())
          {
            OtherLeptons.push_back(SignalLeptons[ii]);
            SignalLeptons.erase(SignalLeptons.begin()+ii); // PROBLEME. test jj=ii
          }
        }
      }

   }


// Next find at least two opposite sign leptons
    int ProductOfLeptonCharges; 
    bool signLepton =false; 
    for(unsigned int ii=0; ii<SignalLeptons.size(); ii++){
     ProductOfLeptonCharges = SignalLeptons[0]->charge() * 
                                SignalLeptons[ii]->charge();
    if( ProductOfLeptonCharges <0 ) { 
     signLepton=true;
     break;  
    }
    }

 // The next cut: ot least two pposite-sign (OS) leptons
    if( !Manager()->ApplyCut(signLepton,"at least 2 OS leptons") )
    return true;


// missing transverse momentum:
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();

    if(!Manager()->ApplyCut((SignalJets.size()>=2),"at least 2 jets"))
    return true;
 
// 1st Cut : Missing energy above 180 GeV
// Note that the plots are made with a relaxed MET cut of 100 GeV


     if(!Manager()->ApplyCut((MET > 180.),"MET > 180 GeV" ))
     return true;

//2nd Cut : At least 4 jets
   if(!Manager()->ApplyCut((SignalJets.size()> 4),"at least 5 jets"))
   return true;


// check for the presence of at least 2 b tag:

    int bcount =0;
    for(unsigned int ii=0; ii<SignalJets.size(); ii++)
    {
      if(SignalJets[ii]->btag()) bcount++ ;
    }


// 3rd Cut: The next cut: at least 3 b tag
  if(!Manager()->ApplyCut((bcount >2),"at least 3 b-tagged jets"))
   return true;

// Next Cut leading jet eta < 1
     double LeadingJetetaLessthan1=99999999;
     double NextLeadingJetetaLessthan1=999999;

     LeadingJetetaLessthan1 = abs(SignalJets[0]->eta()) ;
     NextLeadingJetetaLessthan1 =abs(SignalJets[1]->eta()) ;

// 4th Cut : absolute value of leading jet pseudorapidity <1

     if( !Manager()->ApplyCut((LeadingJetetaLessthan1 < 1.), "Eta(Jet1) < 1") )
      return true;

//5th cut : absolute value of subleading jet rapidity.
      if( !Manager()->ApplyCut((NextLeadingJetetaLessthan1 < 1.),"Eta(Jet2) < 1"  ) )
      return true;


    // Fill histos with RSManager's FillHisto method; the arguments are the
    // string of one of the histos declared in Initialize, and the value to be
    // binned.

     Manager()->FillHisto("njet",  SignalJets.size());
     Manager()->FillHisto("nbjet",  bcount);
     Manager()->FillHisto("j1eta",SignalJets[0]->eta() );
     Manager()->FillHisto("j2eta",SignalJets[1]->eta());
     Manager()->FillHisto("met",MET);
}
    // nothing more to do in the execute function:
    return true;
}
