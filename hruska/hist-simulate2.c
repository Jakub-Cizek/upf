//generator nahodnych cisel z rozdeleni exp + norm 
#define nmax 1000	//pocet hodnot
//#define nbins 100	//pocet binu
#define tau 4		//parametr exponencialniho rozdeleni (casova konstanta)
#define mu 10		//ocekavana hodnota normalniho rozdeleni
#define sigma 2		//standardni odchylka normalniho rozdeleni
#define P_exp 0.75	//pravdepodobnost ze to bude exponencialni rozdeleni  
int simulate(int nbins)						//pocet hodnot a binu promenne funkce "simulate"
{
        FILE *fout;							//soubor kam se zapisi data
        double x[nmax];
        double branch;
        double x_min,x_max;					//minimalni a maximalni hodnota - meze histogramu 
        TRandom3 *gRandom = new TRandom3(); // vytvoreni generatoru nahodnych cisel
        fout=fopen("data.dat","w");			//vystupni soubor s daty - pro zapsani "w"
        for (int i=0; i<nmax; i++) 
        {
          branch=gRandom->Rndm();					//exponencialni nebo normalni rozdeleni?
          if(branch<P_exp) x[i]=gRandom->Exp(tau);	//generovani nahodneho cisla E(tau)
          else x[i]=gRandom->Gaus(mu,sigma);		//generovani nahodneho cisla N(mu,sigma)
          if(i==0) x_min=x_max=x[i];				//aby nebyly nedefinovane meze
          if(x[i]<x_min) x_min=x[i];				//hledani maxima
          if(x[i]>x_max) x_max=x[i];				//hledani minima
          fprintf(fout,"%lf\n",x[i]);				//zapis dat do souboru fout
        }
        printf("min value: %lf\n",x_min);
        printf("max value: %lf\n",x_max);
        TH1D *hist = new TH1D("data", "exp+gauss", nbins, x_min, x_max);	//definice histogramu
        for (int i=0; i<nmax; i++) 
			hist->Fill(x[i]);						//naplneni histogramu
        TCanvas *c1 = new TCanvas("c1", "histogram",5,5,800,600);			//definice okna
        hist->Draw();								//nakresleni histogramu
        fclose(fout);
        return(0);
}

 