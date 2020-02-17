/*
 *  Delphes: a framework for fast simulation of a generic collider experiment
 *  Copyright (C) 2012-2014  Universite catholique de Louvain (UCL), Belgium
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */


/** \class TreeWriter
 *
 *  Fills ROOT tree branches.
 *
 *  \author P. Demin - UCL, Louvain-la-Neuve
 *
 */

#include "modules/TreeWriter.h"

#include "classes/DelphesClasses.h"
#include "classes/DelphesFactory.h"
#include "classes/DelphesFormula.h"

#include "ExRootAnalysis/ExRootResult.h"
#include "ExRootAnalysis/ExRootFilter.h"
#include "ExRootAnalysis/ExRootClassifier.h"
#include "ExRootAnalysis/ExRootTreeBranch.h"

#include "TROOT.h"
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

using namespace std;

//------------------------------------------------------------------------------

TreeWriter::TreeWriter()
{
}

//------------------------------------------------------------------------------

TreeWriter::~TreeWriter()
{
}

//------------------------------------------------------------------------------

void TreeWriter::Init()
{
  fClassMap[GenParticle::Class()] = &TreeWriter::ProcessParticles;
  fClassMap[Vertex::Class()] = &TreeWriter::ProcessVertices;
  fClassMap[Track::Class()] = &TreeWriter::ProcessTracks;
  fClassMap[Tower::Class()] = &TreeWriter::ProcessTowers;
  fClassMap[Photon::Class()] = &TreeWriter::ProcessPhotons;
  fClassMap[Electron::Class()] = &TreeWriter::ProcessElectrons;
  fClassMap[Muon::Class()] = &TreeWriter::ProcessMuons;
  fClassMap[Jet::Class()] = &TreeWriter::ProcessJets;
  fClassMap[MissingET::Class()] = &TreeWriter::ProcessMissingET;
  fClassMap[ScalarHT::Class()] = &TreeWriter::ProcessScalarHT;
  fClassMap[Rho::Class()] = &TreeWriter::ProcessRho;
  fClassMap[Weight::Class()] = &TreeWriter::ProcessWeight;
  fClassMap[HectorHit::Class()] = &TreeWriter::ProcessHectorHit;

  TBranchMap::iterator itBranchMap;
  map< TClass *, TProcessMethod >::iterator itClassMap;

  // read branch configuration and
  // import array with output from filter/classifier/jetfinder modules

  ExRootConfParam param = GetParam("Branch");
  Long_t i, size;
  TString branchName, branchClassName, branchInputArray;
  TClass *branchClass;
  TObjArray *array;
  ExRootTreeBranch *branch;

  size = param.GetSize();
  for(i = 0; i < size/3; ++i)
  {
    branchInputArray = param[i*3].GetString();
    branchName = param[i*3 + 1].GetString();
    branchClassName = param[i*3 + 2].GetString();

    branchClass = gROOT->GetClass(branchClassName);

    if(!branchClass)
    {
      cout << "** ERROR: cannot find class '" << branchClassName << "'" << endl;
      continue;
    }

    itClassMap = fClassMap.find(branchClass);
    if(itClassMap == fClassMap.end())
    {
      cout << "** ERROR: cannot create branch for class '" << branchClassName << "'" << endl;
      continue;
    }

    array = ImportArray(branchInputArray);
    branch = NewBranch(branchName, branchClass);

    fBranchMap.insert(make_pair(branch, make_pair(itClassMap->second, array)));
  }

}

//------------------------------------------------------------------------------

void TreeWriter::Finish()
{
}

//------------------------------------------------------------------------------

void TreeWriter::FillParticles(Candidate *candidate, TRefArray *array)
{
  TIter it1(candidate->GetCandidates());
  it1.Reset();
  array->Clear();
  while((candidate = static_cast<Candidate*>(it1.Next())))
  {
    TIter it2(candidate->GetCandidates());

    // particle
    if(candidate->GetCandidates()->GetEntriesFast() == 0)
    {
      array->Add(candidate);
      continue;
    }

    // track
    candidate = static_cast<Candidate*>(candidate->GetCandidates()->At(0));
    if(candidate->GetCandidates()->GetEntriesFast() == 0)
    {
      array->Add(candidate);
      continue;
    }

    // tower
    it2.Reset();
    while((candidate = static_cast<Candidate*>(it2.Next())))
    {
      array->Add(candidate->GetCandidates()->At(0));
    }
  }
}

//------------------------------------------------------------------------------

bool TreeWriter::TreatOneParticle(ExRootTreeBranch *branch, Candidate *candidate)
{
  const Double_t c_light = 2.99792458E8;

  const TLorentzVector &momentum = candidate->Momentum;
  const TLorentzVector &position = candidate->Position;

  GenParticle* entry = static_cast<GenParticle*>(branch->NewEntry());

  entry->SetBit(kIsReferenced);
  entry->SetUniqueID(candidate->GetUniqueID());

  double pt = momentum.Pt();
  double cosTheta = TMath::Abs(momentum.CosTheta());
  double signPz = (momentum.Pz() >= 0.0) ? 1.0 : -1.0;
  double eta = (cosTheta == 1.0 ? signPz*999.9 : momentum.Eta());
  double rapidity = (cosTheta == 1.0 ? signPz*999.9 : momentum.Rapidity());

  entry->PID = candidate->PID;

  entry->Status = candidate->Status;
  entry->IsPU = candidate->IsPU;

  entry->M1 = candidate->M1;
  entry->M2 = candidate->M2;

  entry->D1 = candidate->D1;
  entry->D2 = candidate->D2;

  entry->Charge = candidate->Charge;
  entry->Mass = candidate->Mass;

  // BEGIN MA5
  entry->MA5index = candidate->MA5index;
  // END MA5
  entry->E = momentum.E();
  entry->Px = momentum.Px();
  entry->Py = momentum.Py();
  entry->Pz = momentum.Pz();

  entry->Eta = eta;
  entry->Phi = momentum.Phi();
  entry->PT = pt;

  entry->Rapidity = rapidity;

  entry->X = position.X();
  entry->Y = position.Y();
  entry->Z = position.Z();
  entry->T = position.T()*1.0E-3/c_light;

  return true;
}

void TreeWriter::ProcessParticles(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0;
  GenParticle *entry = 0;
  Double_t pt, signPz, cosTheta, eta, rapidity;

  const Double_t c_light = 2.99792458E8;
  bool debug=false;

  // --------------------- BEGIN MA5 --------------------------

  // saving all particules into a vector
  std::vector<Candidate*> all;
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    all.push_back(candidate);
  }

  // debug mode
  if (debug)
  {
    std::cout << "---------------------------------------------------------------" << std::endl;
  }

  // tagging particles to save
  std::vector<bool> tosave(all.size(),false);
  for (unsigned int i=0;i<all.size();i++)
  {
    Candidate* candidate = all[i];

    // 1. Keep only :
    //     - initial state
    //     - particles generated in hard process
    //     - lepton in the final state
    //     - b and c quarks
    bool hardprocess = (candidate->Status==-1 || candidate->Status==3);
    bool heavyquark  = (std::abs(candidate->PID)==5 || 
                        std::abs(candidate->PID)==4);
    bool lepton_finalstate = ((std::abs(candidate->PID)==11 || 
                               std::abs(candidate->PID)==13) && 
                               candidate->Status==1);
    bool test = hardprocess || heavyquark || lepton_finalstate;
    if (!test) continue;

    // debug mode
    if (debug)
    {
      std::cout << "i=";
      std::cout.width(5);
      std::cout << i;
      std::cout << "\tcandidate=";
      std::cout.width(8);
      std::cout << candidate->PID;
      std::cout << "\tstatus=" << candidate->Status << "\tM1=";
      std::cout.width(5);
      std::cout << candidate->M1;
      std::cout << "\tM2=";
      std::cout.width(5);
      std::cout << candidate->M2 << std::endl;
    }

    tosave[i]=true;

    // Skip 
    if (hardprocess) continue;
    if (!lepton_finalstate && !heavyquark) continue;

    // 2. Save intermediate particles in case of lepton
    std::vector<unsigned int> tosave1;
    std::vector<unsigned int> tosave2;

    // mother 1
    Candidate* intermediate=candidate;
    while(100)
    {
      Int_t M1=intermediate->M1;
      if (M1>=0 && M1<tosave.size())
      {
        tosave1.push_back(M1);
        intermediate=all[M1];
      }
      else break;
    }

    // mother 2
    intermediate=candidate;
    while(100)
    {
      Int_t M2=intermediate->M2;
      if (M2>=0 && M2<tosave.size())
      {
        tosave2.push_back(M2);
        intermediate=all[M2];
      }
      else break;
    }

    // debug mode
    if (debug)
    {
      std::cout << "-> M1 = ";
    }

    // limit
    int limit=30;
    if (lepton_finalstate) limit=3;
    int counter=0;
    for (unsigned int j=0;j<tosave1.size();j++)
    {
      if (j==0)
      {
        tosave[tosave1[j]]=true;
        counter++;
        if (debug)
        {
          std::cout << all[tosave1[j]]->PID << "[" << tosave1[j] << "] <<- ";
        }
      }
      else if (counter <= limit)
      {
        tosave[tosave1[j]]=true;
        if (all[tosave1[j-1]]->PID!=all[tosave1[j]]->PID) counter++;
        if (debug)
        {
          std::cout << all[tosave1[j]]->PID << "[" << tosave1[j] << "] <- ";
        }
      }
      else break;
    }
      
    // debug mode
    if (debug)
    {
      std::cout << "END" << endl;
      std::cout << "-> M2 = ";
    }

    counter=0;
    for (unsigned int j=0;j<tosave2.size();j++)
    {
      if (j==0)
      {
        tosave[tosave2[j]]=true;
        counter++;
        if (debug)
        {
          std::cout << all[tosave2[j]]->PID << "[" << tosave2[j] << "] <<- ";
        }
      }
      else if (counter <= limit)
      {
        tosave[tosave2[j]]=true;
        if (all[tosave2[j-1]]->PID!=all[tosave2[j]]->PID) counter++;
        if (debug)
        {
          std::cout << all[tosave2[j]]->PID << "[" << tosave2[j] << "] <- ";
        }
      }
      else break;
    }

    // debug mode
    if (debug)
    {
      std::cout << "END" << endl;
    }

  }

  // 3. Storing particle
  for (unsigned int i=0;i<all.size();i++)
  {
    Candidate* candidate = all[i];
    if (tosave[i]) TreatOneParticle(branch,candidate);
  }
  // --------------------- END MA5 --------------------------
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessVertices(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0, *constituent = 0;
  Vertex *entry = 0;

  const Double_t c_light = 2.99792458E8;

  Double_t x, y, z, t, xError, yError, zError, tError, sigma, sumPT2, btvSumPT2, genDeltaZ, genSumPT2;
  UInt_t index, ndf;

  CompBase *compare = Candidate::fgCompare;
  Candidate::fgCompare = CompSumPT2<Candidate>::Instance();
  array->Sort();
  Candidate::fgCompare = compare;

  // loop over all vertices
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {

    index = candidate->ClusterIndex;
    ndf = candidate->ClusterNDF;
    sigma = candidate->ClusterSigma;
    sumPT2 = candidate->SumPT2;
    btvSumPT2 = candidate->BTVSumPT2;
    genDeltaZ = candidate->GenDeltaZ;
    genSumPT2 = candidate->GenSumPT2;

    x = candidate->Position.X();
    y = candidate->Position.Y();
    z = candidate->Position.Z();
    t = candidate->Position.T()*1.0E-3/c_light;

    xError = candidate->PositionError.X ();
    yError = candidate->PositionError.Y ();
    zError = candidate->PositionError.Z ();
    tError = candidate->PositionError.T ()*1.0E-3/c_light;

    entry = static_cast<Vertex*>(branch->NewEntry());

    entry->Index = index;
    entry->NDF = ndf;
    entry->Sigma = sigma;
    entry->SumPT2 = sumPT2;
    entry->BTVSumPT2 = btvSumPT2;
    entry->GenDeltaZ = genDeltaZ;
    entry->GenSumPT2 = genSumPT2;

    entry->X = x;
    entry->Y = y;
    entry->Z = z;
    entry->T = t;

    entry->ErrorX = xError;
    entry->ErrorY = yError;
    entry->ErrorZ = zError;
    entry->ErrorT = tError;


    TIter itConstituents(candidate->GetCandidates());
    itConstituents.Reset();
    entry->Constituents.Clear();
    while((constituent = static_cast<Candidate*>(itConstituents.Next())))
    {
      entry->Constituents.Add(constituent);
    }

  }
}


//------------------------------------------------------------------------------

void TreeWriter::ProcessTracks(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0;
  Candidate *particle = 0;
  Track *entry = 0;
  Double_t pt, signz, cosTheta, eta, rapidity, p, ctgTheta, phi;
  const Double_t c_light = 2.99792458E8;

  // loop over all tracks
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    const TLorentzVector &position = candidate->Position;

    cosTheta = TMath::Abs(position.CosTheta());
    signz = (position.Pz() >= 0.0) ? 1.0 : -1.0;
    eta = (cosTheta == 1.0 ? signz*999.9 : position.Eta());
    rapidity = (cosTheta == 1.0 ? signz*999.9 : position.Rapidity());

    entry = static_cast<Track*>(branch->NewEntry());

    entry->SetBit(kIsReferenced);
    entry->SetUniqueID(candidate->GetUniqueID());

    entry->PID = candidate->PID;

// ------- BEGIN MA5 CHANGE -------
    entry->sumPT02  = candidate->sumPT02;
    entry->sumPT03  = candidate->sumPT03;
    entry->sumPT04  = candidate->sumPT04;
    entry->sumPT05  = candidate->sumPT05;
    entry->sumPTeflow02  = candidate->eflow_sumPT02;
    entry->sumPTeflow03  = candidate->eflow_sumPT03;
    entry->sumPTeflow04  = candidate->eflow_sumPT04;
    entry->sumPTeflow05  = candidate->eflow_sumPT05;
    entry->sumET02  = candidate->sumET02;
    entry->sumET03  = candidate->sumET03;
    entry->sumET04  = candidate->sumET04;
    entry->sumET05  = candidate->sumET05;
    entry->nTrack02 = candidate->nTrack02;
    entry->nTrack03 = candidate->nTrack03;
    entry->nTrack04 = candidate->nTrack04;
    entry->nTrack05 = candidate->nTrack05;
// ------- END MA5 CHANGE -------


    entry->Charge = candidate->Charge;

    entry->EtaOuter = eta;
    entry->PhiOuter = position.Phi();

    entry->XOuter = position.X();
    entry->YOuter = position.Y();
    entry->ZOuter = position.Z();
    entry->TOuter = position.T()*1.0E-3/c_light;

    entry->L = candidate->L;

    entry->D0            = candidate->D0;
    entry->ErrorD0       = candidate->ErrorD0;
    entry->DZ            = candidate->DZ;
    entry->ErrorDZ       = candidate->ErrorDZ;

    entry->ErrorP        = candidate->ErrorP;
    entry->ErrorPT       = candidate->ErrorPT;
    entry->ErrorCtgTheta = candidate->ErrorCtgTheta;
    entry->ErrorPhi      = candidate->ErrorPhi;

    entry->Xd = candidate->Xd;
    entry->Yd = candidate->Yd;
    entry->Zd = candidate->Zd;

    const TLorentzVector &momentum = candidate->Momentum;

    pt = momentum.Pt();
    p = momentum.P();
    phi = momentum.Phi();
    ctgTheta = (TMath::Tan(momentum.Theta()) != 0) ? 1/TMath::Tan(momentum.Theta()) : 1e10;

    cosTheta = TMath::Abs(momentum.CosTheta());
    signz = (momentum.Pz() >= 0.0) ? 1.0 : -1.0;
    eta = (cosTheta == 1.0 ? signz*999.9 : momentum.Eta());
    rapidity = (cosTheta == 1.0 ? signz*999.9 : momentum.Rapidity());

    entry->PT  = pt;
    entry->Eta = eta;
    entry->Phi = phi;
    entry->CtgTheta = ctgTheta;

    particle = static_cast<Candidate*>(candidate->GetCandidates()->At(0));
    const TLorentzVector &initialPosition = particle->Position;

    entry->X = initialPosition.X();
    entry->Y = initialPosition.Y();
    entry->Z = initialPosition.Z();
    entry->T = initialPosition.T()*1.0E-3/c_light;

    entry->Particle = particle;

    entry->VertexIndex = candidate->ClusterIndex;

  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessTowers(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0;
  Tower *entry = 0;
  Double_t pt, signPz, cosTheta, eta, rapidity;
  const Double_t c_light = 2.99792458E8;

  // loop over all towers
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    const TLorentzVector &momentum = candidate->Momentum;
    const TLorentzVector &position = candidate->Position;

    pt = momentum.Pt();
    cosTheta = TMath::Abs(momentum.CosTheta());
    signPz = (momentum.Pz() >= 0.0) ? 1.0 : -1.0;
    eta = (cosTheta == 1.0 ? signPz*999.9 : momentum.Eta());
    rapidity = (cosTheta == 1.0 ? signPz*999.9 : momentum.Rapidity());

    entry = static_cast<Tower*>(branch->NewEntry());

    entry->SetBit(kIsReferenced);
    entry->SetUniqueID(candidate->GetUniqueID());

    entry->Eta = eta;
    entry->Phi = momentum.Phi();
    entry->ET = pt;
    entry->E = momentum.E();
    entry->Eem = candidate->Eem;
    entry->Ehad = candidate->Ehad;
    entry->Edges[0] = candidate->Edges[0];
    entry->Edges[1] = candidate->Edges[1];
    entry->Edges[2] = candidate->Edges[2];
    entry->Edges[3] = candidate->Edges[3];

    entry->T = position.T()*1.0E-3/c_light;
    entry->NTimeHits = candidate->NTimeHits;

    FillParticles(candidate, &entry->Particles);
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessPhotons(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0;
  Photon *entry = 0;
  Double_t pt, signPz, cosTheta, eta, rapidity;
  const Double_t c_light = 2.99792458E8;

  array->Sort();

  // loop over all photons
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    TIter it1(candidate->GetCandidates());
    const TLorentzVector &momentum = candidate->Momentum;
    const TLorentzVector &position = candidate->Position;


    pt = momentum.Pt();
    cosTheta = TMath::Abs(momentum.CosTheta());
    signPz = (momentum.Pz() >= 0.0) ? 1.0 : -1.0;
    eta = (cosTheta == 1.0 ? signPz*999.9 : momentum.Eta());
    rapidity = (cosTheta == 1.0 ? signPz*999.9 : momentum.Rapidity());

    entry = static_cast<Photon*>(branch->NewEntry());

    entry->Eta = eta;
    entry->Phi = momentum.Phi();
    entry->PT = pt;
    entry->E = momentum.E();

    entry->T = position.T()*1.0E-3/c_light;

    // Isolation variables

    entry->IsolationVar = candidate->IsolationVar;
    entry->IsolationVarRhoCorr = candidate->IsolationVarRhoCorr ;
    entry->SumPtCharged = candidate->SumPtCharged ;
    entry->SumPtNeutral = candidate->SumPtNeutral ;
    entry->SumPtChargedPU = candidate->SumPtChargedPU ;
    entry->SumPt = candidate->SumPt ;

    entry->EhadOverEem = candidate->Eem > 0.0 ? candidate->Ehad/candidate->Eem : 999.9;

   // ------- BEGIN MA5 CHANGE -------
    entry->sumPT02 = candidate->sumPT02;
    entry->sumPT03 = candidate->sumPT03;
    entry->sumPT04 = candidate->sumPT04;
    entry->sumPT05 = candidate->sumPT05;
    entry->sumPTeflow02  = candidate->eflow_sumPT02;
    entry->sumPTeflow03  = candidate->eflow_sumPT03;
    entry->sumPTeflow04  = candidate->eflow_sumPT04;
    entry->sumPTeflow05  = candidate->eflow_sumPT05;
    entry->sumET02  = candidate->sumET02;
    entry->sumET03  = candidate->sumET03;
    entry->sumET04  = candidate->sumET04;
    entry->sumET05  = candidate->sumET05;
    entry->nTrack02 = candidate->nTrack02;
    entry->nTrack03 = candidate->nTrack03;
    entry->nTrack04 = candidate->nTrack04;
    entry->nTrack05 = candidate->nTrack05;
// ------- END MA5 CHANGE -------

    FillParticles(candidate, &entry->Particles);
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessElectrons(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0;
  Electron *entry = 0;
  Double_t pt, signPz, cosTheta, eta, rapidity;
  const Double_t c_light = 2.99792458E8;

  array->Sort();

  // loop over all electrons
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    const TLorentzVector &momentum = candidate->Momentum;
    const TLorentzVector &position = candidate->Position;

    pt = momentum.Pt();
    cosTheta = TMath::Abs(momentum.CosTheta());
    signPz = (momentum.Pz() >= 0.0) ? 1.0 : -1.0;
    eta = (cosTheta == 1.0 ? signPz*999.9 : momentum.Eta());
    rapidity = (cosTheta == 1.0 ? signPz*999.9 : momentum.Rapidity());

    entry = static_cast<Electron*>(branch->NewEntry());

    entry->Eta = eta;
    entry->Phi = momentum.Phi();
    entry->PT = pt;

    entry->T = position.T()*1.0E-3/c_light;

    // Isolation variables

    entry->IsolationVar = candidate->IsolationVar;
    entry->IsolationVarRhoCorr = candidate->IsolationVarRhoCorr ;
    entry->SumPtCharged = candidate->SumPtCharged ;
    entry->SumPtNeutral = candidate->SumPtNeutral ;
    entry->SumPtChargedPU = candidate->SumPtChargedPU ;
    entry->SumPt = candidate->SumPt ;


    entry->Charge = candidate->Charge;
// ------- BEGIN MA5 CHANGE -------
    entry->MA5index = candidate->MA5index;
    entry->sumPT02 = candidate->sumPT02;
    entry->sumPT03 = candidate->sumPT03;
    entry->sumPT04 = candidate->sumPT04;
    entry->sumPT05 = candidate->sumPT05;
    entry->sumPTeflow02  = candidate->eflow_sumPT02;
    entry->sumPTeflow03  = candidate->eflow_sumPT03;
    entry->sumPTeflow04  = candidate->eflow_sumPT04;
    entry->sumPTeflow05  = candidate->eflow_sumPT05;
    entry->sumET02  = candidate->sumET02;
    entry->sumET03  = candidate->sumET03;
    entry->sumET04  = candidate->sumET04;
    entry->sumET05  = candidate->sumET05;
    entry->nTrack02 = candidate->nTrack02;
    entry->nTrack03 = candidate->nTrack03;
    entry->nTrack04 = candidate->nTrack04;
    entry->nTrack05 = candidate->nTrack05;
// ------- END MA5 CHANGE -------

    entry->EhadOverEem = 0.0;

    entry->Particle = candidate->GetCandidates()->At(0);
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessMuons(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0;
  Muon *entry = 0;
  Double_t pt, signPz, cosTheta, eta, rapidity;

  const Double_t c_light = 2.99792458E8;

  array->Sort();

  // loop over all muons
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    const TLorentzVector &momentum = candidate->Momentum;
    const TLorentzVector &position = candidate->Position;

    pt = momentum.Pt();
    cosTheta = TMath::Abs(momentum.CosTheta());
    signPz = (momentum.Pz() >= 0.0) ? 1.0 : -1.0;
    eta = (cosTheta == 1.0 ? signPz*999.9 : momentum.Eta());
    rapidity = (cosTheta == 1.0 ? signPz*999.9 : momentum.Rapidity());

    entry = static_cast<Muon*>(branch->NewEntry());

    entry->SetBit(kIsReferenced);
    entry->SetUniqueID(candidate->GetUniqueID());

    entry->Eta = eta;
    entry->Phi = momentum.Phi();
    entry->PT = pt;

    entry->T = position.T()*1.0E-3/c_light;

    // Isolation variables

    entry->IsolationVar = candidate->IsolationVar;
    entry->IsolationVarRhoCorr = candidate->IsolationVarRhoCorr ;
    entry->SumPtCharged = candidate->SumPtCharged ;
    entry->SumPtNeutral = candidate->SumPtNeutral ;
    entry->SumPtChargedPU = candidate->SumPtChargedPU ;
    entry->SumPt = candidate->SumPt ;

    entry->Charge = candidate->Charge;
// ------- BEGIN MA5 CHANGE -------
    entry->MA5index = candidate->MA5index;
    entry->sumPT02 = candidate->sumPT02;
    entry->sumPT03 = candidate->sumPT03;
    entry->sumPT04 = candidate->sumPT04;
    entry->sumPT05 = candidate->sumPT05;
    entry->sumPTeflow02  = candidate->eflow_sumPT02;
    entry->sumPTeflow03  = candidate->eflow_sumPT03;
    entry->sumPTeflow04  = candidate->eflow_sumPT04;
    entry->sumPTeflow05  = candidate->eflow_sumPT05;
    entry->sumET02  = candidate->sumET02;
    entry->sumET03  = candidate->sumET03;
    entry->sumET04  = candidate->sumET04;
    entry->sumET05  = candidate->sumET05;
    entry->nTrack02 = candidate->nTrack02;
    entry->nTrack03 = candidate->nTrack03;
    entry->nTrack04 = candidate->nTrack04;
    entry->nTrack05 = candidate->nTrack05;
// ------- END MA5 CHANGE -------

    entry->Particle = candidate->GetCandidates()->At(0);
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessJets(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0, *constituent = 0;
  Jet *entry = 0;
  Double_t pt, signPz, cosTheta, eta, rapidity;
  Double_t ecalEnergy, hcalEnergy;
  const Double_t c_light = 2.99792458E8;
  Int_t i;

  array->Sort();

  // loop over all jets
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    TIter itConstituents(candidate->GetCandidates());

    const TLorentzVector &momentum = candidate->Momentum;
    const TLorentzVector &position = candidate->Position;

    pt = momentum.Pt();
    cosTheta = TMath::Abs(momentum.CosTheta());
    signPz = (momentum.Pz() >= 0.0) ? 1.0 : -1.0;
    eta = (cosTheta == 1.0 ? signPz*999.9 : momentum.Eta());
    rapidity = (cosTheta == 1.0 ? signPz*999.9 : momentum.Rapidity());

    entry = static_cast<Jet*>(branch->NewEntry());

    entry->Eta = eta;
    entry->Phi = momentum.Phi();
    entry->PT = pt;

    entry->T = position.T()*1.0E-3/c_light;

    entry->Mass = momentum.M();

    entry->Area = candidate->Area;

    entry->DeltaEta = candidate->DeltaEta;
    entry->DeltaPhi = candidate->DeltaPhi;

    entry->Flavor = candidate->Flavor;
    entry->FlavorAlgo = candidate->FlavorAlgo;
    entry->FlavorPhys = candidate->FlavorPhys;

    entry->BTag = candidate->BTag;

    entry->BTagAlgo = candidate->BTagAlgo;
    entry->BTagPhys = candidate->BTagPhys;

    entry->TauTag = candidate->TauTag;

    entry->Charge = candidate->Charge;

    itConstituents.Reset();
    entry->Constituents.Clear();
    ecalEnergy = 0.0;
    hcalEnergy = 0.0;
    while((constituent = static_cast<Candidate*>(itConstituents.Next())))
    {
      entry->Constituents.Add(constituent);
      ecalEnergy += constituent->Eem;
      hcalEnergy += constituent->Ehad;
    }

    entry->EhadOverEem = ecalEnergy > 0.0 ? hcalEnergy/ecalEnergy : 999.9;

    //---   Pile-Up Jet ID variables ----

    entry->NCharged = candidate->NCharged;
    entry->NNeutrals = candidate->NNeutrals;
    entry->Beta = candidate->Beta;
    entry->BetaStar = candidate->BetaStar;
    entry->MeanSqDeltaR = candidate->MeanSqDeltaR;
    entry->PTD = candidate->PTD;

    //--- Sub-structure variables ----

    entry->NSubJetsTrimmed = candidate->NSubJetsTrimmed;
    entry->NSubJetsPruned = candidate->NSubJetsPruned;
    entry->NSubJetsSoftDropped = candidate->NSubJetsSoftDropped;

    for(i = 0; i < 5; i++)
    {
      entry->FracPt[i] = candidate -> FracPt[i];
      entry->Tau[i] = candidate -> Tau[i];
      entry->TrimmedP4[i] = candidate -> TrimmedP4[i];
      entry->PrunedP4[i] = candidate -> PrunedP4[i];
      entry->SoftDroppedP4[i] = candidate -> SoftDroppedP4[i];
    }

    FillParticles(candidate, &entry->Particles);
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessMissingET(ExRootTreeBranch *branch, TObjArray *array)
{
  Candidate *candidate = 0;
  MissingET *entry = 0;

  // get the first entry
  if((candidate = static_cast<Candidate*>(array->At(0))))
  {
    const TLorentzVector &momentum = candidate->Momentum;

    entry = static_cast<MissingET*>(branch->NewEntry());

    entry->Eta = (-momentum).Eta();
    entry->Phi = (-momentum).Phi();
    entry->MET = momentum.Pt();
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessScalarHT(ExRootTreeBranch *branch, TObjArray *array)
{
  Candidate *candidate = 0;
  ScalarHT *entry = 0;

  // get the first entry
  if((candidate = static_cast<Candidate*>(array->At(0))))
  {
    const TLorentzVector &momentum = candidate->Momentum;

    entry = static_cast<ScalarHT*>(branch->NewEntry());

    entry->HT = momentum.Pt();
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessRho(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0;
  Rho *entry = 0;

  // loop over all rho
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    const TLorentzVector &momentum = candidate->Momentum;

    entry = static_cast<Rho*>(branch->NewEntry());

    entry->Rho = momentum.E();
    entry->Edges[0] = candidate->Edges[0];
    entry->Edges[1] = candidate->Edges[1];
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessWeight(ExRootTreeBranch *branch, TObjArray *array)
{
  Candidate *candidate = 0;
  Weight *entry = 0;

  // get the first entry
  if((candidate = static_cast<Candidate*>(array->At(0))))
  {
    const TLorentzVector &momentum = candidate->Momentum;

    entry = static_cast<Weight*>(branch->NewEntry());

    entry->Weight = momentum.E();
  }
}

//------------------------------------------------------------------------------

void TreeWriter::ProcessHectorHit(ExRootTreeBranch *branch, TObjArray *array)
{
  TIter iterator(array);
  Candidate *candidate = 0;
  HectorHit *entry = 0;

  // loop over all roman pot hits
  iterator.Reset();
  while((candidate = static_cast<Candidate*>(iterator.Next())))
  {
    const TLorentzVector &position = candidate->Position;
    const TLorentzVector &momentum = candidate->Momentum;

    entry = static_cast<HectorHit*>(branch->NewEntry());

    entry->E = momentum.E();

    entry->Tx = momentum.Px();
    entry->Ty = momentum.Py();

    entry->T = position.T();

    entry->X = position.X();
    entry->Y = position.Y();
    entry->S = position.Z();

    entry->Particle = candidate->GetCandidates()->At(0);
  }
}

//------------------------------------------------------------------------------

void TreeWriter::Process()
{
  TBranchMap::iterator itBranchMap;
  ExRootTreeBranch *branch;
  TProcessMethod method;
  TObjArray *array;

  for(itBranchMap = fBranchMap.begin(); itBranchMap != fBranchMap.end(); ++itBranchMap)
  {
    branch = itBranchMap->first;
    method = itBranchMap->second.first;
    array = itBranchMap->second.second;

    (this->*method)(branch, array);
  }
}

//------------------------------------------------------------------------------
