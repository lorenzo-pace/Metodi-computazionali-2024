import pandas as pd
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import scipy
import argparse

dati = pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')

E1 = dati['E1']
E2 = dati['E2']
px1 = dati['px1']
py1 = dati['py1']
pz1 = dati['pz1']
px2 = dati['px2']
py2 = dati['py2']
pz2 = dati['pz2']

#massa invariante s
s = np.sqrt((E1+E2)**2 - ((px1+px2)**2 + (py1+py2)**2 + (pz1+pz2)**2 ))

"""
hh = ROOT.TH1F('hh', 'Masse invarianti; myX; Conteggi', 20, 0, 200)
for sj in s:
    hh.Fill(sj)
ch = ROOT.TCanvas( 'ch', '' )
hh.SetLineColor(9)
hh.SetLineWidth(3)
hh.SetFillColor(9)
hh.SetFillStyle(3001)
hh.Draw()
ch.Draw()
"""

def fg1(x, m, A, sigma, p0, p1):
    return A * np.exp(-((x - m)**2) / (2 * sigma**2)) + p1*x + p0

def fg2(x, m, A1, A2, sigma1, sigma2, p0, p1):
    bkg = p1*x+p0
    gf1 = A1*np.exp(-0.5*(x-m)**2 / sigma1**2)
    gf2 = A2*np.exp(-0.5*(x-m)**2 / sigma2**2)
    
    sig=gf1+gf2
    
    return bkg+sig



def parse_arguments():

    parser = argparse.ArgumentParser(description='Plot e fit dati.',
                                     usage      ='python3 fit_data.py  --opzione')
    parser.add_argument('--minv',    action='store_true',    help='Grafici della massa invariante')
    parser.add_argument('--fit1',          action='store_true',    help='Fit con la prima f1 gaussiana')
    parser.add_argument('--fit2',          action='store_true',    help='Fit con la seconda f2 gaussiana')
    
    return  parser.parse_args()

def jpsimass_fit():

    args = parse_arguments()

    if args.minv == True:
    #grafici preliminari: produca un istogramma della massa invariante calcolata e in un intervallo ristretto attorno al picco più alto
        fig, axes = plt.subplots(1,2, figsize=(12,5))
        axes[0].hist(s, bins=150,  color='gold', alpha=0.7 )
        axes[0].set_xlabel('Massa invariante $s$ (GeV)', fontsize=14)
        n, bins, p = axes[1].hist(s, bins=150, range=(2.8, 3.4), color='green', alpha=0.7 )
        axes[1].set_xlabel('Massa invariante (ristretta intorno al massimo) $s$ (GeV)', fontsize=14)
        plt.show()

    if args.fit1 == True or args.fit2 == True:

        # Plot solo istogramma
        plt.subplots(figsize=(9,6))
        n, bins, _ = plt.hist(s, bins=200, range=(2.85,3.35))
        bw=bins[1]-bins[0] 
        plt.xlabel(r'$s$ [GeV]', fontsize=14)
        plt.ylabel(r'Eventi su {:0.3f} GeV'.format(bw), fontsize=14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()
        #per trovare il centro del bin
        xbins = (bins[:-1] + bins[1:]) /2

        if args.fit1 == True:

            p_0 = np.array([3, 100,  0.5, 10, -0.1])         
            params, params_covariance = scipy.optimize.curve_fit(fg1, xbins, n, sigma=np.sqrt(n), absolute_sigma=True,p0=[p_0], maxfev=5000)
            yfit = fg1(xbins, params[0], params[1], params[2], params[3], params[4])
            delta = yfit-n
            chiquadro =  np.sum( (delta)**2 /yfit ) 
            fig, axes = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1,1]}, sharex=True)
            fig.subplots_adjust(hspace=0)
            axes[0].errorbar(xbins, n, yerr=np.sqrt(n), fmt='.', label='Dati')
            axes[0].set_xlabel('Massa invariante (ristretta intorno al massimo) ', fontsize=14)
            axes[0].plot(xbins, yfit, color='royalblue')
            axes[0].set_ylabel('Eventi su {:0.4f} GeV'.format(bw))
            axes[0].legend(fontsize=14, frameon=False)
            axes[1].errorbar(xbins, delta, yerr=np.sqrt(n), fmt='.', color='darkorange' )
            axes[1].axhline(y=0, color='darkorange' )
            axes[1].set_ylabel('Data-Fit')
            axes[1].set_ylim(-45,45)  
            axes[1].set_yticks(np.arange(-25, 26, 25))
            axes[1].grid(True, axis='y')
            axes[2].errorbar(xbins, delta/np.sqrt(n), fmt='.', color='darkred' )
            axes[2].axhline(y=0, color='darkorange')
            axes[2].set_ylabel(r'(Scarti)/$\sigma$')
            axes[2].set_ylim(-4.5,4.5)  
            axes[2].set_yticks(np.arange(-2.5, 2.6, 2.5))
            axes[2].grid(True, axis='y')
            axes[2].set_xlabel(r'$s$ [GeV]')
            axes[2].grid(True, axis='y')
            fig.align_ylabels() 
            plt.show()
            print('Parametri del fit: ', params)
            print('Parametri di covarianza: ', params_covariance)
            print('Chi^2 = ', chiquadro)

        if args.fit2 == True:
            p_0 = np.array([3, 200, 50, 0.5, 2,  10, -0.1])  
            params, params_covariance = scipy.optimize.curve_fit(fg2, xbins, n, sigma=np.sqrt(n), absolute_sigma=True, p0 = [p_0], maxfev=5000)
            yfit2 = fg2(xbins, params[0], params[1], params[2], params[3], params[4], params[5], params[6])
            delta2 = yfit2-n
            chiquadro2 =  np.sum( (delta2)**2 /yfit2 ) 
            #istogramma con fit e sotto grafico degli scarti per la seconda gaussiana
            fig, axes = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1,1]}, sharex=True)
            fig.subplots_adjust(hspace=0)
            axes[0].errorbar(xbins, n, yerr=np.sqrt(n), fmt='.', label='Dati')
            axes[0].set_xlabel('Massa invariante (ristretta intorno al massimo) ', fontsize=14)
            axes[0].plot(xbins, yfit2, color='royalblue')
            axes[0].set_ylabel('Eventi su {:0.4f} GeV'.format(bw))
            axes[0].legend(fontsize=14, frameon=False)
            axes[1].errorbar(xbins, delta2, yerr=np.sqrt(n), fmt='.', color='darkorange' )
            axes[1].axhline(y=0, color='darkorange' )
            axes[1].set_ylabel('Data-Fit')
            axes[1].set_ylim(-45,45)  
            axes[1].set_yticks(np.arange(-25, 26, 25))
            axes[1].grid(True, axis='y')
            axes[2].errorbar(xbins, delta2/np.sqrt(n), fmt='.', color='darkred' )
            axes[2].axhline(y=0, color='darkorange')
            axes[2].set_ylabel(r'(Scarti)/$\sigma$')
            axes[2].set_ylim(-4.5,4.5)  
            axes[2].set_yticks(np.arange(-2.5, 2.6, 2.5))
            axes[2].grid(True, axis='y')
            axes[2].set_xlabel(r'$s$ [GeV]')
            axes[2].grid(True, axis='y')
            fig.align_ylabels() 
            plt.show()
            print('Parametri del fit: ', params)
            print('Parametri di covarianza: ', params_covariance)
            print('Chi^2 = ', chiquadro2)

    """
    ax[1].errorbar(xdata,  ydata/yfit, yerr=yerr/yfit, fmt='.', color='royalblue' )
    ax[1].axhline(1, color='darkorange') 
    ax[1].set_xlabel('Tempo [s]', fontsize =14)
    ax[1].set_ylabel('Dati/Fit',  fontsize =14)
    ax[1].tick_params(axis="x",   labelsize=14) 
    ax[1].tick_params(axis="y",   labelsize=14) 
    ax[1].set_ylim(0.5,1.5)       
    ax[1].set_yticks(np.arange(0.5, 1.51, 0.25))
    ax[1].grid(True, axis='y')
    """

if __name__ == "__main__":

    jpsimass_fit()