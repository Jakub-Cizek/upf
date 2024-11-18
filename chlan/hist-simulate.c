//generator nahodnych cisel z rozdeleni exp + norm 
#define nmax 1000 //kolik hodnot
#define tau 4 //parametr exponencialniho rozdeleni (doba zivota)
#define mu 10  //ocekavana hodnota Normalniho rozdeleni
#define sigma 2 //standardni odchylka normalniho rozdeleni
#define P_exp 0.75 //pravdepodobnost ze to bude exponencialni rozdeleni  
#define nbins 100 //pocet binu
int simulate()
{
        double x[nmax];
        double branch;
        double x_min,x_max;   //minimalni a maximalni hodnota - meze histogramu 
        TRandom3 *gRandom = new TRandom3(); // vytvori generator nahodnych cisel
        for (int i = 0; i < nmax; ++i) 
        {
          branch=gRandom->Rndm(); 
          if(branch<P_exp) x[i]=gRandom->Exp(tau); //generovani nahodneho cisla E(tau)
          else x[i]=gRandom->Gaus(mu,sigma); //generovani nahodneho cisla N(mu,sigma)
          if(i==0) x_min=x_max=x[i];   //aby nebyly nedefinovane
          if(x[i]<x_min) x_min=x[i];
          if(x[i]>x_max) x_max=x[i];
         }
        printf("min value: %lf\n",x_min);
        printf("max value: %lf\n",x_max);
        TH1D *hist = new TH1D("data", "exp+gauss", nbins, x_min, x_max);
        for (int i = 0; i < nmax; ++i) hist->Fill(x[i]);  //naplneni histogramu
        TCanvas *c1 = new TCanvas("c1", "histogram",5,5,800,600); //definice okna
        hist->Draw();     //nakresli histogram
        return(0);
}

 