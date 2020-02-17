// //WARNING: Check that nothing is written after column 80.
//          This renders files nice to be viewed in a shell.
#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_05.h"


using namespace MA5;
using namespace std;

const int n_histo = 0;


// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_susy_2013_05::Initialize(const MA5::Configuration& cfg,
const map<string,string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: ATLAS-SUSY-2013-05              <>" << endmsg;
  INFO << "        <>            JHEP 10 (2013) 189              <>" << endmsg;
  INFO << "        <>            (stop/sbottom search, 0l2b+MET) <>" << endmsg;
  INFO << "        <>  Recasted by: G. Chalons                   <>" << endmsg;
  INFO << "        <>  Contact: chalons@lpsc.in2p3.fr            <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11            <>" << endmsg;
  INFO << "        <>  For more information, see                 <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

  Manager()->AddRegionSelection("SRA, HighDeltaM, MET > 150, MCT > 150");
  Manager()->AddRegionSelection("SRA, HighDeltaM, MET > 150, MCT > 200");
  Manager()->AddRegionSelection("SRA, HighDeltaM, MET > 150, MCT > 250");
  Manager()->AddRegionSelection("SRA, HighDeltaM, MET > 150, MCT > 300");
  Manager()->AddRegionSelection("SRA, HighDeltaM, MET > 150, MCT > 350");
  Manager()->AddRegionSelection("SRB, LowDeltaM, MET > 250");


  // MET Filter at the mc LEVEL
  Manager()->AddCut("MET Filter > 80");
  // No electrons or muons in the final state
  Manager()->AddCut("Lepton veto");
  // MET > 150
  Manager()->AddCut("MET > 150");
  

  // Specific signal region cuts
  string SRACut150[] = {"SRA, HighDeltaM, MET > 150, MCT > 150"};
  string SRACut200[] = {"SRA, HighDeltaM, MET > 150, MCT > 200"};
  string SRACut250[] = {"SRA, HighDeltaM, MET > 150, MCT > 250"};
  string SRACut300[] = {"SRA, HighDeltaM, MET > 150, MCT > 300"};
  string SRACut350[] = {"SRA, HighDeltaM, MET > 150, MCT > 350"};
  string SRACut[] = {"SRA, HighDeltaM, MET > 150, MCT > 150","SRA, HighDeltaM, MET > 150, MCT > 200",
   "SRA, HighDeltaM, MET > 150, MCT > 250", "SRA, HighDeltaM, MET > 150, MCT > 300",
   "SRA, HighDeltaM, MET > 150, MCT > 350"
  };
  string SRBCut[] = {"SRB, LowDeltaM, MET > 250"};
  
  Manager()->AddCut("MET SRB > 250",SRBCut);
  
  Manager()->AddCut("SRA 1st jt btag pT > 130, eta < 2.5",SRACut);
  Manager()->AddCut("SRA 2nd jt btag pT > 50, eta < 2.5",SRACut);
  Manager()->AddCut("SRA 3rd+ jt pT > 50, eta < 2.8",SRACut);
  Manager()->AddCut("SRB 1st jt pT > 150, eta < 2.8",SRBCut);
  Manager()->AddCut("SRB 2nd jt btag pT > 30, eta < 2.5",SRBCut);
  Manager()->AddCut("SRB 3rd jt btag pT > 30, eta < 2.5",SRBCut);
  
  Manager()->AddCut("dPhi(MPT,j1) > 2.5",SRBCut);
  
  // We require 2 b-jets in the first 3rd jets
  Manager()->AddCut("2 b-jets");
  
  Manager()->AddCut("dPhimin > 0.4");
  
  Manager()->AddCut("MET/MEFF (j1,j2) > 0.25",SRACut);
  Manager()->AddCut("MET/MEFF (j1,j2,j3) > 0.25",SRBCut);
  
  Manager()->AddCut("HT3 < 50",SRBCut);
  
  Manager()->AddCut("MBB > 200",SRACut);
  
  Manager()->AddCut("MCT > 150",SRACut150);
  Manager()->AddCut("MCT > 200",SRACut200);
  Manager()->AddCut("MCT > 250",SRACut250);
  Manager()->AddCut("MCT > 300",SRACut300);
  Manager()->AddCut("MCT > 350",SRACut350);
 
  // Declaration of the histograms
  Manager()->AddHisto("MCT SRA",20,0,500,SRACut); // Fig. 3a
  Manager()->AddHisto("MBB SRA and MCT > 150",15,0,600,SRACut150); // Fig. 3b
  Manager()->AddHisto("MET SRB no MET sel",17,150,500,SRBCut); // Fig. 4a
  Manager()->AddHisto("HT3 SRB no HT3 sel",20,0,200,SRBCut); // Fig. 4b
  Manager()->AddHisto("MCT > 150 SRA",16,150,550,SRACut150); // Fig. 7a
  Manager()->AddHisto("MET full SRB",10,250,450,SRBCut); // Fig 7.b

  return true;
}





// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2013_05::Finalize(const SampleFormat& summary,
const vector<SampleFormat>& files)
{
  // Feel free to add anything here which is not in the default output

  return;
}


// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2013_05::Execute(SampleFormat& sample, const EventFormat& event)
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
    vector<const RecLeptonFormat*> CandElectrons, CandMuons, CandLeptons;     
    vector<const RecJetFormat*> CandJets, SignalJets, myJets, SignalBJets; 
    
    
    // The following block is there only for the sake of the comparison
    // against the official cutflows of ATLAS. It can be commented out 
    // for other purposes.
     EventFormat myEvent;
        myEvent = event;
 
        unsigned int n = event.mc()->particles().size();
        MALorentzVector sum_MET;
 
        for(unsigned int i=0; i<n; i++)
        {
          MCParticleFormat* prt = &myEvent.mc()->particles()[i];
          if(prt->pdgid() == 1000022)
          { // neutralino
            sum_MET += prt->momentum(); 
          }
          else if(prt->pdgid() == 12)
          { // neu_e
            sum_MET += prt->momentum();
          }
          else if(prt->pdgid() == 14)
          { // neu_m
            sum_MET += prt->momentum();
          }
          else if(prt->pdgid() == 16)
          { // neu_t
            sum_MET += prt->momentum();
          }
        }
        
        if(!Manager()->ApplyCut((sum_MET.Pt() > 80.),"MET Filter > 80"))
	  return true;  

    
    //<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // collect jets and leptons with the right pT and eta

    // Jets are required to have pt> 20 and |eta| < 2.8
    unsigned int Numjetstot = event.rec()->jets().size();
    for(unsigned int ii=0; ii<Numjetstot; ii++)
    {
      const RecJetFormat * CurrentJet = &(event.rec()->jets()[ii]);
      if ( CurrentJet->pt()   > 20 &&
      fabs(CurrentJet->eta()) < 2.8)
        CandJets.push_back(CurrentJet);
    }
    
    // Order the jets by pT (if you want to order by something else, e.g. ET, E,
    // etc., add a second argument: ETordering, Eordering, etc.)

    SORTER->sort(CandJets);
    
    // Check there is at least 2 jets
    // This is only to optimise the analysis
    unsigned int NumCandJets = CandJets.size();
    if(NumCandJets < 2)
    {
    return true;
    }
    
    // Fill electrons containers fulfilling pt > 7 and |eta| < 2.47
    // A loose electron isolation is also performed to remove
    // non-prompt electrons
    unsigned int Nelectrons = event.rec()->electrons().size();
    for(unsigned int ii=0; ii< Nelectrons; ii++)
    {
      const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ii]);
      for(unsigned int jj=0; jj < CurrentElectron->isolCones().size(); jj++)
      {
        double pTsumInCone = CurrentElectron->isolCones()[jj].sumET();
        double deltaR = CurrentElectron->isolCones()[jj].deltaR();
        if  (CurrentElectron->pt()   > 7. &&
      fabs(CurrentElectron->eta()) < 2.47)
        {
        if(fabs(deltaR-0.2) < 0.001 && pTsumInCone < 0.2*CurrentElectron->pt() )
        {CandElectrons.push_back(CurrentElectron);}
        }
      }
    } 
    
    // Fill muons containers fulfilling pt > 6 and |eta| < 2.4
    unsigned int Nmuons = event.rec()->muons().size();
    for(unsigned int ii=0; ii<Nmuons; ii++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
      if  (CurrentMuon->pt()   > 6.  && fabs(CurrentMuon->eta()) < 2.4)
       {CandMuons.push_back(CurrentMuon);}
    }
    //<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // First overlap removal
    // Any jet candidate within deltaR =0.2 of any electron candidate is discarded
    // We then fill the Signal Jet container
    unsigned int NumElectrons = CandElectrons.size();
    
    for(unsigned int i=0; i<NumCandJets; i++)
    {
      const RecJetFormat * ThisJ = CandJets[i];
      bool AwayFromElectron = true;
       for(unsigned int j=0; j < NumElectrons; j++)
       {
	if(ThisJ->dr(CandElectrons[j]) < 0.2)
	{
	  AwayFromElectron = false;
	  break;
	}
       }
      
      if (AwayFromElectron) {SignalJets.push_back(ThisJ);}
    }
    
    SORTER->sort(SignalJets);
    unsigned int NumSignalJets = SignalJets.size();
    
    
    // Check there is at least 2 jets
    if(NumSignalJets < 2)
    {
    return true;
    }
    //<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Second Overlap removal
    // electrons or muons within deltaR =0.4 of any remaining jet are discarded
    // We fill directly a container with only leptons
    
     for(unsigned int i=0; i<NumElectrons; i++)
     {
      const RecLeptonFormat * ThisE = CandElectrons[i];
      bool AwayFromJet = true;
      for(unsigned int j=0; j < NumSignalJets; j++)
      {
        if(ThisE->dr(SignalJets[j]) < 0.4)
        {
          AwayFromJet = false;
          break;
        }
      }
      if (AwayFromJet) {CandLeptons.push_back(ThisE);}
     }
    
    unsigned int NumMuons = CandMuons.size();
    
     for(unsigned int i=0; i<NumMuons; i++)
     {
      const RecLeptonFormat * ThisMu = CandMuons[i];
      bool AwayFromJet = true;
      for(unsigned int j=0; j < NumSignalJets; j++)
      {
        if(ThisMu->dr(SignalJets[j]) < 0.4)
        {
	  AwayFromJet = false;
          break;
        }
      }
      if (AwayFromJet) {CandLeptons.push_back(ThisMu);}
     }
    
    unsigned int NumLeptons = CandLeptons.size(); 
    
    // Fill container of b-jets from the ordered pT jets
    for(unsigned int ii=0; ii<NumSignalJets; ii++)
    {
      const RecJetFormat * Bjet = SignalJets[ii];
      if(Bjet->btag() && fabs(Bjet->eta())<2.5)
      {
	SignalBJets.push_back(Bjet);
      }
    } 
    

    SORTER->sort(SignalBJets);
    unsigned int NumBJets = SignalBJets.size();
    
    // Fill a jet-container without B-jets, will be useful for the definition
    // of the MCT discriminating variable used in the signal region SRA.
    for(unsigned int ii=0; ii<NumSignalJets; ii++)
    {
      const RecJetFormat * CurrentJet = SignalJets[ii];
      if(!CurrentJet->btag() || (CurrentJet->btag() && fabs(CurrentJet->eta()) > 2.5))
      {
	myJets.push_back(CurrentJet);
      }
    } 
    
    SORTER->sort(myJets);
    unsigned int NummyJets = myJets.size();
    
    //<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    // Reject events with remaining electrons or muons in the final state      
    if(!Manager()->ApplyCut((NumLeptons == 0),"Lepton veto"))
      return true;
    
    // missing transverse momentum:
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();
    // The first cut: MET > 150 GeV
    // If no signal region is left passing cuts, we stop analysing this event.
    if(!Manager()->ApplyCut((MET > 150.),"MET > 150"))
      return true;
    
    //<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // We define here some additional variables that will be need for specific 
    // signal regions SRA and SRB
    // The MinDeltaPhiJet variable is computed in two ways :
    // if there are 2 or 3 jets of interest. For the selection cuts in SRB region
    // we always need 3 jets since the leading jet must not be b-tagged but 
    // the two next-to-leading ones. For SRA only the first two are required
    // to be b-tagged, so an event with only two b-jets is sufficient to pass 
    // the jets cuts.

    double MinDeltaPhiJet;
    
    if(NumSignalJets > 2)
     {
     MinDeltaPhiJet = min(SignalJets[0]->dphi_0_pi(pTmiss),
			  min(SignalJets[1]->dphi_0_pi(pTmiss),SignalJets[2]->dphi_0_pi(pTmiss)));
     }
    else
     {
      MinDeltaPhiJet =  min(SignalJets[0]->dphi_0_pi(pTmiss),SignalJets[1]->dphi_0_pi(pTmiss));
     }
    // Declaration of the variable MEFF for each signal region SRA and SRB
    // In SRA MEFF is computed over the first two leading-jets
    // In SRB MEFF is computed over the first three leading-jets
    
    double MEFF_sum_SRA = 0.;
    double MEFF_SRA = 0.;
    for(unsigned int ii=0; ii<2; ii++)
    {
      double Pt_sum = SignalJets[ii]->pt();
      MEFF_sum_SRA += Pt_sum;
    }
    
    MEFF_SRA = MEFF_sum_SRA + MET;  

    double MEFF_sum_SRB = 0.;
    double MEFF_SRB = 0.;
    if(NumSignalJets > 2)
    {
     for(unsigned int ii=0; ii<3; ii++)
     {
       double Pt_sum = SignalJets[ii]->pt();
       MEFF_sum_SRB += Pt_sum;
     }
     MEFF_SRB = MEFF_sum_SRB + MET;
    }
    
    // Definition of the hadronic activity without the three leading jets
    // HT3 will only be useful for SRB
    double HT3 = 0.;
    if(NumSignalJets > 3)
    {
     for(unsigned int ii=3; ii<NumSignalJets; ii++)
      {
       double Pt_sum = SignalJets[ii]->pt();
       HT3 += Pt_sum;
      }
    }

    //     Definition of the invariant mass of b-tagged jets in the event
    double MBB = 0.;
    if(NumBJets == 2)
    {
    MALorentzVector BJetsSum = SignalBJets[0]->momentum() +
                                 SignalBJets[1]->momentum();
			 
     MBB = BJetsSum.M();
    }

    // Calculation of the angle between the leading jet and the missing pT
    // Will be useful only for SRB region
    // The leading jet, supposed to be from ISR, and the missing momentum
    // will required to be almost back-to-back in Phi
    
    double DeltaPhi_pTmiss_J1 = SignalJets[0]->dphi_0_pi(pTmiss);
    
    // Definition of the contranverse mass. Kinematic variable defined 
    // in arXiv:0802.2879 [hep-ph] and arXiv:0910.0174 [hep-ph]. This variable
    // can be used to measure the masses of pair-produced semi-invisibly
    // decaying heavy particles. The two identical heavy particles decay into two 
    // visible particles (or particle aggregate aka jets) v1 and v2 and into two
    // invisible ones. In this analysis the two visible particles are the b-jets
    // and the two invisible are the LSP's.
    // The boost correction to the MCT variable is computed from the library
    // mctlib available at http://projects.hepforge.org/mctlib
    // The needed files are mctlib.cpp,mctlib.h,
    
    // v1, v2 are the 4-vectors of the two aggregated decay products (here the b-jets)
    // vds is the 4-vector of the downstream objects (excluding v1 and v2)
    // ptm is the pTmiss 2-vector {pxmiss,pymiss}
    // ecm is the centre-of-mass energy (D=14TeV)
    // mxlo is a lower bound on the mass of each invisible decay product (D=0)
    double MCTcorr = 0.;
    
    if(NumBJets == 2)
    {
    MALorentzVector v1,v2,vds;
		   
    v1 = SignalBJets[0]->momentum();
    v2 = SignalBJets[1]->momentum();
    for(unsigned int ii=0; ii<NummyJets;ii++)
    {
    vds += myJets[ii]->momentum();
    }
    
    double ecm = 8000.0;
    double mxlo = 0.0;
    TVector2 ptm;
    ptm.Set(pTmiss.Px(),pTmiss.Py());
    TMctLib t;
    MCTcorr = t.mctcorr(v1,v2,vds,ptm,ecm,mxlo);
    }

    //<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    //  		DEFINITION OF THE SIGNAL REGIONS 
    //<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    
    // After having defined some preselection cuts common to the two signal regions
    // of interest, SRA and SRB, we have to apply the cuts specific to each of them.

    // MET CUT ON SRB
    if(!Manager()->ApplyCut((MET > 250.),"MET SRB > 250"))
    return true; 
   
    // We check directly that the 1st and 2nd jets in SRA and 
    // the 2nd and 3rd in SRB are b-tagged as there is no cutflow validation plot on pT selection.

    bool LeadingJetSRA = (SignalJets[0]->btag() && SignalJets[0]->pt() > 130. &&
    fabs(SignalJets[0]->eta()) < 2.5);
    
    bool LeadingJetSRB = (!SignalJets[0]->btag() && SignalJets[0]->pt() > 150. &&
    fabs(SignalJets[0]->eta()) < 2.8);
    
    bool SecondJetSRA = (SignalJets[1]->btag() && SignalJets[1]->pt() > 50. &&
    fabs(SignalJets[1]->eta()) < 2.5);
    
    bool SecondJetSRB = (SignalJets[1]->btag() && SignalJets[1]->pt() > 30. &&
    fabs(SignalJets[1]->eta()) < 2.5);
    
    // If there are only 2 jets, the condition on the 3rd jet of SRA is 
    // automatically fulfilled therefore we set it to false as 
    // the ApplyCut checks !ThirdJetSRA
    bool ThirdJetSRA=false;
    bool ThirdJetSRB=false;
    
    if(NumSignalJets > 2)
    {
    ThirdJetSRA = (SignalJets[2]->pt() > 50. &&
    fabs(SignalJets[2]->eta()) < 2.8);
    
    ThirdJetSRB = (SignalJets[2]->btag() && SignalJets[2]->pt() > 30. &&
    fabs(SignalJets[2]->eta()) < 2.5);
    }
    
//     Application of each cuts in sequential order
    if(!Manager()->ApplyCut(LeadingJetSRA,"SRA 1st jt btag pT > 130, eta < 2.5"))
      return true;

    if(!Manager()->ApplyCut(LeadingJetSRB,"SRB 1st jt pT > 150, eta < 2.8"))
      return true;
    
    if(!Manager()->ApplyCut(SecondJetSRA,"SRA 2nd jt btag pT > 50, eta < 2.5"))
      return true;
    
    if(!Manager()->ApplyCut(SecondJetSRB,"SRB 2nd jt btag pT > 30, eta < 2.5"))
      return true;

    if(!Manager()->ApplyCut(!ThirdJetSRA,"SRA 3rd+ jt pT > 50, eta < 2.8"))
      return true;
    
    if(!Manager()->ApplyCut(ThirdJetSRB,"SRB 3rd jt btag pT > 30, eta < 2.5"))
      return true;
    
    // Requirement that the leading jet and the missing pT almost back to back in phi,
    // only valid for SRB
    if(!Manager()->ApplyCut((DeltaPhi_pTmiss_J1 > 2.5),"dPhi(MPT,j1) > 2.5"))
      return true;
    
    // Select events with 2 b jets  
    if(!Manager()->ApplyCut((NumBJets == 2),"2 b-jets"))
      return true;
    
    // Cut on MinDeltaPhiJet to reject background multijet events applied to both regions
    if(!Manager()->ApplyCut((MinDeltaPhiJet > 0.4),"dPhimin > 0.4"))
      return true;
    
    // Apply the cut on MET/MEFF in each signal region	
    if(!Manager()->ApplyCut((MET/MEFF_SRA > 0.25),"MET/MEFF (j1,j2) > 0.25"))
      return true;
    
    if(!Manager()->ApplyCut((MET/MEFF_SRB > 0.25),"MET/MEFF (j1,j2,j3) > 0.25"))
      return true;
    
    // Apply the cut on invariant mass of the dibi-jet only in SRA 
    if(!Manager()->ApplyCut((MBB > 200.),"MBB > 200"))
       return true;
    
    // Fill Histo of MCT distribution before MCT cut 
    Manager()->FillHisto("MCT SRA", MCTcorr);//fig3a
    
    // Apply the MCT cut for SRA
    if(!Manager()->ApplyCut((MCTcorr > 150.),"MCT > 150"))
      return true;
    
    if(!Manager()->ApplyCut((MCTcorr > 200.),"MCT > 200"))
	          return true;

    if(!Manager()->ApplyCut((MCTcorr > 250.),"MCT > 250"))
	          return true;

    if(!Manager()->ApplyCut((MCTcorr > 300.),"MCT > 300"))
	          return true;

    if(!Manager()->ApplyCut((MCTcorr > 350.),"MCT > 350"))
	          return true;
    
    // Fill Histo of MBB distribution
    Manager()->FillHisto("MBB SRA and MCT > 150",MBB);//fig3b
    
    // Fill Histo HT3
    Manager()->FillHisto("HT3 SRB no HT3 sel",HT3); //fig4b
    
    // Apply the cut on the hadronic activity only on SRB
    if(!Manager()->ApplyCut((HT3 < 50),"HT3 < 50"))
      return true;
	
    // Fill MET distrib in SRB without MET cut at 250 GeV 
    Manager()->FillHisto("MET SRB no MET sel",MET);// fig4a
    
      
    // Fill Histos for MCT distribution after the complete SRA selection cuts 
    // and the MET distribution after the complete SRB selection cuts.
    Manager()->FillHisto("MCT > 150 SRA",MCTcorr);// figaux_2a
    Manager()->FillHisto("MET full SRB", MET);    // figaux_2b

  }

  return true;
}


// This consists of analysis specific functions (the MCT observable)
TMctLib::TMctLib()
{}

TMctLib::~TMctLib()
{}

double TMctLib::mctcorr(const MALorentzVector v1,const MALorentzVector v2
			,const MALorentzVector vds,const TVector2 ptm
			,const double ecm,const double mxlo)
{
  double v1t[4] = {v1.E(),v1.Px(),v1.Py(),v1.Pz()};
  double v2t[4] = {v2.E(),v2.Px(),v2.Py(),v2.Pz()};
  double vdst[4] = {vds.E(),vds.Px(),vds.Py(),vds.Pz()};
  double ptmt[2] = {ptm.Px(),ptm.Py()};
  return mctcorr(v1t,v2t,vdst,ptmt,ecm,mxlo);
}

double TMctLib::mct(const MALorentzVector v1,const MALorentzVector v2)
{
  double v1t[4] = {v1.E(),v1.Px(),v1.Py(),v1.Pz()};
  double v2t[4] = {v2.E(),v2.Px(),v2.Py(),v2.Pz()};
  return mct(v1t,v2t);
}

double TMctLib::mt2(const MALorentzVector v1,const MALorentzVector v2
			,const MALorentzVector vds,const TVector2 ptm
			,const double ecm,const double mxlo)
{
  double v1t[4] = {v1.E(),v1.Px(),v1.Py(),v1.Pz()};
  double v2t[4] = {v2.E(),v2.Px(),v2.Py(),v2.Pz()};
  double vdst[4] = {vds.E(),vds.Px(),vds.Py(),vds.Pz()};
  double ptmt[2] = {ptm.Px(),ptm.Py()};
  return mt2(v1t,v2t,vdst,ptmt,ecm,mxlo);
}

double TMctLib::mt2neg(const MALorentzVector v1,const MALorentzVector v2
			,const TVector2 ptm,const double mxlo)
{
  double v1t[4] = {v1.E(),v1.Px(),v1.Py(),v1.Pz()};
  double v2t[4] = {v2.E(),v2.Px(),v2.Py(),v2.Pz()};
  double ptmt[2] = {ptm.Px(),ptm.Py()};
  return mt2neg(v1t,v2t,ptmt,mxlo);
}

double TMctLib::mcy(const MALorentzVector v1,const MALorentzVector v2
		    ,const MALorentzVector vds,const TVector2 ptm)
{
  double v1t[4] = {v1.E(),v1.Px(),v1.Py(),v1.Pz()};
  double v2t[4] = {v2.E(),v2.Px(),v2.Py(),v2.Pz()};
  double vdst[4] = {vds.E(),vds.Px(),vds.Py(),vds.Pz()};
  double ptmt[2] = {ptm.Px(),ptm.Py()};
  return mcy(v1t,v2t,vdst,ptmt);
}

double TMctLib::mcx(const MALorentzVector v1,const MALorentzVector v2
		    ,const MALorentzVector vds,const TVector2 ptm)
{
  double v1t[4] = {v1.E(),v1.Px(),v1.Py(),v1.Pz()};
  double v2t[4] = {v2.E(),v2.Px(),v2.Py(),v2.Pz()};
  double vdst[4] = {vds.E(),vds.Px(),vds.Py(),vds.Pz()};
  double ptmt[2] = {ptm.Px(),ptm.Py()};
  return mcx(v1t,v2t,vdst,ptmt);
}


mctlib::mctlib()
{}

mctlib::~mctlib()
{}

double mctlib::mctcorr(const double v1[4],const double v2[4]
		       ,const double vds[4],const double ptm[2]
		       ,const double ecm,const double mxlo)
{
// v1, v2 are the 4-vectors of the two aggregated decay products
// vds is the 4-vector of the downstream objects (excluding v1 and v2)
// ptm is the pTmiss 2-vector {pxmiss,pymiss}
// ecm is the centre-of-mass energy (D=14TeV)
// mxlo is a lower bound on the mass of each invisible decay product (D=0)

  double ptus[2] = {-v1[1]-v2[1]-vds[1]-ptm[0],-v1[2]-v2[2]-vds[2]-ptm[1]};
  m_pb = sqrt(pow(ptus[0],2)+pow(ptus[1],2));

  if (m_pb==0) {

    return mct(v1,v2);    

  } else {

// Transform to new basis in transverse plane
// ISR goes in +ve x direction

    double vb1[4] = {v1[0],(v1[1]*ptus[0]+v1[2]*ptus[1])/m_pb
	      ,(v1[1]*ptus[1]-v1[2]*ptus[0])/m_pb,v1[3]};
    double vb2[4] = {v2[0],(v2[1]*ptus[0]+v2[2]*ptus[1])/m_pb
	      ,(v2[1]*ptus[1]-v2[2]*ptus[0])/m_pb,v2[3]};
    double vey1 = sqrt(fmax(pow(vb1[0],2)-pow(vb1[1],2)-pow(vb1[3],2),0.0));
    double vey2 = sqrt(fmax(pow(vb2[0],2)-pow(vb2[1],2)-pow(vb2[3],2),0.0));
    double ax = vb1[1]*vey2+vb2[1]*vey1;

// Boost v1 and v2 with Ecm
// v1 and v2 were boosted in -ve x direction,
// so to correct we boost v1 and v2 in +ve x direction 

    double beta = m_pb/ecm;
    double gamma = 1.0/sqrt(1.0-beta*beta);
    double vb1p[4] = {gamma*(vb1[0]+vb1[1]*beta),gamma*(vb1[1]+vb1[0]*beta)
		      ,vb1[2],vb1[3]};
    double vb2p[4] = {gamma*(vb2[0]+vb2[1]*beta),gamma*(vb2[1]+vb2[0]*beta)
		      ,vb2[2],vb2[3]};
    double vey1p = sqrt(fmax(pow(vb1p[0],2)-pow(vb1p[1],2)
			     -pow(vb1p[3],2),0.0));
    double vey2p = sqrt(fmax(pow(vb2p[0],2)-pow(vb2p[1],2)
			     -pow(vb2p[3],2),0.0));
    double axecm = vb1p[1]*vey2p+vb2p[1]*vey1p;
    m_mctecm = mct(vb1p,vb2p);

// Boost v1 and v2 with e0
// v1 and v2 were boosted in -ve x direction,
// so to correct we boost v1 and v2 in +ve x direction  

    beta = m_pb/(v1[0]+v2[0]+vds[0]
	       +sqrt(pow(ptm[0],2)+pow(ptm[1],2)+4.0*pow(mxlo,2)));
    gamma = 1.0/sqrt(1.0-beta*beta);
    double vb1pp[4] = {gamma*(vb1[0]+vb1[1]*beta),gamma*(vb1[1]+vb1[0]*beta)
		      ,vb1[2],vb1[3]};
    double vb2pp[4] = {gamma*(vb2[0]+vb2[1]*beta),gamma*(vb2[1]+vb2[0]*beta)
		      ,vb2[2],vb2[3]};
    double vey1pp = sqrt(fmax(pow(vb1pp[0],2)-pow(vb1pp[1],2)
			      -pow(vb1pp[3],2),0.0));
    double vey2pp = sqrt(fmax(pow(vb2pp[0],2)-pow(vb2pp[1],2)
			      -pow(vb2pp[3],2),0.0));
    double axehat = vb1pp[1]*vey2pp+vb2pp[1]*vey1pp;
    m_mctehat = mct(vb1pp,vb2pp);

    if ( (ax>=0) || (axecm>=0) ) {
      return m_mctecm;
    } else {
      if (axehat<0) {
	return m_mctehat;
      } else {    
	return sqrt(fmax(pow(vey1+vey2,2)-pow(vb1[2]-vb2[2],2),0.0));
      }
    }
  }
}

double mctlib::mct(const double v1[4],const double v2[4]) 
{
  double et1 = sqrt(fmax(v1[0]*v1[0]-v1[3]*v1[3],0.0));
  double et2 = sqrt(fmax(v2[0]*v2[0]-v2[3]*v2[3],0.0));
  return sqrt(fmax(pow(et1+et2,2)-pow(v1[1]-v2[1],2)
		      -pow(v1[2]-v2[2],2),0.0));
}

double mctlib::mt2(const double v1[4],const double v2[4]
		       ,const double vds[4],const double ptm[2]
		       ,const double ecm,const double mxlo)
{
  // Boost corrected analytical mt2
  double m1sqr = pow(v1[0],2)-pow(v1[1],2)-pow(v1[2],2)-pow(v1[3],2);
  double m2sqr = pow(v2[0],2)-pow(v2[1],2)-pow(v2[2],2)-pow(v2[3],2);
  double chisqr = pow(mxlo,2);
  double m1 = sqrt(fmax(m1sqr,0.0));
  double m2 = sqrt(fmax(m2sqr,0.0));
  double chi = mxlo;

  double qtest[3] = {0.0,ptm[0]-(chi/m1)*v1[1],ptm[1]-(chi/m1)*v1[2]};
  qtest[0] = sqrt(chisqr+pow(qtest[1],2)+pow(qtest[2],2));
  double ptest[3] = {0.0,ptm[0]-(chi/m2)*v2[1],ptm[1]-(chi/m2)*v2[2]};
  ptest[0] = sqrt(chisqr+pow(ptest[1],2)+pow(ptest[2],2));

  double et1 = sqrt(fmax(v1[0]*v1[0]-v1[3]*v1[3],0.0));
  double et2 = sqrt(fmax(v2[0]*v2[0]-v2[3]*v2[3],0.0));

  double bq[3] = {et2+qtest[0],v2[1]+qtest[1],v2[2]+qtest[2]};
  double ap[3] = {et1+ptest[0],v1[1]+ptest[1],v1[2]+ptest[2]};

  // Use unbalanced solutions
  // This is an approximation as we haven't boost-corrected bq and ap

  if (pow(m1+chi,2)>=pow(bq[0],2)-pow(bq[1],2)-pow(bq[2],2)) {
    return m1+chi;
  } else if (pow(m2+chi,2)>=pow(ap[0],2)-pow(ap[1],2)-pow(ap[2],2)) {
    return m2+chi;
  }

  // Else use balanced solution
  // Note that call to mctcorr also sets m_mctehat, m_mctecm and m_pb

  double mctminsqr = pow(mctcorr(v1,v2,vds,ptm,ecm,mxlo),2);
  double mdmin = mctminmt2(mctminsqr,m1sqr,m2sqr,chisqr);
  if (m_pb == 0) return mdmin;

  double mctecmsqr = pow(m_mctecm,2);
  double mctehatsqr = pow(m_mctehat,2);
  double mctmaxsqr = fmax(mctecmsqr,mctehatsqr);

  double mctdsqr[4] = {(chi*(3.0*m1sqr+m2sqr)+2.0*m1*(m1sqr+m2sqr))/(chi+m1),
		       (chi*(3.0*m1sqr+m2sqr)-2.0*m1*(m1sqr+m2sqr))/(chi-m1),
		       (chi*(3.0*m2sqr+m1sqr)+2.0*m2*(m2sqr+m1sqr))/(chi+m2),
		       (chi*(3.0*m2sqr+m1sqr)-2.0*m2*(m2sqr+m1sqr))/(chi-m2)};
  mdmin = fmin(mdmin,mctminmt2(mctmaxsqr,m1sqr,m2sqr,chisqr));

  for (int i=0;i<4;i++)
    if ( (mctdsqr[i]>mctminsqr) && (mctdsqr[i]<mctmaxsqr) )
      mdmin = fmin(mdmin,mctminmt2(mctdsqr[i],m1sqr,m2sqr,chisqr));
  
  return fmax(fmax(mdmin,m1+chi),m2+chi);
}

double mctlib::mctminmt2(const double mctsqr,const double m1sqr,
			  const double m2sqr, const double chisqr)
{
  double at = 0.5*(mctsqr - m1sqr - m2sqr);
  return sqrt(fmax(chisqr+at+sqrt(fmax((1.0+(4.0*chisqr)/(2.0*at-m1sqr-m2sqr))
				       *(pow(at,2)-m1sqr*m2sqr),0.0)),0.0));
}

double mctlib::mt2neg(const double v1[4],const double v2[4]
		       ,const double ptm[2],const double mxlo)
{
  // Non boost-corrected analytical mt2
  double m1sqr = pow(v1[0],2)-pow(v1[1],2)-pow(v1[2],2)-pow(v1[3],2);
  double m2sqr = pow(v2[0],2)-pow(v2[1],2)-pow(v2[2],2)-pow(v2[3],2);
  double chisqr = pow(mxlo,2);
  double m1 = sqrt(fmax(m1sqr,0.0));
  double m2 = sqrt(fmax(m2sqr,0.0));
  double chi = mxlo;

  double qtest[3] = {0.0,ptm[0]-(chi/m1)*v1[1],ptm[1]-(chi/m1)*v1[2]};
  qtest[0] = sqrt(chisqr+pow(qtest[1],2)+pow(qtest[2],2));
  double ptest[3] = {0.0,ptm[0]-(chi/m2)*v2[1],ptm[1]-(chi/m2)*v2[2]};
  ptest[0] = sqrt(chisqr+pow(ptest[1],2)+pow(ptest[2],2));

  double et1 = sqrt(fmax(v1[0]*v1[0]-v1[3]*v1[3],0.0));
  double et2 = sqrt(fmax(v2[0]*v2[0]-v2[3]*v2[3],0.0));

  double bq[3] = {et2+qtest[0],v2[1]+qtest[1],v2[2]+qtest[2]};
  double ap[3] = {et1+ptest[0],v1[1]+ptest[1],v1[2]+ptest[2]};

  // Use unbalanced solutions
  if (pow(m1+chi,2)>=pow(bq[0],2)-pow(bq[1],2)-pow(bq[2],2)) {
    return m1+chi;
  } else if (pow(m2+chi,2)>=pow(ap[0],2)-pow(ap[1],2)-pow(ap[2],2)) {
    return m2+chi;
  }

  // Else use balanced solution
  double mctminsqr = pow(mct(v1,v2),2);
  double mdmin = mctminmt2(mctminsqr,m1sqr,m2sqr,chisqr);
  
  return fmax(fmax(mdmin,m1+chi),m2+chi);
}


double mctlib::mcy(const double v1[4],const double v2[4]
		       ,const double vds[4],const double ptm[2])
{
// v1, v2 are the 4-vectors of the two aggregated decay products
// vds is the 4-vector of the downstream objects (excluding v1 and v2)
// ptm is the pTmiss 2-vector {pxmiss,pymiss}

  double ptus[2] = {-v1[1]-v2[1]-vds[1]-ptm[0],-v1[2]-v2[2]-vds[2]-ptm[1]};
  double pb = sqrt(pow(ptus[0],2)+pow(ptus[1],2));

  if (pb==0) {

    return mct(v1,v2);    

  } else {

// Transform to new basis in transverse plane
// ISR goes in +ve x direction

    double vb1[4] = {v1[0],(v1[1]*ptus[0]+v1[2]*ptus[1])/pb
	      ,(v1[1]*ptus[1]-v1[2]*ptus[0])/pb,v1[3]};
    double vb2[4] = {v2[0],(v2[1]*ptus[0]+v2[2]*ptus[1])/pb
	      ,(v2[1]*ptus[1]-v2[2]*ptus[0])/pb,v2[3]};
    double vey1 = sqrt(fmax(pow(vb1[0],2)-pow(vb1[1],2)-pow(vb1[3],2),0.0));
    double vey2 = sqrt(fmax(pow(vb2[0],2)-pow(vb2[1],2)-pow(vb2[3],2),0.0));
    return sqrt(fmax(pow(vey1+vey2,2)-pow(vb1[2]-vb2[2],2),0.0));
  }
}

double mctlib::mcx(const double v1[4],const double v2[4]
		       ,const double vds[4],const double ptm[2])
{
// v1, v2 are the 4-vectors of the two aggregated decay products
// vds is the 4-vector of the downstream objects (excluding v1 and v2)
// ptm is the pTmiss 2-vector {pxmiss,pymiss}

  double ptus[2] = {-v1[1]-v2[1]-vds[1]-ptm[0],-v1[2]-v2[2]-vds[2]-ptm[1]};
  double pb = sqrt(pow(ptus[0],2)+pow(ptus[1],2));

  if (pb==0) {

    return mct(v1,v2);    

  } else {

// Transform to new basis in transverse plane
// ISR goes in +ve x direction

    double vb1[4] = {v1[0],(v1[1]*ptus[0]+v1[2]*ptus[1])/pb
	      ,(v1[1]*ptus[1]-v1[2]*ptus[0])/pb,v1[3]};
    double vb2[4] = {v2[0],(v2[1]*ptus[0]+v2[2]*ptus[1])/pb
	      ,(v2[1]*ptus[1]-v2[2]*ptus[0])/pb,v2[3]};
    double vex1 = sqrt(fmax(pow(vb1[0],2)-pow(vb1[2],2)-pow(vb1[3],2),0.0));
    double vex2 = sqrt(fmax(pow(vb2[0],2)-pow(vb2[2],2)-pow(vb2[3],2),0.0));
    return sqrt(fmax(pow(vex1+vex2,2)-pow(vb1[1]-vb2[1],2),0.0));
  }
}


