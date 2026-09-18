import numpy as np

def calibration_episode(seed,n=300,onset=180,degraded=True):
    rng=np.random.default_rng(seed); p=np.full(n,.90)
    drift=np.clip((np.arange(n)-onset)/max(1,n-onset),0,1) if degraded else np.zeros(n)
    true_p=p-.35*drift
    outcome=(rng.random(n)<true_p).astype(float)
    return {"p":p,"outcome":outcome,"residual":outcome-p,"onset":onset}

def trajectory_episode(seed,n=500,onset=220,degraded=True):
    rng=np.random.default_rng(seed); x=np.zeros(n)
    correct=(rng.random(n)<.90).astype(float); confidence=np.full(n,.90)
    for t in range(1,n):
        d=max(0,(t-onset)/max(1,n-onset)) if degraded else 0
        a=.72+.42*d
        decision_noise=(1-correct[t])*rng.choice([-1.,1.])
        x[t]=np.clip(a*x[t-1]+.12*rng.normal()+.035*decision_noise,-20,20)
    return {"x":x,"correct":correct,"confidence":confidence,
            "residual":correct-confidence,"onset":onset}
