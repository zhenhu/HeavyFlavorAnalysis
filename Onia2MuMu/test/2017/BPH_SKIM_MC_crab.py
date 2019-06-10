# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: skims -s SKIM:BPHSkim --dasquery=file dataset=/Charmonium/Run2016B-PromptReco-v1/AOD -n -1 --data --conditions auto:com10 --python_filename=crab-skim.py --processName=BPHSkim --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('BPHSkim')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.Skims_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'file:/eos/uscms/store/user/l1upgrades/TVP_13/TVP13_LHE_RECO_01/TVPMC_13/MC_TVP13_LHE_RECO_01/180523_204705/0000/BPH_RECO_13TeV_4.root'
#'root://cms-xrd-global.cern.ch//store/mc/Summer12DR53X/FourMuon_UpsilonInvMassCut_MSEL5_8TeV_pythia6/AODSIM/PU_RD2_START53_V19F_ext1-v1/00000/02BD8C8E-B90F-E711-A21B-FA163E180050.root',
#'/store/mc/RunIISummer17DRStdmix/UpsilonMuMu_UpsilonPt6_TuneCUEP8M1_13TeV-pythia8-evtgen/AODSIM/NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/00000/0059AB5D-9FBA-E711-B0C0-0025905B8568.root',
#'/store/mc/RunIISummer17DRStdmix/H0ToUps1SMuMu_m18p5_TuneCUEP8M1_13TeV-pythia8/AODSIM/NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/150000/0C5DF8BB-8FAA-E711-9A73-0CC47AD98C5E.root',
#'/store/mc/RunIISummer17DRStdmix/H0ToUps1SMuMu_m18p5_TuneCUEP8M1_13TeV-pythia8/AODSIM/NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/150000/1000B701-B1AB-E711-A68E-008CFAC93BAC.root',
#'root://cms-xrd-global.cern.ch//store/data/Run2017D/MuOnia/AOD/PromptReco-v1/000/302/031/00000/06A5FA59-418F-E711-9F75-02163E0139C0.root'
	 ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('skims nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('skims_SKIM.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)


#process.oniaSelectedMuonsCounter = cms.EDFilter('CandViewCountFilter',
#      src = cms.InputTag('oniaSelectedMuons'),
#      minNumber = cms.uint32(4),
#)

process.BPHSkimSequence = cms.Sequence(process.oniaPATMuonsWithoutTrigger*process.oniaSelectedMuons*process.onia2MuMuPAT*process.onia2MuMuPATCounter)
#process.BPHSkimSequence = cms.Sequence(process.oniaPATMuonsWithoutTrigger*process.oniaSelectedMuons*process.onia2MuMuPAT*process.onia2MuMuPATCounter*process.oniaSelectedMuonsCounter)

# Additional output definition
process.SKIMStreamBPHSkim = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('BPHSkimPath')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('USER'),
        filterName = cms.untracked.string('BPHSkim')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('BPHSkim.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep recoVertexs_offlinePrimaryVertices_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_TriggerResults_*_HLT', 
#        'keep *_hltGtStage2ObjectMap_*_HLT', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep recoGenParticles_genParticles_*_*',
		  'keep patPackedGenParticles_packedGenParticles_*_*',
		  'keep recoGenParticles_prunedGenParticles_*_*',
#        'keep *_gmtStage2Digis_Muon_RECO', 
#        'keep *_gtDigis_*_RECO', 
#        'keep *_oniaSelectedTracks_*_*', 
#        'keep *_oniaPhotonCandidates_*_*', 
        'keep *_oniaPATMuonsWithoutTrigger_*_*',
		  'keep *_oniaSelectedMuons_*_*',
#		  'keep *_patMuons_*_*',
		  'keep *_onia2MuMuPAT_*_*', 
 #       'keep *_oniaV0Tracks_*_*', 
        'keep PileupSummaryInfos_*_*_*')
)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:com10', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '94X_dataRun2_ReReco_EOY17_v2', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v10', '')

process.load('PhysicsTools.PatAlgos.slimming.genParticles_cff')
process.packedGenParticles.inputVertices = cms.InputTag('offlinePrimaryVertices')

process.oniaSelectedMuons.cut = cms.string('muonID(\"TMOneStationTight\")'
                    ' && abs(innerTrack.dxy) < 0.3'
                    ' && abs(innerTrack.dz)  < 20.'
                    ' && innerTrack.hitPattern.trackerLayersWithMeasurement > 5'
                    ' && innerTrack.hitPattern.pixelLayersWithMeasurement > 0'
                    ' && innerTrack.quality(\"highPurity\")'
                    ' && (abs(eta) <= 2.4 && pt > 2.0)'
)

#process.onia2MuMuPAT.muons=cms.InputTag('oniaPATMuonsWithoutTrigger')
process.onia2MuMuPAT.higherPuritySelection = cms.string("(isGlobalMuon || isTrackerMuon || (innerTrack.isNonnull && genParticleRef(0).isNonnull)) && abs(innerTrack.dxy)<4 && abs(innerTrack.dz)<35 && muonID('TrackerMuonArbitrated')")
process.onia2MuMuPAT.lowerPuritySelection = cms.string("(isGlobalMuon || isTrackerMuon || (innerTrack.isNonnull && genParticleRef(0).isNonnull)) && abs(innerTrack.dxy)<4 && abs(innerTrack.dz)<35 && muonID('TrackerMuonArbitrated')")

#process.onia2MuMuPAT.higherPuritySelection = cms.string("")
#process.onia2MuMuPAT.lowerPuritySelection = cms.string("")

process.onia2MuMuPAT.addMCTruth = cms.bool(True)

# Path and EndPath definitions
process.genTask_step = cms.Path(process.genParticlesTask)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.SKIMStreamBPHSkimOutPath = cms.EndPath(process.SKIMStreamBPHSkim)

# Schedule definition
#process.schedule = cms.Schedule(process.BPHSkimPath, process.SKIMStreamBPHSkimOutPath)
process.schedule = cms.Schedule(process.genTask_step, process.BPHSkimPath, process.SKIMStreamBPHSkimOutPath)

# Schedule definition
#process.schedule = cms.Schedule(process.BPHSkimPath,process.RECOSIMoutput_step,process.SKIMStreamBPHSkimOutPath)
#from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
#associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
#from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
#process = customiseEarlyDelete(process)
# End adding early deletion

