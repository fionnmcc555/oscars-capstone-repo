# Project Requirements

## Goal  
Create an ETL pipeline for the Oscar Awards dataset and deliver a Streamlit application showcasing insights.

The CEOs of the Oscars have approached us with a requirement to create a dataset that their data analysts can work with, to help build an application that shows trends and insights from the Oscar Awards spanning 1927 to the present.

They require an ETL pipeline that extracts Oscars data from the Pagila database, then cleans and transforms it to produce an enriched dataset. Additionally, they want an interactive dashboard-style application that displays statistics and visualisations from the dataset. This will allow the company to better understand their data and evaluate whether they are being representative enough in selecting their winners.

---

## Epic 0 – Project Statement
**As a customer**, I want a working ETL pipeline that extracts, cleans, standardises, and transforms Oscar Awards data from a SQL source, and then loads the data into an interactive Streamlit application **so that I can interactively filter categories, years, and people to discover patterns**.

---

## Epic 1 – Extract
**Epic:** As a data analyst, I want to be able to access the Oscar Awards dataset, so that it can be enriched for analysis.

- **User Story 1:** As a data analyst, I want to extract Oscars data from the Pagila database, so that it can be transformed and prepared for analysis.  
  **Acceptance Criteria:**  
  - The extraction process connects successfully to the Pagila database.  
  - Raw data is saved in the `/data/raw` folder in CSV format with timestamped file names.  
  - Column names and row counts are logged after extraction.

---

## Epic 2 – Transform
**Epic:** As a data analyst, I want to be able to access clean, standardised, and enriched data, so that it is ready to be used for analysis.

- **User Story 3:** As a data analyst, I want the Oscars data to have consistent formats for dates and categories, so that I can run accurate queries.  
  **Acceptance Criteria:**  
  - All date fields are in `YYYY-MM-DD` format.  
  - Award category names follow a consistent naming convention.

- **User Story 4:** As a data analyst, I want duplicate data removed, so that the analysis is based on reliable information.  
  **Acceptance Criteria:**  
  - No duplicate award entries exist in the transformed dataset.  
  - Row counts before and after deduplication are documented.

- **User Story 5:** As a data analyst, I want to create new derived columns, so that I can infer more enriched insights.  
  **Acceptance Criteria:**  
  - At least one new derived column is added (e.g., `Decade` or `Award_Type`).  
  - New column values are verified against sample records.

---

## Epic 3 – Load
**Epic:** As a data analyst, I want to be able to access the curated dataset in a single, queryable SQL table, so that analysis on Oscars trends can be done more easily.

- **User Story 6:** As a data analyst, I want the cleaned, transformed data to be available in a single SQL table, so that it can be analysed efficiently.  
  **Acceptance Criteria:**  
  - A table named `oscars_curated` exists in the database.  
  - All transformed records are loaded without errors.  
  - Querying the table returns results within 2 seconds on local hardware.

---

## Epic 4 – Insights & Visualisation
**Epic:** As a data analyst, I want to use the enriched data to generate clear insights and trends.

- **User Story 7:** As the customer, I want a Streamlit application showcasing transformed Oscars data, so that I can view trends and insights at a glance.  
  **Acceptance Criteria:**  
  - Streamlit app loads without errors.  
  - At least 3 visualisations (e.g., bar chart, line chart, pie chart) are available.  
  - Titles, labels, and legends are clear and accurate.

- **User Story 8:** As a film industry stakeholder, I want to be able to filter and compare Oscars data by category, year, and nominee demographics in the Streamlit app, so that I can assess representation and diversity over time.  
  **Acceptance Criteria:**  
  - Filter controls for category, year, and demographics exist and work correctly.  
  - Charts and tables update dynamically when filters are applied.  
  - At least one chart visualises diversity or representation trends.