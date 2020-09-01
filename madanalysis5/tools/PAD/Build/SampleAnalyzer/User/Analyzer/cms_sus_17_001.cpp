#include "SampleAnalyzer/User/Analyzer/cms_sus_17_001.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_sus_17_001::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>   Analysis: CMS-SUS-17-001                   <>" << endmsg;
  INFO << "      <>             (stops with OS2L)                <>" << endmsg;
  INFO << "      <>   Recaster: S.~Bein, S.-M.~Choi, S.~Jeong,   <>" << endmsg;
  INFO << "      <>             D.-W.~Kang, J.~Li, J.~Sonneveld  <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  // initialize variables, histos

//   Manager()->AddRegionSelection("SR_curflow");
   Manager()->AddRegionSelection("SRA0");
   Manager()->AddRegionSelection("SRA1");
   Manager()->AddRegionSelection("SRA2");

   Manager()->AddCut("2OSL");
   Manager()->AddCut("mll20");
   Manager()->AddCut("mllZ");
   Manager()->AddCut("nj2");
   Manager()->AddCut("nb1");
   Manager()->AddCut("met80");
   Manager()->AddCut("s5");
   Manager()->AddCut("cphi80");
   Manager()->AddCut("cphi96");

//   Manager()->AddCut("mt2ll140","SR_curflow");

   Manager()->AddCut("met200a0","SRA0");
   Manager()->AddCut("mt2ll14","SRA0");

   Manager()->AddCut("met200a1","SRA1");
   Manager()->AddCut("mt2ll24","SRA1");

   Manager()->AddCut("mt2ll240","SRA2");
//   float bins[] = {0,20,40,60,80,100,150,250,350};

 //    hmt2ll = new TH1F("hmt2ll","ht2ll",8,bins);
 //   Manager()->AddHisto("mt2ll (combined flavor)",8,0,350);

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_sus_17_001::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
//  // saving histos
//    TFile * f = new TFile("hists.root","recreate");
//    hmt2ll->Write();
//
//    for(int i=1;i<=8;i++)
//    {
//        cout<<"bin number "<<i<<" bin content: "<<hmt2ll->GetBinContent(i)<<endl;
//    }
//
//    f->Close();
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_sus_17_001::Execute(SampleFormat& sample, const EventFormat& event)
{

    vector<const RecLeptonFormat*> SignalMuons,SignalElectrons;
    vector<const RecJetFormat*> SignalJets;


  // ***************************************************************************
  // Example of analysis with reconstructed objects
  // Concerned samples : 
  //   - LHCO samples
  //   - LHE/STDHEP/HEPMC samples after applying jet-clustering algorithm
  // ***************************************************************************

    double myEventWeight = 1.;
    if(Configuration().IsNoEventWeight()) myEventWeight=1;
    else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
    Manager()->InitializeForNewEvent(myEventWeight);

  if (event.rec()!=0)
  {
   // cout << "---------------NEW EVENT-------------------" << endl;

      for (unsigned int i=0;i<event.rec()->electrons().size();i++)
      {
          const RecLeptonFormat* elec = &(event.rec()->electrons()[i]);
          if(elec->pt() > 20.0 && fabs(elec->eta())<2.4)
              SignalElectrons.push_back(elec);
      }

      for (unsigned int i=0;i<event.rec()->muons().size();i++)
      {
          const RecLeptonFormat* mu = &(event.rec()->muons()[i]);
          if(mu->pt()>20.0 && fabs(mu->eta())<2.4)
              SignalMuons.push_back(mu);
      }

      int nb=0;
      for (unsigned int i=0;i<event.rec()->jets().size();i++)
      {
          const RecJetFormat* jet = &(event.rec()->jets()[i]);
          if(jet->pt()>30 && fabs(jet->eta())<2.4)
          {
              SignalJets.push_back(jet);
              if(jet->btag()) nb++;
          }
      }

      // The MET
      MALorentzVector pTmiss = event.rec()->MET().momentum();
      double MET = pTmiss.Pt();

      int lep_charge_sum=0;
      for(unsigned int i=0;i<SignalElectrons.size();i++)
      {
          if(SignalElectrons[i]->charge()>0) lep_charge_sum++;
          if(SignalElectrons[i]->charge()<0) lep_charge_sum--;
      }

      for(unsigned int i=0;i<SignalMuons.size();i++)
      {
          if(SignalMuons[i]->charge()>0) lep_charge_sum++;
          if(SignalMuons[i]->charge()<0) lep_charge_sum--;
      }

      // leading lepton
      double ptl1=0;
      if(SignalElectrons.size()>0&&SignalMuons.size()>0)
      {
          ptl1=SignalElectrons[0]->pt();
          if(ptl1<SignalMuons[0]->pt()) ptl1=SignalMuons[0]->pt();
      }
      if(SignalElectrons.size()>1)
      {
          ptl1=SignalElectrons[0]->pt();
      }
      if(SignalMuons.size()>1)
      {
          ptl1=SignalMuons[0]->pt();
      }

      // cut 2osl.
      if(!Manager()->ApplyCut((SignalMuons.size()+SignalElectrons.size()==2)&&lep_charge_sum==0&&ptl1>25.0,"2OSL")){
          return true;
      }

      // cut mll20
      double mll=0;
      if(SignalElectrons.size()>0&&SignalMuons.size()>0)
          mll=(SignalMuons[0]->momentum()+SignalElectrons[0]->momentum()).M();
      if(SignalElectrons.size()>1)
          mll=(SignalElectrons[1]->momentum()+SignalElectrons[0]->momentum()).M();
      if(SignalMuons.size()>1)
          mll=(SignalMuons[1]->momentum()+SignalMuons[0]->momentum()).M();

      if(!Manager()->ApplyCut(mll>20.0,"mll20"))
      {
          return true;
      }

      // mll not around Z
      int zveto=0;

      if(SignalElectrons.size()>1 || SignalMuons.size()>1)
      {
          if(fabs(mll-91.2)<15.0) zveto=1;
      }

      if(!Manager()->ApplyCut(zveto==0,"mllZ"))
      {
          return true;
      }

      // cut nj
      if(!Manager()->ApplyCut(SignalJets.size()>=2,"nj2"))
      {
          return true;
      }

      // cut nb
      if(!Manager()->ApplyCut(nb>=1,"nb1"))
      {
          return true;
      }

      // met
      if(!Manager()->ApplyCut(MET>80,"met80"))
      {
          return true;
      }

      // s
      double s=0;
      for(int i=0;i<SignalJets.size();i++)
      {
          s+=SignalJets[i]->pt();
      }
      for(int i=0;i<SignalMuons.size();i++)
      {
          s+=SignalMuons[i]->pt();
      }
      for(int i=0;i<SignalElectrons.size();i++)
      {
          s+=SignalElectrons[i]->pt();
      }

      s=MET/sqrt(s);

      if(!Manager()->ApplyCut(s>5,"s5"))
      {
          return true;
      }

      // dphi jet-met
      double dphij1=99;
      double dphij2=99;

      if(SignalJets.size()>1)
      {
          dphij1=SignalJets[0]->dphi_0_pi(pTmiss);
          dphij2=SignalJets[1]->dphi_0_pi(pTmiss);
      }

      if(!Manager()->ApplyCut(cos(dphij1)<0.8,"cphi80"))
      {
          return true;
      }

      if(!Manager()->ApplyCut(cos(dphij2)<0.96,"cphi96"))
      {
          return true;
      }

      // end of table 1

      // mt2ll

      double mt2ll=0;
      if(SignalElectrons.size()>0&&SignalMuons.size()>0)
      {
          MA5::ParticleBaseFormat *p1 = new MA5::ParticleBaseFormat(*SignalElectrons[0]);
          MA5::ParticleBaseFormat *p2 = new MA5::ParticleBaseFormat(*SignalMuons[0]);
          mt2ll=PHYSICS->Transverse->MT2(p1,p2,event.rec()->MET(),0);
      }
      if(SignalElectrons.size()>1)
      {
          MA5::ParticleBaseFormat *p1 = new MA5::ParticleBaseFormat(*SignalElectrons[0]);
          MA5::ParticleBaseFormat *p2 = new MA5::ParticleBaseFormat(*SignalElectrons[1]);
          mt2ll=PHYSICS->Transverse->MT2(p1,p2,event.rec()->MET(),0);
      }
      if(SignalMuons.size()>1)
      {
          MA5::ParticleBaseFormat *p1 = new MA5::ParticleBaseFormat(*SignalMuons[0]);
          MA5::ParticleBaseFormat *p2 = new MA5::ParticleBaseFormat(*SignalMuons[1]);
          mt2ll=PHYSICS->Transverse->MT2(p1,p2,event.rec()->MET(),0);
      }

//      hmt2ll->Fill(mt2ll);

      //sr_cutflow

//      if(!Manager()->ApplyCut(mt2ll>140,"mt2ll140")) return true;

      // sra0

      if(!Manager()->ApplyCut(MET>200,"met200a0")) return true;
      if(!Manager()->ApplyCut(mt2ll>100 && mt2ll<140,"mt2ll14")) return true;

      //sra1

      if(!Manager()->ApplyCut(MET>200,"met200a1")) return true;
      if(!Manager()->ApplyCut(mt2ll>140 && mt2ll<240,"mt2ll24")) return true;

      //sra2

      if(!Manager()->ApplyCut(mt2ll>240,"mt2ll240")) return true;


  }

  return true;
}

