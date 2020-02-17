#ifndef analysis_atlas_susy_2013_05_h
#define analysis_atlas_susy_2013_05_h

#include "SampleAnalyzer/Interfaces/root/RootMainHeaders.h"
#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class atlas_susy_2013_05 : public AnalyzerBase
{
  INIT_ANALYSIS(atlas_susy_2013_05,"atlas_susy_2013_05")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);

 private:
};
}

class mctlib {

 public:

  mctlib();
  virtual ~mctlib();

  virtual double mctcorr(const double v1[4],const double v2[4]
			 ,const double vds[4],const double ptm[2]
			 ,const double ecm=14000.0,const double mxlo=0.0);
  virtual double mct(const double v1[4],const double v2[4]);
  virtual double mt2(const double v1[4],const double v2[4]
		     ,const double vds[4],const double ptm[2]
		     ,const double ecm=14000.0,const double mxlo=0.0);
  virtual double mctminmt2(const double mctsqr,const double m1sqr,
			   const double m2sqr,const double chisqr=0.0);
  virtual double mt2neg(const double v1[4],const double v2[4]
			,const double ptm[2],const double mxlo=0.0);
  virtual double mcy(const double v1[4],const double v2[4]
		     ,const double vds[4],const double ptm[2]);
  virtual double mcx(const double v1[4],const double v2[4]
		     ,const double vds[4],const double ptm[2]);

 private:

  double m_mctecm, m_mctehat, m_pb;

};


class TMctLib : public mctlib {

 public:

  TMctLib();
  ~TMctLib();

  double mctcorr(const MA5::MALorentzVector v1,const MA5::MALorentzVector v2
		 ,const MA5::MALorentzVector vds,const TVector2 ptm
		 ,const double ecm=14000.0,const double mxlo=0.0);
  double mct(const MA5::MALorentzVector v1,const MA5::MALorentzVector v2);
  double mt2(const MA5::MALorentzVector v1,const MA5::MALorentzVector v2
		 ,const MA5::MALorentzVector vds,const TVector2 ptm
		 ,const double ecm=14000.0,const double mxlo=0.0);
  double mt2neg(const MA5::MALorentzVector v1,const MA5::MALorentzVector v2
		 ,const TVector2 ptm,const double mxlo=0.0);
  double mcy(const MA5::MALorentzVector v1,const MA5::MALorentzVector v2
	     ,const MA5::MALorentzVector vds,const TVector2 ptm);
  double mcx(const MA5::MALorentzVector v1,const MA5::MALorentzVector v2
	     ,const MA5::MALorentzVector vds,const TVector2 ptm);

  using mctlib::mctcorr;
  using mctlib::mct;
  using mctlib::mt2;
  using mctlib::mt2neg;
  using mctlib::mcy;
  using mctlib::mcx;

};



#endif

