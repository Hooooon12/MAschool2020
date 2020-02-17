// STL headers
#include <iostream>

// ROOT headers
#include <TAxis.h>
#include <TH1F.h>
#include <TLegend.h>
#include <TCanvas.h>
#include <TFile.h>
#include <THStack.h>
#include <TStyle.h>
#include <TSystem.h>
#include <TROOT.h>

// Including histograms
#include "selection_0.C"
#include "selection_1.C"

// Main program
int main()
{
  std::cout << "BEGIN-STAMP" << std::endl;
  selection_0();
  selection_1();
  std::cout << "END-STAMP" << std::endl;
  return 0;
}
