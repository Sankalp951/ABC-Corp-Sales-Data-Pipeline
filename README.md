# ABC-Corp-Sales-Data-Pipeline in Google Cloud

Automated Data Pipeline for Global Sales Data on Google Cloud Platform (GCP). This repository contains an automated data pipeline designed to process and analyze global sales data using Google Cloud Platform (GCP) services. The pipeline integrates data ingestion, transformation, and visualization to provide comprehensive sales insights.

## Table of Contents
- [Project Description](#project-description)
- [Looker Studio Project Output](#looker-studio-project-output)
- [Project Architecture Diagram](#project-architecture-diagram)
- [Technical Stack](#technical-stack)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)

## Project Description

- **Technology Stack**: 
  - Python
  - Flask
  - Google Cloud Platform (GCP)
  - BigQuery
  - Looker Studio

- **Web Portal**:
  - Developed using Python and Flask.
  - Allows uploading of sales data files from multiple regions (EMEA, APAC, NA).

- **Storage**:
  - Uploaded files are stored in a Google Cloud Storage bucket.

- **Data Processing**:
  - A Cloud Function is triggered upon file upload.
  - The Cloud Function extracts data from the files.
  - Extracted data is loaded into a BigQuery dataset.

- **Reporting and Visualization**:
  - Looker Studio is used for reporting purposes.
  - Provides data visualization through graphs and charts.
  - Supports filtering and dropdown capabilities for dynamic data interaction.

## Looker Studio Project Output

![Page 1](https://github.com/Sankalp951/ABC-Corp-Sales-Data-Pipeline/assets/137797143/66f26f81-3033-4de1-9ff2-e3781915127a)

![Page 2](https://github.com/Sankalp951/ABC-Corp-Sales-Data-Pipeline/assets/137797143/6774f1f5-3c73-4f3f-85c4-59b79130187a)

## Project Architecture Diagram 

![Project Architecture - Sales Data Pipeline](https://github.com/Sankalp951/ABC-Corp-Sales-Data-Pipeline/assets/137797143/83429fcc-e846-45ce-ab19-5ef9d4256a2a)

## Technical Stack

![Technical Stack](https://github.com/Sankalp951/ABC-Corp-Sales-Data-Pipeline/assets/137797143/3312154c-d425-4558-80f4-c83e92f31401)

## Prerequisites

- **For the sales dataset, please visit Kaggle.com and download any publicly accessible dataset free of charge.**

- **Google Cloud SDK (gcloud SDK)**:
  - Required to run the project on your local system.
  - Follow the [installation guide](https://cloud.google.com/sdk/docs/install) to set up gcloud SDK on your machine.
  - Make sure to authenticate with your GCP account:
    ```bash
    gcloud auth login
    gcloud config set project YOUR_PROJECT_ID
    ```

## Setup and Installation

1. **Clone the repository**
2. **Install the required Python packages**
3. **Set up environment variables or GCP credentials, bucket names, etc.**

   
