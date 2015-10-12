# CSC_eff_74
CSC efficiency package for 2015 (Run 2)

1) Run on RAW data or MC and produce the Ntuple. Here is the example how to run on data using PromptReco recipe:

cmsRun NtupleMaker_2015C.py

2) Run TnP on the Ntuple. Require that probe has at least one segment matched to it in one station (other then station of interest).

python Step1_matchOtherStationsORME13.py Ntuple_file.root

3) make efficiecny plot maping all stations. With color sheme where green=100%.

python Step2_PlotAll_pallete.py
