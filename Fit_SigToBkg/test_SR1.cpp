void test_SR1() {
	using namespace RooFit;
	TFile* f = new TFile("tripletM.root");

	bool trigSig = false;
	bool trigBkg = false;
	bool trigTotal = true;

	TString br;
	if (trigSig) br = "gen_tripletM_sr1";
	else br = "tripletM_sr1";

	TTree* tr = (TTree*)f->Get(br);
	RooRealVar x(br, "x", 50, 600);

	//==== import data
	RooDataSet data("data", "data", RooArgSet(x), Import(*tr));
	RooDataHist* dhist = data.binnedClone();

	//==== Signal function
	//==== define variables
    //==== name of observable should be the same with the branch name
    //==== for signal, use double gaussian model
	double m1 = 209.1, m1err = 10.77;
	double s1 = 19.9, s1err = 2.37;
	double m2 = 195.0, m2err = 13.84;
	double s2 = 55.9, s2err = 20.02;
    RooRealVar mean1("mean1", "mean1", m1, m1-2*m1err, m1+2*m1err);
    RooRealVar mean2("mean2", "mean2", m2, m2-2*m2err, m2+2*m2err);
    RooRealVar sigma1("sigma1", "sigam1", s1, s1-2*s1err, s1+2*s1err);
    RooRealVar sigma2("sigma2", "sigma2", s2, s2-2*s2err, s2+2*s2err);
	
	//RooRealVar mean1("mean1", "mean1", 200, 195, 210);
	//RooRealVar mean2("mean2", "mean2", 190, 180, 195);
	//RooRealVar sigma1("sigma1", "sigma1", 0, 100);
	//RooRealVar sigma2("sigma2", "sigma2", 0, 100);

	RooGaussian sig1("sig1", "sig1", x, mean1, sigma1);
    RooGaussian sig2("sig2", "sig2", x, mean2, sigma2);

    RooRealVar sig1_frac("sig1_frac", "sig1_frac", 0.5, 0., 1.);
    RooAddPdf sig("sig", "sig", RooArgList(sig1, sig2), sig1_frac);

	//==== Backgournd function
	RooRealVar a("a", "a", 10e22, 10e28);
	RooRealVar b("b", "b", 500, 700);
	RooRealVar c("c", "c", -200, 200);
	RooRealVar d("d", "d", 10e-2, 0., 1.0);
	//RooRealVar d("d", "d", 0);
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
		model.fitTo(*dhist);

		RooPlot* total_frame = x.frame();
		data.plotOn(total_frame);
		model.plotOn(total_frame, Components(bkg), LineStyle(kDashed));
		model.plotOn(total_frame);

		total_frame->Draw();
	}
}


