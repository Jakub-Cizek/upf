//generator nahodnych cisel z rozdeleni exp + norm 
#define nmax 10000		//maximalni pocet hodnot
#define nsim 1000		//pocet simulaci ktere budeme delat pro kazde N_tot 
#define nbins 100		//pocet binu
#define tau 4			//parametr exponencialniho rozdeleni (casova konstanta)
#define mu 10			//ocekavana hodnota normalniho rozdeleni
#define sigma 2			//standardni odchylka normalniho rozdeleni
#define P_exp 0.75		//pravdepodobnost ze to bude exponencialni rozdeleni  
#define nN 50			//50 ruznych hodnot N_tot
int simulate()
{
        double x[nmax];			//nahodna promenna x
        double branch;
        double x_min,x_max;		//minimalni a maximalni hodnota - meze histogramu
        int k_bin = 50;			//bin, ktery budeme testovat
        int x_bin[nsim];		//hodnota v k-tem binu pro danou simulaci
        int i,j,k,l;
        int ntot[nN];			//pole celkoveho poctu hodnot N_tot
        double x_bin_mean[nN];	//stredni hodnota v k-tem binu pro dane N_tot
		double x_bin_sigma[nN];	//rozptyl hodnot v k-tem binu pro dane N_tot
        double x_nN[nN],x_sqrt[nN];		//x-ove hodnoty pro N_tot a sqrt(N_tot)
        double mean_P_k;		//prumerna relativni cetnost v k-tem binu
        double y_P[nN];			//teoreticke hodnoty sigma

        TRandom3 *gRandom = new TRandom3();	//definice generatoru nahodnych cisel
        x_min=0;							//pevne minimum
        x_max=10;							//pevne maximum
        TH1D *hist = new TH1D("data", "exp+gauss", nbins, x_min, x_max);	//definice histogramu
        mean_P_k=0.0;						//vynulovani prumerne relativni cetnosti v k-tem binu

        for(l=0; l<nN; l++)					//CYKLUS pro ruzne pocty hodnot v histogramu N_tot
        {
          ntot[l]=100*(l+1);				//N_tot od 100 do 5000 hodnot
          x_bin_mean[l]=0.0;				//vynulovani stredni hodnoty pro danou simulaci
          x_bin_sigma[l]=0.0;				//vynulovani rozptylu pro danou simulaci
          
		  for(j=0; j<nsim; j++)				//SIMULACE ruznych histogramu se stejnym N_tot
          {

            for (i=0; i<ntot[l]; i++)		//HISTOGRAM = soucet exponencialniho a normalniho rozdeleni
            {
              branch=gRandom->Rndm();					//exponencialni nebo normalni rozdeleni?
              if(branch<P_exp) x[i]=gRandom->Exp(tau);	//generovani nahodneho cisla E(tau)
              else x[i]=gRandom->Gaus(mu,sigma);		//generovani nahodneho cisla N(mu,sigma)
              hist->Fill(x[i]);							//naplneni histogramu
            }	// i-cyklus (histogram)

            x_bin[j]=hist->GetBinContent(k_bin);				//obsah histogramu v k-tem binu
            x_bin_mean[l]=x_bin_mean[l]+x_bin[j]/(double)nsim;	//vypocet prumerne hodnoty v k-tem binu
			for(k=0; k<nbins; k++) hist->SetBinContent(k,0);	//vynulovani histogramu
            }	//j-cyklus (simulace stredni hodnoty)

          mean_P_k=mean_P_k+(x_bin_mean[l]/(double)ntot[l])/(double)nN;		//prumerna relativni cetnost v k-tem binu
          
		  for(j=0; j<nsim; j++)				//ROZPTYL hodnot pro nasimulovane histogramy
          {
            x_bin_sigma[l]=x_bin_sigma[l]+pow(x_bin[j]-x_bin_mean[l],2)/(double)nsim;	//vypocet rozptylu hodnot v k-tem binu
          }		//j-cyklus (simulace rozptylu)

          x_bin_sigma[l]=sqrt(x_bin_sigma[l]);					//rozptyl -> odchylka (odmocnina)
          x_nN[l]=(double)ntot[l];								//hodnoty N_tot pro x-ovou osu
          x_sqrt[l]=(double)sqrt(ntot[l]);						//hodnoty sqrt(N_tot) pro x-ovou osu
        }		 //l-cyklus (ruzny pocet hodnot N_tot)

        for(l=0; l<nN; l++) y_P[l]=sqrt(mean_P_k*x_nN[l]);		//teoreticka zavislost y=sqrt(x) -> sigma=sqrt(P*N_tot)		
        
        TCanvas *c0 = new TCanvas("c0", "mean",20,20,800,600);	//definice okna 1
        TGraph *g0= new TGraph(nN,x_nN,x_bin_mean);				//stredni pocet hodnot v k-tem binu vs pocet hodnot v histogramu	
        g0->SetMarkerStyle(4);
        g0->SetMarkerColor(2);
        g0->SetTitle("stredni hodnota v k-tem binu");
        g0->Draw("APo");		//nakresli graf
        g0->GetXaxis()->SetTitle("N_{tot}");
        g0->GetXaxis()->CenterTitle();
        g0->GetYaxis()->SetTitle("<N_{k}>");
        g0->GetYaxis()->CenterTitle();
        g0->Draw("APo");		//nakresli graf

        TCanvas *c1 = new TCanvas("c1", "sigma",40,40,800,600);	//definice okna 2
        TGraph *g1= new TGraph(nN,x_nN,x_bin_sigma);			//odchylka vysky k-teho binu vs pocet hodnot v histogramu
        TGraph *f1= new TGraph(nN,x_nN,y_P);					//teoreticka zavislost (odmocnina)
        g1->SetMarkerStyle(4);
        g1->SetMarkerColor(4);
        f1->SetLineColor(2);
        g1->SetTitle("chyba vysky k-teho binu versus N_{tot}");
        g1->Draw("APo");		//nakresli graf
        g1->GetXaxis()->SetTitle("N_{tot}");
        g1->GetXaxis()->CenterTitle();
        g1->GetYaxis()->SetTitle("#sigma_{k}");
        g1->GetYaxis()->CenterTitle();
        g1->Draw("APo");		//nakresli graf - simulovana data
        f1->Draw("L");			//nakresli graf - teoreticka zavislost
        
        TCanvas *c2 = new TCanvas("c2", "sigma vs sqrt N",60,60,800,600);		//definice okna 3
        TGraph *g2= new TGraph(nN,x_sqrt,x_bin_sigma);			//odchylka vysky k-teho binu vs odmocnina z poctu hodnot
        g2->SetMarkerStyle(4);
        g2->SetMarkerColor(2);
        g2->SetTitle("chyba vysky k-teho binu versus (N_{tot})^{1/2}");
        g2->Draw("APo");		//nakresli graf
        g2->GetXaxis()->SetTitle("N_{tot}^{1/2}");
        g2->GetXaxis()->CenterTitle();
        g2->GetYaxis()->SetTitle("#sigma_{k}");
        g2->GetYaxis()->CenterTitle();
        g2->Draw("APo");		//nakresli graf
        return(0);
}

 