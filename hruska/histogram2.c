//histogram 
#define ndata 1000 //pocet dat
//#define nbins 100 //pocet binu
int run(int nbins)							//pocet binu promenna funkce "run"
{
        FILE *fin,*fout;					//soubory odkud se prectou a kam se zapisi data
        double x[ndata];
        double x_min,x_max;					//minimalni a maximalni hodnota - meze histogramu 
        fin=fopen("data.dat","r");			//vstupni soubor s daty - pro cteni "r"
        fout=fopen("histogram.txt","w");	//vystupni soubor s daty - pro zapsani "w"
        for (int i=0; i<ndata; i++) 
        {
			fscanf(fin,"%lf",&x[i]);		//nacteni dat
			if(i==0) x_min=x_max=x[i];		//aby nebyly nedefinovane meze
			if(x[i]<x_min) x_min=x[i];		//hledani minima
			if(x[i]>x_max) x_max=x[i];		//hledani maxima
        }
        fclose(fin);
        printf("min value: %lf\n",x_min);
        printf("max value: %lf\n",x_max);
        printf("bin width: %lf\n",(x_max-x_min)/nbins);
        TH1D *hist = new TH1D("hist", "histogram", nbins, x_min, x_max);	//definice histogramu
        for (int i=0; i<ndata; i++) 
			hist->Fill(x[i]);				//naplneni histogramu
		TCanvas *c1 = new TCanvas("c1", "histogram",10,10,800,600);			//definice okna
        hist->Draw();						//nakresleni histogramu
        for (int i=0; i<nbins; i++)			//zapis histogramu do souboru fout
        {
			counts=hist->GetBinContent(i);		//zjisteni hodnoty v i-tem binu
			fprintf(fout,"%ld %ld\n",i,counts);	//zapis hodnoty do souboru fout
        }
        fclose(fout);
        return(0);
}

 