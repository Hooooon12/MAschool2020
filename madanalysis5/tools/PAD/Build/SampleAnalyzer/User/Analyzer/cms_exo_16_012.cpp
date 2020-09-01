#include "SampleAnalyzer/User/Analyzer/cms_exo_16_012.h"
#include <iostream>
#include <TCanvas.h>
#include <vector>
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool cms_exo_16_012::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // initialize variables, histos
  AA=0; BB=0;CC++;begin_before=0;begin_after=0;
  Manager()->AddRegionSelection("higgs_aa");
  Manager()->AddCut("dip_mass_95","higgs_aa");
  Manager()->AddCut("azimuthal separation","higgs_aa");
  Manager()->AddCut("minimum azimuthal angle with jet","higgs_aa");
  Manager()->AddCut("more than two electrons","higgs_aa");
  Manager()->AddCut("more than one muon","higgs_aa");
  Manager()->AddCut("MissET > 105","higgs_aa");
  Manager()->AddCut("120_dip_mass_130","higgs_aa");


  Manager()->AddHisto("NDiphoton",10,0,1000);
  Manager()->AddHisto("NDiphoton2",10,0,600);

  Manager()->AddHisto("before_MissET",10,0,200);
  Manager()->AddHisto("after_MissET",10,100,250);
  Manager()->AddHisto("after_dip_mass",10,120,130);
  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_exo_16_012::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_exo_16_012::Execute(SampleFormat& sample, const EventFormat& event)
{
  double myEventWeight;
  if(Configuration().IsNoEventWeight()) myEventWeight=1.;
  else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
  else
  {
    //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
    return false;
  }
  Manager()->InitializeForNewEvent(myEventWeight);

  //the loop start
  if (event.rec()==0) { return true;}
  //Defining the containers


//  MALorentzVector pTmiss = MALorentzVector();
  MALorentzVector pTmiss = event.rec()->MET().momentum();
  double MissET = pTmiss.Pt();

   vector<const RecPhotonFormat*> SignalPhotons;
  for(int ii=event.rec()->photons().size()-1;ii>=0;ii--)
  {
    const RecPhotonFormat * myPhoton = &(event.rec()->photons()[ii]);
    double mypt=myPhoton->pt();  double ph_eta= fabs(myPhoton->eta());
    double chargept=PHYSICS->Isol->eflow->sumIsolation(myPhoton,event.rec(),0.3,0.,IsolationEFlow::TRACK_COMPONENT);
    double neutralpt=PHYSICS->Isol->eflow->sumIsolation(myPhoton,event.rec(),0.3,0.,IsolationEFlow::NEUTRAL_COMPONENT);
    double photonpt=PHYSICS->Isol->eflow->sumIsolation(myPhoton,event.rec(),0.3,0.,IsolationEFlow::PHOTON_COMPONENT);
    double photonplt=photonpt-mypt;
    double photonID=myPhoton->HEoverEE();
    if(mypt > 20. &&( ph_eta<1.44 || (ph_eta>1.56 && ph_eta<2.5) )   ){
      if(!(chargept > 1.5||neutralpt > (1.0+0.04*mypt)||photonplt > (0.7+0.005*mypt)||photonID > 0.1))
       SignalPhotons.push_back(myPhoton);
    }
  }

   for(int ii=SignalPhotons.size()-1;ii>=0;ii--){
      const RecPhotonFormat * myPhoton = SignalPhotons[ii];
      double ph_pt=myPhoton->pt(); double ph_eta= fabs(myPhoton->eta());
      if(ph_pt < 20. || (ph_eta>1.44 && ph_eta<1.56) || ph_eta>2.5)
      SignalPhotons.erase(SignalPhotons.begin()+ii);
   }




 int n_sig_ph=SignalPhotons.size();
 Manager()->FillHisto("NDiphoton",         n_sig_ph);

 double test=0;    MALorentzVector diPhoton;
 vector<const RecPhotonFormat*> v_signalPhotons;
  for(unsigned int i=0; i<SignalPhotons.size(); ++i){
    const RecPhotonFormat * myphoton1 = &(event.rec()->photons()[i]);
    MALorentzVector photon1;
//    photon1.SetPtEtaPhiE(myphoton1->pt(), myphoton1->eta(), myphoton1->phi(), myphoton1->e());
    photon1.SetPxPyPzE(myphoton1->px(),myphoton1->py(),myphoton1->pz(),myphoton1->e());
    for(unsigned int j=0; j<event.rec()->photons().size(); ++j){
      const RecPhotonFormat * myphoton2 = &(event.rec()->photons()[j]);
      MALorentzVector photon2;
//      photon2.SetPtEtaPhiE(myphoton2->pt(), myphoton2->eta(), myphoton2->phi(), myphoton2->e());
      photon2.SetPxPyPzE(myphoton2->px(),myphoton2->py(),myphoton2->pz(),myphoton2->e());
      if( (photon1 + photon2).M() > 95.0 ){

        if(myphoton1->pt() < myphoton2->pt()){
          myphoton1=myphoton2;
        }
        v_signalPhotons.push_back(myphoton1);
	    v_signalPhotons.push_back(myphoton2);
//        pt_1=myphoton1->pt();
//        pt_2=myphoton2->pt();


/*      diPhoton.SetPtEtaPhiE(v_signalPhotons[0]->pt()+v_signalPhotons[1]->pt(),
      v_signalPhotons[0]->eta()+v_signalPhotons[1]->eta(),
      v_signalPhotons[0]->phi()+v_signalPhotons[1]->phi(),
      v_signalPhotons[0]->e()+v_signalPhotons[1]->e());  */

      diPhoton.SetPxPyPzE(v_signalPhotons[0]->px()+v_signalPhotons[1]->px(),
                          v_signalPhotons[0]->py()+v_signalPhotons[1]->py(),
                          v_signalPhotons[0]->pz()+v_signalPhotons[1]->pz(),
                          v_signalPhotons[0]->e()+v_signalPhotons[1]->e());
      test=1.;
      break;
      }
    }
  }



  if( !Manager()->ApplyCut(test==1., "dip_mass_95")) return true;
  int n_dip = v_signalPhotons.size();
  Manager()->FillHisto("NDiphoton2",        n_dip );





/*  diPhoton.SetPtEtaPhiE(v_signalPhotons[0]->pt()+v_signalPhotons[1]->pt(),
      v_signalPhotons[0]->eta()+v_signalPhotons[1]->eta(),
      v_signalPhotons[0]->phi()+v_signalPhotons[1]->phi(),
      v_signalPhotons[0]->e()+v_signalPhotons[1]->e());
*/

  double dip_mass=diPhoton.M();

  if( !Manager()->ApplyCut(fabs(diPhoton.DeltaPhi(pTmiss)) > 2.1, "azimuthal separation")) return true;
//   if( fabs(diPhoton.DeltaPhi(pTmiss)) < 2.1)  return true;



 vector<const RecJetFormat*> SignalJets;
 vector<const RecLeptonFormat*> SignalElectrons;
 for(unsigned int ij=0;ij<event.rec()->jets().size();ij++){
    const RecJetFormat * CurrentJet = &(event.rec()->jets()[ij]);
    double pt_jet=CurrentJet->pt(); double pt_eta=fabs(CurrentJet->eta());
    if(pt_jet > 50. && pt_eta < 4.7)
    SignalJets.push_back(CurrentJet);
 }





  begin_before++;

  for(unsigned int ij=0;ij<SignalJets.size();ij++){
 //   if( SignalJets[ij]->dphi_0_pi(pTmiss) < 0.5)  return true;
     if( !Manager()->ApplyCut(SignalJets[ij]->dphi_0_pi(pTmiss) > 0.5, "minimum azimuthal angle with jet")) return true;
  }

  begin_after++;





  int NE=0, Nmu=0;
  for(unsigned int ie=0; ie<event.rec()->electrons().size(); ie++)
  {
    const RecLeptonFormat * CurrentElectron = &(event.rec()->electrons()[ie]);
    if(CurrentElectron->pt()>10.0) NE++;
  }
  if( !Manager()->ApplyCut( NE<=2, "more than two electrons")) return true;






  for(unsigned int ie=0; ie<event.rec()->muons().size(); ie++)
  {
    const RecLeptonFormat * CurrentMuon = &(event.rec()->muons()[ie]);
    if(CurrentMuon->pt()>30.0 && fabs(CurrentMuon->eta()) < 2.4) Nmu++;
  }
  if( !Manager()->ApplyCut( Nmu == 0, "more than one muon"))  return true;
//  if(Nmu > 0) return true;


  BB++;
  Manager()->FillHisto("before_MissET",        MissET );

  if( !Manager()->ApplyCut(MissET > 105.,"MissET > 105")) return true;
  AA++;
  Manager()->FillHisto("after_MissET",        MissET );
  if( !Manager()->ApplyCut(dip_mass>120. && dip_mass<130.,"120_dip_mass_130")) return true;
  CC++;
  Manager()->FillHisto("after_dip_mass",        dip_mass );

  return true;
}
