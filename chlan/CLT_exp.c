#include <TFile.h>
#include <TH1F.h>
#include <TRandom3.h>

int CLTexp(int Nexponential) // Pocet sumaci

{
  TRandom3 *r = new TRandom3(0);	
  const int Nexperiments = 100000;                   // Pocet exponencialne rozdelenych cisel
  double pi = 3.14159265358979323846264338328;      

// Vytvoreni histogramu
  TH1F *Hist_Sum         = new TH1F("Hist_Sum", "Hist_Sum", 120, -6.0, 6.0);
  TH1F *Hist_Exponential = new TH1F("Hist_Exponential", "Hist_Exponential", 240, -6.0, 6.0);
 
// Nakrmeni historgramu
  for (int iexp = 0; iexp < Nexperiments; iexp++) {
    double sum = 0.0;
      // Exponencialne rozdelena cisla se stredni hodnotou 0 a standardni odchylkou 1):
    for (int i = 0; i < Nexponential; i++) {
      double x = -log(r.Uniform()) - 1.0;                // Exponencialni rozdeleni se zacatkem v -1
      sum += x;
      Hist_Exponential->Fill(x);
    }
    sum = sum / sqrt(double(Nexponential));		// normovani
    Hist_Sum->Fill(sum);
  }
  
  TCanvas *c0 = new TCanvas("c0", "mean",50,50,1200,900);			//definice okna
  
  //nafitujeme gaussovkou
  TF1 *f1 = new TF1("f1","gaus",-2.5,2.5);
  f1->SetParameters(Hist_Sum.GetMaximum(), Hist_Sum.GetMean(), Hist_Sum.GetRMS());  
 // Hist_Sum.Fit("f1");																
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
