# PT Line — How Australians Commute (DV2)

**Author:** Muhammad Mohid Khanzada  
**Student ID:** 33891095

Public transport commuting & operations in Australia using **Vega-Lite**. This DV2 project is **distinct from DV1**.

- **DV1 domain:** _[replace with your DV1 topic]_  
- **DV2 domain:** Public transport commuting & operations (ABS 2021 + VIC patronage + SA validations) with a GTFS-derived infrastructure proxy.

## What / Why / How (Munzner)

- **What (Data):**  
  ABS 2021 MTWP (state % & national mode split), Natural Earth Admin-1 (TopoJSON), GTFS stops by state (deduped via `COALESCE(parent_station, stop_id)` → stops per 100k), VIC monthly patronage (2018–2025), Adelaide Metrocard banded validations (2021 Q1).  
- **Why (Tasks):**  
  Compare state PT shares; locate geography; summarise national modes; relate access (stops/100k) to uptake; inspect temporal/weekday usage.  
- **How (Idioms):**  
  Lollipop + divergence; choropleth + waffles; donut; scatter + regression; multi-series line; 100% stacked bars; weekday heatmap.

## Live Page

- Hosted via **GitHub Pages** (Settings → Pages → Source: `main`, root).  
- All **Vega-Lite JSON** are in `/spec`, data are in `/data`. Each chart links to its spec (“View JSON”).

## Data Weight

- Designed to load fast: total downloadable data target < **1 MB**.  
  If you exceed this, simplify `au-states.json` with mapshaper and trim unused CSV columns, or note tutor approval.

## Design Process

- **Five Design Sheets (FDS):** scans in `/design/`.  
- Highlights: early focus on static snapshot → final storyboard spans snapshot → geography → composition → access vs uptake → operations.

## Sources & Licenses (short)

- **ABS Census 2021 (MTWP)** & **ABS ERP Dec-2021** — attribution.  
- **Natural Earth Admin-1** — public domain.  
- **GTFS** static feeds: VIC (DataVic), QLD (Translink), SA (data.sa.gov.au), WA (Transperth).  
- **VIC patronage**: Vic DTP CSV.  
- **Adelaide validations 2021 Q1**: CC BY (band floors).

## Reproduce

1. Open `index.html` directly or serve statically (no build step).  
2. Ensure `data/au-states.json` TopoJSON `objects` key matches the `"feature"` in `spec/au-pt-map.json` (default: `states`).  
3. Hard refresh if caching interferes (Ctrl/Cmd+Shift+R).

