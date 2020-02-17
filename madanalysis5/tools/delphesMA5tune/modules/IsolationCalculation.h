// ------- BEGIN MA5 CHANGE -------
#ifndef IsolationCalculation_h
#define IsolationCalculation_h

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

#include "classes/DelphesModule.h"

class TObjArray;

class ExRootFilter;
class IsolationCalculationClassifier;

class IsolationCalculation: public DelphesModule
{
public:

  IsolationCalculation();
  ~IsolationCalculation();

  void Init();
  void Process();
  void Finish();

private:

  IsolationCalculationClassifier *fClassifier; //!

  TObjArray *fOutputArray; //!

  TIterator *fItTrackInputArray; //!
  TIterator *fItCaloTowerInputArray; //!
  TIterator *fIt_eflow_InputArray; //!
  TIterator *fItCandidateInputArray; //!

  const TObjArray *fTrackInputArray; //!
  const TObjArray *fCaloTowerInputArray; //!
  const TObjArray *f_eflow_InputArray; //!
  const TObjArray *fCandidateInputArray; //!

  // pileup
  const TObjArray *fRhoInputArray; //!

  ClassDef(IsolationCalculation, 1)
};

#endif
// ------- END MA5 CHANGE -------
