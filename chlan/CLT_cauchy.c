#include <TFile.h>
#include <TH1F.h>
#include <TRandom3.h>

int CLTcauchy(int Ncauchy)   // Pocet sumaci

{
  TRandom3 *r = new TRandom3(0);	
  const int Nexperiments = 1000000;                   // Pocet simulaci
  double pi = 3.14159265358979323846264338328;      
  
// Vytvoreni histogramu
  TH1F *Hist_Sum         = new TH1F("Hist_Sum", "Hist_Sum", 120, -16.0, 16.0);
  TH1F *Hist_Cauchy      = new TH1F("Hist_Cauchy", "Hist_Cauchy", 240, -16.0, 16.0);

// Nakrmeni historgramu
  for (int iexp = 0; iexp < Nexperiments; iexp++) {
    double sum = 0.0;
    
      // generovani cisel podle Cauchyho rozdeleni (1 / (1 + x^2)):
    for (int i = 0; i < Ncauchy; i++) {
      double x = tan(pi * (r.Uniform() - 0.5));          // Cauchyho rozdeleni s maximem v 0
      sum += x;
      Hist_Cauchy->Fill(x);
    }
    
    sum = sum / sqrt(double(Ncauchy));
    Hist_Sum->Fill(sum);
  }

  TCanvas *c0 = new TCanvas("c0", "mean",50,50,1200,900);			//definice okna
  
  //nafitujeme gaussovkou
  TF1 *f1 = new TF1("f1","gaus",-2.5,2.5);
  f1->SetParameters(Hist_Sum.GetMaximum(), Hist_Sum.GetMean(), Hist_Sum.GetRMS());  
  Hist_Sum.Fit("f1");																
  f1->SetLineColor(2);
  double mu = f1->GetParameter(1);
  double sigma = f1->GetParameter(2);
  
  Hist_Sum->SetTitle(Form("mu = %f, sigma = %f",mu,sigma));					//nadpis grafu
  Hist_Sum->GetXaxis()->SetTitle("y");								//popis osy x
  Hist_Sum->GetXaxis()->CenterTitle();
  Hist_Sum->GetYaxis()->SetTitle("pocet pripadu");					//popis osy y
  Hist_Sum->GetYaxis()->CenterTitle();
  Hist_Sum->SetMinimum(0);
  Hist_Sum->Draw();													//vykresleni histogramu
}
