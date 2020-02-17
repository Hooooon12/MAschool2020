#define PI 3.1415926535897932384626433832795028841971693993751

#include "SampleAnalyzer/User/Analyzer/atlas_higg_2013_03.h"
using namespace MA5;
using namespace std;

template<typename T1, typename T2> void OverlapRmv(std::vector<const T1*> &,
  std::vector<const T2*>, const double &);

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_higg_2013_03::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{

  // General information on the implementers
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: ATLAS-HIGG-2013-03              <>" << endmsg;
  INFO << "        <>            arXiv:1402.3244                 <>" << endmsg;
  INFO << "        <>            (Higgs two leptons + MET)       <>" << endmsg;
  INFO << "        <>  Recasted by: B.Dumont                     <>" << endmsg;
  INFO << "        <>  Contact: dumont@lpsc.in2p3.fr             <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11            <>" << endmsg;
  INFO << "        <>  For more information, see                 <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;


  // Definition of the signal regions
  Manager()->AddRegionSelection("sig");

  // Definition of the cuts
  Manager()->AddCut("2 OS leptons");
  Manager()->AddCut("Z window");
  Manager()->AddCut("MET > 90 GeV");
  Manager()->AddCut("dilepton-MET separation");
  Manager()->AddCut("lepton-lepton separation");
  Manager()->AddCut("pTmiss-MET separation");
  Manager()->AddCut("pTll-MET similarity");
  Manager()->AddCut("jet veto");


  // finally, definition of histograms
  // they are all available on
  // https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/HIGG-2013-03/
  // we consider all available histograms: Fig. 1, Fig. 2, Figaux. 3a,b,c,d,e
  // and Figaux. 5a
  Manager()->AddHisto("MET initial",50,0,500); // Fig. 1
  Manager()->AddHisto("MET final",12,90,450); // Fig. 2
  Manager()->AddHisto("pTmiss-MET separation",8,0.,PI); // Figaux. 3a
  Manager()->AddHisto("dilepton-MET separation",8,0.,PI); // Figaux. 3b
  Manager()->AddHisto("pTll-MET similarity",10,0.,2.); // Figaux. 3c
  Manager()->AddHisto("njets",6,-0.5,5.5); // Figaux. 3d
  Manager()->AddHisto("lepton-lepton separation",16,0.,PI); // Figaux. 3e
  Manager()->AddHisto("MET Figaux5a",18,0,360); // Figaux. 5a

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_higg_2013_03::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  return;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_higg_2013_03::Execute(SampleFormat& sample, const EventFormat& event)
{
  if(event.rec()!=0)
  {
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Book-keeping with the event weight: do not modify this
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    double myEventWeight;
    if(Configuration().IsNoEventWeight()) myEventWeight=1.;
    else if(event.mc()->weight()!=0.) myEventWeight = event.mc()->weight();
    else
    {
      //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
      return false;
    }
    Manager()->InitializeForNewEvent(myEventWeight);

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Object definitions
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    // Declaration of all containers
    std::vector<const RecLeptonFormat*> myElectrons, myMuons;
    std::vector<const RecJetFormat*> myJets;
    std::vector<const RecTrackFormat*> myTracks;

    // filling lepton containers
    // electron satify the 'medium' criteria (put in the Delphes card)
    // and are required to be weakly isolated
    for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ii]);
      double pt = CurrentElectron->pt();
      double abseta = fabs(CurrentElectron->eta());

      if(pt > 7. && abseta < 2.47)
        for(unsigned int jj=0; jj<CurrentElectron->isolCones().size(); jj++)
          if(fabs(CurrentElectron->isolCones()[jj].deltaR() - 0.2) < 0.001)
            if(CurrentElectron->isolCones()[jj].sumET()/pt<0.2)
              myElectrons.push_back(CurrentElectron);
    }
    for(unsigned int ii=0; ii<event.rec()->muons().size(); ii++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[ii]);
      double pt = CurrentMuon->pt();
      double abseta = fabs(CurrentMuon->eta());

      if(pt > 7. && abseta < 2.4)
        myMuons.push_back(CurrentMuon);
    }

    // filling jet container (anti-kt, r=0.4)
    for(unsigned int ii=0; ii<event.rec()->jets().size(); ii++)
    {
      const RecJetFormat *CurrentJet = &(event.rec()->jets()[ii]);
      double pt = CurrentJet->pt();
      double abseta = fabs(CurrentJet->eta());

      if(pt > 20. && abseta < 4.5)
        myJets.push_back(CurrentJet);
    }

    // filling track container
    for(unsigned int ii=0; ii<event.rec()->tracks().size(); ii++)
    {
      const RecTrackFormat *CurrentTrack = &(event.rec()->tracks()[ii]);
      double pt = CurrentTrack->momentum().Pt();
      double abseta = fabs(CurrentTrack->momentum().Eta());

      if(pt>0.5 && abseta<2.5)
        myTracks.push_back(CurrentTrack);
    }

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Overlap removals and isolation
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    OverlapRmv(myElectrons,myMuons,0.2);
    OverlapRmv(myJets,myElectrons,0.2);
    OverlapRmv(myElectrons,myJets,0.4);
    OverlapRmv(myMuons,myJets,0.4);

    // scalar sum of track momenta not associated with the lepton in a cone of
    // DR=0.2 around the lepton direction should be < 10% lepton pT
    // information on the value of the tracks pTmin is not given in the paper
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
          break;
        }
      }
    }
    for(int ii=myMuons.size()-1; ii>=0; ii--)
    {
      for(unsigned int jj=0; jj<myMuons[ii]->isolCones().size(); jj++)
      {
        if(fabs(myMuons[ii]->isolCones()[jj].deltaR() - 0.2) < 0.001)
        {
          if(myMuons[ii]->isolCones()[jj].sumPT()
             > .10*myMuons[ii]->pt())
          {
            myMuons.erase(myMuons.begin()+ii);
          }
          break;
        }
      }
    }

    // define candidate leptons (tighter pt cuts)
    std::vector<const RecLeptonFormat*> candLeptons;
    for(unsigned int ii=0; ii<myElectrons.size(); ii++)
    {
      if(myElectrons[ii]->pt() > 20.)
        candLeptons.push_back(myElectrons[ii]);
    }
    for(unsigned int ii=0; ii<myMuons.size(); ii++)
    {
      if(myMuons[ii]->pt() > 20.)
        candLeptons.push_back(myMuons[ii]);
    }

    // trigger efficiency: unknown... hence assumed to be 100%

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // end of preselection
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // signal region requirements
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    // 2 OS leptons
    bool OScond = candLeptons.size() == 2;
    if(OScond) OScond = candLeptons[0]->charge() != candLeptons[1]->charge();

    if(!Manager()->ApplyCut(OScond, "2 OS leptons"))
      return true;

    // basic variables for the two leptons
    MALorentzVector p_lepton1 = candLeptons[0]->momentum();
    MALorentzVector p_lepton2 = candLeptons[1]->momentum();
    MALorentzVector p_dilepton = (p_lepton1 + p_lepton2);
    double mll = p_dilepton.M();
    double pTll = p_dilepton.Pt();

    // MET and pTmiss
    MALorentzVector p_met = event.rec()->MET().momentum();
    double met = p_met.Pt();
    MALorentzVector ptmiss;
    for(unsigned int ii=0; ii<myTracks.size(); ii++)
    {
      ptmiss -= myTracks[ii]->momentum();
      // "tracks matched to electrons are discarded and replaced by the
      // transverse energy E_T of the matched cluster measured in the
      // calorimeter to include any photon radiation in the calculation":
      // not implemented
    }

    // azimuthal separation between...
    double dphi_met_ptmiss = fabs(p_met.DeltaPhi(ptmiss)); // MET and pTmiss
    double dphi_ll_met = fabs(p_dilepton.DeltaPhi(p_met)); // di-lepton pair and MET
    double dphi_l_l = fabs(p_lepton1.DeltaPhi(p_lepton2)); // the two leptons

    // similarity between pT of dilepton pair and MET
    double frac_diff = fabs(met - pTll) / pTll;

    // number of jets with pT > 25 GeV and |eta| < 2.5
    int njets = 0;
    for(unsigned int ii=0; ii<myJets.size(); ii++)
    {
      double abseta = fabs(myJets[ii]->eta());
      double pt = myJets[ii]->pt();

      if(pt > 25. && abseta < 2.5)
        ++njets;
    }

    // proceed with all remaining cuts and fill the histograms

    // 76 GeV < mll < 106 GeV (\pm 20 GeV around Z boson mass)
    if(!Manager()->ApplyCut(mll > 76. && mll < 106., "Z window"))
      return true;

    // filling histogram Fig. 1
    Manager()->FillHisto("MET initial", met);

    // uncomment this multi-line comment to generate the MET histo Figaux. 5a
    // /*

    // MET > 90 GeV
    if(!Manager()->ApplyCut(met > 90., "MET > 90 GeV"))
      return true;

    // filling histogram Figaux. 3
    Manager()->FillHisto("pTmiss-MET separation", dphi_met_ptmiss); // Figaux. 3a
    Manager()->FillHisto("dilepton-MET separation", dphi_ll_met); // Figaux. 3b
    Manager()->FillHisto("pTll-MET similarity", frac_diff); // Figaux. 3c
    Manager()->FillHisto("njets", njets); // Figaux. 3d
    Manager()->FillHisto("lepton-lepton separation", dphi_l_l); // Figaux. 3e

    // the azimuthal separation between the dilepton system and the MET
    // is required to be larger than 2.6
    if(!Manager()->ApplyCut(dphi_ll_met > 2.6, "dilepton-MET separation"))
      return true;

    // the azimuthal opening angle of the two leptons is required to be less
    // than 1.7
    if(!Manager()->ApplyCut(dphi_l_l < 1.7, "lepton-lepton separation"))
      return true;

    // end of multi-line comment to generate the MET histo Figaux. 5a
    // */

    // cut on the azimuthal angle between MET and pTmiss to reject MET from
    // misreconstructed energy in the calorimeter (dphi < 0.2)
    if(!Manager()->ApplyCut(dphi_met_ptmiss < 0.2, "pTmiss-MET separation"))
      return true;

    // pT of the dilepton pair and MET should be similar
    if(!Manager()->ApplyCut(frac_diff < 0.2, "pTll-MET similarity"))
      return true;

    // no reconstructed jet with pT > 25 GeV and |eta| < 2.5
    if(!Manager()->ApplyCut(njets == 0, "jet veto"))
      return true;

    // filling histogram Fig. 2
    Manager()->FillHisto("MET final", met);

    // filling histogram Figaux. 5a
    // (meaningful only if the above multi-line comment is present)
    Manager()->FillHisto("MET Figaux5a", met);
  }
  return true;
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

