void type_converter() {
	//==== Macro to convert the data type of TTree
	//==== from vector 
	//==== since vector cannot be read in RooFit framework
	
	//==== Load files to convert ====
	TFile* f_sr1 = new TFile("$PWD/BaseFiles/test_SR1_go200.root");
	TFile* f_sr2 = new TFile("$PWD/BaseFiles/test_SR2_go500.root");
	TFile* f_sr3 = new TFile("$PWD/BaseFiles/test_SR3_go900.root");
	TFile* f_sr4 = new TFile("$PWD/BaseFiles/test_SR4_go1600.root");

	TTree* t_sr1 = (TTree*)f_sr1->Get("SR_1");
	TTree* t_sr2 = (TTree*)f_sr2->Get("SR_2");
	TTree* t_sr3 = (TTree*)f_sr3->Get("SR_3");
	TTree* t_sr4 = (TTree*)f_sr4->Get("SR_4");

	vector<double>* p_mass1=0;
    vector<double>* p_mass2=0;
    vector<double>* p_mass3=0;
    vector<double>* p_mass4=0;
    vector<double>* p_gen_mass1=0;
    vector<double>* p_gen_mass2=0;
    vector<double>* p_gen_mass3=0;
    vector<double>* p_gen_mass4=0;
    t_sr1->SetBranchAddress("tripletM", &p_mass1);
    t_sr2->SetBranchAddress("tripletM", &p_mass2);
    t_sr3->SetBranchAddress("tripletM", &p_mass3);
    t_sr4->SetBranchAddress("tripletM", &p_mass4);
    t_sr1->SetBranchAddress("gen_tripletM", &p_gen_mass1);
    t_sr2->SetBranchAddress("gen_tripletM", &p_gen_mass2);
    t_sr3->SetBranchAddress("gen_tripletM", &p_gen_mass3);
    t_sr4->SetBranchAddress("gen_tripletM", &p_gen_mass4);

	//==== files & trees to store data ====
	TFile* f_out = new TFile("tripletM.root", "recreate");
	double m1, m2, m3, m4;
	double gen_m1, gen_m2, gen_m3, gen_m4;
	TTree* t_mass_sr1 = new TTree("tripletM_sr1", "");
	TTree* t_mass_sr2 = new TTree("tripletM_sr2", "");
	TTree* t_mass_sr3 = new TTree("tripletM_sr3", "");
	TTree* t_mass_sr4 = new TTree("tripletM_sr4", "");
	TTree* t_gen_mass_sr1 = new TTree("gen_tripletM_sr1", "");
	TTree* t_gen_mass_sr2 = new TTree("gen_tripletM_sr2", "");
	TTree* t_gen_mass_sr3 = new TTree("gen_tripletM_sr3", "");
	TTree* t_gen_mass_sr4 = new TTree("gen_tripletM_sr4", "");

	t_mass_sr1->Branch("tripletM_sr1", &m1);
	t_mass_sr2->Branch("tripletM_sr2", &m2);
	t_mass_sr3->Branch("tripletM_sr3", &m3);
	t_mass_sr4->Branch("tripletM_sr4", &m4);
	t_gen_mass_sr1->Branch("gen_tripletM_sr1", &gen_m1);
	t_gen_mass_sr2->Branch("gen_tripletM_sr2", &gen_m2);
	t_gen_mass_sr3->Branch("gen_tripletM_sr3", &gen_m3);
	t_gen_mass_sr4->Branch("gen_tripletM_sr4", &gen_m4);

	//==== Fill trees ====
	for (unsigned int i = 0; i < t_sr1->GetEntries(); i++) {
		t_sr1->GetEntry(i);
		for (unsigned int it = 0; it < p_mass1->size(); it++) {
			m1 = p_mass1->at(it);
			t_mass_sr1->Fill();
		}
		for (unsigned int it = 0; it< p_gen_mass1->size(); it++) {
			gen_m1 = p_gen_mass1->at(it);
			t_gen_mass_sr1->Fill();
		}
	}
	cout << "job for sr1 finished" << endl;
	
	for (unsigned int i = 0; i < t_sr2->GetEntries(); i++) {
        t_sr2->GetEntry(i);
        for (unsigned int it = 0; it < p_mass2->size(); it++) {
            m2 = p_mass2->at(it);
            t_mass_sr2->Fill();
        }
        for (unsigned int it = 0; it< p_gen_mass2->size(); it++) {
            gen_m2 = p_gen_mass2->at(it);
            t_gen_mass_sr2->Fill();
        }
    }
    cout << "job for sr2 finished" << endl;

	for (unsigned int i = 0; i < t_sr3->GetEntries(); i++) {
        t_sr3->GetEntry(i);
        for (unsigned int it = 0; it < p_mass3->size(); it++) {
            m3 = p_mass3->at(it);
            t_mass_sr3->Fill();
        }
        for (unsigned int it = 0; it< p_gen_mass3->size(); it++) {
            gen_m3 = p_gen_mass3->at(it);
            t_gen_mass_sr3->Fill();
        }
    }
    cout << "job for sr3 finished" << endl;

	for (unsigned int i = 0; i < t_sr4->GetEntries(); i++) {
        t_sr4->GetEntry(i);
        for (unsigned int it = 0; it < p_mass4->size(); it++) {
            m4 = p_mass4->at(it);
            t_mass_sr4->Fill();
        }
        for (unsigned int it = 0; it< p_gen_mass4->size(); it++) {
            gen_m4 = p_gen_mass4->at(it);
            t_gen_mass_sr4->Fill();
        }
    }
    cout << "job for sr4 finished" << endl;

	
	f_out->cd();
	t_mass_sr1->Write(); t_mass_sr2->Write(); t_mass_sr3->Write(); t_mass_sr4->Write();
	t_gen_mass_sr1->Write(); t_gen_mass_sr2->Write(); t_gen_mass_sr3->Write(); t_gen_mass_sr4->Write();
	f_out->Close();
}

