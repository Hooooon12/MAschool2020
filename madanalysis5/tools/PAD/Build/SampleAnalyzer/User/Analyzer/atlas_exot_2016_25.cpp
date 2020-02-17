#include "SampleAnalyzer/User/Analyzer/atlas_exot_2016_25.h"
#include <TCanvas.h>
using namespace MA5;
using namespace std;
// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_exot_2016_25::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // Information on the analysis, authors, ...
  // VERY IMPORTANT FOR DOCUMENTATION, TRACEABILITY, BUG REPORTS
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>    Analysis: atlas_exot_2016_25                <>" << endmsg;
  INFO << "        <>    Monojet @sqrt(s) = 13 TeV, 36 fb^-1 luminosity  <>" << endmsg;
  INFO << "        <>    Recasted by: D. Sengupta <>" << endmsg;
  INFO << "        <>    Contact: dipan@lpsc.in2p3.fr           <>" << endmsg;
  INFO << "        <>    Based on MadAnalysis 5 v1.3 and above        <>" << endmsg;
  INFO << "        <>    For more information, see               <>" << endmsg;
  INFO << "        <>    http://madanalysis.irmp.ucl.ac.be/wiki/PublicAnalysisDatabase <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;

// =====Declare the signal regions in this analysis=====
  Manager()->AddRegionSelection("RESOLVED");

  Manager()->AddCut("RESOLVED_Trigger_&_ElectronMuonVeto", "RESOLVED");
  Manager()->AddCut("RESOLVED_MET_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_PtTrkMiss_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_min.dPhi(MET,Jet)_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_dPhi(MET,TrkMiss)_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_nJet_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_PtLeadingJet_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_HT_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_dPhi(DiJet)_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_dPhi(MET,Higgs)_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_nTau_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_dR(DiJet)_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_nBJet_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_HTRatio_cut", "RESOLVED");
  Manager()->AddCut("RESOLVED_2BJet_cut", "RESOLVED");

  math_pi = 3.141592;

  Manager()->AddHisto("trkmiss",10, 0,200);

  return true;
}


// Finalize
// function called one time at the end of the analysis
void atlas_exot_2016_25::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}

bool atlas_exot_2016_25::Execute(SampleFormat& sample, const EventFormat& event)
{

// unchange
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
  if (event.rec()==0) {return true;}
  EventFormat myEvent;
  myEvent = event;



//Defining the containers
   vector<const RecJetFormat*> Jets, centralJets, forwardJets;
   vector<const RecJetFormat*> fatJets, awayJets;
   vector<const RecLeptonFormat*> Muons;
   vector<const RecLeptonFormat*> Electrons;

//Fat jets
  for(unsigned int i=0; i<event.rec()->fatjets().size(); i++){
    const RecJetFormat *this_fatjet = &(event.rec()->fatjets()[i]);
    if( this_fatjet->pt() > 200.0 && fabs(this_fatjet->eta()) < 2.0 ){
      fatJets.push_back(this_fatjet);
    }
  }


//Jets
  double allHT = 0.;
  for(unsigned int i=0; i<event.rec()->jets().size(); i++){
    const RecJetFormat *this_jet = &(event.rec()->jets()[i]);
    if( this_jet->pt() > 20.0 && fabs(this_jet->eta()) < 2.5 ){
      centralJets.push_back(this_jet);
    }
    if( this_jet->pt() > 30.0 && fabs(this_jet->eta())>2.5 && fabs(this_jet->eta())<4.5){
      forwardJets.push_back(this_jet);
    }
    if((this_jet->pt() > 30.0 && fabs(this_jet->eta())>2.5 && fabs(this_jet->eta())<4.5)
    || ( this_jet->pt() > 20.0 && fabs(this_jet->eta()) < 2.5 )){
      Jets.push_back(this_jet);
      allHT += this_jet->pt();
    }
  }

  if(fatJets.size() > 0){
    for(unsigned int i=0; i<Jets.size(); i++){
      const RecJetFormat *this_jet = Jets.at(i);
      double dr = this_jet->dr(fatJets.at(0));

      if(dr > 1.0) awayJets.push_back(this_jet);
    }
  }

//Electrons
  for(unsigned int i=0; i<event.rec()->electrons().size(); i++){
    const RecLeptonFormat *this_electron = &(event.rec()->electrons()[i]);
    if(this_electron->pt() > 7. && fabs(this_electron->eta()) < 2.47){
      double el_E=this_electron->pt();
      double all_E=PHYSICS->Isol->eflow->sumIsolation(this_electron,event.rec(),0.4,0.,IsolationEFlow::ALL_COMPONENTS);
      if(all_E < 0.2*el_E) Electrons.push_back(this_electron);
    }
  }

//Muons
  for(unsigned int i=0; i<event.rec()->muons().size(); i++){
    const RecLeptonFormat *this_muon = &(event.rec()->muons()[i]);
    if(this_muon->pt() > 7. && fabs(this_muon->eta()) < 2.7){
      double mu_E=this_muon->pt();
      double all_E=PHYSICS->Isol->eflow->sumIsolation(this_muon,event.rec(),0.4,0.,IsolationEFlow::ALL_COMPONENTS);
      if(all_E < 0.2*mu_E) Muons.push_back(this_muon);
    }
  }

//MET
  MALorentzVector MET = (event.rec()->MET()).momentum();

//TrkMiss
  MALorentzVector TrkMiss;
  for(unsigned int i=0; i<event.rec()->tracks().size(); i++){
    const RecTrackFormat *this_track = &(event.rec()->tracks()[i]);
    MALorentzVector this_track4vec;
    this_track4vec.SetPxPyPzE(this_track->px(), this_track->py(), this_track->pz(), this_track->e());
    TrkMiss += this_track4vec;
  }
  TrkMiss.SetPxPyPzE(-TrkMiss.Px(), -TrkMiss.Py(), TrkMiss.Pz(), TrkMiss.E());
//Denominator for cutflow
  if(!Manager()->ApplyCut(Muons.size() == 0 && Electrons.size() == 0 && MET.Pt() > 110, "RESOLVED_Trigger_&_ElectronMuonVeto")) return true;


//Define 2 different regions
  int region = 0;
  if((MET.Pt() > 150.) && (MET.Pt() < 500.)) region = 1;//RESOLVED
  if((MET.Pt() > 500.)) region = 2;//MERGED

  if(!Manager()->ApplyCut(region == 1, "RESOLVED_MET_cut")) return true;

//Resolved region
  if( region == 1 ){
    vector<const RecJetFormat*> hJets;
    int NBJet = 0;
    for(unsigned int i=0; i<centralJets.size(); i++){
      if(centralJets.at(i)->btag()){
        hJets.push_back(centralJets.at(i));
        NBJet ++;
      }
    }
    for(unsigned int i=0; i<centralJets.size(); i++){
      if(!centralJets.at(i)->btag()) hJets.push_back(centralJets.at(i));
    }

    if(!Manager()->ApplyCut((TrkMiss.Pt() > 30.), "RESOLVED_PtTrkMiss_cut")) return true;

    bool mindPhiMETJets_big = true;
    for(unsigned int i=0; i<Jets.size(); i++){
      double this_dPhi = GetdPhi(Jets.at(i)->phi(), MET.Phi());
      if(this_dPhi < math_pi/9) mindPhiMETJets_big = false;
      if(i==3) break;
    }
    if(Jets.size() == 0) mindPhiMETJets_big = false;
    if(!Manager()->ApplyCut((mindPhiMETJets_big), "RESOLVED_min.dPhi(MET,Jet)_cut")) return true;

    double dPhiMETTrkMiss = GetdPhi(TrkMiss.Phi(),MET.Phi());
    if(!Manager()->ApplyCut((dPhiMETTrkMiss < math_pi/2 ),"RESOLVED_dPhi(MET,TrkMiss)_cut")) return true;


    if(!Manager()->ApplyCut((centralJets.size() > 1),"RESOLVED_nJet_cut")) return true;

    if(!Manager()->ApplyCut((centralJets.at(0)->pt() > 45.), "RESOLVED_PtLeadingJet_cut")) return true;

    bool centralHT_sum_big = false;
    if(centralJets.size() == 2){
      if((centralJets.at(0)->pt()+centralJets.at(1)->pt()) > 120.){
        centralHT_sum_big = true;
      }
    }
    else{
      if((centralJets.at(0)->pt()+centralJets.at(1)->pt()+centralJets.at(2)->pt()) > 150.){
        centralHT_sum_big = true;
      }
    }

    if(!Manager()->ApplyCut((centralHT_sum_big), "RESOLVED_HT_cut")) return true;

    double dPhiHiggsDiJet = GetdPhi(hJets.at(0)->phi(),hJets.at(1)->phi());
    if(!Manager()->ApplyCut((dPhiHiggsDiJet < (7.*math_pi/9)), "RESOLVED_dPhi(DiJet)_cut")) return true;


    MALorentzVector hCandidate4vec, hJets4vec[2];
    for(unsigned int i=0; i<2; i++){
      hJets4vec[i].SetPxPyPzE(hJets.at(i)->px(), hJets.at(i)->py(), hJets.at(i)->pz(), hJets.at(i)->e());
    }
    hCandidate4vec = hJets4vec[0]+hJets4vec[1];

    double dPhiMETHiggs = GetdPhi(hCandidate4vec.Phi(), MET.Phi());
    if(!Manager()->ApplyCut((dPhiMETHiggs > (2.*math_pi/3)), "RESOLVED_dPhi(MET,Higgs)_cut")) return true;

    if(!Manager()->ApplyCut((event.rec()->taus().size() == 0), "RESOLVED_nTau_cut")) return true;

    if(!Manager()->ApplyCut((hJets4vec[0].DeltaR(hJets4vec[1]) < 1.8), "RESOLVED_dR(DiJet)_cut")) return true;

    if(!Manager()->ApplyCut(NBJet < 3, "RESOLVED_nBJet_cut")) return true;
    double allHT=0., hjetsHT=0.;
    for(unsigned int i=0; i<Jets.size(); i++){
      allHT += Jets.at(i)->pt();
    }
    for(unsigned int i=0; i<2; i++){
      hjetsHT += hJets.at(i)->pt();
    }
    if((forwardJets.size()!=0) || (hJets.size()>2)){
      if((forwardJets.size()!=0) && (hJets.size()>2)){
        if(forwardJets.at(0)->pt() > hJets.at(2)->pt()) hjetsHT += forwardJets.at(0)->pt();
        else hjetsHT += hJets.at(2)->pt();
      }
      else if((forwardJets.size()!=0)) hjetsHT += forwardJets.at(0)->pt();
      else hjetsHT += hJets.at(2)->pt();
    }
    if(!Manager()->ApplyCut((hjetsHT/allHT > 0.63), "RESOLVED_HTRatio_cut")) return true;
    if(!Manager()->ApplyCut(NBJet == 2, "RESOLVED_2BJet_cut")) return true;


  }
  return false;
}



double atlas_exot_2016_25::GetdPhi(double phi1, double phi2){
  double math_pi = 3.141592;
  double dphi = phi1 - phi2;
  if(fabs(dphi) > math_pi) dphi = (fabs(dphi)-2*math_pi);

  return fabs(dphi);

}
