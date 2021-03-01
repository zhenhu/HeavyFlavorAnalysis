# Skim for UL
```
cmsrel CMSSW_10_6_20
cd CMSSW_10_6_20/src/
cmsenv
git clone https://github.com/zhenhu/HeavyFlavorAnalysis
scram b
cd HeavyFlavorAnalysis
cd Onia2MuMu/test/UL/
voms-proxy-init -voms cms --valid 172:00
```
To skim MC events, first run local test with
```
cmsRun BPH_SKIM_UL_MC2018.py
cmsRun BPH_SKIM_UL_MC2017.py
cmsRun BPH_SKIM_UL_MC2016.py
cmsRun BPH_SKIM_UL_MC2016preVFP.py

```
, then submit crab jobs with your self-written crab config.

To skim data events, first run local test with
```
cmsRun BPH_SKIM_UL_data.py
```
, then submit crab jobs with your self-written crab config.

# Skim for 2017
```
cmsrel CMSSW_9_4_2
cd CMSSW_9_4_2/src/
cmsenv
git clone https://github.com/zhenhu/HeavyFlavorAnalysis
scram b
cd HeavyFlavorAnalysis
cd Onia2MuMu/test/2017
voms-proxy-init -voms cms --valid 172:00
```
To skim MC events, first run local test with
```
cmsRun BPH_SKIM_MC_crab.py
```
, then submit crab jobs with your self-written crab config. 

To skim data events, first run local test with
```
cmsRun BPH_SKIM_crab_2017.py
```
, then submit crab jobs using either your self-written crab config or the multicrab tool below:
```
./multicrab_2017 --crabCmd=submit
./multicrab_2017_MinBias --crabCmd=submit
```

Following script will loop over all jobs within director (crabOutput2017_)  and will keep resubmitting failing jobs after every 30 mints
```
nohup python manageCrabTask.py -l -r -t crabOutput2017_ >& crabOutput2017_.log &
```

# Skim for 2018
```
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src
cmsenv
git clone https://github.com/zhenhu/HeavyFlavorAnalysis
scram b 
cd HeavyFlavorAnalysis
cd Onia2MuMu/test/2018
voms-proxy-init -voms cms --valid 172:00
```
To skim MC events, first run local test with
```
cmsRun BPH_SKIM_MC_crab.py
```
, then submit crab jobs with your self-written crab config. 

To skim data events, first run local test with
```
cmsRun BPH_SKIM_crab_2018ABC.py
cmsRun BPH_SKIM_crab_2018D.py
```
,  then submit crab jobs using either your self-written crab config or the multicrab tool below:
```
./multicrab_2018ABC --crabCmd=submit
./multicrab_2018D --crabCmd=submit
./multicrab_2018ABC_MinBias --crabCmd=submit
./multicrab_2018D_MinBias --crabCmd=submit
```

Following script will loop over all jobs within director (crabOutput2018ABC_)  and will keep resubmitting failing jobs after every 30 mints
```
nohup python manageCrabTask.py -l -r -t crabOutput2018ABC_ >& crabOutput2018ABC_.log &
```

# Skim for 2016
```
cmsrel CMSSW_8_0_31
cd CMSSW_8_0_31/src/
cmsenv
git clone https://github.com/zhenhu/HeavyFlavorAnalysis
scram b
cd HeavyFlavorAnalysis
cd Onia2MuMu/test/2016
voms-proxy-init -voms cms --valid 172:00
```
To skim MC events, first run local test with
```
cmsRun BPH_SKIM_MC_crab.py
```
, then submit crab jobs with your self-written crab config.

To skim data events, first run local test with
```
BPH_SKIM_crab_2016.py
```
,  then submit crab jobs using either your self-written crab config or the multicrab tool below:
```
./multicrab_2016 --crabCmd=submit
```

Following script will loop over all jobs within director (crabOutput2016_)  and will keep resubmitting failing jobs after every 30 mints
```
nohup python manageCrabTask.py -l -r -t crabOutput2016_ >& crabOutput2016_.log &
```
