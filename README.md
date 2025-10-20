The PT Line — An Australian Commuting Story (FIT3179 DV2)

Author: Muhammad Mohid Khanzada
Student ID: 33891095

This project is an interactive data story exploring Australian public transport commuting and operational patterns, created using Vega-Lite. It serves as my Data Visualisation 2 submission and is on a distinctly different domain from my DV1 project.

Project Narrative & Munzner's Framework

The visualisation follows a narrative structure, taking the user from a high-level national overview down to specific operational details, framed as a journey along a metro line.

What (Data): The project synthesises multiple datasets to build a comprehensive picture.

Commuting Patterns: ABS 2021 Census (Method of Travel to Work) data for state-level percentages and the national mode split.

Geography: Australian state boundaries from Natural Earth, simplified to TopoJSON format for web performance.

Infrastructure Proxy: A derived dataset of public transport stop/station counts per state from publicly available GTFS feeds. This provides a proxy for infrastructure density when combined with ABS Estimated Resident Population (ERP) data.

Operational Data (Victoria): Monthly patronage figures from Public Transport Victoria, showing trends over time.

Operational Data (South Australia): Anonymised Metrocard validation counts for Q1 2021, revealing daily and weekly usage rhythms.

Why (Tasks & Insights): The primary goal is to tell an engaging story that helps an average Australian understand public transport usage patterns across the country. Key tasks for the user include:

Compare states to see which have higher or lower PT uptake.

Identify geographic concentrations of PT usage.

Understand the composition of the national PT network (i.e., which modes are most common).

Explore the relationship between infrastructure density and actual ridership.

Discover real-world usage patterns through operational data, such as the impact of the pandemic or typical weekday rhythms.

How (Idioms & Enhancements): A range of carefully selected Vega-Lite idioms are used to effectively encode the data.

Comparison: Lollipop and Diverging Bar Charts to rank states and show deviation from the mean.

Geography: A Choropleth Map to show spatial distribution.

Composition: A horizontal Bar Chart for a clear, accessible comparison of national mode share.

Relationship: A Scatter Plot with a regression line and annotated points to explore the link between infrastructure and uptake.

Time-Series & Trends: A Multi-Series Line Chart for Victorian patronage and a Heatmap for Adelaide's weekly tap data.

Part-to-Whole: A 100% Stacked Bar Chart to show the monthly mode mix in Adelaide.

Annotations: Key charts are annotated directly to highlight significant data points (e.g., pandemic impact, outlier states), guiding the user towards insights.

Design & Implementation Notes

Web Performance: All data files have been optimised to keep the total download size under 1MB for a fast user experience. The au-states.json TopoJSON file is simplified, and CSVs contain only necessary columns.

Accessibility & Theming: The design features a high-contrast colour palette that adapts to both light and dark system modes. The typography uses the 'Inter' font for excellent readability. Semantic colours are used consistently for different transport modes across the page and charts.

Live Page: The project is hosted on GitHub Pages. All Vega-Lite specifications are in the /spec directory and data is in /data. Each visualisation includes a button to view the underlying JSON spec.

Design Process: The final design is the result of an iterative process documented in Five Design Sheets (FDS), which are available separately. The narrative evolved from a simple collection of charts to a cohesive, themed story.

Data Sources & Licensing

ABS Census 2021 (MTWP) & ABS ERP Dec-2021: Attribution required.

Natural Earth Admin-1: Public domain.

GTFS Feeds: Sourced from VIC (DataVic), QLD (Translink), SA (data.sa.gov.au), WA (Transperth).

Victorian Patronage: Vic DTP “Monthly public transport patronage by mode” CSV.

Adelaide Validations 2021 Q1: CC BY licence.