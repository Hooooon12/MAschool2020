void selection_0()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo1","canvas_plotflow_tempo1",0,0,700,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S1_PT_0 = new TH1F("S1_PT_0","S1_PT_0",100,0.0,1000.0);
  // Content
  S1_PT_0->SetBinContent(0,0.0); // underflow
  S1_PT_0->SetBinContent(1,1074.5478435);
  S1_PT_0->SetBinContent(2,5723.40131404);
  S1_PT_0->SetBinContent(3,8359.87193154);
  S1_PT_0->SetBinContent(4,7772.69997432);
  S1_PT_0->SetBinContent(5,7078.20962284);
  S1_PT_0->SetBinContent(6,5230.55867305);
  S1_PT_0->SetBinContent(7,3030.19770436);
  S1_PT_0->SetBinContent(8,2983.71547463);
  S1_PT_0->SetBinContent(9,1513.39039177);
  S1_PT_0->SetBinContent(10,1760.15292646);
  S1_PT_0->SetBinContent(11,1172.2963107);
  S1_PT_0->SetBinContent(12,928.267312667);
  S1_PT_0->SetBinContent(13,342.460849399);
  S1_PT_0->SetBinContent(14,292.561507693);
  S1_PT_0->SetBinContent(15,97.0648918819);
  S1_PT_0->SetBinContent(16,97.7483079053);
  S1_PT_0->SetBinContent(17,244.029061752);
  S1_PT_0->SetBinContent(18,49.2158619644);
  S1_PT_0->SetBinContent(19,97.7483079053);
  S1_PT_0->SetBinContent(20,97.7483079053);
  S1_PT_0->SetBinContent(21,0.0);
  S1_PT_0->SetBinContent(22,98.4317239288);
  S1_PT_0->SetBinContent(23,49.2158619644);
  S1_PT_0->SetBinContent(24,0.0);
  S1_PT_0->SetBinContent(25,0.0);
  S1_PT_0->SetBinContent(26,0.0);
  S1_PT_0->SetBinContent(27,48.5324459409);
  S1_PT_0->SetBinContent(28,0.0);
  S1_PT_0->SetBinContent(29,0.0);
  S1_PT_0->SetBinContent(30,97.0648918819);
  S1_PT_0->SetBinContent(31,0.0);
  S1_PT_0->SetBinContent(32,0.0);
  S1_PT_0->SetBinContent(33,0.0);
  S1_PT_0->SetBinContent(34,0.0);
  S1_PT_0->SetBinContent(35,0.0);
  S1_PT_0->SetBinContent(36,0.0);
  S1_PT_0->SetBinContent(37,0.0);
  S1_PT_0->SetBinContent(38,0.0);
  S1_PT_0->SetBinContent(39,0.0);
  S1_PT_0->SetBinContent(40,0.0);
  S1_PT_0->SetBinContent(41,0.0);
  S1_PT_0->SetBinContent(42,0.0);
  S1_PT_0->SetBinContent(43,0.0);
  S1_PT_0->SetBinContent(44,0.0);
  S1_PT_0->SetBinContent(45,0.0);
  S1_PT_0->SetBinContent(46,0.0);
  S1_PT_0->SetBinContent(47,0.0);
  S1_PT_0->SetBinContent(48,0.0);
  S1_PT_0->SetBinContent(49,0.0);
  S1_PT_0->SetBinContent(50,0.0);
  S1_PT_0->SetBinContent(51,0.0);
  S1_PT_0->SetBinContent(52,0.0);
  S1_PT_0->SetBinContent(53,0.0);
  S1_PT_0->SetBinContent(54,0.0);
  S1_PT_0->SetBinContent(55,0.0);
  S1_PT_0->SetBinContent(56,0.0);
  S1_PT_0->SetBinContent(57,0.0);
  S1_PT_0->SetBinContent(58,0.0);
  S1_PT_0->SetBinContent(59,0.0);
  S1_PT_0->SetBinContent(60,0.0);
  S1_PT_0->SetBinContent(61,0.0);
  S1_PT_0->SetBinContent(62,0.0);
  S1_PT_0->SetBinContent(63,0.0);
  S1_PT_0->SetBinContent(64,0.0);
  S1_PT_0->SetBinContent(65,0.0);
  S1_PT_0->SetBinContent(66,0.0);
  S1_PT_0->SetBinContent(67,0.0);
  S1_PT_0->SetBinContent(68,0.0);
  S1_PT_0->SetBinContent(69,0.0);
  S1_PT_0->SetBinContent(70,0.0);
  S1_PT_0->SetBinContent(71,0.0);
  S1_PT_0->SetBinContent(72,0.0);
  S1_PT_0->SetBinContent(73,0.0);
  S1_PT_0->SetBinContent(74,0.0);
  S1_PT_0->SetBinContent(75,0.0);
  S1_PT_0->SetBinContent(76,0.0);
  S1_PT_0->SetBinContent(77,0.0);
  S1_PT_0->SetBinContent(78,0.0);
  S1_PT_0->SetBinContent(79,0.0);
  S1_PT_0->SetBinContent(80,0.0);
  S1_PT_0->SetBinContent(81,0.0);
  S1_PT_0->SetBinContent(82,0.0);
  S1_PT_0->SetBinContent(83,0.0);
  S1_PT_0->SetBinContent(84,0.0);
  S1_PT_0->SetBinContent(85,0.0);
  S1_PT_0->SetBinContent(86,0.0);
  S1_PT_0->SetBinContent(87,0.0);
  S1_PT_0->SetBinContent(88,0.0);
  S1_PT_0->SetBinContent(89,0.0);
  S1_PT_0->SetBinContent(90,0.0);
  S1_PT_0->SetBinContent(91,0.0);
  S1_PT_0->SetBinContent(92,0.0);
  S1_PT_0->SetBinContent(93,0.0);
  S1_PT_0->SetBinContent(94,0.0);
  S1_PT_0->SetBinContent(95,0.0);
  S1_PT_0->SetBinContent(96,0.0);
  S1_PT_0->SetBinContent(97,0.0);
  S1_PT_0->SetBinContent(98,0.0);
  S1_PT_0->SetBinContent(99,0.0);
  S1_PT_0->SetBinContent(100,0.0);
  S1_PT_0->SetBinContent(101,0.0); // overflow
  S1_PT_0->SetEntries(987);
  // Style
  S1_PT_0->SetLineColor(9);
  S1_PT_0->SetLineStyle(1);
  S1_PT_0->SetLineWidth(1);
  S1_PT_0->SetFillColor(9);
  S1_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_2","mystack");
  stack->Add(S1_PT_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("N. of mu ( L_{int} = 10 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("p_{T} [ mu ] (GeV/c) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_0.eps");

}
