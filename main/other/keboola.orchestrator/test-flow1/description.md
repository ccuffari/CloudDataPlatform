**TestFlow1** is designed to extract, transform, and load data in a structured sequence of phases, ensuring data integrity and process efficiency.

## Step 1
This phase focuses on data extraction. The task in this phase utilizes the `keboola.ex-onedrive` component to extract data from OneDrive. This is the initial step in the flow, setting the foundation for subsequent data processing.

## Step 2
In this phase, data transformation is performed. The task employs the `keboola.python-transformation-v2` component to transform the extracted data. This step is crucial for preparing the data for loading, ensuring it meets the necessary format and quality standards.

## Step 3
The final phase is dedicated to data loading. The task uses the `keboola.wr-google-bigquery-v2` component to write the transformed data into Google BigQuery. This phase completes the data pipeline, making the data available for analysis and reporting.
