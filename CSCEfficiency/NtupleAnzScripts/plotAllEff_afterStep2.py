from  ROOT import *
from  numpy import *
from array import *
import CMS_lumi, tdrstyle

from ROOT import gROOT, TCanvas, TF1, TFile, TTree, gRandom, TH1F, TEfficiency, TLegend

from ROOT import SetOwnership

gROOT.SetStyle("Plain")
gStyle.SetPaintTextFormat("0.3g")
gStyle.SetOptStat(0)
tdrstyle.setTDRStyle()

dir=""

ptbin=[3,6,10,20,40,60,80,100] #pt binning
etabin1=[ 0,0.85,1.18,1.3,1.5,1.7,1.9,2.1,2.4 ] #station 1 eta binning 
etabin2=[ 0,0.95,1.2,1.4,1.6,1.8,2.0,2.2,2.4 ] #station 2 eta binning
etabin3=[ 0,0.9,1.08,1.3,1.5,1.72,1.9,2.2,2.4 ] #station 3 eta binning
etabin4=[ 0,0.9,1.15,1.4,1.6,1.78,2.0,2.2,2.4 ] #station 4 eta binning
#phibin=[-0.0872664626+x*0.698131701 for x in range(10)] #phi binning: 18/36 chambers-->9bins, 0 deg points at ring 2, chamber 1 center
phibin=[-0.0872664626+(x*0.698131701)/3. for x in range(28)] #phi binning: 18/36 chambers-->9bins, 0 deg points at ring 2, chamber 1 center
#phibin=[((-0.0872664626+x*0.3490658505)*360/6.2831853) for x in range(20)] #phi binning: 18/36 chambers-->9bins, 0 deg points at ring 2, chamber 1 center
#phibin=[(x*5) for x in range(73)] #phi binning: 18/36 chambers-->9bins, 0 deg points at ring 2, chamber 1 center

ResultPlotsFileName="resultplots_NtupleAnzScripts_newAlign_segment.root"
file_out=TFile.Open(ResultPlotsFileName,'RECREATE')


#for binning in (ptbin,phibin,etabin1):
for binning in (phibin):
#for binning in (1,2):

    c1=TCanvas("c1","c1",600,600)
    #legend=TLegend(0.5, 0.8, 0.5, 0.8)
#    legend=TLegend()
#    legend2=TLegend(0.5, 1.0, 0.5, 1.0)
#    legend3=TLegend(1.5, 2.0, 1.5, 2.0)
    leg=TLegend(0.7, 0.5, 0.9, 0.65)
    
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetShadowColor(0)
    leg.SetBorderSize(0)
    leg.SetTextFont(132)
    leg.SetTextSize(0.03)
#    leg.SetTextSize(0.05)
#    SetOwnership( legend, 0 )   # 0 = release (not keep), 1 = keep

    #legend=TLegend()
    
    color=0
    
    input_file_name=dir+"resultplots_NtupleAnzScripts.root"
    print " input file: ",input_file_name
    file_in = TFile.Open(input_file_name,"read")
    
#    for st_ in ("11A","11B","12+13","2","3","4"):
#    for st_ in ("4","3","2","12+13","11B","11A"):
#    for st_ in ("4","3","2","11B","11A"):
    for st_ in ("4","3","2","12+13"):

        color+=1
#	if (st_=="11B"):
#	   color+=1

        variable=""
        print "st: %s, binning: %s"%(st_,binning)

#ME4seg_effV
#        histo=file_in.Get("eff_seg_binomErr_%s"%variable)
	try:
            histo=file_in.Get("ME%sseg_effV"%st_)
            print " found %s"%st_
        except:
	    print "not found %s"%st_
            continue

        print " plotting %s"%st_
        histo=file_in.Get("ME%sseg_effV"%st_)	
        print "ME%sseg_effV"%st_
        c1.cd()
        histo.SetLineColor(color)
#        histo.SetMarkerStyle(21)
#        histo.SetMarkerSize(1.)
#        histo.SetMarkerColor(color)
#        legend.AddEntry(histo,"ME%s"%st_,"lp")
#        legend2.AddEntry(histo,"ME%s"%st_,"lp")
#        legend3.AddEntry(histo,"ME%s"%st_,"lp")
        leg.AddEntry(histo,"ME%s"%st_,"lp")
        if (color==1):
            histo.SetTitle(";%s;efficiency"%variable);
            histo.SetMinimum(0.7) # no way to set range or max with tefficiecny! -> need to make asymmetricerror histogram and then set range...
#            histo.GetYaxis().SetRangeUser(0.7,1.05)
            histo.GetYaxis().SetRangeUser(-0.1,1.1)
#            histo.GetXaxis().SetTitle("p_{T}")
            histo.GetXaxis().SetTitle("#phi")
            histo.GetYaxis().SetTitleOffset(1.4)
            histo.GetYaxis().SetTitle("segment efficiency")
#            gPad.SetLogx() 
            histo.Draw("AL")
        else:
            histo.Draw("Lsame")
#        legend.Draw()
#        legend2.Draw()
#        legend3.Draw()
#        leg.Draw()
       
         
    c1.cd()
#    legend.Draw()
#    legend2.Draw()
#    legend3.Draw()
    leg.Draw()
    file_out.cd()
    c1.Write("eff_seg_TnPZ_newAlign_binomErr_%s"%variable)
    c1.SaveAs("eff_seg_TnPZ_newAlign_binomErr_%s.pdf"%variable)
    c1.SaveAs("eff_seg_TnPZ_newAlign_binomErr_%s.root"%variable)
