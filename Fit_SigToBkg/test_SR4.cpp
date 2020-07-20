void test_SR4() {
	using namespace RooFit;
	TFile* f = new TFile("tripletM.root");

	bool trigSig = false;
	bool trigBkg = false;
	bool trigTotal = true;

	TString br;
	if (trigSig) br = "gen_tripletM_sr4";
	else br = "tripletM_sr4";

	TTree* tr = (TTree*)f->Get(br);
	RooRealVar x(br, "x", 1000, 2500);

	//==== import data
	RooDataSet data("data", "data", RooArgSet(x), Import(*tr));
	RooDataHist* dhist = data.binnedClone();

	//==== Signal function
	//==== define variables
    //==== name of observable should be the same with the branch name
    //==== for signal, use double gaussian model
	double m1 = 1498., m1err = 1.2;
	double m2 = 1444., m2err = 6.5;
	double s1 = 120.5, s1err = 1.25;
	double s2 = 362.0, s2err = 3.098;
    RooRealVar mean1("mean1", "mean1", m1, m1-2*m1err, m1+2*m2err);
    RooRealVar mean2("mean2", "mean2", m2, m2-2*m2err, m2+2*m2err);
    RooRealVar sigma1("sigma1", "sigam1", s1, s1-2*s1err, s1+2*s1err);
    RooRealVar sigma2("sigma2", "sigma2", s2, s2-2*s2err, s2+2*s2err);

	RooGaussian sig1("sig1", "sig1", x, mean1, sigma1);
    RooGaussian sig2("sig2", "sig2", x, mean2, sigma2);

	double s1_frac = 0.749, s1_frac_err = 0.00696;
    RooRealVar sig1_frac("sig1_frac", "sig1_frac", s1_frac, s1_frac-2*s1_frac_err, s1_frac+2*s1_frac_err);
    RooAddPdf sig("sig", "sig", RooArgList(sig1, sig2), sig1_frac);

	//==== Backgournd function
	RooRealVar a("a", "a", 10e24, 10e28);
	RooRealVar b("b", "b", 15500, 17500);
	RooRealVar c("c", "c", -400, 400);
	RooRealVar d("d", "d", 1.4, 2.2);
    RooGenericPdf bkg("bkg", "bkg", "(a / x^(5+d*TMath::Log((x+c)/13000)))*(1 / (TMath::Exp(b / (x+c))-1))", RooArgSet(x, a, b, c, d));

	//==== sig+bkg model
	RooRealVar bkg_frac("bkg_frac", "bkg_frac", 0.8, 0., 1.);
	RooAddPdf model("model", "sig+bkg", RooArgList(bkg, sig), bkg_frac);

	//==== proceed fitting and draw
	if (trigSig) {
		sig.fitTo(data);

		RooPlot* sig_frame = x.frame();
		data.plotOn(sig_frame);
		sig.plotOn(sig_frame);

		sig_frame->Draw();
	}

	if (trigBkg) {
		bkg.fitTo(data);

		RooPlot* bkg_frame = x.frame();
		data.plotOn(bkg_frame);
		bkg.plotOn(bkg_frame);
		
		bkg_frame->Draw();
	}

	if (trigTotal) {
		model.chi2FitTo(*dhist);

		RooPlot* total_frame = x.frame();
		data.plotOn(total_frame);
		model.plotOn(total_frame, Components(bkg), LineStyle(kDashed));
		model.plotOn(total_frame);

		total_frame->Draw();
	}
}


