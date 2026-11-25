import csv, sys
from datetime import datetime
path = sys.argv[1]
rows=[]
with open(path) as fh:
    lines = fh.read().splitlines()
start = next(i for i,l in enumerate(lines) if l.startswith("Date,Time"))
for r in csv.DictReader(lines[start:]):
    try:
        t = datetime.strptime(r["Date"]+" "+r["Time"], "%m/%d/%Y %I:%M:%S %p")
        rows.append((t, float(r["Internal Temperature (deg F)"]), float(r["Ambient Temperature (deg F)"]), float(r["Tip 1 (deg F)"]), float(r["Tip 4 (deg F)"])))
    except Exception as e:
        pass
print("rows", len(rows), rows[0][0], rows[-1][0])
t0=rows[0][0]
# 15-min table
last=None
print("time  int  amb")
for t,i,a,t1,t4 in rows:
    m=int((t-t0).total_seconds()//60)
    if m%20==0 and m!=last:
        last=m
        print(t.strftime("%H:%M"), f"{i:6.1f} {a:6.1f}")
# peak
pk=max(rows,key=lambda r:r[1]); print("peak", pk[0], pk[1])
# first time internal >=160, 150, 140, 100
for th in (100,130,140,150,155,160,165):
    h=next((r for r in rows if r[1]>=th),None)
    print("first >=",th, h[0].strftime("%H:%M") if h else None)
# last time ambient>150 (cook end)
hot=[r for r in rows if r[2]>=150]
print("ambient>=150 from", hot[0][0].strftime("%H:%M"), "to", hot[-1][0].strftime("%H:%M"))
# ambient phases: average by 30min while hot
import statistics
buck={}
for t,i,a,_,_ in hot:
    k=t.replace(minute=0 if t.minute<30 else 30, second=0)
    buck.setdefault(k,[]).append(a)
for k in sorted(buck): print(k.strftime("%H:%M"), round(statistics.mean(buck[k]),1), round(min(buck[k]),1), round(max(buck[k]),1))
