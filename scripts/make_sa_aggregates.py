import csv, datetime as dt
from collections import defaultdict

SRC = "data/a-validations-2021Q1.csv"
OUT_MONTH = "data/sa-monthly-mode-share.csv"
OUT_HEAT = "data/sa-weekday-heat.csv"

def parse_date(s):
    for fmt in ("%d/%m/%Y","%-d/%-m/%Y","%Y-%m-%d"):
        try: return dt.datetime.strptime(s, fmt).date()
        except: pass
    return None

def get_date(row):
    for k in ("VALIDATION_DATE","Validation Date","validation_date","Date","date"):
        if k in row and row[k]: return parse_date(row[k])
    return None

def get_count(row):
    for k in ("BAND_BOARDINGS_FLOOR","band_boardings_floor","BOARDINGS","Validations"):
        if k in row and row[k]:
            try: return int(float(row[k]))
            except: return 0
    return 0

def get_mode(row):
    # NUM_MODE_TRANSPORT: 1=Bus, 5=Train, 4=Tram (per your notes)
    v = row.get("NUM_MODE_TRANSPORT","")
    try: v = int(v)
    except: return "Other"
    return {1:"Bus",5:"Train",4:"Tram"}.get(v,"Other")

monthly = defaultdict(int)
heat = defaultdict(int)

with open(SRC, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        d = get_date(row)
        if not d: continue
        c = get_count(row)
        if c <= 0: continue
        m = get_mode(row)

        ym = f"{d.year:04d}-{d.month:02d}"
        monthly[(ym,m)] += c

        # weeks W1..W13 within Q1 2021 (Mon..Sun = 0..6 as Mon-first)
        q1_start = dt.date(2021,1,1)
        week = ((d - q1_start).days // 7) + 1
        week = max(1, min(13, week))
        dow = d.weekday()  # 0=Mon .. 6=Sun
        heat[(week,dow)] += c

# Write monthly by mode
with open(OUT_MONTH,"w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["month","mode","validations"])
    for (month,mode),v in sorted(monthly.items()):
        if mode in ("Bus","Train","Tram"):
            w.writerow([month,mode,v])

# Write weekday heat
with open(OUT_HEAT,"w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["week","dow","validations"])
    for (week,dow),v in sorted(heat.items()):
        w.writerow([week,dow,v])

print("Done. Now delete the big CSV to meet the <1 MB rule.")
