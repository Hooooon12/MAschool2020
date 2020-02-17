#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_02.h"
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
bool atlas_susy_2013_02::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
   // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: ATLAS-1405_7875              <>" << endmsg;
  INFO << "        <>                         <>" << endmsg;
  INFO << "        <>            (atlas_2_6 jets) <>" << endmsg;
  INFO << "        <>  Recasted by: D. Sengupta                   <>" << endmsg;
  INFO << "        <>  Contact: dipan@lpsc.in2p3.fr            <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11            <>" << endmsg;
  INFO << "        <>  For more information, see                 <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
//   INFO << "        <>  Note that the signal regions 2jl, 4jm, 6jm are not validated or implemented due to lack of validation material" << endmsg;

  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;



// Specification of signal regions
Manager()->AddRegionSelection("2jl");
Manager()->AddRegionSelection("2jm");
Manager()->AddRegionSelection("2jt");
Manager()->AddRegionSelection("3j");
Manager()->AddRegionSelection("4jl");
Manager()->AddRegionSelection("4jm");
Manager()->AddRegionSelection("4jlm");
Manager()->AddRegionSelection("4jt");
Manager()->AddRegionSelection("5j");
Manager()->AddRegionSelection("6jl");
Manager()->AddRegionSelection("6jm");
Manager()->AddRegionSelection("6jt");
Manager()->AddRegionSelection("6jtp");



//=========================================================
// Applied to signal regions 2jl, 2jm,2jt
Manager()->AddCut("MET > 160");
Manager()->AddCut("NJets > 1");
Manager()->AddCut("Nleptons = 0");

  string SR_2Jl[] ={ "2jl"};
  Manager()->AddCut("PTJet1(2jl) > 130",SR_2Jl);
  Manager()->AddCut("PTJet2(2jl) > 60",SR_2Jl);
  Manager()->AddCut("dPhi(J1,MET)(2jl) > 0.4",SR_2Jl);
  Manager()->AddCut("dPhi(J2,MET)(2jl) > 0.4",SR_2Jl);
  Manager()->AddCut("MET/sqrt(HT)(2jl) > 8",SR_2Jl);
  Manager()->AddCut("meff2j > 800",SR_2Jl);






  string SR_2Jm[] ={ "2jm"};
  Manager()->AddCut("PTJet1(2jm) > 130",SR_2Jm);
  Manager()->AddCut("PTJet2(2jm) > 60",SR_2Jm);
  Manager()->AddCut("dPhi(J1,MET)(2jm) > 0.4",SR_2Jm);
  Manager()->AddCut("dPhi(J2,MET)(2jm) > 0.4",SR_2Jm);  
  Manager()->AddCut("MET/sqrt(HT)(2jm) > 15",SR_2Jm);
  Manager()->AddCut("meff2j > 1200",SR_2Jm);

 string SR_2Jt[] ={ "2jt"};

  Manager()->AddCut("PTJet1(2jt) > 130",SR_2Jt);
  Manager()->AddCut("PTJet2(2jt) > 60",SR_2Jt);
  Manager()->AddCut("dPhi(J1,MET)(2jt) > 0.4",SR_2Jt);
  Manager()->AddCut("dPhi(J2,MET)(2jt) > 0.4",SR_2Jt);
  Manager()->AddCut("MET/sqrt(HT)(2jt) > 15",SR_2Jt);
  Manager()->AddCut("meff2j > 1600",SR_2Jt);
//==========================================================
//Applied to the 3 jet signal region

string SR_3J[] ={ "3j" };
  Manager()->AddCut("PTJet1(3J) > 130",SR_3J);
  Manager()->AddCut("PTJet2(3J) > 60",SR_3J);
  Manager()->AddCut("PTJet3(3J) > 60",SR_3J);
  Manager()->AddCut("dPhi(J1,MET)(3J) > 0.4",SR_3J);
  Manager()->AddCut("dPhi(J2,MET)(3J) > 0.4",SR_3J);
  Manager()->AddCut("dPhi(J3,MET)(3J) > 0.4",SR_3J);
  Manager()->AddCut("MET/meff > 0.3",SR_3J);
  Manager()->AddCut("meff3j > 2200", SR_3J);
//===================================================   
string SR_4Jlm[] ={"4jlm"};
  Manager()->AddCut("PTJet1(4jlm) > 130",SR_4Jlm);
  Manager()->AddCut("PTJet2(4jlm) > 60",SR_4Jlm);
  Manager()->AddCut("PTJet3(4jlm) > 60",SR_4Jlm);
  Manager()->AddCut("PTJet4(4jlm) > 60",SR_4Jlm);
  Manager()->AddCut("dPhi(J1,MET)(4jlm) > 0.4",SR_4Jlm);
  Manager()->AddCut("dPhi(J2,MET)(4jlm) > 0.4",SR_4Jlm);
  Manager()->AddCut("dPhi(J3,MET)(4jlm) > 0.4",SR_4Jlm);
  Manager()->AddCut("dPhi(J4,MET)(4jlm) > 0.2",SR_4Jlm);
  Manager()->AddCut("MET/sqrt(HT)(4jlm) > 10",SR_4Jlm);
  Manager()->AddCut("meff4j > 700",SR_4Jlm);


string SR_4Jl[] ={"4jl"};
  Manager()->AddCut("PTJet1(4jl) > 130",SR_4Jl);
  Manager()->AddCut("PTJet2(4jl) > 60",SR_4Jl);
  Manager()->AddCut("PTJet3(4jl) > 60",SR_4Jl);
  Manager()->AddCut("PTJet4(4jl) > 60",SR_4Jl);
  Manager()->AddCut("dPhi(J1,MET)(4jl) > 0.4",SR_4Jl);
  Manager()->AddCut("dPhi(J2,MET)(4jl) > 0.4",SR_4Jl);
  Manager()->AddCut("dPhi(J3,MET)(4jl) > 0.4",SR_4Jl);
  Manager()->AddCut("dPhi(J4,MET)(4jl) > 0.2",SR_4Jl);
  Manager()->AddCut("MET/sqrt(HT) > 10",SR_4Jl);
  Manager()->AddCut("meff4j > 1000",SR_4Jl);



string SR_4Jm[] ={"4jm"};
  Manager()->AddCut("PTJet1(4jm) > 130",SR_4Jm);
  Manager()->AddCut("PTJet2(4jm) > 60",SR_4Jm);
  Manager()->AddCut("PTJet3(4jm) > 60",SR_4Jm);
  Manager()->AddCut("PTJet4(4jm) > 60",SR_4Jm);
  Manager()->AddCut("dPhi(J1,MET)(4jm) > 0.4",SR_4Jm);
  Manager()->AddCut("dPhi(J2,MET)(4jm) > 0.4",SR_4Jm);
  Manager()->AddCut("dPhi(J3,MET)(4jm) > 0.4",SR_4Jm);
  Manager()->AddCut("dPhi(J4,MET)(4jm) > 0.2",SR_4Jm);
  Manager()->AddCut("MET/meff > 0.4",SR_4Jm);
  Manager()->AddCut("meff4j > 1300",SR_4Jm);




//==================================================
string SR_4Jt[] ={ "4jt" };
 Manager()->AddCut("PTJet1(4jt) > 130",SR_4Jt);
  Manager()->AddCut("PTJet2(4jt) > 60",SR_4Jt);
  Manager()->AddCut("PTJet3(4jt) > 60",SR_4Jt);
  Manager()->AddCut("PTJet4(4jt) > 60",SR_4Jt);
  Manager()->AddCut("dPhi(J1,MET)(4jt) > 0.4",SR_4Jt);
  Manager()->AddCut("dPhi(J2,MET)(4jt) > 0.4",SR_4Jt);
  Manager()->AddCut("dPhi(J3,MET)(4jt) > 0.4",SR_4Jt);
  Manager()->AddCut("dPhi(J4,MET)(4jt) > 0.2",SR_4Jt);
  Manager()->AddCut("MET/meff > 0.25",SR_4Jt);
  Manager()->AddCut("meff4j > 2200",SR_4Jt);

//=====================================================



string SR_5J[] ={ "5j"};
  Manager()->AddCut("PTJet1(5J) > 130",SR_5J);
  Manager()->AddCut("PTJet2(5J) > 60",SR_5J);
  Manager()->AddCut("PTJet3(5J) > 60",SR_5J);
  Manager()->AddCut("PTJet4(5J) > 60",SR_5J);
  Manager()->AddCut("PTJet5(5J) > 60",SR_5J);
  Manager()->AddCut("dPhi(J1,MET)(5J) > 0.4",SR_5J);
  Manager()->AddCut("dPhi(J2,MET)(5J) > 0.4",SR_5J);
  Manager()->AddCut("dPhi(J3,MET)(5J) > 0.4",SR_5J);
  Manager()->AddCut("dPhi(J4,MET)(5J) > 0.2",SR_5J);
  Manager()->AddCut("dPhi(J5,MET)(5J) > 0.2",SR_5J);
  Manager()->AddCut("MET/meff > 0.2",SR_5J); 
  Manager()->AddCut("meff5j > 1200",SR_5J);
//=============================================

string SR_6Jl[] ={ "6jl" };

Manager()->AddCut("PTJet1(6jl) > 130",SR_6Jl);
Manager()->AddCut("PTJet2(6jl) > 60",SR_6Jl);
Manager()->AddCut("PTJet3(6jl) > 60",SR_6Jl);
Manager()->AddCut("PTJet4(6jl) > 60",SR_6Jl);
Manager()->AddCut("PTJet5(6jl) > 60",SR_6Jl);
Manager()->AddCut("PTJet6(6jl) > 60",SR_6Jl);
Manager()->AddCut("dPhi(J1,MET)(6jl) > 0.4",SR_6Jl);
Manager()->AddCut("dPhi(J2,MET)(6jl) > 0.4",SR_6Jl);
Manager()->AddCut("dPhi(J3,MET)(6jl) > 0.4",SR_6Jl);
Manager()->AddCut("dPhi(J4,MET)(6jl) > 0.2",SR_6Jl);
Manager()->AddCut("dPhi(J5,MET)(6jl) > 0.2",SR_6Jl);
Manager()->AddCut("dPhi(J6,MET)(6jl) > 0.2",SR_6Jl);
Manager()->AddCut("MET/meff(6jl) > 0.2",SR_6Jl);     
Manager()->AddCut("meff6j > 900",SR_6Jl);
//==========================6Jm=============================//

string SR_6Jm[] ={ "6jm" };



Manager()->AddCut("PTJet1(6jm) > 130",SR_6Jm);
Manager()->AddCut("PTJet2(6jm) > 60",SR_6Jm);
Manager()->AddCut("PTJet3(6jm) > 60",SR_6Jm);
Manager()->AddCut("PTJet4(6jm) > 60",SR_6Jm);
Manager()->AddCut("PTJet5(6jm) > 60",SR_6Jm);
Manager()->AddCut("PTJet6(6jm) > 60",SR_6Jm);
Manager()->AddCut("dPhi(J1,MET)(6jm) > 0.4",SR_6Jm);
Manager()->AddCut("dPhi(J2,MET)(6jm) > 0.4",SR_6Jm);
Manager()->AddCut("dPhi(J3,MET)(6jm) > 0.4",SR_6Jm);
Manager()->AddCut("dPhi(J4,MET)(6jm) > 0.2",SR_6Jm);
Manager()->AddCut("dPhi(J5,MET)(6jm) > 0.2",SR_6Jm);
Manager()->AddCut("dPhi(J6,MET)(6jm) > 0.2",SR_6Jm);
Manager()->AddCut("MET/meff(6jm) > 0.2",SR_6Jm);
Manager()->AddCut("meff6j > 1200",SR_6Jm);





//===================================================
string SR_6Jt[] ={ "6jt" };
Manager()->AddCut("PTJet1(6jt) > 130",SR_6Jt);
Manager()->AddCut("PTJet2(6jt) > 60",SR_6Jt);
Manager()->AddCut("PTJet3(6jt) > 60",SR_6Jt);
Manager()->AddCut("PTJet4(6jt) > 60",SR_6Jt);
Manager()->AddCut("PTJet5(6jt) > 60",SR_6Jt);
Manager()->AddCut("PTJet6(6jt) > 60",SR_6Jt);
Manager()->AddCut("dPhi(J1,MET)(6jt) > 0.4",SR_6Jt);
Manager()->AddCut("dPhi(J2,MET)(6jt) > 0.4",SR_6Jt);
Manager()->AddCut("dPhi(J3,MET)(6jt) > 0.4",SR_6Jt);
Manager()->AddCut("dPhi(J4,MET)(6jt) > 0.2",SR_6Jt);
Manager()->AddCut("dPhi(J5,MET)(6jt) > 0.2",SR_6Jt);
Manager()->AddCut("dPhi(J6,MET)(6jt) > 0.2",SR_6Jt);
Manager()->AddCut("MET/meff(6jt) > 0.25",SR_6Jt);
Manager()->AddCut("meff6j > 1500",SR_6Jt);
//================6jtp===========================
string SR_6Jtp[] ={ "6jtp" };
Manager()->AddCut("PTJet1(6jtp) > 130",SR_6Jtp);
Manager()->AddCut("PTJet2(6jtp) > 60",SR_6Jtp);
Manager()->AddCut("PTJet3(6jtp) > 60",SR_6Jtp);
Manager()->AddCut("PTJet4(6jtp) > 60",SR_6Jtp);
Manager()->AddCut("PTJet5(6jtp) > 60",SR_6Jtp);
Manager()->AddCut("PTJet6(6jtp) > 60",SR_6Jtp);
Manager()->AddCut("dPhi(J1,MET)(6jtp) > 0.4",SR_6Jtp);
Manager()->AddCut("dPhi(J2,MET)(6jtp) > 0.4",SR_6Jtp);
Manager()->AddCut("dPhi(J3,MET)(6jtp) > 0.4",SR_6Jtp);
Manager()->AddCut("dPhi(J4,MET)(6jtp) > 0.2",SR_6Jtp);
Manager()->AddCut("dPhi(J5,MET)(6jtp) > 0.2",SR_6Jtp);
Manager()->AddCut("dPhi(J6,MET)(6jtp) > 0.2",SR_6Jtp);
Manager()->AddCut("MET/meff(6jtp) > 0.15",SR_6Jtp);
Manager()->AddCut("meff6j > 1700",SR_6Jtp);






//====================================================
   



  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2013_02::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
//  cout << "BEGIN Finalization" << endl;
  // saving histos
//  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2013_02::Execute(SampleFormat& sample, const EventFormat& event)
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



    // Jets are required to have pt> 40 and |eta| < 2.8
    unsigned int Numjetstot = event.rec()->jets().size();

    double HT = 0;  
    double meff=0;

    for(unsigned int ii=0; ii<Numjetstot; ii++)
    {
      const RecJetFormat * CurrentJet = &(event.rec()->jets()[ii]);
      if ( CurrentJet->pt()   > 40 &&
      fabs(CurrentJet->eta()) < 2.8)
       SignalJets.push_back(CurrentJet);
        HT +=  CurrentJet->pt();
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
    unsigned int NumSignalJets = SignalJets.size();


    OverlapRmvPT(myElectrons,0.05);
    OverlapRmv(SignalJets,myElectrons,0.4);
    OverlapRmv(myElectrons,SignalJets,0.4);
    OverlapRmv(myMuons,SignalJets,0.4);
    OverlapRmv(SignalJets,myElectrons,0.4);
    OverlapDoubleRmv(myMuons,myElectrons,0.01);
    OverlapDoubleRmv(myMuons,0.05);


 
// ===========
// isolation criteria
// ===========

// isolation of the electron

    for(int ii=myElectrons.size()-1; ii>=0; ii--)
    {




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
    unsigned int NumJets = SignalJets.size();

  


    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();

     meff = HT + MET;

     
     
    double metht= MET/sqrt(HT);
    double meteff1J = 0.0 ;
    double meteff2J = 0.0 ;
    double meteff3J = 0.0 ;
    double meteff4J = 0.0 ; 
    double meteff5J = 0.0 ;
    double meteff6J =0.0  ;    
      
    if(NumJets > 0 )  meteff1J= MET/(SignalJets[0]->pt());
    if(NumJets > 1)  meteff2J= MET/( SignalJets[0]->pt() + SignalJets[1]->pt() + MET );
    if(NumJets > 2)  meteff3J= MET/(SignalJets[0]->pt() + SignalJets[1]->pt()+ SignalJets[2]->pt() + MET ) ;
    if(NumJets > 3)  meteff4J= MET/(SignalJets[0]->pt() + SignalJets[1]->pt()+ SignalJets[2]->pt()+SignalJets[3]->pt() + MET  );
    if(NumJets > 4)  meteff5J= MET/(SignalJets[0]->pt() + SignalJets[1]->pt()+ SignalJets[2]->pt()+SignalJets[3]->pt() + SignalJets[4]->pt() + MET  ) ;
    if(NumJets  > 5)  meteff6J= MET/ ( SignalJets[0]->pt() + SignalJets[1]->pt()+ SignalJets[2]->pt()+SignalJets[3]->pt() + SignalJets[4]->pt() + SignalJets[5]->pt() + MET ) ;


//  Applying preselection cuts

double DeltaPhiJet1 = 0.0;
if( NumJets > 0) 
{DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
}

double DeltaPhiJet2 = 999999.9;
if( NumJets > 1)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
}

double DeltaPhiJet3 = 999999.9;

if( NumJets > 2)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3= SignalJets[2]->dphi_0_pi(pTmiss);
}

double DeltaPhiJet4 = 999999.9;
if( NumSignalJets > 3)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3= SignalJets[2]->dphi_0_pi(pTmiss);
DeltaPhiJet4= SignalJets[3]->dphi_0_pi(pTmiss);
}

double DeltaPhiJet5 = 999999.9;

if( NumSignalJets > 4)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3= SignalJets[2]->dphi_0_pi(pTmiss);
DeltaPhiJet4= SignalJets[3]->dphi_0_pi(pTmiss);
DeltaPhiJet5= SignalJets[4]->dphi_0_pi(pTmiss);
}

double DeltaPhiJet6 = 999999.9;
if( NumSignalJets > 5)
{
DeltaPhiJet1= SignalJets[0]->dphi_0_pi(pTmiss);
DeltaPhiJet2= SignalJets[1]->dphi_0_pi(pTmiss);
DeltaPhiJet3= SignalJets[2]->dphi_0_pi(pTmiss);
DeltaPhiJet4= SignalJets[3]->dphi_0_pi(pTmiss);
DeltaPhiJet5= SignalJets[4]->dphi_0_pi(pTmiss);
DeltaPhiJet6= SignalJets[5]->dphi_0_pi(pTmiss);
}

//==================================================================

if(!Manager()->ApplyCut((MET > 160),"MET > 160"))
   return true;

if(!Manager()->ApplyCut((NumJets > 1),"NJets > 1"))
   return true;

if(!Manager()->ApplyCut((NumLeptons == 0),"Nleptons = 0"))
   return true;




//==============================2Jl========================================
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(2jl) > 130"))
   return true;

if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(2jml > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(2jl) > 0.4"))
   return true;

if (!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(2jl) > 0.4"))
return true ;
if(!Manager()->ApplyCut((metht > 8),"MET/sqrt(HT)(2jl) > 8"))
   return true;
if(!Manager()->ApplyCut((meff> 800),"meff2j > 800"))
   return true;












//==============================2Jm========================================
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(2jm) > 130"))
   return true;

if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(2jm) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(2jm) > 0.4"))
   return true;

if (!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(2jm) > 0.4"))
return true ;
if(!Manager()->ApplyCut((metht > 15),"MET/sqrt(HT)(2jm) > 15"))
   return true;
if(!Manager()->ApplyCut((meff> 1200),"meff2j > 1200"))
   return true;


//==========================2Jt=============================================
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(2jt) > 130"))
   return true;
if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(2jt) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(2jt) > 0.4"))
   return true;

if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(2jt) > 0.4"))
   return true;
if(!Manager()->ApplyCut((metht > 15),"MET/sqrt(HT)(2jt) > 15"))
   return true;
if(!Manager()->ApplyCut((meff> 1600),"meff2j > 1600"))
   return true;

//================================3J==================================
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(3J) > 130"))
   return true;

if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(3J) > 60"))
   return true;
if(NumJets > 2 ){
if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(3J) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(3J) > 0.4"))
   return true;

if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(3J) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(3J) > 0.4"))
   return true;
if(!Manager()->ApplyCut((meteff3J > 0.3  ),"MET/meff > 0.3"))
   return true;
if(!Manager()->ApplyCut((meff > 2200  ),"meff3j > 2200"))
   return true;
}
//==================================4Jlm===================================
//if(NumJets > 3 ){
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(4jlm) > 130"))
return true;
if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(4jlm) > 60"))
return true;
if(NumJets > 2 ){
if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(4jlm) > 60"))
return true;
if(NumJets > 3 ){
if(!Manager()->ApplyCut((SignalJets[3]->pt() > 60),"PTJet4(4jlm) > 60"))
 return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(4jlm) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(4jlm) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(4jlm) > 0.4"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.2  ),"dPhi(J4,MET)(4jlm) > 0.2"))
return true;
if(!Manager()->ApplyCut((metht > 10  ),"MET/sqrt(HT)(4jlm) > 10"))
   return true;
if(!Manager()->ApplyCut((meff > 700  ),"meff4j > 700"))
  return true;
//==============================4Jl======================================
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(4jl) > 130"))
return true;
if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(4jl) > 60"))
return true;
if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(4jl) > 60"))
return true;
if(!Manager()->ApplyCut((SignalJets[3]->pt() > 60),"PTJet4(4jl) > 60"))
 return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(4jl) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(4jl) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(4jl) > 0.4"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.2  ),"dPhi(J4,MET)(4jl) > 0.2"))
return true;
if(!Manager()->ApplyCut((metht > 10  ),"MET/sqrt(HT) > 10"))
   return true;
if(!Manager()->ApplyCut((meff > 1000  ),"meff4j > 1000"))
   return true;


//==================4Jt========================================================
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(4jt) > 130"))
   return true;
if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(4jt) > 60"))
   return true;
if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(4jt) > 60"))
   return true;
if(!Manager()->ApplyCut((SignalJets[3]->pt() > 60),"PTJet4(4jt) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(4jt) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(4jt) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(4jt) > 0.4"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.2  ),"dPhi(J4,MET)(4jt) > 0.2"))
return true;
if(!Manager()->ApplyCut((meteff4J > 0.25  ),"MET/meff > 0.25"))
   return true;
if(!Manager()->ApplyCut((meff > 2200  ),"meff4j > 2200"))
  return true;
}
}
//if(NumJets > 4){ 
//===================================5J======================================
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(5J) > 130"))
   return true;
if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(5J) > 60"))
   return true;
if(NumJets > 2 ){
if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(5J) > 60"))
   return true;
if(NumJets > 3 ){
if(!Manager()->ApplyCut((SignalJets[3]->pt() > 60),"PTJet4(5J) > 60"))
   return true;
if(NumJets > 4 ){
if(!Manager()->ApplyCut((SignalJets[4]->pt() > 60),"PTJet5(5J) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(5J) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(5J) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(5J) > 0.4"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.2  ),"dPhi(J4,MET)(5J) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet5 > 0.2  ),"dPhi(J5,MET)(5J) > 0.2"))
return true;
if(!Manager()->ApplyCut((meteff5J > 0.2  ),"MET/meff > 0.2"))
   return true;
if(!Manager()->ApplyCut((meff > 1200  ),"meff5j > 1200"))
  return true;
}
}
}

//if(NumJets > 5 ){
//================================6Jl=========================================
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(6jl) > 130"))
   return true;

if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(6jl) > 60"))
   return true;
if(NumJets > 2 ){
if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(6jl) > 60"))
   return true;
if(NumJets > 3 ){
if(!Manager()->ApplyCut((SignalJets[3]->pt() > 60),"PTJet4(6jl) > 60"))
   return true;
if(NumJets > 4 ){
if(!Manager()->ApplyCut((SignalJets[4]->pt() > 60),"PTJet5(6jl) > 60"))
   return true;
if(NumJets > 5 ){
if(!Manager()->ApplyCut((SignalJets[5]->pt() > 60),"PTJet6(6jl) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(6jl) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(6jl) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(6jl) > 0.4"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.2  ),"dPhi(J4,MET)(6jl) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet5 > 0.2  ),"dPhi(J5,MET)(6jl) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet6 > 0.2  ),"dPhi(J6,MET)(6jl) > 0.2"))
return true;
if(!Manager()->ApplyCut((meteff6J > 0.2  ),"MET/meff(6jl) > 0.2"))
   return true;
if(!Manager()->ApplyCut((meff > 900  ),"meff6j > 900"))
   return true;
//================================6Jm=========================================
}}}}
if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(6jm) > 130"))
   return true;

if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(6jlm) > 60"))
   return true;
if(NumJets > 2 ){
if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(6jm) > 60"))
   return true;
if(NumJets > 3 ){
if(!Manager()->ApplyCut((SignalJets[3]->pt() > 60),"PTJet4(6jm) > 60"))
   return true;
if(NumJets > 4 ){
if(!Manager()->ApplyCut((SignalJets[4]->pt() > 60),"PTJet5(6jm) > 60"))
   return true;
if(NumJets > 5 ){
if(!Manager()->ApplyCut((SignalJets[5]->pt() > 60),"PTJet6(6jm) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(6jm) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(6jm) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(6jm) > 0.4"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.2  ),"dPhi(J4,MET)(6jm) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet5 > 0.2  ),"dPhi(J5,MET)(6jm) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet6 > 0.2  ),"dPhi(J6,MET)(6jm) > 0.2"))
return true;
if(!Manager()->ApplyCut((meteff6J > 0.2  ),"MET/meff(6jm) > 0.2"))
   return true;
if(!Manager()->ApplyCut((meff > 900  ),"meff6j > 1200"))
   return true;






//============================6jt====================================

if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(6jt) > 130"))
   return true;

if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(6jt) > 60"))
   return true;

if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(6jt) > 60"))
   return true;
if(!Manager()->ApplyCut((SignalJets[3]->pt() > 60),"PTJet4(6jt) > 60"))
   return true;
if(!Manager()->ApplyCut((SignalJets[4]->pt() > 60),"PTJet5(6jt) > 60"))
   return true;
if(!Manager()->ApplyCut((SignalJets[5]->pt() > 60),"PTJet6(6jt) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(6jt) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(6jt) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(6jt) > 0.4"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.2  ),"dPhi(J4,MET)(6jt) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet5 > 0.2  ),"dPhi(J5,MET)(6jt) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet6 > 0.2  ),"dPhi(J6,MET)(6jt) > 0.2"))
return true;
if(!Manager()->ApplyCut((meteff6J > 0.25  ),"MET/meff(6jt) > 0.25"))
   return true;
if(!Manager()->ApplyCut((meff > 1500  ),"meff6j > 1500"))
   return true;
//============================6jtp===================================================

if(!Manager()->ApplyCut((SignalJets[0]->pt() > 130),"PTJet1(6jtp) > 130"))
   return true;

if(!Manager()->ApplyCut((SignalJets[1]->pt() > 60),"PTJet2(6jtp) > 60"))
   return true;

if(!Manager()->ApplyCut((SignalJets[2]->pt() > 60),"PTJet3(6jtp) > 60"))
   return true;
if(!Manager()->ApplyCut((SignalJets[3]->pt() > 60),"PTJet4(6jtp) > 60"))
   return true;
if(!Manager()->ApplyCut((SignalJets[4]->pt() > 60),"PTJet5(6jtp) > 60"))
   return true;
if(!Manager()->ApplyCut((SignalJets[5]->pt() > 60),"PTJet6(6jtp) > 60"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet1 > 0.4  ),"dPhi(J1,MET)(6jtp) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet2 > 0.4  ),"dPhi(J2,MET)(6jtp) > 0.4"))
   return true;
if(!Manager()->ApplyCut((DeltaPhiJet3 > 0.4  ),"dPhi(J3,MET)(6jtp) > 0.4"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet4 > 0.2  ),"dPhi(J4,MET)(6jtp) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet5 > 0.2  ),"dPhi(J5,MET)(6jtp) > 0.2"))
return true;
if(!Manager()->ApplyCut((DeltaPhiJet6 > 0.2  ),"dPhi(J6,MET)(6jtp) > 0.2"))
return true;
if(!Manager()->ApplyCut((meteff6J > 0.25  ),"MET/meff(6jtp) > 0.15"))
   return true;
if(!Manager()->ApplyCut((meff > 1500  ),"meff6j > 1700"))
   return true;



}
}
}
}  

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

