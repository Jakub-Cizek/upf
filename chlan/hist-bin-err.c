//generator nahodnych cisel z rozdeleni exp + norm 

#define tau 4 //parametr exponencialniho rozdeleni (doba zivota)
#define mu 10  //ocekavana hodnota Normalniho rozdeleni
#define sigma 2 //standardni odchylka normalniho rozdeleni
#define P_exp 0.75 //pravdepodobnost ze to bude exponencialni rozdeleni  
#define nbins 100 //pocet binu
#define nsim 100 //kolik simulaci budeme delat pro kazde N_tot 
#define nN 50
int simulate()
{
        double x[10000];
        double branch;
        double x_min,x_max;   //minimalni a maximalni hodnota - meze histogramu
        int k_bin = 50; //bin, ktery budeme testovat
        int x_bin[nsim];
        int i,j,k,l;
        int ntot[nN]; //celkovy pocet dat
        double x_bin_mean[nN],x_bin_sigma[nN];
        double x_nN[nN],x_sqrt[nN];
        double mean_P_k;
        double y_P[nN];
        TRandom3 *gRandom = new TRandom3(); // vytvori generator nahodnych cisel
        x_min=0;
        x_max=10;
        TH1D *hist = new TH1D("data", "exp+gauss", nbins, x_min, x_max);
        mean_P_k=0.0;
        for(l = 0; l < nN; l++) //loop ruzne N_tot
        {
          ntot[l]=100*(l+1);
          x_bin_mean[l]=0.0;
          x_bin_sigma[l]=0.0;
          for(j = 0; j < nsim; j++) //loop histogramy pro stejne N_tot
          {
            for (int i = 0; i < ntot[l]; i++) 
            {
              branch=gRandom->Rndm(); 
              if(branch<P_exp) x[i]=gRandom->Exp(tau); //generovani nah. cisla E(tau)
              else x[i]=gRandom->Gaus(mu,sigma); //generovani nah. cisla N(mu,sigma)
              hist->Fill(x[i]); //naplneni histogramu
            }  // i
            x_bin[j]=hist->GetBinContent(k_bin); //obsah histogramu v k-tem binu
            for(k = 0; k < nbins; k++) hist->SetBinContent(k,0); //vynulovani hist.
            x_bin_mean[l]=x_bin_mean[l]+x_bin[j]/(double)nsim; //prum. hod. v k-tem binu
            } //j
          mean_P_k=mean_P_k+(x_bin_mean[l]/(double)ntot[l])/(double)nN;
          for(j = 0; j < nsim; j++)
          {
            x_bin_sigma[l]=x_bin_sigma[l]+pow(x_bin[j]-x_bin_mean[l],2)/(double)nsim; //rozptyl
          } //j
          x_bin_sigma[l]=sqrt(x_bin_sigma[l]);
          x_nN[l]=(double)ntot[l];
          x_sqrt[l]=(double)sqrt(ntot[l]);
        }   //l 
        for(l = 0; l < nN; l++) y_P[l]=sqrt(mean_P_k*x_nN[l]); 
        
        TCanvas *c0 = new TCanvas("c0", "mean",5,5,800,600); //definice okna
        TGraph *g0= new TGraph(nN,x_nN,x_bin_mean);
        g0->SetMarkerStyle(4);
        g0->SetMarkerColor(2);
        g0->SetTitle("stredni hodnota v k-tem binu");
        g0->Draw("APo");     //nakresli histogram
        g0->GetXaxis()->SetTitle("N_{tot}");
        g0->GetXaxis()->CenterTitle();
        g0->GetYaxis()->SetTitle("<N_{k}>");
        g0->GetYaxis()->CenterTitle();
        g0->Draw("APo");     //nakresli histogram

        
        TCanvas *c1 = new TCanvas("c1", "sigma",5,5,800,600); //definice okna
        TGraph *g1= new TGraph(nN,x_nN,x_bin_sigma);
        TGraph *f1= new TGraph(nN,x_nN,y_P);
        g1->SetMarkerStyle(4);
        g1->SetMarkerColor(4);
        f1->SetLineColor(2);
        g1->SetTitle("chyba vysky k-teho binu versus N_{tot}");
        g1->Draw("APo");     //nakresli graf
        g1->GetXaxis()->SetTitle("N_{tot}");
        g1->GetXaxis()->CenterTitle();
        g1->GetYaxis()->SetTitle("#sigma_{k}");
        g1->GetYaxis()->CenterTitle();
        g1->Draw("APo");     //nakresli graf
        f1->Draw("L");     //nakresli graf
        
        TCanvas *c2 = new TCanvas("c2", "sigma vs sqrt N",5,5,800,600); //definice okna
        TGraph *g2= new TGraph(nN,x_sqrt,x_bin_sigma);
        g2->SetMarkerStyle(4);
        g2->SetMarkerColor(2);
        g2->SetTitle("chyba vysky k-teho binu versus (N_{tot})^{1/2}");
        g2->Draw("APo");     //nakresli histogram
        g2->GetXaxis()->SetTitle("N_{tot}^{1/2}");
        g2->GetXaxis()->CenterTitle();
        g2->GetYaxis()->SetTitle("#sigma_{k}");
        g2->GetYaxis()->CenterTitle();
        g2->Draw("APo");     //nakresli histogram
        return(0);
}

 