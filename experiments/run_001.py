import common, json
from pathlib import Path
from src.sim import calibration_episode
from src.detectors import rolling_abs_mean,efmw_residual,cusum_abs,ewma
from src.eval import threshold_from_null,first_alarm,summarize
NN,NT,A=2000,1000,.05
methods={"rolling":lambda e:rolling_abs_mean(e["residual"]),
"ewma":lambda e:abs(ewma(e["residual"])),"cusum":lambda e:cusum_abs(e["residual"]),
"efmw":lambda e:efmw_residual(e["residual"])}
null=[calibration_episode(10000+i,degraded=False) for i in range(NN)]
test=[calibration_episode(50000+i) for i in range(NT)]
r={}
for n,f in methods.items():
    th=threshold_from_null([f(e) for e in null],A)
    al=[first_alarm(f(e),th,e["onset"]) for e in test]
    r[n]={"threshold":th,**summarize(al,test[0]["onset"],NT)}
Path("results").mkdir(exist_ok=True); Path("results/jev_efmw_001.json").write_text(json.dumps(r,indent=2)); print(json.dumps(r,indent=2))
