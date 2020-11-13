void acceptance_cal() {
	double frac_sr1 = 0.2654; // mass range 50 ~ 600
	double frac_sr2 = 0.1477; // mass range 100 ~1200
	double frac_sr3 = 0.213; // mass range 500 ~ 1600
	double frac_sr4 = 0.099; // mass range 1000 ~ 2500

	int n_sr1 = 168;
	int n_sr2 = 9289;
	int n_sr3 = 90554;
	int n_sr4 = 357303;

	double acc1 = n_sr1*frac_sr1/200000;
	double acc2 = n_sr2*frac_sr2/200000;
	double acc3 = n_sr3*frac_sr3/200000;
	double acc4 = n_sr4*frac_sr4/200000;

	cout << "acc1 = " << acc1 << endl;
	cout << "acc2 = " << acc2 << endl;
	cout << "acc3 = " << acc3 << endl;
	cout << "acc4 = " << acc4 << endl;
}

