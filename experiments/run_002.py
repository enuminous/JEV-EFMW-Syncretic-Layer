import common, json, numpy as np
from pathlib import Path
from src.sim import trajectory_episode
from src.detectors import rolling_abs_mean,cusum_abs,trajectory_ewma
from src.eval import threshold_from_null,first_alarm,summarize
NN,NT,A=3000,2000,.05
null=[trajectory_episode(100000+i,degraded=False) for i in range(NN)]
b=float(np.mean([np.mean(e["x"][:e["onset"]]**2) for e in null]))
test=[trajectory_episode(200000+i) for i in range(NT)]
methods={"rolling_calibration":lambda e:rolling_abs_mean(e["residual"]),
"decision_cusum":lambda e:cusum_abs(e["residual"]),
"efmw_trajectory":lambda e:trajectory_ewma(e["x"],b,.97)}
r={"baseline_variance":b,"methods":{}}
for n,f in methods.items():
    th=threshold_from_null([f(e) for e in null],A); al=[first_alarm(f(e),th,e["onset"]) for e in test]
    r["methods"][n]={"threshold":th,**summarize(al,test[0]["onset"],NT)}
Path("results").mkdir(exist_ok=True); Path("results/jev_efmw_002.json").write_text(json.dumps(r,indent=2)); print(json.dumps(r,indent=2))
