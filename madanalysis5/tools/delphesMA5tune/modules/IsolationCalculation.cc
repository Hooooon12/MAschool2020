// ------- BEGIN MA5 CHANGE -------

/** \class Isolation
 *
 *  Sums transverse momenta of isolation objects (tracks, calorimeter towers, etc)
 *  within a DeltaR cone around a candidate and calculates fraction of this sum
 *  to the candidate's transverse momentum. outputs candidates that have
 *  the transverse momenta fraction within (PTRatioMin, PTRatioMax].
 *
 *  $Date: 2013-08-19 15:40:54 +0200 (Mon, 19 Aug 2013) $
 *  $Revision: 1267 $
 *
 *
 *  \author P. Demin - UCL, Louvain-la-Neuve
 *
 */

#include "modules/IsolationCalculation.h"

#include "classes/DelphesClasses.h"
#include "classes/DelphesFactory.h"
#include "classes/DelphesFormula.h"

#include "ExRootAnalysis/ExRootResult.h"
#include "ExRootAnalysis/ExRootFilter.h"
#include "ExRootAnalysis/ExRootClassifier.h"

#include "TMath.h"
#include "TString.h"
#include "TFormula.h"
#include "TRandom3.h"
#include "TObjArray.h"
#include "TDatabasePDG.h"
#include "TLorentzVector.h"

#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

//------------------------------------------------------------------------------

class IsolationCalculationClassifier : public ExRootClassifier
{
public:

  IsolationCalculationClassifier() {}

  Int_t GetCategory(TObject *object);

  Double_t fTrack_PTMin;
  Double_t fCaloTower_PTMin;
  Double_t fEflow_PTMin;
};

//------------------------------------------------------------------------------

Int_t IsolationCalculationClassifier::GetCategory(TObject *object)
{
  Candidate *track = static_cast<Candidate*>(object);
  const TLorentzVector &momentum = track->Momentum;

  if(momentum.Pt() < fTrack_PTMin) return -1;

  return 0;
}


IsolationCalculation::IsolationCalculation() :
  fClassifier(0), 
  fOutputArray(0),
  fItTrackInputArray(0), 
  fItCaloTowerInputArray(0), 
  fIt_eflow_InputArray(0), 
  fItCandidateInputArray(0)
{
  fClassifier = new IsolationCalculationClassifier;
}

//------------------------------------------------------------------------------

IsolationCalculation::~IsolationCalculation()
{
}

//------------------------------------------------------------------------------

void IsolationCalculation::Init()
{
  // Import parameters
  fClassifier->fTrack_PTMin        = GetDouble("Track_PTMin",        0.5);
  fClassifier->fEflow_PTMin        = GetDouble("Eflow_PTMin",        0.5);
  fClassifier->fCaloTower_PTMin    = GetDouble("CaloTower_PTMin",    0.5);

  // Create output arrays
  fOutputArray = ExportArray(GetString("OutputArray", "DelphesMA5tuneElectrons"));

  // Import input arrays
  fTrackInputArray          = ImportArray(GetString("TrackInputArray",        "Delphes/partons"));
  f_eflow_InputArray        = ImportArray(GetString("EflowInputArray",        "Delphes/partons"));
  fCaloTowerInputArray      = ImportArray(GetString("CaloTowerInputArray",    "Delphes/partons"));
  fCandidateInputArray      = ImportArray(GetString("CandidateInputArray",    "Calorimeter/electrons"));

  // Iterator
  fItTrackInputArray          = fTrackInputArray->MakeIterator();
  fIt_eflow_InputArray   = f_eflow_InputArray->MakeIterator();
  fItCaloTowerInputArray      = fCaloTowerInputArray->MakeIterator();
  fItCandidateInputArray      = fCandidateInputArray->MakeIterator();

  // PileUp
  const char *rhoInputArrayName;
  rhoInputArrayName = GetString("RhoInputArray", "");
  if(rhoInputArrayName[0] != '\0') fRhoInputArray = ImportArray(rhoInputArrayName);
  else fRhoInputArray = 0;
}

//------------------------------------------------------------------------------

void IsolationCalculation::Finish()
{
  if (fItCandidateInputArray)      delete fItCandidateInputArray;
  if (fItCaloTowerInputArray)      delete fItCaloTowerInputArray;
  if (fItTrackInputArray)          delete fItTrackInputArray;
  if (fIt_eflow_InputArray)        delete fIt_eflow_InputArray;
}

//------------------------------------------------------------------------------
void ProcessAgainstCollection(Candidate* candidate, TIterator* itArray,
                              double PTmin, 
                              const std::vector<double>& cones,
                              std::vector<double>& sumPT, 
                              std::vector<unsigned int>& counter) 
{
  // Initialize output containers
  sumPT.resize(cones.size(),0.);
  counter.resize(cones.size(),0);

  // safety
  if (cones.size()==0) return;

  // Reset the iterator
  itArray->Reset();

  // Loop over particles
  Candidate* isolation = 0;
  while((isolation = static_cast<Candidate*>(itArray->Next())))
  {
    // reject overlapping particle
    if (candidate->Overlaps(isolation)) {continue;}

    // Short-cut to the 4-momentum
    const TLorentzVector &isolationMomentum = isolation->Momentum;

    // reject particle PT
    if (isolationMomentum.Pt()<PTmin) continue;
    else if (isolationMomentum.Pt()<1.e-6) continue;

    // Computing DeltaR
    double DR = isolationMomentum.DeltaR(candidate->Momentum);
      
    // Compute the sumPT
    for (unsigned int i=0;i<cones.size();i++)
    {
      if (DR<=cones[i]) 
      {
        sumPT[i]+=isolationMomentum.Pt();
        counter[i]++;
      }
    }
  }

}

void IsolationCalculation::Process()
{
  Candidate* candidate = 0;

  // Pile-Up
  Double_t rho = 0.0;
  if (fRhoInputArray && fRhoInputArray->GetEntriesFast() > 0)
  {
    candidate = static_cast<Candidate*>(fRhoInputArray->At(0));
    rho = candidate->Momentum.Pt();
  }

  // container with cones size
  std::vector<double> cones;
  cones.push_back(0.5);
  cones.push_back(0.4);
  cones.push_back(0.3);
  cones.push_back(0.2);

  // loop over all candidate
  fItCandidateInputArray->Reset();
  while((candidate = static_cast<Candidate*>(fItCandidateInputArray->Next())))
  {
    const TLorentzVector &candidateMomentum = candidate->Momentum;

    // safety: no particle with null pt
    if (candidateMomentum.Pt()<1.e-6) continue;

    // compute isolation values against tracks
    std::vector<double> track_sumPT;
    std::vector<unsigned int> track_counter;
    ProcessAgainstCollection(candidate,fItTrackInputArray,fClassifier->fTrack_PTMin,cones,track_sumPT,track_counter);

    // compute isolation values against calo tower
    std::vector<double> calo_sumET;
    std::vector<unsigned int> calo_counter;
    ProcessAgainstCollection(candidate,fItCaloTowerInputArray,fClassifier->fCaloTower_PTMin,cones,calo_sumET,calo_counter);

    // compute isolation values against eflow tracks
    std::vector<double> eflow_sumPT;
    std::vector<unsigned int> eflow_counter;
    ProcessAgainstCollection(candidate,fIt_eflow_InputArray,fClassifier->fEflow_PTMin,cones,eflow_sumPT,eflow_counter);

    // Clone the candidate 
    candidate = static_cast<Candidate*>(candidate->Clone());
    candidate->sumPT05  = track_sumPT[0];
    candidate->sumPT04  = track_sumPT[1];
    candidate->sumPT03  = track_sumPT[2];
    candidate->sumPT02  = track_sumPT[3];
    candidate->sumET05  = calo_sumET[0];
    candidate->sumET04  = calo_sumET[1];
    candidate->sumET03  = calo_sumET[2];
    candidate->sumET02  = calo_sumET[3];
    candidate->nTrack05 = track_counter[0];
    candidate->nTrack04 = track_counter[1];
    candidate->nTrack03 = track_counter[2];
    candidate->nTrack02 = track_counter[3];
    candidate->eflow_sumPT05  = eflow_sumPT[0];
    candidate->eflow_sumPT04  = eflow_sumPT[1];
    candidate->eflow_sumPT03  = eflow_sumPT[2];
    candidate->eflow_sumPT02  = eflow_sumPT[3];

    candidate->eflow_nTrack05 = track_sumPT[0];
    candidate->eflow_nTrack04 = track_sumPT[1];
    candidate->eflow_nTrack03 = track_sumPT[2];
    candidate->eflow_nTrack02 = track_sumPT[3];

    // Correct sum for pile-up contamination
    candidate->sumPT05 -= rho*0.5*0.5*TMath::Pi();  
    candidate->sumPT04 -= rho*0.4*0.4*TMath::Pi();  
    candidate->sumPT03 -= rho*0.3*0.3*TMath::Pi();  
    candidate->sumPT02 -= rho*0.2*0.2*TMath::Pi();  
    candidate->eflow_sumPT05 -= rho*0.5*0.5*TMath::Pi();  
    candidate->eflow_sumPT04 -= rho*0.4*0.4*TMath::Pi();  
    candidate->eflow_sumPT03 -= rho*0.3*0.3*TMath::Pi();  
    candidate->eflow_sumPT02 -= rho*0.2*0.2*TMath::Pi();  

    // Save the new candidate
    fOutputArray->Add(candidate);
  }
}

//------------------------------------------------------------------------------

// ------- END MA5 CHANGE -------
