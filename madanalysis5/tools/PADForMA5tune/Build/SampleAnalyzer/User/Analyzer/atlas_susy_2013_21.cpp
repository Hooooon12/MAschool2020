#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_21.h"
#include "TRandom3.h"
using namespace MA5;
using namespace std;


template<typename T1> void OverlapRmvPT(std::vector<const T1*> &, const double &);
template<typename T1> void OverlapDoubleRmv(std::vector<const T1*> &, const double &);
template<typename T1, typename T2> void OverlapRmv(std::vector<const T1*> &,
  std::vector<const T2*>, const double &);
template<typename T1,typename T2> void OverlapDoubleRmv(std::vector<const T1*> &,
  std::vector<const T2*> &, const double &);
template<typename T1> void KillResonances(std::vector<const T1*> &, const double &);

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_susy_2013_21::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
   // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: ATLAS-SUSY-2013-21             <>" << endmsg;
  INFO << "        <>            Phys- Rev D. 90.052008          <>" << endmsg;
  INFO << "        <>            (stop > c + LSP, monojet + MET) <>" << endmsg;
  INFO << "        <>  Recasted by: D. Sengupta, G. Chalons      <>" << endmsg;
  INFO << "        <>  Contact: dipan@lpsc.in2p3.fr              <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11            <>" << endmsg;
  INFO << "        <>  For more information, see                 <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;



// Specification of signal regions
  Manager()->AddRegionSelection("M1");
  Manager()->AddRegionSelection("M2");
  Manager()->AddRegionSelection("M3");



// Preselection Criteria
  Manager()->AddCut("MET Filter > 80");
//MET > 100 GeV
  Manager()->AddCut("MET > 100 GeV");

// Skipping all trigger related stuff, will be added as a multiplicative factor by hand

//Lepton Veto
  Manager()->AddCut("Lepton veto");

//Njets<4
  Manager()->AddCut("Njets <= 3");

//Delta-phi(E_Tmiss, jets) > 0.4
  Manager()->AddCut("dphij1 > 0.4");
  Manager()->AddCut("dphij2 > 0.4");
  Manager()->AddCut("DeltaPhi(MET,jets) > 0.4");

//Leading Jet p_T > 150 GeV
  Manager()->AddCut("Leading jet pT > 150 GeV");

//MET > 150
  Manager()->AddCut("MET > 150 GeV");

//Defining signal region specific cuts
// Cuts for signal regions M1,M2,M3
// Only the monojet-like analysis is implemented


  string SRM1Cuts[] = {"M1"}; 
  string SRM2Cuts[] = {"M2"};
  string SRM3Cuts[] = {"M3"};

  Manager()->AddCut("pT(j1) > 280 GeV",SRM1Cuts);
  Manager()->AddCut("MET > 220 GeV",SRM1Cuts);

  Manager()->AddCut("pT(j1) > 340 GeV",SRM2Cuts);
  Manager()->AddCut("MET > 340 GeV",SRM2Cuts);

  Manager()->AddCut("pT(j1) > 450 GeV",SRM3Cuts);
  Manager()->AddCut("MET > 450 GeV",SRM3Cuts);

  //Declaration of Histograms
  Manager()->AddHisto("MET presel",17.,150.,1000.); // figaux_09
//   Manager()->AddHisto("MET > 80 GeV",20.,0.,1020.); // figaux_01a
//   Manager()->AddHisto("MET > 80 + pT(jet1) > 290 GeV",20.,0,1020.); // figaux_01b 
  
  Manager()->AddHisto("NJets",5.,-0.5,4.5,"M1"); //figaux_08a
  Manager()->AddHisto("j1 eta",20.,-5.0,5.0,"M1"); // figaux_08b
  Manager()->AddHisto("DeltaPhi(MET,jet1)",25.,0.0,3.2,"M1"); // figaux_08c
//   Manager()->AddHisto("MET M1",26.,220.,1500.,"M1"); // fig_07a
//   Manager()->AddHisto("pT(j1) M1",25.,280.,1500.,"M1"); // fig_07b
  
//   Manager()->AddHisto("MET M2",23.,340.,1500.,"M2"); // fig_07c
//   Manager()->AddHisto("pT(j1) M2",23.,340.,1500.,"M2"); // fig_07d
  
//   Manager()->AddHisto("MET M3",21.,450.,1500.,"M3"); // fig_07e
//   Manager()->AddHisto("pT(j1) M3",21.,450.,1500.,"M3"); // fig_07f
 
  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2013_21::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
//  cout << "BEGIN Finalization" << endl;
  // saving histos
//  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2013_21::Execute(SampleFormat& sample, const EventFormat& event)
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
    vector<const RecLeptonFormat*> myElectrons,myMuons, CandMuons, CandLeptons;
    vector<const RecJetFormat*> CandJets, SignalJets, myJets, SignalBJets;

      //<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // collect jets and leptons with the right pT and eta


     EventFormat myEvent;
     myEvent = event;
// Computation of the MET at the MC level
// This is needed to apply the 80 GeV Filter
// performed at the particle level
        
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
// 80 GeV MET Filter cut at the particle level
// Only useful for comparison with the official cutflows
// on https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-21
// see Fig. 47.
        if(!Manager()->ApplyCut((sum_MET.Pt() > 80.),"MET Filter > 80"))
      return true;




    // Jets are required to have pt> 30 and |eta| < 2.8
    unsigned int Numjetstot = event.rec()->jets().size();
    for(unsigned int ii=0; ii<Numjetstot; ii++)
    {
      const RecJetFormat * CurrentJet = &(event.rec()->jets()[ii]);
      if ( CurrentJet->pt()   > 30 &&
      fabs(CurrentJet->eta()) < 2.8)
        SignalJets.push_back(CurrentJet);
    }

   // Order the jets by pT (if you want to order by something else, e.g. ET, E,
    // etc., add a second argument: ETordering, Eordering, etc.)


   // filling lepton containers
    // electron satify the 'medium' criteria (put in the Delphes card)
    for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ii]);
      double pt = CurrentElectron->pt();
      double abseta = fabs(CurrentElectron->eta());

      if(pt > 20. && abseta < 2.47)
        myElectrons.push_back(CurrentElectron);
    }
    for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
      double pt = CurrentMuon->pt();
      double abseta = fabs(CurrentMuon->eta());

      if(pt > 20. && abseta < 2.4)
        myMuons.push_back(CurrentMuon);
    }

    SORTER->sort(myElectrons);
    SORTER->sort(myMuons);
    SORTER->sort(SignalJets);
    


    OverlapRmvPT(myElectrons,0.05);
    OverlapRmv(SignalJets,myElectrons,0.4);
    OverlapRmv(myElectrons,SignalJets,0.4);
    OverlapRmv(myMuons,SignalJets,0.4);
    OverlapRmv(SignalJets,myElectrons,0.4);
    OverlapDoubleRmv(myMuons,myElectrons,0.01);
    OverlapDoubleRmv(myMuons,0.05);
    unsigned int NumSignalJets = SignalJets.size();

 
// ===========
// isolation criteria
// ===========

// isolation of the electron

    for(int ii=myElectrons.size()-1; ii>=0; ii--)
    {



      // 1) the pT scalar sum of tracks above 400 MeV within a cone a size
      // Delta R = 0.3 around each electron candidate (excluding the electron
      // candidate iself) and associated to the primary vertex is required to
      // be less than 16% of the electron pT

      for(unsigned int jj=0; jj<myElectrons[ii]->isolCones().size(); jj++)
      {
        if(fabs(myElectrons[ii]->isolCones()[jj].deltaR() - 0.2) < 0.001)
        {
          if(myElectrons[ii]->isolCones()[jj].sumPT()
             > .10*myElectrons[ii]->pt())
          {
            myElectrons.erase(myElectrons.begin()+ii);
}
          }
          break;
        }
      }



        // isolation of the muon
    for(int ii=myMuons.size()-1; ii>=0; ii--)

    {
      // the pT scalar sum of tracks above 400 MeV within a cone of size
      // Delta R = 0.3 around the muon candidate and associated to the primary
      // vertex is required to be less than 16% of the muon pT.

      for(unsigned int jj=0; jj<myMuons[ii]->isolCones().size(); jj++)
      {
        if(fabs(myMuons[ii]->isolCones()[jj].deltaR() - 0.2) < 0.001)
        {
          if(myMuons[ii]->isolCones()[jj].sumPT()
             > 1.8)
          {
            myMuons.erase(myMuons.begin()+ii);
          }
          break;
        }
      }
    }

 
   std::vector<const RecLeptonFormat*> SignalLeptons;
    int ne=0, nmu=0;

    for(unsigned int ii=0; ii<myElectrons.size(); ii++)
    {
        SignalLeptons.push_back(myElectrons[ii]);
        ++ne;
    }
    for(unsigned int ii=0; ii<myMuons.size(); ii++)
    {
        SignalLeptons.push_back(myMuons[ii]);
        ++nmu;
    }


    unsigned int NumLeptons = SignalLeptons.size();

    
    // missing transverse momentum:
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET_old = pTmiss.Pt();
    double MET_x = pTmiss.Px();
    double MET_y = pTmiss.Py();

    // Smearing of the MET. The MET is smeared by adding a random vector
    // of magnitude smear_MET distributed over a gaussian of mean one 
    // and width 20 GeV. The smear_x and smear_y components are then obtained from the 
    // the Circle Root method which generates them uniformly.
    // Largely inspired and similar to what is performed in CHECKMATE
    TRandom3 * R = new TRandom3();
    
    double_t smear_MET = R->Gaus(1.,20.);
    double_t smear_x=0.;
    double_t smear_y=0.;
    R->Circle(smear_x,smear_y,smear_MET); 
    
    double new_MET = sqrt(pow(MET_x+smear_x,2)+pow(MET_y+smear_y,2));
    pTmiss.SetPxPyPzE(MET_x+smear_x,MET_y+smear_y,0.,new_MET);
    double MET = pTmiss.Pt();
//     std::cout << " MET_old = " << MET_old << " | " << "MET_new = " << MET << std::endl;
//=========Met weight=============
if (MET<60.)  myEventWeight*=0.;
else if(MET > 60. && MET < 115.)    myEventWeight*=(-133.502 + 8.24539*MET -0.200154*pow(MET,2)   + 0.00238408*pow(MET,3) - 1.3928E-5*pow(MET,4) + 3.19811E-8*pow(MET,5));
//  else myEventWeight*=1;
else if(MET > 115. && MET < 250.)    myEventWeight*=(-11.9738 + 0.321823*MET -0.0032124*pow(MET,2)   + 1.60901E-5*pow(MET,3) - 4.03489E-8*pow(MET,4) + 4.04488E-11*pow(MET,5));
else  myEventWeight*=1.;
//std::cout << "MET = " << MET << " | " << " Event Weight = " << myEventWeight << std::endl;
Manager()->SetCurrentEventWeight(0.85*myEventWeight);   


//  Applying preselection cuts
if(!Manager()->ApplyCut((MET > 100.),"MET > 100 GeV"))
return true;

// Applying lepton veto
if(!Manager()->ApplyCut((NumLeptons == 0),"Lepton veto"))
      return true;

if(!Manager()->ApplyCut((NumSignalJets < 4),"Njets <= 3"))
return true;

double DeltaPhiJet1 = 0.0;
double DeltaPhiJet2 = 0.0 ;
double DeltaPhiJet3 =0.0;
//cout << " numsignaljets " << NumSignalJets<< endl;
if( NumSignalJets > 0) 
{DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2=9999999.9;
DeltaPhiJet3=9999999.9;
}

if( NumSignalJets > 1)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3=999999.9;
}

if( NumSignalJets > 2)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3= SignalJets[2]->dphi_0_pi(pTmiss);
}
//if(NumSignalJets > 1)
//{
//cout << " dphj1, dphij2 , dphij3= " << DeltaPhiJet1 << " " << DeltaPhiJet2 << " " <<DeltaPhiJet3 << endl;
//}



    if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4),"dphij1 > 0.4"))
      return true;

  
   
     if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4),"dphij2 > 0.4"))
      return true;




   if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4),"DeltaPhi(MET,jets) > 0.4"))
      return true;


 
   if(!Manager()->ApplyCut((SignalJets[0]->pt() > 150),"Leading jet pT > 150 GeV"))
   return true;
 
   if(!Manager()->ApplyCut((MET > 150),"MET > 150 GeV"))
   return true;

   Manager()->FillHisto("MET presel",MET);
// Signal Region specific cuts
// SRM1
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 280),"pT(j1) > 280 GeV"))
   return true;
if(!Manager()->ApplyCut((MET > 220),"MET > 220 GeV"))
   return true;

  Manager()->FillHisto("NJets",NumSignalJets);
  Manager()->FillHisto("j1 eta",SignalJets[0]->eta());
  Manager()->FillHisto("DeltaPhi(MET,jet1)",DeltaPhiJet1);

//SRM2
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 340),"pT(j1) > 340 GeV"))
   return true;
if(!Manager()->ApplyCut((MET > 340),"MET > 340 GeV"))
   return true;

//SRM3
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 450),"pT(j1) > 450 GeV"))
   return true;
if(!Manager()->ApplyCut((MET > 450),"MET > 450 GeV"))
   return true;




}  
  return true;
}

////For Overlap Removals


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



// remove both objects if overlap
template<typename T1,typename T2> void OverlapDoubleRmv(std::vector<const T1*> &v1,
  std::vector<const T2*> &v2, const double &DR)
{
  for(int i=v1.size()-1; i>=0; i--)
    for(int j=v2.size()-1; j>=0; j--)
      if(v1[i]->dr(v2[j])<DR)
      {
        v1.erase(v1.begin()+i);
        v2.erase(v2.begin()+j);
        break;
      }
  return;
}


// remove both objects if overlap (in case of overlap with same-type objects)
template<typename T1> void OverlapDoubleRmv(std::vector<const T1*> &v1, const double &DR)
{
  for(int i=v1.size()-1; i>=0; i--)
    for(int j=i-1; j>=0; j--)
      if(v1[i]->dr(v1[j])<DR)
      {
        v1.erase(v1.begin()+i);
        v1.erase(v1.begin()+j);
        i--;
        break;
      }
  return;
}


// remove light resonances for oppose-sign pairs of objects
template<typename T1> void KillResonances(std::vector<const T1*> &v1,
  const double &threshold)
{
  for(int i=v1.size()-1; i>=0; i--)
    for(int j=i-1; j>=0; j--)
    {
      double mll = (v1[i]->momentum()+v1[j]->momentum()).M();
      if( (v1[i]->charge() != v1[j]->charge()) && (mll<threshold) )
      {
        v1.erase(v1.begin()+i);
        v1.erase(v1.begin()+j);
        i--;
        break;
      }
    }
  return;
}

