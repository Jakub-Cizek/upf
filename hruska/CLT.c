//test centralni limitni vety 
#define N 12			//kolik nahodnych promennych U(0,1) secist
#define ndata 1000000	//pocet simulaci
#define nbins 1000		//pocet binu
#define pi 3.1415926535897932384626433832795

int run()
{
        double x;
        double y[ndata];		//histogram souctu 
        double x_gauss[nbins],y_gauss[nbins];	//predikce CLT - gaussian
        double delta;			//sirka binu
        double x_min,x_max;		//minimalni a maximalni hodnota - meze histogramu
        double mu,sigma;		//ocekavana hodnota a standardni odchylka gaussianu
        int i,k;
        
        printf("N = %d\n",N);
		mu=N/2.0;				//ocekavana hodnota - predpoved CLT
		printf("mu = %lf\n",mu);
		sigma=sqrt(N/12.0);		//standardni odchylka - predpoved CLT
		printf("sigma = %lf\n",sigma);
        x_min=0;				//minimum histogramu
        x_max=N;				//maximum histogramu
		delta=(x_max-x_min)/(double)nbins;		//vypocet sirky binu 
        printf("delta (bin width) = %lf\n",delta); 
        
		TRandom3 *gRandom = new TRandom3();		//vytvori generator nahodnych cisel
        
        for(i=0; i<ndata; i++) 
        {
          y[i]=0; 
          for(k=0; k<N; k++)
          {
               x=gRandom->Rndm();	//generovani nahodne promenne U(0,1)
               y[i]=y[i]+x;			//suma N nahodnych promennych U(0,1)
          }	//k - soucet N nahodnych promennych
        }	//i - ndata simulaci
                    
        for(i=0; i<nbins; i++)		//vypocet gaussianu - predpoved CLT
        {
          x_gauss[i]=x_min+i*delta;
          y_gauss[i]=ndata*delta*1.0/(sqrt(2.0*pi)*sigma)*exp(-pow(x_gauss[i]-mu,2)/(2.0*pow(sigma,2)));
        }

        TCanvas *c0 = new TCanvas("c0", "mean",50,50,800,600);			//definice okna
        TH1D *hist = new TH1D("hist","histogram",nbins,x_min,x_max);	//definice histogramu
        for(i=0; i<ndata; i++) hist->Fill(y[i]);						//naplneni histogramu
        TGraph *g0= new TGraph(nbins,x_gauss,y_gauss);					//definice grafu s gaussianem
        hist->Draw();													//vyktresleni histogramu
        g0->SetLineColor(2);											//barva cary grafu
        hist->SetTitle("histogram + CLT prediction");					//nadpis grafu
        hist->GetXaxis()->SetTitle("y");								//popis osy x
        hist->GetXaxis()->CenterTitle();
        hist->GetYaxis()->SetTitle("pocet pripadu");					//popis osy y
        hist->GetYaxis()->CenterTitle();
        hist->Draw();													//vykresleni histogramu
        g0->Draw("L");													//nakresli graf        
        return(0);
}

 