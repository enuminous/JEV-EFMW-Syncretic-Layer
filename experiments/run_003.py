import common, json, numpy as np
from pathlib import Path
from src.sim import trajectory_episode
from src.detectors import trajectory_ewma,cusum_abs,page_hinkley,energy
from src.eval import threshold_from_null,first_alarm,summarize
NN,NT,A=3000,2000,.05
null=[trajectory_episode(300000+i,degraded=False) for i in range(NN)]
b=float(np.mean([np.mean(e["x"][:e["onset"]]**2) for e in null]))
test=[trajectory_episode(400000+i) for i in range(NT)]
methods={"efmw_recursive_energy":lambda e:trajectory_ewma(e["x"],b,.97),
"trajectory_ewma_090":lambda e:trajectory_ewma(e["x"],b,.90),
"trajectory_ewma_099":lambda e:trajectory_ewma(e["x"],b,.99),
"energy_cusum":lambda e:cusum_abs(energy(e["x"],b),.01),
"page_hinkley_energy":lambda e:page_hinkley(energy(e["x"],b))}
r={"baseline_variance":b,"methods":{}}
for n,f in methods.items():
    th=threshold_from_null([f(e) for e in null],A); al=[first_alarm(f(e),th,e["onset"]) for e in test]
    r["methods"][n]={"threshold":th,**summarize(al,test[0]["onset"],NT)}
Path("results").mkdir(exist_ok=True); Path("results/jev_efmw_003.json").write_text(json.dumps(r,indent=2)); print(json.dumps(r,indent=2))
