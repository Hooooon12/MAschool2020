from ROOT import *
import sys, os
import numpy as np

def drawMassHist(fIn, i, d) :
  t = fIn.Get('SR_%d'%i)
  l = []
  for evt in t :
    for mass in evt.tripletM :
      l.append(mass)
  h = TH1D('', 'triplet mass in signal region %d'%i, 100, 0, max(l)*1.1)
  for mass in l : h.Fill(mass)
  c = TCanvas()
  h.Draw()
  c.SaveAs('%s/tripletMass_%d.png'%(d,i))

def drawDiff(fIn, prefix, i, d) :
  bH = fIn.Get('%s_before_%d'%(prefix, i))
  aH = fIn.Get('%s_after_%d'%(prefix, i))
  bH.SetLineColor(kBlue)
  aH.SetLineColor(kRed)
  bH.SetStats(0)
  aH.SetStats(0)
  c = TCanvas()
  c.SetLogy()
  bH.SetTitle('%s'%prefix)
  bH.Draw()
  aH.Draw('same')
  c.SaveAs('%s/%s_cut_%d.png'%(d, prefix, i))


if __name__ == '__main__' :
  import argparse
  parse = argparse.ArgumentParser()
  parse.add_argument('--fIn', '-f', default='test.root', help='input root file')
  parse.add_argument('--sr', '-s', type=int, default=2, help='signal region to draw')
  parse.add_argument('--plotdir', '-p', default='plots', help='directory for plotting output')
  args = parse.parse_args()
  fIn = TFile.Open(args.fIn, 'read')
  os.system('mkdir -p %s'%args.plotdir)
  drawMassHist(fIn, args.sr, args.plotdir)
  prefixes = ['Am', 'Delta', 'MDS32', 'MDS6332']
  for prefix in prefixes :
    drawDiff(fIn, prefix, args.sr, args.plotdir)
