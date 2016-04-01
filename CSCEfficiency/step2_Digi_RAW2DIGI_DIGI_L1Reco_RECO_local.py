# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2_Digi --filein file:/hdfs/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/GEN-SIM-RAW/StartupFlat10to50bx50Raw_MCRUN2_74_V8-v1/10000/420FECC0-5A01-E511-A616-AC853DA0692A.root --fileout file:SMP-RunIISpring15DR74-00007_step2.root --mc --eventcontent AODSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier AODSIM --conditions MCRUN2_74_V9 --step RAW2DIGI,DIGI,L1Reco,RECO --magField 38T_PostLS1 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.load("EventFilter.CSCTFRawToDigi.csctfunpacker_cfi")
#process.csctfunpacker.producer = cms.InputTag("rawDataCollector")

process.CSCTFunpacker=cms.Path(process.csctfunpacker)

process.load("EventFilter.CSCTFRawToDigi.csctfpacker_cfi")
process.CSCTFpacker=cms.Path(process.csctfpacker)

HLTProcessName='HLT'
from RecoMuon.TrackingTools.MuonSegmentMatcher_cff import *
process.load("TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff") 
from TrackingTools.TrackAssociator.default_cfi import *
from RecoMuon.MuonIsolationProducers.trackExtractorBlocks_cff import MIsoTrackExtractorBlock


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:/hdfs/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/GEN-SIM-RAW/StartupFlat10to50bx50Raw_MCRUN2_74_V8-v1/10000/420FECC0-5A01-E511-A616-AC853DA0692A.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2_Digi nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('file:SMP-RunIISpring15DR74-00007_step2_Digi.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

process.aodDump = cms.EDAnalyzer('TPTrackMuonSys',
                                 TrackAssociatorParameterBlock,
                                 MuonSegmentMatcher,
                                 TrackExtractor=cms.PSet(MIsoTrackExtractorBlock),
                                 rootFileName   = cms.untracked.string('CSCPFG_Ineff_DATA_test_1_DYtest_digi.root'),
                                 CSCUseTimingCorrections = cms.bool( True ),
                                 CSCUseGasGainCorrections = cms.bool( True ),
                                 isMC            = cms.untracked.bool(False),
                                 mcTag           = cms.untracked.InputTag('genParticles'),
                                 vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                 gTracksTag      = cms.untracked.InputTag('generalTracks'),
                                 trackProducer   = cms.InputTag('csctfunpacker:'),
                                 readBadChannels = cms.bool(True),
                                 readBadChambers = cms.bool(True),
                                 hltTag      = cms.untracked.InputTag("TriggerResults","",HLTProcessName),
                                 hltEvTag    = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
                                 HLTMuTrgNames =  cms.vstring("HLT_Mu?_v*","HLT_Mu??_v*","HLT_Mu???_v*","HLT_IsoMu?_v*","HLT_IsoMu??_v*","HLT_IsoMu???_v*","HLT_L2Mu?_v*","HLT_L2Mu??_v*","HLT_L2Mu???_v*","HLT_SingleMu*","HLT_L1SingleMu*","HLT_IsoTkMu??_v*","HLT_TkMu??_v*","HLT_IsoTkMu??_v*","HLT_TkMu??_v*"),
                                 HLTDiMuTrgName =  cms.string("HLT_DoubleMu?_v*"),
                                 #                      hltEvTag    = cms.untracked.InputTag("hltTriggerSummaryAOD","","REDIGI36X"),
                                 L1extraTag   = cms.untracked.InputTag("l1extraParticles"),
                                 dedxTag         =  cms.untracked.InputTag('dedxHarmonic2')
                                 )


#process.outputstep = cms.EndPath(process.aodDump)

process.TrackAssociatorParameterBlock = cms.untracked.PSet(
    TrackAssociatorParameters = cms.untracked.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(True),
        useHO = cms.bool(True),
        useHcal = cms.bool(True),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    )
)



# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

# Path and EndPath definitions
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

process.outputstep = cms.EndPath(process.aodDump)


# Schedule definition

# working but no digi2raw
#process.schedule = cms.Schedule(process.raw2digi_step,process.digitisation_step,process.CSCTFunpacker,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step,process.outputstep)

# not working:
#process.schedule = cms.Schedule(process.digitisation_step,process.digi2raw_step,process.raw2digi_step,process.CSCTFunpacker,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step,process.outputstep)

# not working:
#process.schedule = cms.Schedule(process.raw2digi_step,process.digi2raw_step,process.digitisation_step,process.CSCTFunpacker,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step,process.outputstep)

#process.schedule = cms.Schedule(process.raw2digi_step,process.digitisation_step,process.L1simulation_step,process.CSCTFunpacker,process.CSCTFpacker,process.digi2raw_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step,process.outputstep)

process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step,process.outputstep)


# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions

