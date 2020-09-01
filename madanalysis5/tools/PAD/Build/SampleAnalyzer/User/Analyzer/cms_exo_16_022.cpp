#include "SampleAnalyzer/User/Analyzer/cms_exo_16_022.h"
using namespace MA5;
using namespace std;

double calcSumPt(const RecLeptonFormat* mylepton, double coneSize)
{
    double sumPt_ = 0;
    for(unsigned int c=0; c<mylepton->isolCones().size(); c++)
    {
        if(!(fabs(mylepton->isolCones()[c].deltaR() - coneSize)<0.0001)) continue;
        sumPt_ = mylepton->isolCones()[c].sumPT();
    }
    return sumPt_;
}



// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// cms_exo_16_022.cpp version 3.
// -----------------------------------------------------------------------------
bool cms_exo_16_022::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
    INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
    INFO << "        <>   Analysis:  CMS-EXO-16-022,                     <>" << endmsg;
    INFO << "        <>             (Long lived particles)               <>" << endmsg;
    INFO << "        <>   Recasted by: J.Chang, D.Kang, P.Wu and S.Yang  <>" << endmsg;
    INFO << "        <>   Contact: lovejesus99wwjd@gmail.com             <>" << endmsg;
    INFO << "        <>            dayou17@gmail.com                     <>" << endmsg;
    INFO << "        <>            peiwen.wu123@gmail.com                <>" << endmsg;
    INFO << "        <>            slowmoyang@gmail.com                  <>" << endmsg;
    INFO << "        <>   Based on MadAnalysis 5 v1.6.25                 <>" << endmsg;
    INFO << "        <>   For more information, see                      <>" << endmsg;
    INFO << "        <>  http://madanalysis.irmp.ucl.ac.be/wiki/PhysicsAnalysisDatabase" << endmsg;
    INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
    
    
    // Declaration of the signal regions
    Manager()->AddRegionSelection("SR1");
    Manager()->AddRegionSelection("SR2");
    Manager()->AddRegionSelection("SR3");
    
    // Declaration of the preselection cuts
    Manager()->AddCut("one e, one m");
    Manager()->AddCut("e v0, vz");
    Manager()->AddCut("m v0, vz");

    Manager()->AddCut("opposite charge");
    Manager()->AddCut("dR_emu>0.5");
    
    string SR1Cut[] = {
        "SR1"};
    Manager()->AddCut("200<|d0|<500",SR1Cut);
    
    string SR2Cut[] = {
        "SR2"};
    Manager()->AddCut("500<|d0|<1000",SR2Cut);
    
    string SR3Cut[] = {
        "SR3"};
    Manager()->AddCut("1000<|d0|<100000",SR3Cut);
    
    // Histogram declaration
    Manager()->AddHisto("electron_d0", 40,0,1000);
    Manager()->AddHisto("muon_d0", 40,0,1000);
    Manager()->AddHisto("dR(e,mu)", 50,0,5);
    Manager()->AddHisto("eta(e)", 50,-5,5);
    Manager()->AddHisto("eta(mu)", 50,-5,5);
    Manager()->AddHisto("PT(e)", 50,0,1000);
    Manager()->AddHisto("PT(mu)", 50,0,1000);
    
    
    // Histogram declaration
    Manager()->AddHisto("electron_d0_c", 40,0,1000);
    Manager()->AddHisto("muon_d0_c", 40,0,1000);
    Manager()->AddHisto("dR(e,mu)_c", 50,0,5);
    Manager()->AddHisto("eta(e)_c", 50,-5,5);
    Manager()->AddHisto("eta(mu)_c", 50,-5,5);
    Manager()->AddHisto("PT(e)_c", 50,0,1000);
    Manager()->AddHisto("PT(mu)_c", 50,0,1000);
    
    return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void cms_exo_16_022::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
    cout << "BEGIN Finalization" << endl;
    cout << "END   Finalization" << endl;
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool cms_exo_16_022::Execute(SampleFormat& sample, const EventFormat& event)
{
    
    double myWeight;
    if(Configuration().IsNoEventWeight()) myWeight=1.;
    else if(event.mc()->weight()!=0.) myWeight=event.mc()->weight();
    else
    {
        //WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
        return false;
    }
    Manager()->InitializeForNewEvent(myWeight);
    
    if (event.rec()!=0)
    {
        std::vector<const RecLeptonFormat*> SignalElectrons,SignalElectronsSR1, SignalElectronsSR2, SignalElectronsSR3;
        std::vector<const RecLeptonFormat*> SignalMuons, SignalMuonsSR1, SignalMuonsSR2, SignalMuonsSR3;
        
        
        
        // ------- Fill the electron container ------------------------------------------------
        
        
        for (MAuint32 i=0;i<event.rec()->electrons().size();i++)
        {
            const RecLeptonFormat *myElec = &(event.rec()->electrons()[i]);
            double eta = fabs(myElec->eta());
            double pt = myElec->pt();
            double sumpt = calcSumPt(myElec, 0.3);
 
            // ------- isolation condition ------- //
            if(eta > 1.57 && eta < 2.4){if(!(sumpt/pt < 0.065)) continue;}
            if(eta < 1.44) {if(!(sumpt/pt < 0.035)) continue; }
            
            // ------- preselection ------- //
            if( (eta > 1.44) and (eta<1.57) ) continue;
            if(eta > 2.4) continue;
            if(pt < 42) continue;

            SignalElectrons.push_back(myElec);
        }
        

        // --------------------------------------------------------------------------------
        
        
        
        
        // ------- Fill the muon container ------------------------------------------------
        
        for (MAuint32 i=0;i<event.rec()->muons().size();i++)
        {
            
            const RecLeptonFormat *myMuon = &(event.rec()->muons()[i]);
            double eta = fabs(myMuon->eta());
            double pt = myMuon->pt();
            double sumpt = calcSumPt(myMuon, 0.4);
            
            // ------- isolation ------- //
            
            if(!(sumpt/pt < 0.15)) continue;
            
            // ------- preselection ------- //
            
            if(eta > 2.4) continue;
            if(pt < 40) continue;
            
            SignalMuons.push_back(myMuon);
        }
        
        
        // --------------------------------------------------------------------------------
        
        int ne = SignalElectrons.size(); // ---- # of e pass preselection
        int nm = SignalMuons.size(); // ---- # of mu pass preselection
        int ce = 0; // ---- charge of e
        int cm = 0; // ---- charge of mu
        double d0e = 0; // ---- d0 of e
        double d0m = 0; // ---- d0 of mu
        double pte = 0; // ---- pt of e
        double ptm = 0; // ---- pt of mu
        double etae = 0; // ---- eta of e
        double etam = 0; // ---- eta of mu
        double dr_em=0; // ---- DeltaR (e,mu)
       
        double exd = 0;
        double eyd = 0;
        double ezd = 0;
        double ev0 = 0;
        double mxd = 0;
        double myd = 0;
        double mzd = 0;
        double mv0 = 0;
        
        // ------- only 1 e and 1 muon is allowed, no for interatin is needed ---
        
        if(!Manager()->ApplyCut((ne == 1 && nm == 1),"one e, one m"))
            return true;
    
        int i=0;
        int j=0;
        d0e = fabs(SignalElectrons[j]->d0());
        pte = SignalElectrons[j]->pt();
        etae = SignalElectrons[j]->eta();
        ce = SignalElectrons[j]->charge();
        
        d0m = fabs(SignalMuons[i]->d0());
        ptm = SignalMuons[i]->pt();
        etam = SignalMuons[i]->eta();
        cm = SignalMuons[i]->charge();
        
        dr_em = SignalMuons[i]->dr(SignalElectrons[j]);
        
        exd = fabs(SignalElectrons[j]->closestPoint().X());
        eyd = fabs(SignalElectrons[j]->closestPoint().Y());
        ezd = fabs(SignalElectrons[j]->closestPoint().Z());
        ev0 = sqrt( exd * exd + eyd * eyd);
        mxd = fabs(SignalMuons[i]->closestPoint().X());
        myd = fabs(SignalMuons[i]->closestPoint().Y());
        mzd = fabs(SignalMuons[i]->closestPoint().Z());
        mv0 = sqrt( mxd * mxd + myd * myd);
        
        // ------- Fill Histograms before dr, charge, and number of e, mu selection. ------
        
        Manager()->FillHisto("electron_d0", d0e);
        Manager()->FillHisto("muon_d0", d0m);
        Manager()->FillHisto("dR(e,mu)", dr_em);
        Manager()->FillHisto("eta(e)", etae);
        Manager()->FillHisto("eta(mu)", etam);
        Manager()->FillHisto("PT(e)", pte);
        Manager()->FillHisto("PT(mu)", ptm);
        
        // ------- Apply Cuts -------------------------------------------------------------
        
        if(!Manager()->ApplyCut((ezd < 300 && ev0 < 40),"e v0, vz"))
            return true;
        if(!Manager()->ApplyCut((mzd < 300 && mv0 < 40),"m v0, vz"))
            return true;
        
        if(!Manager()->ApplyCut((ce!=cm),"opposite charge"))
            return true;
        
        if(!Manager()->ApplyCut((dr_em > 0.5),"dR_emu>0.5"))
            return true;
        Manager()->FillHisto("dR(e,mu)", dr_em);
        
        if(!Manager()->ApplyCut((d0e>0.2 && d0m > 0.2) && (d0e < 100. && d0m < 100.) ,"200<|d0|<500"))
            return true;
        
        
        if(!Manager()->ApplyCut((d0e>0.5 && d0m > 0.5) && (d0e < 100. && d0m < 100.) ,"500<|d0|<1000"))
            return true;
        
        
        if(!Manager()->ApplyCut((d0e>1. && d0m > 1.) && (d0e < 100. && d0m < 100.) ,"1000<|d0|<100000"))
            return true;
        
        
        
        // --------------------------------------------------------------------------------
        
        
        // ------- Fill Histograms before dr, charge, and number of e, mu selection. ------
        
        Manager()->FillHisto("electron_d0_c", d0e);
        Manager()->FillHisto("muon_d0_c", d0m);
        Manager()->FillHisto("dR(e,mu)_c", dr_em);
        Manager()->FillHisto("eta(e)_c", etae);
        Manager()->FillHisto("eta(mu)_c", etam);
        Manager()->FillHisto("PT(e)_c", pte);
        Manager()->FillHisto("PT(mu)_c", ptm);
        
        
    }
    
    return true;
}

