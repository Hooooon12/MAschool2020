#include "SampleAnalyzer/User/Analyzer/atlas_susy_2013_11.h"
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
bool atlas_susy_2013_11::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{

  // General information on the implementers
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: ATLAS-SUSY-2013-11              <>" << endmsg;
  INFO << "        <>            arXiv:1403.5294                 <>" << endmsg;
  INFO << "        <>            (two leptons + met)             <>" << endmsg;
  INFO << "        <>  Recasted by: B.Dumont, B.Fuks             <>" << endmsg;
  INFO << "        <>  Contact: dumont@lpsc.in2p3.fr             <>" << endmsg;
  INFO << "        <>           fuks@cern.ch                     <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v1.1.11            <>" << endmsg;
  INFO << "        <>  For more information, see                 <>" << endmsg;
  INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;


  // Definition of the signal regions
  Manager()->AddRegionSelection("MT2-90 ee");
  Manager()->AddRegionSelection("MT2-90 mumu");
  Manager()->AddRegionSelection("MT2-90 emu");
  Manager()->AddRegionSelection("MT2-120 ee");
  Manager()->AddRegionSelection("MT2-120 mumu");
  Manager()->AddRegionSelection("MT2-120 emu");
  Manager()->AddRegionSelection("MT2-150 ee");
  Manager()->AddRegionSelection("MT2-150 mumu");
  Manager()->AddRegionSelection("MT2-150 emu");

  Manager()->AddRegionSelection("WWa ee");
  Manager()->AddRegionSelection("WWa mumu");
  Manager()->AddRegionSelection("WWa emu");
  Manager()->AddRegionSelection("WWb ee");
  Manager()->AddRegionSelection("WWb mumu");
  Manager()->AddRegionSelection("WWb emu");
  Manager()->AddRegionSelection("WWc ee");
  Manager()->AddRegionSelection("WWc mumu");
  Manager()->AddRegionSelection("WWc emu");

  Manager()->AddRegionSelection("Zjets ee");
  Manager()->AddRegionSelection("Zjets mumu");

  // Definition of the cuts
  std::string SRforMT2_90[] = {"MT2-90 ee", "MT2-90 mumu", "MT2-90 emu",
                               "WWb ee", "WWb mumu", "WWb emu"};
  std::string SRforMT2_120[] = {"MT2-120 ee", "MT2-120 mumu", "MT2-120 emu"};
  std::string SRforMT2_150[] = {"MT2-150 ee", "MT2-150 mumu", "MT2-150 emu"};

  std::string SRforWWa[] = {"WWa ee", "WWa mumu", "WWa emu"};
  std::string SRforWWb[] = {"WWb ee", "WWb mumu", "WWb emu"};
  std::string SRforWWc[] = {"WWc ee", "WWc mumu", "WWc emu"};

  std::string SRforZjets[] = {"Zjets ee", "Zjets mumu"};

  std::string SRforee[] = {"MT2-90 ee", "MT2-120 ee", "MT2-150 ee",
                           "WWa ee", "WWb ee", "WWc ee", "Zjets ee"};
  std::string SRformumu[] = {"MT2-90 mumu", "MT2-120 mumu", "MT2-150 mumu",
                             "WWa mumu", "WWb mumu", "WWc mumu", "Zjets mumu"};
  std::string SRforemu[] = {"MT2-90 emu", "MT2-120 emu", "MT2-150 emu",
                            "WWa emu", "WWb emu", "WWc emu"};

  std::string SRforMT2_WW[] = {"MT2-90 ee", "MT2-90 mumu", "MT2-90 emu",
                               "MT2-120 ee", "MT2-120 mumu", "MT2-120 emu",
                               "MT2-150 ee", "MT2-150 mumu", "MT2-150 emu",
                               "WWa ee", "WWa mumu", "WWa emu",
                               "WWb ee", "WWb mumu", "WWb emu",
                               "WWc ee", "WWc mumu", "WWc emu"};

  std::string SRforZveto[] = {"MT2-90 ee", "MT2-90 mumu",
                              "MT2-120 ee", "MT2-120 mumu",
                              "MT2-150 ee", "MT2-150 mumu",
                              "WWa ee", "WWa mumu",
                              "WWb ee", "WWb mumu",
                              "WWc ee", "WWc mumu"};

  std::string SRforWWa_Zjets[] = {"WWa ee", "WWa mumu", "WWa emu",
                               "Zjets ee", "Zjets mumu"};

  Manager()->AddCut("2 OS leptons");
  Manager()->AddCut("mll > 20 GeV");
  Manager()->AddCut("tau veto");

  Manager()->AddCut("ee leptons", SRforee);
  Manager()->AddCut("mumu leptons", SRformumu);
  Manager()->AddCut("emu leptons", SRforemu);

  Manager()->AddCut("jet veto", SRforMT2_WW);
  Manager()->AddCut(">= 2 central light jets", SRforZjets);
  Manager()->AddCut("b and forward jet veto", SRforZjets);

  Manager()->AddCut("Z veto", SRforZveto);
  Manager()->AddCut("Z window", SRforZjets);

  Manager()->AddCut("pTll > 80 GeV", SRforWWa_Zjets);

  Manager()->AddCut("METrel > 80 GeV", SRforWWa_Zjets);

  Manager()->AddCut("mT2 > 90 GeV", SRforMT2_90);
  Manager()->AddCut("mT2 > 100 GeV", SRforWWc);
  Manager()->AddCut("mT2 > 120 GeV", SRforMT2_120);
  Manager()->AddCut("mT2 > 150 GeV", SRforMT2_150);

  Manager()->AddCut("mll < 120 GeV", SRforWWa);
  Manager()->AddCut("mll < 170 GeV", SRforWWb);

  Manager()->AddCut("0.3 < Delta Rll < 1.5", SRforZjets);
  Manager()->AddCut("50 < mjj < 100 GeV", SRforZjets);
  Manager()->AddCut("pT 2 central jets > 45 GeV", SRforZjets);

  // finally, definition of histograms
  // they are all available on
  // https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-11/
  
  std::string SRforWWa_SF[] = {"WWa ee", "WWa mumu"};
  std::string SRforMT2_SF[] = {"MT2-90 ee", "MT2-90 mumu",
                               "MT2-120 ee", "MT2-120 mumu",
                               "MT2-150 ee", "MT2-150 mumu"};
  std::string SRforMT2_DF[] = {"MT2-90 emu", "MT2-120 emu", "MT2-150 emu"};

  
  Manager()->AddHisto("mll SF SR-WWa",12,20,140,SRforWWa_SF); // Fig. 3a
  Manager()->AddHisto("mll DF SR-WWa",12,20,140,"WWa emu"); // Fig. 3b
  Manager()->AddHisto("METrel SF SR-WWa",17,0,170,SRforWWa_SF); // Fig. 3c
  Manager()->AddHisto("METrel DF SR-WWa",17,0,170,"WWa emu"); // Fig. 3d

  Manager()->AddHisto("mT2 SF SR-mT2",20,0,200,SRforMT2_SF); // Fig. 4a
  Manager()->AddHisto("mT2 DF SR-mT2",20,0,200,SRforMT2_DF); // Fig. 4b
  Manager()->AddHisto("METrel SF SR-Zjets",20,0,200,SRforZjets); // Fig. 4c

  Manager()->AddHisto("METrel SF SR-mT2",20,0,200,SRforMT2_SF); // Fig. aux. 35a
  Manager()->AddHisto("METrel DF SR-mT2",20,0,200,SRforMT2_DF); // Fig. aux. 35b

  // for Fig. 3: need to switch off the first cut on mll ("Z veto")
  // (no need to switch off "mll < 120 GeV" for 3a, 3b which is the last cut)
  // (idem 3c, 3d:
  // "METrel > 80 GeV" and "mll < 120 GeV" are the last two cuts anyway)

  // for Fig. 4c: need to switch off the METrel cut
  // i.e. "METrel > 80 GeV"

  // for Fig. 4a, 4b, Fig. aux. 35a and 35b:
  // no need to switch off anything (mT2 is last cut)

  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2013_11::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  return;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2013_11::Execute(SampleFormat& sample, const EventFormat& event)
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
    std::vector<const RecJetFormat*> myJets, CentralLightJets, CentralBJets,
                                     ForwardJets;
    std::vector<const RecTauFormat*> myTaus;

    // filling lepton containers
    // electron satify the 'medium' criteria (put in the Delphes card)
    // and are required to be weakly isolated
    for(unsigned int ii=0; ii<event.rec()->electrons().size(); ii++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[ii]);
      double pt = CurrentElectron->pt();
      double abseta = fabs(CurrentElectron->eta());

      if(pt > 10. && abseta < 2.47)
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

      if(pt > 10. && abseta < 2.4)
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

    // filling tau container
    for(unsigned int ii=0; ii<event.rec()->taus().size(); ii++)
    {
      const RecTauFormat *CurrentTau = &(event.rec()->taus()[ii]);
      double pt = CurrentTau->pt();
      double abseta = fabs(CurrentTau->eta());

      if(pt > 20. && abseta < 2.5)
        myTaus.push_back(CurrentTau);
    }
      
    SORTER->sort(myElectrons);
    SORTER->sort(myMuons);
    SORTER->sort(myJets);
    SORTER->sort(myTaus);

    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    // Overlap removals
    // <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    OverlapRmvPT(myElectrons,0.05);
    OverlapRmv(myJets,myElectrons,0.2);
    OverlapRmv(myTaus,myElectrons,0.2);
    OverlapRmv(myTaus,myMuons,0.2);
    OverlapRmv(myElectrons,myJets,0.4);
    OverlapRmv(myMuons,myJets,0.4);
    OverlapDoubleRmv(myMuons,myElectrons,0.01);
    OverlapDoubleRmv(myMuons,0.05);

    KillResonances(myElectrons,12.);
    KillResonances(myMuons,12.);

    OverlapRmv(myJets,myTaus,0.2);

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
        if(fabs(myElectrons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        {
          if(myElectrons[ii]->isolCones()[jj].sumPT()
             > .16*myElectrons[ii]->pt())
          {
            myElectrons.erase(myElectrons.begin()+ii);
          }
          break;
        }
      }

      // 2) the sum of transverse energies of the surrounding calorimeter
      // clusters within Delta R = 0.3 of each electron candidate is required to
      // be less than 18% of the electron pT
      // this is *not* implemented at the current stage
    }

    // isolation of the muon
    for(int ii=myMuons.size()-1; ii>=0; ii--)
    {
      // the pT scalar sum of tracks above 400 MeV within a cone of size
      // Delta R = 0.3 around the muon candidate and associated to the primary
      // vertex is required to be less than 16% of the muon pT.

      for(unsigned int jj=0; jj<myMuons[ii]->isolCones().size(); jj++)
      {
        if(fabs(myMuons[ii]->isolCones()[jj].deltaR() - 0.3) < 0.001)
        {
          if(myMuons[ii]->isolCones()[jj].sumPT()
             > .16*myMuons[ii]->pt())
          {
            myMuons.erase(myMuons.begin()+ii);
          }
          break;
        }
      }
    }


    // now, fill the signal jets containers
    // *central b-jets satisfy |eta| < 2.4 and the b-jet identification criteria
    // *central light-flavour jets also satisfy |eta| < 2.5 but no b-tag
    // *forward jets are those with 2.4 < |eta| < 4.5 and pT > 30 GeV
    for(int ii=myJets.size()-1; ii>=0; ii--)
    {
      double abseta = fabs(myJets[ii]->eta());
      double pt = myJets[ii]->pt();

      if(abseta < 2.4)
      {
        if(myJets[ii]->btag())
          CentralBJets.push_back(myJets[ii]);
        else
          CentralLightJets.push_back(myJets[ii]);
      }
      else if(abseta < 4.5 && pt > 30.)
      {
        ForwardJets.push_back(myJets[ii]);
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

    // sort signal leptons by pT
    SORTER->sort(SignalLeptons);

    // 2 OS leptons with pT > 35 GeV and > 20 GeV
    bool CutCondition = (ne + nmu == 2);
    if(CutCondition) CutCondition = (SignalLeptons[0]->charge() != SignalLeptons[1]->charge());
    if(CutCondition) CutCondition = (SignalLeptons[0]->pt() > 35. && SignalLeptons[1]->pt() > 20.);

    if(CutCondition) // i.e. if there are 2 OS leptons with pT > 35 GeV and > 20 GeV
    {
      // apply trigger efficiencies
      if(ne == 2) myEventWeight *= 0.97;
      else if(nmu == 2) myEventWeight *= 0.89;
      else myEventWeight *= 0.75;

      // delphesMA5tune electrons are already medium
      // no need to apply a medium -> tight electron factor
      //if(ne == 2) myEventWeight *= 0.8;
      //else if(ne == 1) myEventWeight *= 0.9;

      Manager()->SetCurrentEventWeight(myEventWeight);
    }

    if(!Manager()->ApplyCut(CutCondition, "2 OS leptons"))
      return true;

    double mll = (SignalLeptons[0]->momentum() + SignalLeptons[1]->momentum()).M();

    // mll > 20 GeV
    if(!Manager()->ApplyCut(mll > 20., "mll > 20 GeV"))
      return true;

    // hadronic tau veto
    if(!Manager()->ApplyCut(myTaus.size() == 0, "tau veto"))
      return true;

    // ===============
    // end of preselection
    // ===============


    // ===============
    // definitions prior to the event selection per se
    // ===============

    // calculate metrel, the E_T^{miss,rel}
    MALorentzVector pmet = event.rec()->MET().momentum();
    double metrel = pmet.Pt();

    // calculate azimutal angle between the pTmiss and the nearest lepton
    // (only signal leptons are considered because extra leptons
    // veto the event anyway) or the nearest central jet (b- or light flavor)
    // (note that central jets are not vetoed in Zjets SRs
    double dphi = M_PI;
    double min_dr = 9999.;
    double cur_dr;

    for(unsigned int ii=0; ii<CentralBJets.size(); ii++)
    {
        cur_dr = CentralBJets[ii]->dr(pmet);
        if(cur_dr < min_dr)
        {
            dphi = CentralBJets[ii]->dphi_0_pi(pmet);
            min_dr = cur_dr;
        }
    }
    for(unsigned int ii=0; ii<CentralLightJets.size(); ii++)
    {
        cur_dr = CentralLightJets[ii]->dr(pmet);
        if(cur_dr < min_dr)
        {
            dphi = CentralLightJets[ii]->dphi_0_pi(pmet);
            min_dr = cur_dr;
        }
    }
    for(unsigned int ii=0; ii<SignalLeptons.size(); ii++)
    {
        cur_dr = SignalLeptons[ii]->dr(pmet);
        if(cur_dr < min_dr)
        {
            dphi = SignalLeptons[ii]->dphi_0_pi(pmet);
            min_dr = cur_dr;
        }
    }

    if(dphi < 0.5*M_PI)
        metrel *= sin(dphi);

    // calculate pTll, pT of the lepton pair
    double pTll = (SignalLeptons[0]->momentum() + SignalLeptons[1]->momentum()).Pt();

    // calculate mT2
    double mT2 = PHYSICS->Transverse->MT2(SignalLeptons[0], SignalLeptons[1], event.rec()->MET(), 0.);

    // ===============
    // next, we follow the cutflows from figaux_46-47-48-49 from Twiki page
    // ===============

    // the following corresponds to the "Two signal leptons" line in cutflows
    if(!Manager()->ApplyCut(ne == 2, "ee leptons")) // SF e+e-
        return true;
    if(!Manager()->ApplyCut(nmu == 2, "mumu leptons")) // SF mu+mu-
        return true;
    if(!Manager()->ApplyCut(ne == 1 && nmu == 1, "emu leptons")) // DF emu
        return true;

    double n_centralb_forward_jets = CentralBJets.size() + ForwardJets.size();
    double n_centrallight_jets = CentralLightJets.size();
    double ntot_jets = n_centralb_forward_jets + n_centrallight_jets;

    double mz = 91.2; // Z boson mass, in GeV

    // corresponds to "Jet veto" line in cutflows for the mT2 and WW SRs
    if(!Manager()->ApplyCut(ntot_jets == 0, "jet veto"))
        return true;

    // for the Zjets SRs
    // corresponds to "> 1 light jets" in cutflows
    if(!Manager()->ApplyCut(n_centrallight_jets > 1, ">= 2 central light jets"))
        return true;
    // corresponds to "No b- and forward jets" in cutflows
    if(!Manager()->ApplyCut(n_centralb_forward_jets == 0, "b and forward jet veto"))
        return true;

    // "Z veto" line in mT2 and WW SRs with SF leptons
    // §§ should be switched off for Fig. 3
    if(!Manager()->ApplyCut(fabs(mll - mz) > 10., "Z veto"))
        return true;
    // "Z window" line in Zjets SRs
    if(!Manager()->ApplyCut(fabs(mll - mz) < 10., "Z window"))
        return true;

    // "p_{T,ll} > 80 GeV" in WWa and Zjets SRs
    if(!Manager()->ApplyCut(pTll > 80., "pTll > 80 GeV"))
        return true;

    // fill Fig. 3c and 3d: satify all SR-WWa cuts except cuts on mll and METrel
    // (!note that Z veto above should be switched off!)
    Manager()->FillHisto("METrel SF SR-WWa", metrel);
    Manager()->FillHisto("METrel DF SR-WWa", metrel);

    // "E_T^{miss,rel} > 80 GeV" in WWa and Zjets SRs
    // §§ should be switched off for Fig. 4c
    if(!Manager()->ApplyCut(metrel > 80., "METrel > 80 GeV"))
        return true;

    // fill Fig. 4a, 4b, Fig. aux. 35a and 35b:
    // satisfy all SR-mT2 except the cuts on mT2
    Manager()->FillHisto("mT2 SF SR-mT2", mT2);
    Manager()->FillHisto("mT2 DF SR-mT2", mT2);
    Manager()->FillHisto("METrel SF SR-mT2", metrel);
    Manager()->FillHisto("METrel DF SR-mT2", metrel);

    // "m_{T2} > 90 GeV" in WWb SRs and to "SR-m^{90}_{T2}" in mT2-90 SRs
    if(!Manager()->ApplyCut(mT2 > 90., "mT2 > 90 GeV"))
        return true;
    // "m_{T2} > 100 GeV" in WWc SRs
    if(!Manager()->ApplyCut(mT2 > 100., "mT2 > 100 GeV"))
        return true;
    // "SR-m^{120}_{T2}" in mT2-120 SRs
    if(!Manager()->ApplyCut(mT2 > 120., "mT2 > 120 GeV"))
        return true;
    // SR-m^{150}_{T2}" in mT2-150 SRs
    if(!Manager()->ApplyCut(mT2 > 150., "mT2 > 150 GeV"))
        return true;

    // fill Fig. 3a and 3b: satify all SR-WWa cuts except cuts on mll
    // (!note that Z veto above should be switched off!)
    Manager()->FillHisto("mll SF SR-WWa", mll);
    Manager()->FillHisto("mll DF SR-WWa", mll);

    // "m_{ll} < 120 GeV" in WWa SRs
    if(!Manager()->ApplyCut(mll < 120., "mll < 120 GeV"))
        return true;
    // "m_{ll} < 170 GeV" in WWb SRs
    if(!Manager()->ApplyCut(mll < 170., "mll < 170 GeV"))
        return true;

    // specific to Zjets SRs
    double deltaRll = SignalLeptons[0]->dr(SignalLeptons[1]);
    double mjj=0., pTjet1=0., pTjet2=0.;
    if(n_centrallight_jets > 1)
    {
      // Zjets SRs
      mjj = (CentralLightJets[0]->momentum() + CentralLightJets[1]->momentum()).M();
      pTjet1 = CentralLightJets[0]->pt();
      pTjet2 = CentralLightJets[1]->pt();
    }

    // "0.3 < \Delta R_{ll} < 1.5" in Zjets SRs
    if(!Manager()->ApplyCut(deltaRll > 0.3 && deltaRll < 1.5, "0.3 < Delta Rll < 1.5"))
        return true;

    // "50 < m_{jj} < 100 GeV" in Zjets SRs
    if(!Manager()->ApplyCut(mjj > 50. && mjj < 100., "50 < mjj < 100 GeV"))
        return true;

    // "Jet p_T > 45 GeV" in Zjets SRs
    // corresponds to "The two highest-pT central light jets must have pT > 45 GeV"
    if(!Manager()->ApplyCut(pTjet1 > 45. && pTjet2 > 45., "pT 2 central jets > 45 GeV"))
        return true;

    // fill Fig. 4c: satify all SR-Zjets cuts except the one on METrel
    // (!note that the METrel cut above should be switchedd off!)
    Manager()->FillHisto("METrel SF SR-Zjets", metrel);
  }
  return true;
}


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

