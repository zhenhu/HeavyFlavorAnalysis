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
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/data/Run2018D/MuOnia/AOD/PromptReco-v2/000/325/000/00000/DEC682AE-EB09-654E-9F83-21B10F3381A2.root'
#'/store/data/Run2018A/MuOnia/AOD/PromptReco-v1/000/315/267/00000/420129AE-DC4B-E811-B21A-FA163E42C086.root'
#'/store/data/Run2018D/MuOnia/AOD/PromptReco-v2/000/320/673/00000/0423D458-D497-E811-8871-02163E01A93F.root'
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


process.oniaSelectedMuonsCounter = cms.EDFilter('CandViewCountFilter',
      src = cms.InputTag('oniaSelectedMuons'),
      minNumber = cms.uint32(4),
)

process.BPHSkimSequence = cms.Sequence(process.oniaPATMuonsWithoutTrigger*process.oniaSelectedMuons*process.onia2MuMuPAT*process.onia2MuMuPATCounter*process.oniaSelectedMuonsCounter)

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
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_dataRun2_Prompt_v4', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_v10', '')

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

# Path and EndPath definitions
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.SKIMStreamBPHSkimOutPath = cms.EndPath(process.SKIMStreamBPHSkim)

# Schedule definition
process.schedule = cms.Schedule(process.BPHSkimPath, process.SKIMStreamBPHSkimOutPath)

# Schedule definition
#process.schedule = cms.Schedule(process.BPHSkimPath,process.RECOSIMoutput_step,process.SKIMStreamBPHSkimOutPath)
#from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
#associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
#from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
#process = customiseEarlyDelete(process)
# End adding early deletion

