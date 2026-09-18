import numpy as np
def threshold_from_null(stats,alpha=.05):
    return float(np.quantile([np.max(s) for s in stats],1-alpha))
def first_alarm(stat,threshold,onset):
    q=np.flatnonzero(np.asarray(stat)[onset:]>threshold)
    return None if len(q)==0 else int(onset+q[0])
def summarize(alarms,onset,total):
    d=[a-onset for a in alarms if a is not None]
    return {"episodes":total,"detections":len(d),"detection_rate":len(d)/total,
            "median_delay":None if not d else float(np.median(d))}
