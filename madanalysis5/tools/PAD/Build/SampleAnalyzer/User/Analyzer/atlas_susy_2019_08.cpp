#include "SampleAnalyzer/User/Analyzer/atlas_susy_2019_08.h"
using namespace MA5;
using namespace std;


MAfloat64 sumET(const RecLeptonFormat* part, 
                              const std::vector<RecTrackFormat>& towers,
                              const MAfloat64& DR) 
{
  MAfloat64 sumET=0.;
  MAuint32 counter=0;

  // Loop over the tracks
  for (MAuint32 i=0;i<towers.size();i++)
  {
    const RecTrackFormat& tower = towers[i];


    // Cut on the DR
    if (part->momentum().DeltaR(tower.momentum()) > DR) continue;

    // Sum
    sumET += tower.et();
    counter++;
  }

  // return PT sum of towers in the cone
  return sumET;
};


MAfloat64 sumET(const RecLeptonFormat* part, 
                              const std::vector<RecTowerFormat>& towers,
                              const MAfloat64& DR) 
{
  MAfloat64 sumET=0.;
  MAuint32 counter=0;

  // Loop over the tracks
  for (MAuint32 i=0;i<towers.size();i++)
  {
    const RecTowerFormat& tower = towers[i];


    // Cut on the DR
    if (part->momentum().DeltaR(tower.momentum()) > DR) continue;

    // Sum
    sumET += tower.et();
    counter++;
  }

  // return PT sum of towers in the cone
  return sumET;
};




MAfloat64 sumET(const RecLeptonFormat* part, 
                              const std::vector<RecParticleFormat>& towers,
                              const MAfloat64& DR) 
{
  MAfloat64 sumET=0.;
  MAuint32 counter=0;

  // Loop over the tracks
  for (MAuint32 i=0;i<towers.size();i++)
  {
    const RecParticleFormat& tower = towers[i];


    // Cut on the DR
    if (part->momentum().DeltaR(tower.momentum()) > DR) continue;

    // Sum
    sumET += tower.et();
    counter++;
  }

  // return PT sum of towers in the cone
  return sumET;
};


MAfloat64 sumETIsolation(const RecLeptonFormat* part, const RecEventFormat* event, const MAfloat64& DR) 
    {
      if (part==0) return 0;
      if (event==0) return 0;
      MAfloat64 sum=0.;   
      sum += sumET(part,event->EFlowTracks(),DR);
      sum += sumET(part,event->EFlowPhotons(),DR);
      sum += sumET(part,event->EFlowNeutralHadrons(),DR);
      sum -= part->et();
      return sum;
    }





bool IsLooseTightLepton(const RecLeptonFormat* Lep, const EventFormat& event,
		   const double DeltaRp, const double DeltaRE, const double pratio, const double Eratio)
{
  // varconeXX for momentum, coneXX for transverse energy
  double pt = Lep->pt();
  if(pt < 1.0) // just to be sure ... cut is much stricter than this on pt anyway
    {
      return false;
    };
  double DRp = std::min(10.0/pt,DeltaRp);
  double imini = (PHYSICS->Isol->eflow->sumIsolation(Lep,event.rec(),DRp,1.0,IsolationEFlow::ALL_COMPONENTS))/pt;
  
  if (imini > pratio)
    {
      return false;

    };
  
  double jmini = sumETIsolation(Lep,event.rec(),DeltaRE)/pt;
  
  if (jmini > Eratio)
    {
      return false;

    };


  return true;
}


bool IsHighPTCaloOnly(const RecLeptonFormat* Lep, const EventFormat& event,
		    const double DeltaRE)
{
  // double eta = std::fabs(Lep->eta());
  // double pt = Lep->pt();

  // double DR = 10./std::min(std::max(pt,50.),200.);
  // double imini = (PHYSICS->Isol->eflow->sumIsolation(Lep,
  //   event.rec(),DR,0.,IsolationEFlow::ALL_COMPONENTS))/pt;

  // if( eta<etaTH && pt>ptTH && imini<0.4) return true;

  // varconeXX for momentum, coneXX for transverse energy
  double pt = Lep->pt();
  if(pt < 1.0) // We only apply this for pt> 200, but here we're just being safe
    {
      return false;
    };
  //double DRp = std::min(10.0/pt,DeltaRp);
  double ETratio=std::max(0.015*pt,3.5);
  
  double jmini = sumETIsolation(Lep,event.rec(),DeltaRE);
 
  if (jmini > ETratio)
    {
      return false;

    };


  return true;
}





// Overlap Removal
template<typename T1, typename T2> std::vector<const T1*>
  Removal(std::vector<const T1*> &v1, std::vector<const T2*> &v2,
  const double &drmin)
{
  // Determining with objects should be removed
  std::vector<bool> mask(v1.size(),false);
  for (unsigned int j=0;j<v1.size();j++)
    for (unsigned int i=0;i<v2.size();i++)
      if (v2[i]->dr(v1[j]) < drmin)
      {
        mask[j]=true;
        break;
      }

  // Building the cleaned container
  std::vector<const T1*> cleaned_v1;
  for (unsigned int i=0;i<v1.size();i++)
    if (!mask[i]) cleaned_v1.push_back(v1[i]);

  return cleaned_v1;
}



// Overlap Removal for electrons with Delta R < min(0.4, 0.04 + 10 GeV/pT) around Jet
template<typename T1, typename T2> std::vector<const T1*>
  RemovalJE(std::vector<const T1*> &v1, std::vector<const T2*> &v2)
{
  // Determining with objects should be removed
  double EPT,drmin;
  std::vector<bool> mask(v1.size(),false);
  for (unsigned int j=0;j<v1.size();j++)
    {
      EPT=v1[j]->pt();
      drmin=0.04+10/EPT;
      if(drmin > 0.4) drmin=0.4;
    
      for (unsigned int i=0;i<v2.size();i++)
	if (v2[i]->dr(v1[j]) < drmin)
	  {
	    mask[j]=true;
	    break;
	  }
    }
  // Building the cleaned container
  std::vector<const T1*> cleaned_v1;
  for (unsigned int i=0;i<v1.size();i++)
    if (!mask[i]) cleaned_v1.push_back(v1[i]);

  return cleaned_v1;
}



// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool atlas_susy_2019_08::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  // initialize variables, histos
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "      <>    Analysis: ATLAS-SUSY-2019-08              <>" << endmsg;
  INFO << "      <>             arXiv:1909.09226                 <>" << endmsg;
  INFO << "      <>         chargino + neutralino->W->lv+H->bb   <>" << endmsg;
  INFO << "      <>   Recasters:  M. Goodsell                    <>" << endmsg;
  INFO << "      <>   Contact: goodsell@lpthe.jussieu.fr         <>" << endmsg;
  INFO << "      <>   Based on MadAnalysis 5 v1.8                <>" << endmsg;
  INFO << "      <><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;


  // Declaration of the signal regions (SR)
  Manager()->AddRegionSelection("LMdisc");
  Manager()->AddRegionSelection("MMdisc");
  Manager()->AddRegionSelection("HMdisc");

  Manager()->AddRegionSelection("LMlowCT");
  Manager()->AddRegionSelection("LMmedCT");
  Manager()->AddRegionSelection("LMhighCT");

  Manager()->AddRegionSelection("MMlowCT");
  Manager()->AddRegionSelection("MMmedCT");
  Manager()->AddRegionSelection("MMhighCT");

  Manager()->AddRegionSelection("HMlowCT");
  Manager()->AddRegionSelection("HMmedCT");
  Manager()->AddRegionSelection("HMhighCT");

  //Preselection Cuts
  //Manager()->AddCut("Preselection cuts");
  


  
  std::string alldiscSRs[]={"LMdisc","MMdisc","HMdisc"};
  std::string allSRs[]={"LMdisc","MMdisc","HMdisc","LMlowCT","LMmedCT","LMhighCT","MMlowCT","MMmedCT","MMhighCT","HMlowCT","HMmedCT","HMhighCT"};

  std::string LMexcl[]={"LMlowCT","LMmedCT","LMhighCT"};
  std::string allLM[]={"LMdisc","LMlowCT","LMmedCT","LMhighCT"};

  std::string MMexcl[]={"MMlowCT","MMmedCT","MMhighCT"};
  std::string allMM[]={"MMdisc","MMlowCT","MMmedCT","MMhighCT"};

  std::string HMexcl[]={"HMlowCT","HMmedCT","HMhighCT"};
  std::string allHM[]={"HMdisc","HMlowCT","HMmedCT","HMhighCT"};
  
    
  std::string lowCT[]={"LMlowCT","MMlowCT","HMlowCT"};
  std::string medCT[]={"LMmedCT","MMmedCT","HMmedCT"};
  std::string highCT[]={"LMhighCT","MMhighCT","HMhighCT"};


  
  
  // for cutflows, preselection cuts are split out:
  
  Manager()->AddCut("Njets25 >=2",allSRs);
  Manager()->AddCut("1 signal lepton",allSRs);
  Manager()->AddCut("Second baseline lepton veto",allSRs);
  Manager()->AddCut("mT>50",allSRs);
  Manager()->AddCut("ET>180",allSRs);
  Manager()->AddCut("Njets<=3",allSRs);
  Manager()->AddCut("2 bjets",allSRs);
  Manager()->AddCut("mbb>50",allSRs);
  Manager()->AddCut("ET>240",allSRs);
  Manager()->AddCut("mbb",allSRs);

  // Then add the actual cuts

  Manager()->AddCut("mlb > 120",allHM);

  Manager()->AddCut("mT in [100,160]",allLM);
  Manager()->AddCut("mT in [160,240]",allMM);
  Manager()->AddCut("mT > 240",allHM);

  Manager()->AddCut("minCT",alldiscSRs);

  Manager()->AddCut("mCT in [180,230]",lowCT);
  Manager()->AddCut("mCT in [230,280]",medCT);
  Manager()->AddCut("mCT > 280",highCT);

  // Event counter
  Nevents = 0;
  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void atlas_susy_2019_08::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  cout << "BEGIN Finalization" << endl;
  // saving histos
  cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool atlas_susy_2019_08::Execute(SampleFormat& sample, const EventFormat& event)
{
  
  Nevents += 1;
  //  cout << "Executing event" << Nevents << endl;

  // Event weight
  if(event.rec()!=0)
  {
    //    cout << "Event has " << (event.rec()->electrons().size()+event.rec()->muons().size()) << " leptons and weight " << event.mc()->weight() << endl;
  }
  double myWeight=1.;
  if (!Configuration().IsNoEventWeight()) myWeight=event.mc()->weight();
  else if(event.mc()->weight()!=0.) myWeight=event.mc()->weight();
  else
  {
    //////WARNING << "Found one event with a zero weight. Skipping...\n";
    return false;
  }

  
  Manager()->InitializeForNewEvent(myWeight);
  //cout << "weight is " << myWeight << endl;
  // The event loop start here
  if(event.rec()!=0)
  {
    //cout << "Good event" << endl;
    // Containers
    std::vector<const RecLeptonFormat*> Electrons, Muons, BaselineLeptons;
    std::vector<const RecJetFormat*> Jets, SignalJets, bJets;

    //cout << "Event has " << (event.rec()->electrons().size()+event.rec()->muons().size()) << " leptons" << endl;
    
    // Electrons
    for(unsigned int e=0; e<event.rec()->electrons().size(); e++)
    {
      const RecLeptonFormat *CurrentElectron = &(event.rec()->electrons()[e]);
      if(CurrentElectron->pt()>7. && fabs(CurrentElectron->eta())<2.47)
	{
	  // Loose -> Baseline
	  // then check tight, tight + HighPTCaloOnly for pt > 200
	  // dRp, dRE, ratiop, ratio
	  // loose is 0.2, 0.2, 0.15, 0.2
	  // tight is 0.2, 0.2, 0.06, 0.06
	  
	      if(IsLooseTightLepton(CurrentElectron, event,
			       0.2, 0.2, 0.15, 0.2))
		{
		  // at least it's loose
		  if((IsLooseTightLepton(CurrentElectron, event, 0.2, 0.2, 0.06, 0.06)))
		    {
		      
		      // may be signal depends on pt check
		      if((CurrentElectron->pt()<200.0) || IsHighPTCaloOnly(CurrentElectron, event,0.2))
		     {
		       Electrons.push_back(CurrentElectron);
		     }
		      else
			{
			  BaselineLeptons.push_back(CurrentElectron);
			}
		    }
		  else
		    {
		      BaselineLeptons.push_back(CurrentElectron);
		    }
		}
	        
	}
    }
    SORTER->sort(Electrons);
    
    // Muons
    for(unsigned int mu=0; mu<event.rec()->muons().size(); mu++)
    {
      const RecLeptonFormat *CurrentMuon = &(event.rec()->muons()[mu]);
      if(CurrentMuon->pt()>6. && fabs(CurrentMuon->eta())<2.7)
	{
	  // at least a baseline muon
	  
	  if(CurrentMuon->pt()>6. && fabs(CurrentMuon->eta())<2.5)
	    {
	      if(IsLooseTightLepton(CurrentMuon, event,
			       0.3, 0.2, 0.15, 0.3))
		{
		  Muons.push_back(CurrentMuon);
		  
		}
	      else
		{
		  BaselineLeptons.push_back(CurrentMuon);
		}
	    }
	  else
	    {
	      BaselineLeptons.push_back(CurrentMuon);
	    }
	}
      //Muons.push_back(CurrentMuon);
    }
    
    // Jets
    for(unsigned int j=0; j<event.rec()->jets().size(); j++)
    {
      const RecJetFormat *CurrentJet = &(event.rec()->jets()[j]);
      //      if(CurrentJet->pt()>30. && fabs(CurrentJet->eta())<2.8)
      //  Jets.push_back(CurrentJet);
      if(CurrentJet->pt()>20. && fabs(CurrentJet->eta())<2.8)
        Jets.push_back(CurrentJet);
      
    }

    //Overlap removal
    //Jets = Removal(Jets, Electrons,  0.2);
    Jets = Removal(Jets, Muons,  0.2);
    //   Electrons = Removal(Electrons, Jets,  0.4);   // actually this should be min(0.4,0.04 + 10 GeV/pT)
    Electrons = RemovalJE(Electrons, Jets);  
    //Muons = Removal(Muons, Jets,  0.4);
    Muons = RemovalJE(Muons, Jets);
    
    // MET
    MALorentzVector pTmiss = event.rec()->MET().momentum();
    double MET = pTmiss.Pt();

    //int nb=0;

    MALorentzVector bJetMomentum;
    for (unsigned int i=0;i<Jets.size();i++)
      {
        if(Jets[i]->pt()>30.)
	  {
	    SignalJets.push_back(Jets[i]);
	  }
              
	if(Jets[i]->btag() && fabs(Jets[i]->eta())<2.5)
	  {
	    bJets.push_back(Jets[i]);
	    bJetMomentum+=Jets[i]->momentum();
	  };

      }

    SORTER->sort(bJets);
    
    unsigned int NJets = SignalJets.size();
    //Preselection cuts
    // Manager()->AddCut("Njets25 >=2",allSRs);
  // Manager()->AddCut("1 signal lepton",allSRs);
  // Manager()->AddCut("ET>180",allSRs);
  // Manager()->AddCut("Njets<=3",allSRs);
  // Manager()->AddCut("2 bjets",allSRs);
  // Manager()->AddCut("mbb>50",allSRs);
  // Manager()->AddCut("ET>240",allSRs);
  // Manager()->AddCut("mbb",allSRs);

    
    bool IsMET180=  (MET>180.);
    bool IsNJets2 = (NJets>1);
    
    bool IsMET = (MET>240.);
    bool IsLeptons = ((Electrons.size()+Muons.size())==1);
    bool IsNJets = (NJets ==2) || (NJets ==3);
    bool isBJets = (bJets.size() == 2);

    unsigned int NbaselineL= BaselineLeptons.size();

    bool NoBaselineLeptons= (NbaselineL == 0);
    
    bool isFromHiggs = false;
    bool mbb50 = false;
    if(isBJets)
      {
	double mbb = bJetMomentum.M();
	mbb50=(mbb>50.0);
	isFromHiggs = (mbb > 100.) && (mbb < 140.);
      }
    
    if(!Manager()->ApplyCut(IsNJets2,"Njets25 >=2")) return true;
    if(!Manager()->ApplyCut(IsLeptons,"1 signal lepton")) return true;
    if(!Manager()->ApplyCut(NoBaselineLeptons,"Second baseline lepton veto")) return true;
    MALorentzVector leptonp;
    if (Electrons.size() == 1)
      {
	// only one, so lepton pt is electron pt
	leptonp=Electrons[0]->momentum();
      }
    else
      {
	leptonp=Muons[0]->momentum();
      }
    
    double mT = sqrt(2.0*leptonp.Pt()*MET*(1.0-cos(leptonp.DeltaPhi(pTmiss))));
    bool IsMT50 = (mT > 50.);
    if(!Manager()->ApplyCut(IsMT50,"mT>50")) return true;
    if(!Manager()->ApplyCut(IsMET180,"ET>180")) return true;
    if(!Manager()->ApplyCut(IsNJets,"Njets<=3")) return true;
    if(!Manager()->ApplyCut(isBJets,"2 bjets")) return true;
    if(!Manager()->ApplyCut(mbb50,"mbb>50")) return true;
    if(!Manager()->ApplyCut(IsMET,"ET>240")) return true;
    if(!Manager()->ApplyCut(isFromHiggs,"mbb")) return true;
    
    
    MALorentzVector bjetmom1,bjetmom2;
    bjetmom1=bJets[0]->momentum();
    bjetmom2=bJets[1]->momentum();
    
    double mCT = sqrt(2.0*(bjetmom1.Pt())*(bjetmom2.Pt())*(1.0+cos(bjetmom1.DeltaPhi(bjetmom2))));
    double mlb = (bjetmom1+leptonp).M();

    if(!Manager()->ApplyCut(mlb> 120.0,"mlb > 120")) return true;

    if(!Manager()->ApplyCut((mT > 100.0) && (mT < 160.0),"mT in [100,160]")) return true;
    if(!Manager()->ApplyCut((mT > 160.0) && (mT < 240.0),"mT in [160,240]")) return true;
    if(!Manager()->ApplyCut(mT > 240.0,"mT > 240")) return true;
        
    if(!Manager()->ApplyCut(mCT> 180.0,"minCT")) return true;

    if(!Manager()->ApplyCut(((mCT > 180.) && (mCT < 230.0)),"mCT in [180,230]")) return true;
    if(!Manager()->ApplyCut(((mCT > 230.) && (mCT < 280.0)),"mCT in [230,280]")) return true;
    if(!Manager()->ApplyCut(mCT > 280.,"mCT > 280")) return true;
    
  }
  
    return true;
}

