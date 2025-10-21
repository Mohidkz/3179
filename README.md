The PT Line — An Australian Commuting Story (FIT3179 DV2)

Author: Muhammad Mohid Khanzada

Student ID: 33891095

This project is an interactive data story exploring Australian public transport commuting and operational patterns, created using Vega-Lite. It serves as my Data Visualisation 2 submission and is on a distinctly different domain from my DV1 project.

Project Narrative & Munzner's Framework

The visualisation follows a narrative structure, taking the user on a themed journey along a metro line. Each "station" stops at a key part of the story, moving from a high-level national overview down to specific, real-world operational details.

What (Data): The project synthesises multiple datasets to build a comprehensive picture:

Commuting Patterns: ABS 2021 Census data provides the foundation with state-level percentages and the national mode split.

Geography: Australian state boundaries from Natural Earth provide the geographic context for the map.

Infrastructure Proxy: We created a measure of infrastructure density by counting public transport stops/stations from official GTFS data and combining it with ABS population data.

Operational Data: Real-world usage is shown through monthly patronage figures from Public Transport Victoria and anonymised smartcard validation data from Adelaide Metro for 2021.

Why (Tasks & Insights): The primary goal is to help an average Australian understand public transport usage patterns across the country. Key questions the user can answer include:

Which states have the highest and lowest public transport uptake?

Where are most PT users located geographically?

What are the most common modes of transport nationally?

Is there a link between the amount of infrastructure and the number of riders?

How do real-world events (like a pandemic) or weekly rhythms (work vs. weekend) affect usage?

How (Idioms & Rationale): A range of carefully selected Vega-Lite idioms are used to effectively tell the story:

Lollipop & Diverging Bar Charts: Chosen to clearly rank states and powerfully visualise their deviation from the national average.

Choropleth Map: The most effective idiom for showing how a value (PT usage) is distributed across geographic regions.

Scatter Plot with Regression Line: Used to clearly investigate the relationship between two continuous variables: infrastructure density and ridership.

Line Chart & Heatmap: These idioms are ideal for showing trends over time. The line chart tracks Victoria's post-pandemic recovery, while the heatmap reveals the strong weekly commuting rhythm in Adelaide.

100% Stacked Bar Chart: This is used to show the changing proportion of each transport mode's contribution to Adelaide's total usage over several months.

Design & Implementation Notes

Web Performance: All data files have been optimised to keep the total download size under 1MB for a fast user experience.

Accessibility & Theming: The design features a high-contrast colour palette that adapts to both light and dark system modes. The typography uses the 'Inter' font for excellent readability.

Live Page: The project is hosted on GitHub Pages. All Vega-Lite specifications are in the /spec directory and data is in /data.

Data Sources & Licensing

ABS Census 2021 (MTWP) & ABS ERP Dec-2021: Attribution required.

Natural Earth Admin-1: Public domain.

GTFS Feeds: Sourced from VIC (DataVic), QLD (Translink), SA (data.sa.gov.au), WA (Transperth).

Victorian Patronage: Vic DTP “Monthly public transport patronage by mode” CSV.

Adelaide Validations 2021: Sourced from data