//histogram automaticke urceni poctu binu
//algoritmus Shimazaki and Shinomoto. Neural Comput, 2007, 19(6), 1503-1527
#define ndata 1000 //pocet dat
int run()
{
        FILE *fin,*fout; //soubor adkud ctu data a kam pisu vysledny histogram
        int i;  //index pro pole
        int nbin; //pocet binu
        double x[ndata]; //pole ve kterem budou namerena data
        double C[ndata]; //ztratova funkce
        double xmin,xmax; //minimalni a maximalni hodnota - meze histogramu
        double delta[ndata]; //sirka binu 
        double mu,var;   //ocekavana hodnota a rozptyl 
        double C_min; //minimum, ztratove funkce 
        int nbin_opt; //optimalni pocet binu
        
        fin=fopen("data.dat","r"); //otevreni souboru data.dat pro cteni
        fout=fopen("histogram.txt","w"); //vytvoreni a otevreni vystupniho souboru histogram.txt pro psani
        for(i=0;i<ndata;i++)   //cyklus ve kterem nactu data
        {
          fscanf(fin,"%lf",&x[i]);
          if(i==0) xmin=xmax=x[i]; //to je proto aby xmin a xmax bylo definovano (dame tam nejdriv prvni hodnotu)
          if(x[i]<xmin) xmin=x[i]; //aby nejmensi hodnota byla v xmin
          if(x[i]>xmax) xmax=x[i]; //aby nejvetsi hodnota byla v xmax
        }
       printf("minimalni hodnota:%lf\n",xmin);
       printf("maximalni hodnota:%lf\n",xmax);
       for(nbin=1;nbin<ndata;nbin++) //pocet binu budu postupne menit od 1 to ndata a pocitat ztratovou funkci C(Delta)
       {
          delta[nbin]=(xmax-xmin)/(double)nbin; //sirka binu
          TH1D *hist = new TH1D("hist","histogram",nbin,xmin,xmax); //vytvori histogram
          for(i=0;i<ndata;i++) hist->Fill(x[i]); //naplneni histogramu
          mu=0;
          for(i=0;i<nbin;i++) mu=mu+hist->GetBinContent(i); //spocitame stredni hodnotu vysky sloupecku
          mu=mu/(double)nbin;
          var=0; 
          for(i=0;i<nbin;i++) var=var+pow((hist->GetBinContent(i)-mu),2); //spocitame rozptyl
          var=var/(double)nbin;
          C[nbin]=(2*mu-var)/pow(delta[nbin],2); //ztratova funkce
          if(nbin==1) C_min=C[nbin];   //najdeme minimum ztratove funkce
          if(C[nbin]<C_min) 
          {
              C_min=C[nbin];
              nbin_opt=nbin;
          }
          delete hist;          //smazani histogramu 
                                           
       }
       C[0]=0;
       delta[0]=0;
       TCanvas *c1 = new TCanvas("c1", "ztratova funkce",5,5,800,600); //vytvoreni okna (platna)
       TGraph *g1 = new TGraph(ndata,delta,C); //vytvoreni grafu ztratove funnkce C(Delta) 
       g1->SetMarkerColor(kBlue); //nastaveni barvy bodu
       g1->SetMarkerStyle(20); //nastaveni typu bodu 
       g1->SetMarkerSize(1); //nbstaveni velikosti bodu  
       g1->SetTitle("ztratova funkce"); //nadpis grafu
       g1->GetXaxis()->SetTitle("sirka binu");  //popis osy X
       g1->GetYaxis()->SetTitle("ztratova funkce");  //popis osy Y
       gPad->SetLogx();
       g1->Draw("AP");  //vykresleni grafu 
       
       printf("optimalni pocet binu = %ld\n",nbin_opt); //vypis optimalniho poctu binu
       printf("optimalni sirka binu = %lf\n",(xmax-xmin)/(double)nbin_opt);  //vypis optimalni sirky binu
       TCanvas *c3 = new TCanvas("c3", "optimalni histogram",5,5,800,600); //vytvoreni okna (platna)
       TH1D *hist_opt = new TH1D("hist_opt","optimalni histogram",nbin_opt,xmin,xmax); //vytvori histogram s optimalnim poctem binu
       for(i=0;i<ndata;i++) hist_opt->Fill(x[i]);  //naplni histogram
       hist_opt->GetXaxis()->SetTitle("bin");  //popis osy X
       hist_opt->GetYaxis()->SetTitle("pocet pripadu"); //popis osy Y
       hist_opt->SetFillColor(45); //barva plochy histogramu
       hist_opt->Draw();  //vykresleni histogramu
       return(0); //kdyz funkce spravne probehne vrati 0 
}
 

 