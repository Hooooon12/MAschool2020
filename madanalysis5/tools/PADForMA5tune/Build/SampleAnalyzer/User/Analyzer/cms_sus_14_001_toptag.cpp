#include "SampleAnalyzer/User/Analyzer/cms_sus_14_001_toptag.h"

using namespace MA5;
using namespace std;

double CalcSumpT(const RecLeptonFormat* myLepton, double conesize)
{
  double SumpT=0;
  for(unsigned ii=0; ii<myLepton->isolCones().size(); ii++)
    {
      if(fabs(myLepton->isolCones()[ii].deltaR() - conesize)<0.0001)
	SumpT=myLepton->isolCones()[ii].sumPT();
    }
  return SumpT;
}

double DeltaPhi(double phi1, double phi2) {
  double result = phi1 - phi2;
  while (result > M_PI)    result -= 2 * M_PI;
  while (result <= -M_PI)  result += 2 * M_PI;
  return result;
}

double DeltaR(double eta1, double phi1, double eta2, double phi2) {
  double deta = eta1 - eta2;
  double dphi = DeltaPhi(phi1, phi2);
  return std::sqrt(deta*deta + dphi*dphi);
}

double CalcDeltaR(const MALorentzVector& v1, const MALorentzVector& v2)
{
  double deltaR=DeltaR(v1.Eta(),v1.Phi(),v2.Eta(),v2.Phi());
  return deltaR;
}
//static const double TOP_MASS = 173.4;//Sam: Changing this actually made a 10% difference!
static const double TOP_MASS = 173.1;
static const double W_MASS = 80.4;
static const double BQuark_MASS = 4;
const double myratio = W_MASS/TOP_MASS;
double Rmin;//I moved the initialization of these because somehow they were 10^125 in execute.
double Rmax;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_sus_14_001_toptag::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: CMS-SUS-14-001,<arXiv:1503.08037          <>" << endmsg;
  INFO << "        <>  (stop search, all hadronic with t-tags)             <>" << endmsg;
  INFO << "        <>  Recasted by: P.Atmasiddha, S.Bein & C.Sharma        <>" << endmsg;
  INFO << "        <>  Contact: prachi.atmariddha@students.iiserpune.ac.in <>" << endmsg;
  INFO << "        <>           samuel.bein@gmail.com                      <>" << endmsg;
  INFO << "        <>           seema@iiserpune.ac.in                      <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11                      <>" << endmsg;
  INFO << "        <>  For more information, see                           <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;


  // initialize variables, histos

  Rmin=0.85*myratio;
  Rmax=1.25*myratio;

  Manager()->AddRegionSelection("MET200-350, Nbjets=1");
  Manager()->AddRegionSelection("MET>350, Nbjets=1");
  Manager()->AddRegionSelection("MET200-350, Nbjets>1");
  Manager()->AddRegionSelection("MET>350, Nbjets>1");

  // Declare cuts. 


  Manager()->AddCut("No Mu");
  Manager()->AddCut("No Ele");
  Manager()->AddCut("Njet70>1");
  Manager()->AddCut("Njet50>3");
  Manager()->AddCut("Njet30>4");
  Manager()->AddCut("MinDeltaPhi");
  Manager()->AddCut("Nbjets>0");
  Manager()->AddCut("MET>200");
  Manager()->AddCut("Top Reco");
  Manager()->AddCut("MTsum>500");


  //Declare the SR-defining cuts
  std::string SR1_Cut[] = 
    {
      "MET200-350, Nbjets=1"
    };
  Manager()->AddCut("SR1_Cut",SR1_Cut);

  std::string SR2_Cut[] = 
    {
      "MET>350, Nbjets=1"
    };
  Manager()->AddCut("SR2_Cut",SR2_Cut);

  std::string SR3_Cut[] = 
    {
      "MET200-350, Nbjets>1"
    };
  Manager()->AddCut("SR3_Cut",SR3_Cut);

  string SR4_Cut[] = 
    {
      "MET>350, Nbjets>1"
    };
  Manager()->AddCut("SR4_Cut",SR4_Cut);


  // Declare Histograms.

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_sus_14_001_toptag::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  // saving histos
  return;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_sus_14_001_toptag::Execute(SampleFormat& sample, const EventFormat& event)
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

if(event.rec()!=0)
  {

    double MT2, MT_3Jet, MT_Rsys;
    //===============================================================//
    // Define collection of objects.. 
    //===============================================================//

    // Define empty containers:
    vector<const RecLeptonFormat*> IsoElectrons, IsoMuons;
    vector<const RecJetFormat*> myJets;
 
 // Fill muons container :
    for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
      {
        const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
	double pt= CurrentMuon->momentum().Pt();
	double abseta= fabs(CurrentMuon->momentum().Eta());
	if((pt>5) && (abseta<2.1) && (((CalcSumpT(CurrentMuon,0.2))/pt)<9.5))
	  IsoMuons.push_back(CurrentMuon);
      }

	// Fill electrons container :
	for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
	  {
        const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ii]);
	double pt= CurrentElectron->momentum().Pt();
	double abseta= fabs(CurrentElectron->momentum().Eta());
	if((pt>5 && abseta<1.44 && ((CalcSumpT(CurrentElectron, 0.2))/pt)<6.2) || (pt>5 && (abseta>1.56 && abseta<2.5) && ((CalcSumpT(CurrentElectron, 0.3)/pt)<6.2)))
	  
	   IsoElectrons.push_back(CurrentElectron);
	  }

   // Fill Jet container : 
	int NumJetsPtAbv70GeV=0;
	int NumJetsPtAbv50GeV=0;
	int NumJetsPtAbv30GeV=0;
//	int Njets=event.rec()->jets().size();

	for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
	  {
	    const RecJetFormat *CurrentJet= &(event.rec()->jets()[ii]);
	    double pt=CurrentJet->momentum().Pt();
	    double abseta=fabs(CurrentJet->momentum().Eta());
            if(pt>30 && abseta<2.4)
	      myJets.push_back(CurrentJet);
	    if(abseta<2.4)
	      {
	        if(pt>30)
		  NumJetsPtAbv30GeV++;
		if(pt>50)
		  NumJetsPtAbv50GeV++;
		if(pt>70)
		  NumJetsPtAbv70GeV++;
	      }
	  }
	SORTER->sort(myJets);
    
       //============ Missing Transverse Momentum================= //
	      MALorentzVector pTmiss = event.rec()->MET().momentum();
	      double MET = pTmiss.Pt();   
	     
       //============Calculating number of b-jets ================ //
	      int Nbjets=0;
	      for(unsigned int ii=0; ii<myJets.size(); ii++)
		{
		  const RecJetFormat *CurrentJet = myJets[ii];
		  
		    if(CurrentJet->btag())
		    Nbjets++;
		   
		}

 

	      //==============Apply Cuts=================//


	      //==============Apply cut 1: MuonVeto ============//
  
  if(!Manager()->ApplyCut((IsoMuons.size() == 0), "No Mu")) return true;
 
  //====================Apply Cut 2: ElectronVeto===================//

  if(!Manager()->ApplyCut((IsoElectrons.size()==0), "No Ele")) return true;

  //====================Apply Cut 3: NJets(pT>70GeV)>=2===============//
  if(!Manager()->ApplyCut((NumJetsPtAbv70GeV>=2), "Njet70>1")) return true;
 
  //====================Apply Cut 4: NJets(pT>50GeV)>=4==============//
  if(!Manager()->ApplyCut((NumJetsPtAbv50GeV>=4), "Njet50>3")) return true;

  //====================Apply Cut 5: NJets(pT>30GeV)>=5 ===============//
  if(!Manager()->ApplyCut((NumJetsPtAbv30GeV>=5), "Njet30>4")) return true;
        

  //====================Apply Cut 6: delphi(pT(j),pTmiss) ===============//
  if(!Manager()->ApplyCut((myJets[0]->dphi_0_pi(pTmiss)>0.5 && myJets[1]->dphi_0_pi(pTmiss)>0.5 && myJets[2]->dphi_0_pi(pTmiss)>0.3), "MinDeltaPhi")) return true;

  //===================Apply Cut 7: Nbjets>=1 =====================//
  if(!Manager()->ApplyCut((Nbjets>=1), "Nbjets>0")) return true;

  //===================Apply Cut 8: MET>200GeV ======================//
  if(!Manager()->ApplyCut((MET>200),"MET>200")) return true;
  		
  //====================== Full top reconstruction===========================//
 
  const RecJetFormat* FullTopCand_1[120][3];
  unsigned int Row_rank_1=0;
  
  //====================3 Jet Candidates =====================//


  for(unsigned int ii=0; ii<myJets.size(); ii++)//original Prachi
    {
      for(unsigned int jj=ii+1; jj<myJets.size(); jj++)
         {
         for(unsigned int kk=jj+1; kk<myJets.size(); kk++)
            {
  	      double M_12, M_23, M_13, M_123;
              MALorentzVector Sys_3Jet= myJets[ii]->momentum()+myJets[jj]->momentum()+myJets[kk]->momentum();

  	      M_12=(myJets[ii]->momentum()+myJets[jj]->momentum()).M();
  	      M_23=(myJets[jj]->momentum()+myJets[kk]->momentum()).M();
              M_13=(myJets[ii]->momentum()+myJets[kk]->momentum()).M();
              M_123=(myJets[ii]->momentum()+myJets[jj]->momentum()+myJets[kk]->momentum()).M();
             
  	      if(CalcDeltaR(Sys_3Jet,myJets[ii]->momentum())<1.5 && CalcDeltaR(Sys_3Jet,myJets[jj]->momentum())<1.5 && CalcDeltaR(Sys_3Jet,myJets[kk]->momentum())<1.5)
  		{
  		  if(Sys_3Jet.M()>80 && Sys_3Jet.M()<270)
  		    {
    
  		      if(((0.2<atan(M_13/M_12) && atan(M_13/M_12)<1.3) && (Rmin<(M_23/M_123) && (M_23/M_123)<Rmax)) || ((pow(Rmin,2)*(1+(pow((M_13/M_12),2))))<(1-(pow((M_23/M_123),2))) && (1-(pow((M_23/M_123),2)))<(pow(Rmax,2)*(1+(pow((M_13/M_12),2)))) && (M_23/M_123)>0.35) || ((pow(Rmin,2)*(1+pow((M_12/M_13),2)))<(1-pow((M_23/M_123),2)) && (1-pow((M_23/M_123),2))<(pow(Rmax,2)*(1+pow((M_12/M_13),2))) && (M_23/M_123)>0.35))
  			{
    
  	  FullTopCand_1[Row_rank_1][0]=myJets[ii];
          FullTopCand_1[Row_rank_1][1]=myJets[jj];
          FullTopCand_1[Row_rank_1][2]=myJets[kk];
  	  Row_rank_1++;
  			}
		    
  		    }
  		}
  	    }
  	 }	 
    }
  
 const RecJetFormat* FullTopCand_1F[Row_rank_1][3];
 for(unsigned int ii=0; ii<Row_rank_1; ii++)
   {
     FullTopCand_1F[ii][0]=FullTopCand_1[ii][0];
     FullTopCand_1F[ii][1]=FullTopCand_1[ii][1];
     FullTopCand_1F[ii][2]=FullTopCand_1[ii][2];
   }


 //====================B-tagged jet in Rsys criterian ========================// 


 unsigned int No_Rows_1=sizeof(FullTopCand_1F)/sizeof(FullTopCand_1F[0]);
 if(No_Rows_1==0) 
   {
     return false;
   }

  
  const RecJetFormat* FullTopCand_2[No_Rows_1][3];
  unsigned int Row_rank_2=0;
  int Nbjets_Rsys;
  for(unsigned int ii=0; ii<No_Rows_1; ii++)
     {
      vector<const RecJetFormat*> CurrentRsys=(myJets);
	      for(int jj=myJets.size()-1; jj>=0; jj--)
		{
		  if(FullTopCand_1F[ii][0]==CurrentRsys[jj])
                    CurrentRsys.erase(CurrentRsys.begin()+jj);
		  else if(FullTopCand_1F[ii][1]==CurrentRsys[jj])
                    CurrentRsys.erase(CurrentRsys.begin()+jj);
		  else if(FullTopCand_1F[ii][2]==CurrentRsys[jj])
                    CurrentRsys.erase(CurrentRsys.begin()+jj);
	        
		}

              Nbjets_Rsys=0;
	      for(unsigned int ll=0; ll<CurrentRsys.size(); ll++)
		{
		  
		  if(CurrentRsys[ll]->btag())
		    Nbjets_Rsys++;
		}
	      if(Nbjets_Rsys>0)
		{
		  for(int kk=0; kk<3; kk++)
		    {
		     FullTopCand_2[Row_rank_2][kk]=FullTopCand_1F[ii][kk];
		    }
		  Row_rank_2++;
		}
    }
 if(Row_rank_2==0) 
   {
     return false;
   }

 const RecJetFormat* FullTopCand_2F[Row_rank_2][3];
 for(unsigned int ii=0; ii<Row_rank_2; ii++)
   {
     FullTopCand_2F[ii][0]=FullTopCand_2[ii][0];
     FullTopCand_2F[ii][1]=FullTopCand_2[ii][1];
     FullTopCand_2F[ii][2]=FullTopCand_2[ii][2];
     }

 //=================Additional: bjet criterian for the 3 jet system===========//

 const RecJetFormat* FullTopCand_3[Row_rank_2][3];
 unsigned int Row_rank_3=0;
 for(unsigned int ii=0;ii<Row_rank_2;ii++)
   {
    if(Nbjets>=2)
     {
       int no_bjets=0;
       for(int kk=0; kk<3; kk++)
       { 
         if(FullTopCand_2F[ii][kk]->btag())
	   {
             no_bjets++;
	   }
       }
       if(no_bjets>0)/////Sam: this was ==1. I think we want at least 1 b-jet in TriJet, but more is OK.
	 {
          for(int kk=0; kk<3; kk++)
	     {
               
	       FullTopCand_3[Row_rank_3][kk]=FullTopCand_2F[ii][kk];
	     }
             Row_rank_3++;
	 }
       else 
             continue;
     }
     else 
       {
         FullTopCand_3[Row_rank_3][0]=FullTopCand_2F[ii][0];
         FullTopCand_3[Row_rank_3][1]=FullTopCand_2F[ii][1];
         FullTopCand_3[Row_rank_3][2]=FullTopCand_2F[ii][2];
         Row_rank_3++;
       }
   }
 if(Row_rank_3==0)
   {
     return false;
   }


 const RecJetFormat* FullTopCand_3F[Row_rank_3][3];
 for(unsigned int ii=0; ii<Row_rank_3; ii++)
   {
     FullTopCand_3F[ii][0]=FullTopCand_3[ii][0];
     FullTopCand_3F[ii][1]=FullTopCand_3[ii][1];
     FullTopCand_3F[ii][2]=FullTopCand_3[ii][2];
   }



  //=======================Top mass Comparison with the 3-Jet Combination=========//

  double Err_FullTopMass=100000.0;
  const RecJetFormat* FullRecTopJets[3];
 
  MALorentzVector p_FullRecTop;
  int No_Rows_3=sizeof(FullTopCand_3F)/sizeof(FullTopCand_3F[0]);
  for(int ii=0; ii<No_Rows_3; ii++)
    {
      double Calc3JetMass=(FullTopCand_3F[ii][0]->momentum()+FullTopCand_3F[ii][1]->momentum()+FullTopCand_3F[ii][2]->momentum()).M();	 
      double Diff_TopMass=fabs(Calc3JetMass-TOP_MASS);
        if(Diff_TopMass<Err_FullTopMass)
	{
	Err_FullTopMass=Diff_TopMass;
	FullRecTopJets[0]=FullTopCand_3F[ii][0];
	FullRecTopJets[1]=FullTopCand_3F[ii][1];
	FullRecTopJets[2]=FullTopCand_3F[ii][2];
	}
      
    }
  
  p_FullRecTop=FullRecTopJets[0]->momentum()+FullRecTopJets[1]->momentum()+FullRecTopJets[2]->momentum();

  ParticleBaseFormat Temp_FullTop=ParticleBaseFormat(p_FullRecTop);
  const ParticleBaseFormat *FullTopQuark= &(Temp_FullTop);

//================Determining the 3Jet System Bjet Seed======================//

  const RecJetFormat* BSeed_3Jet;
  
  if(Nbjets>=2)
    {
         int nobjets=0;
         for(unsigned int kk=0; kk<3; kk++)
            {
              if(FullRecTopJets[kk]->btag())
		{
                 nobjets++;
                 BSeed_3Jet=FullRecTopJets[kk];
		}
            }
    }

  /*double BSeed_Pt=0;
  if(Nbjets>=2)
    {
      for(int ii=0; ii<3; ii++)
	{
	  if(FullRecTopJets[ii]->btag() && (FullRecTopJets[ii]->momentum().Pt())>BSeed_Pt)
	    {
		  BSeed_Pt=FullRecTopJets[ii]->momentum().Pt();
                  BSeed_3Jet=FullRecTopJets[ii];
	    }
	}
	}*/

  //========================Partial Top Reconstruction: ======================//

 vector<const RecJetFormat*> FullTopJets;
 FullTopJets.push_back(FullRecTopJets[0]);
 FullTopJets.push_back(FullRecTopJets[1]);
 FullTopJets.push_back(FullRecTopJets[2]);
  vector<const RecJetFormat*> RsysJets=myJets;
  for(int ii=myJets.size()-1; ii>=0; ii--)
    {
      if(RsysJets[ii]==FullTopJets[0] || RsysJets[ii]==FullTopJets[1] || RsysJets[ii]==FullTopJets[2])
	  RsysJets.erase(RsysJets.begin()+ii);
    }

  SORTER->sort(RsysJets);
  
  const RecJetFormat* BSeed_Rsys;
  MALorentzVector p_Rsys(0.,0.,0.,0.);
  double Err_TopMass_ParRec=1000.0;
  vector<const RecJetFormat*> Rsys;
  

//  double BSeed_Dphi_Met=4;
  double BSeed_Pt=0;
      for(unsigned int ii=0; ii<RsysJets.size(); ii++)
	{
	  if(RsysJets[ii]->btag() && RsysJets[ii]->momentum().Pt()>BSeed_Pt)
	    {
		  BSeed_Pt=RsysJets[ii]->momentum().Pt();
                  BSeed_Rsys=RsysJets[ii];
	      
	    }
	}
          /*if(RsysJets[ii]->btag() && RsysJets[ii]->dphi_0_pi(pTmiss)<BSeed_Dphi_Met)
            {
	      BSeed_Dphi_Met=RsysJets[ii]->dphi_0_pi(pTmiss);
              BSeed_Rsys=RsysJets[ii];
	    }
	    }*/
      for(unsigned int ii=0; ii<RsysJets.size(); ii++)
	{
	  if(RsysJets[ii]==BSeed_Rsys)
          RsysJets.erase(RsysJets.begin()+ii);
	}

if(RsysJets.size()>=2)
    {
	  for(unsigned int ii=0; ii<RsysJets.size(); ii++)
	    {
	      for(unsigned int jj=ii+1; jj<RsysJets.size(); jj++)
		{
                  double CalcTopMass=(RsysJets[ii]->momentum()+RsysJets[jj]->momentum()+BSeed_Rsys->momentum()).M();
		  double CalcDijetMass=(RsysJets[ii]->momentum()+RsysJets[jj]->momentum()).M();
		  double Diff_TopMass=fabs(TOP_MASS-CalcTopMass);
		  if(Diff_TopMass<Err_TopMass_ParRec && CalcDijetMass>50 && CalcDijetMass<120) 
		    {
		      Err_TopMass_ParRec=Diff_TopMass;
		      if(Rsys.size()==0) 
			{
                          
			  Rsys.push_back(RsysJets[ii]);
			  Rsys.push_back(RsysJets[jj]);
			  Rsys.push_back(BSeed_Rsys);
			 
			}
		      else 
			{
                          
			  int size_1=Rsys.size();
			  for(int kk=size_1-1; kk>=0; kk--)
			    {
                               Rsys.erase(Rsys.begin()+kk);
			    }       
		          Rsys.push_back(RsysJets[ii]);
			  Rsys.push_back(RsysJets[jj]);
			  Rsys.push_back(BSeed_Rsys);
			}
		    }
		}
	    }
	  if(Rsys.size()==0)
	 {
	   //MALorentzVector Dijet_sys;
	   double Smallest_DeltaR=4;
	   for(unsigned int kk=0; kk<RsysJets.size(); kk++)
	     {
	       double Current_DijetSys_Mass=(RsysJets[kk]->momentum()+BSeed_Rsys->momentum()).M();
	       if(CalcDeltaR(BSeed_Rsys->momentum(),RsysJets[kk]->momentum())<=2.0 && Current_DijetSys_Mass<TOP_MASS)
		 {
		   double Current_DeltaR=CalcDeltaR(BSeed_Rsys->momentum(),RsysJets[kk]->momentum());
		   if(Current_DeltaR<Smallest_DeltaR)
		     {
		       Smallest_DeltaR=Current_DeltaR;
		       if(Rsys.size()==0) 
			{
			  
			  Rsys.push_back(RsysJets[kk]);
			  Rsys.push_back(BSeed_Rsys);
			}
		      else
			{
			  int size_2=Rsys.size();
                          for(int ll=size_2-1; ll>=0; ll--)
			     {
			       Rsys.erase(Rsys.begin()+ll);
			     }
                          
                          Rsys.push_back(RsysJets[kk]);
			  Rsys.push_back(BSeed_Rsys);
			}
		     }
		 }
	     }
	   if(Rsys.size()==0)
	     {               
	       Rsys.push_back(BSeed_Rsys);
	     }
	 }
    }
    
else if(RsysJets.size()==1)
    {
      double Current_DijetSys_Mass=(RsysJets[0]->momentum()+BSeed_Rsys->momentum()).M();
      if((fabs(BSeed_Rsys->momentum().DeltaPhi(RsysJets[0]->momentum())))<=2.0 && Current_DijetSys_Mass<TOP_MASS)///Sam: added "fabs"(deltaphi)       
	  {
	    Rsys.push_back(RsysJets[0]);
	    Rsys.push_back(BSeed_Rsys);
	  }
    if(Rsys.size()==0)
      {
        Rsys.push_back(BSeed_Rsys);
      }
    }

 
 for(unsigned int ii=0; ii<Rsys.size(); ii++)
   {
     p_Rsys=p_Rsys+Rsys[ii]->momentum();
   }

 ParticleBaseFormat Temp_PartialTop=ParticleBaseFormat(p_Rsys);
 const ParticleBaseFormat *PartialTopQuark = &(Temp_PartialTop);
  
//======================Calculation of MT2 ==========================//

MT2=PHYSICS->Transverse->MT2(FullTopQuark,PartialTopQuark, event.rec()->MET(), 0.);

  //===================Apply Cut 9: Top Tagger ===============//

  if(!Manager()->ApplyCut((MT2>=300),"Top Reco")) return true;

 
//======================Calculation of MT ==========================//

/*MT_3Jet=FullTopQuark->mt_met(pTmiss);
  MT_Rsys=PartialTopQuark->mt_met(pTmiss);*/

////Sam: I added what's between the 8s to match what Hongxuan said: p_Rsys doesnt change for MT2, just for MT_Rsys
//////88888888888888
 if((Rsys.size()>2)) 
   {
     p_Rsys=BSeed_Rsys->momentum();
   }
 /////8888888888888



 double Et3Jet=sqrt(pow(p_FullRecTop.M(),2)+pow(p_FullRecTop.Pt(),2));
 double EtRsys=sqrt(pow(p_Rsys.M(),2)+pow(p_Rsys.Pt(),2));

MT_3Jet=sqrt(pow(p_FullRecTop.M(),2)+2*(Et3Jet*MET-p_FullRecTop.Pt()*MET*cos(p_FullRecTop.DeltaPhi(pTmiss))));
MT_Rsys=sqrt(pow(p_Rsys.M(),2)+2*(EtRsys*MET-p_Rsys.Pt()*MET*cos(p_Rsys.DeltaPhi(pTmiss))));


//Sam: commented this out. (this was my previous interpretation of Hongxuans instructions, passed on to Prachi)
 // if(RsysJets.size()>=2 && Nbjets>=2 && fabs(BSeed_Rsys->momentum().DeltaPhi(pTmiss))>fabs(BSeed_3Jet->momentum().DeltaPhi(pTmiss)))////need fabs
 //    {
 //      MALorentzVector p_Rsys_1=BSeed_Rsys->momentum();
 //      ParticleBaseFormat Temp_PartialTop_1=ParticleBaseFormat(p_Rsys_1);
 //      const ParticleBaseFormat *PartialTopQuark_1 = &(Temp_PartialTop_1);
 //      double EtRsys_1=sqrt(pow(p_Rsys_1.M(),2)+pow(p_Rsys_1.Pt(),2));
 //      //cout<<pTmiss.DeltaPhi(p_Rsys_1) <<"   "<<PartialTopQuark_1->dphi_0_pi(pTmiss)<<endl;
 //      MT_Rsys=sqrt(pow(p_Rsys_1.M(),2)+2*(EtRsys_1*MET-p_Rsys_1.Pt()*MET*cos(p_Rsys_1.DeltaPhi(pTmiss))));
 //    }


  //===================Apply Cut 10: Linear_Comb_of_MTs============//

  if(!Manager()->ApplyCut((((0.5*MT_3Jet)+MT_Rsys)>=500),"MTsum>500")) return true;
		
  //==================Apply Signal Region-Dependent Cut================//
		
  Manager()->ApplyCut(((MET>200) && (MET<350) && (Nbjets==1)),"SR1_Cut");
  Manager()->ApplyCut(((MET>350) && (Nbjets==1)),"SR2_Cut");
  Manager()->ApplyCut(((MET>200) && (MET<350) && (Nbjets>=2)),"SR3_Cut");
  Manager()->ApplyCut(((MET>350) && (Nbjets>=2)),"SR4_Cut");  
    }
    return true;
}
