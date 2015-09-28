#!/usr/bin/python
#######################################################
# Tracker track to LCT/Segments distance study script #
# Author: Zhang Jinzhong, zhangjin@cern.ch            #
#######################################################
#Usage: python MatchStudy.py TheNtupleRootFile.root
from  ROOT import *
from Config import *
import sys
from  numpy import *

stations={
    1:("( CSCRg1==4 )","ME11A",kMagenta,1)
#    2:("( CSCRg1==1 )","ME11B",kRed-9,1),
#    3:("(CSCRg1==2 || CSCRg1==3)","ME12+13",kBlack,1),
#    4:("CSCRg2","ME2",kRed,2),
#    5:("CSCRg3","ME3",kGreen,3),
#    6:("CSCRg4","ME4",kBlue,4)
}
n_stations=len(stations)


gROOT.SetStyle("Plain")
gStyle.SetOptStat(0)

if sys.argv[0] == "python":
    args=sys.argv[2:]
else:
    args=sys.argv[1:]

print "args: ", args

def AddWeightToTree(tree_,sampleweight=1.):
  pileup_file=TFile.Open(DataPileupRootFileName,"read")
  pileup_data=pileup_file.Get("pileup")
  maxPU=len(pileup_mc)
  puweight=[0]*maxPU
  renormalize=100/pileup_data.Integral()
  for nPU in range(0,maxPU):
    if pileup_mc[nPU]>0:
      puweight[nPU]=pileup_data.GetBinContent(pileup_data.FindBin(nPU))/pileup_mc[nPU]*renormalize
  pileup_file.Close()
  tree_cloned_=tree_.CloneTree(0)
# create 1 dimensional float arrays (python's float datatype corresponds to c++ doubles) as fill variables
  weight = zeros(1, dtype=float)
  weightBranch = tree_cloned_.Branch('weight',weight, 'weight/D')
  for n in range(tree_.GetEntries()):
    tree_.GetEntry(n)
    weight[0] = tree_.mcweight*puweight[int(tree_.numberOfPUVerticesMixingTruth)]*sampleweight
    tree_cloned_.Fill()
  return tree_cloned_

file_in = TFile.Open(args[0],"read")
tree_in = file_in.Get("Fraction")
if RunOnMC:
    tmpoutputfile=TFile.Open(TemporaryOutputFile,'RECREATE')
    tree_in = AddWeightToTree(tree_in)
    tree_in.AutoSave()

#content order: name:(formula,x_min,x_max,y_max)
plots={
       "TracktoSegX":('CSCDxTTSeg#',-40.,40.),
       "TracktoSegY":('CSCDyTTSeg#',-40.,40.),
       "TracktoSegXY":('CSCDxyTTSeg#',-1.,40.),
       "TracktoLCTX":('CSCDxTTLCT#',-40,40.),
       "TracktoLCTY":('CSCDyTTLCT#',-40.,40.),
       "TracktoLCTXY":('CSCDxyTTLCT#',0.,40.),
       "TracktoSegXY_Check":('sqrt(pow(CSCDxTTSeg#,2)+pow(CSCDyTTSeg#,2))',-1.,150.),# should be the same with TracktoSegR
       "TracktoLCTXY_Check":('sqrt(CSCDxTTLCT#*CSCDxTTLCT#+CSCDyTTLCT#*CSCDyTTLCT#)',-1.,150.),# should be the same with TracktoLCTR
    "SegtoLCTX":('CSCSegxLc#-CSCLCTxLc#',-40.,40.),
    "SegtoLCTY":('CSCSegyLc#-CSCLCTyLc#',-40.,40.),
    "LCTX":('CSCLCTxLc#',-40.,40.),
    "LCTY":('CSCLCTyLc#',-40.,40.),
    "SegX":('CSCSegxLc#',-40.,40.),
    "SegY":('CSCSegyLc#',-40.,40.),
    	 "SegtoLCTXY":('sqrt(pow(CSCSegxLc#-CSCLCTxLc#,2)+pow(CSCSegyLc#-CSCLCTyLc#,2))',-1.,40.),
    "DisttoEdge":('CSCProjDistEdge#',-60,0.)
       }

def MakeAPlot(Name_,Forumla_,Cut_,color_):
    if RunOnMC:
        tree_in.Project(Name_,Forumla_,'weight*(%s)'%(Cut_))
    else:
        tree_in.Project(Name_,Forumla_,Cut_)
    exec( 'NEntries='+Name_+'.GetEntries()')
    exec( 'Integral='+Name_+'.Integral()')

#    if NEntries>0:
    if Integral>0:
        exec( Name_+'.Scale( 100/'+Name_+'.Integral() )' )
        exec( Name_+'.SetLineColor(color_)' )
        exec( Name_+'.SetMarkerColor(color_)' )
        exec( 'result=(%s.GetMean(),%s.GetRMS())'%(Name_,Name_) )
        print Name_,"(mean,RMS)=",result,"NEntries=",NEntries
        return result
    else:
        print "Skip "+Name_+", no entry."
        return (0,0)
    
for plot in plots:
    exec( plot+'=TCanvas("%s","%s",500,500)'%(plot,plot) )
    exec( plot+"_Max=0" )
#    exec( 'legend_%s=TLegend(0.6,0.6,0.8,0.8)'%(plot) )
    exec( 'legend_%s=TLegend(0.55,0.75,0.9,0.9)'%(plot) )
    exec( 'legend_%s.SetFillColor(0)'%(plot) )
    exec( 'legend_%s.SetTextSize(0.015)'%(plot) )

for idx in range(1,n_stations+1):
#for idx in range(1,2):
#    Cut=stations[idx][0]+" && "+DenominatorRequire.replace("#",str(stations[idx][3]))+" && "+MuTrackPairCut + " && CSCRg1==4 && (CSCSegxLc1-CSCLCTxLc1)<-5. && (CSCSegxLc1-CSCLCTxLc1)>-10." #+" && "+InvariantMass+#"&& (tracks_phi>4.7996554444 && tracks_phi<5.4977871454)"
    Cut=stations[idx][0]+" && "+DenominatorRequire.replace("#",str(stations[idx][3]))+" && "+MuTrackPairCut + " &&  CSCRg1==4 && (CSCSegxLc1-CSCLCTxLc1)<-14. && (CSCSegxLc1-CSCLCTxLc1)>-20." #+" && "+InvariantMass+#"&& (tracks_phi>4.7996554444 && tracks_phi<5.4977871454)"
    for plot in plots:
        Name='%s_%d'%(plot,idx)
        exec( Name+'=TH1D(Name,plot+";cm;scaled number of entries",100,%f,%f)'%(plots[plot][1],plots[plot][2]) )
        MeanAndRMS=MakeAPlot(Name,plots[plot][0].replace('#',str(stations[idx][3])),Cut,stations[idx][2])
        exec( "max="+Name+".GetBinContent("+Name+".GetMaximumBin())" )
        exec( "if "+plot+"_Max<max: "+plot+"_Max=max" )
        exec( 'legend_%s.AddEntry('%(plot)+Name+',\"'+stations[idx][1]+': mean:%.1fcm;RMS:%.1fcm\",\"l\")'%(MeanAndRMS[0],MeanAndRMS[1]) )

for plot in plots:
    exec( plot+'.cd()')
    DrawOption="H"
    for idx in range(1,n_stations+1):
        Name='%s_%d'%(plot,idx)
        exec( Name+'.Draw(\"'+DrawOption+'\")' )
        if DrawOption is "H":
#            exec( Name+'.SetMaximum(%s_Max*1.05)'%(plot) )
            exec( Name+'.SetMaximum(120.)' )
            exec( Name+'.SetMinimum(0.005)')
            if "XY" in plot:
                print "    ========> plot ", plot, "  has XY!!!"
	        exec( Name+'.SetMaximum(50.)' )
                exec( Name+'.SetMinimum(0.02)')
            DrawOption="H,same"
        exec( 'legend_%s.Draw()'%(plot) )
        exec( plot+'.SetLogy()')

raw_input("Please adjust plots. Press ENTER when finish.")

for plot in plots:
  exec( plot+'.cd()')
  exec( plot+'.SaveAs("%s.pdf")'%(plot+args[1]) )
  exec( plot+'.SaveAs("%s.C")'%(plot+args[1]) )

file_in.Close()
if RunOnMC:
    tmpoutputfile.Close()
    import os
    os.system( "rm "+TemporaryOutputFile )
#print "It will probably crash while running sys.exit(). Just ignore that."
