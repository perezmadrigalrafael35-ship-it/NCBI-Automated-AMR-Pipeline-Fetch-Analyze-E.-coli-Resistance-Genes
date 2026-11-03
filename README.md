# NCBI Automated AMR Pipeline: Fetch & Analyze E. coli Resistance Genes

## Overview
This repository contains an automated bioinformatics pipeline designed to retrieve, process, and analyze Antimicrobial Resistance (AMR) data from the NCBI database. 

The project is divided into two main scripts:
1. **Data Retrieval:** Connects to the NCBI E-utilities API to fetch specific resistance genes (e.g., `blaCTX-M` in *E. coli*) and saves the data into a structured CSV file.
2. **Data Analysis & Visualization:** Uses `pandas` to clean the dataset and `matplotlib` to generate comparative visualizations of the retrieved gene sequences.

## Use Case
This pipeline is a foundational tool for epidemiological surveillance and bioinformatics. It demonstrates the ability to bridge clinical microbiology with data automation and analysis.

## Technologies Used
* **Python 3**
* **Biopython** (NCBI API connection)
* **Pandas** (Data cleaning and manipulation)
* **Matplotlib** (Data visualization)

## How to Run
1. Ensure you have the required libraries installed:
   `pip install biopython pandas matplotlib`
2. Run the retrieval script: `python descarga_masiva_amr.py`
3. Run the analysis script: `python analisis_amr.py`
4. The scripts will generate a `datos_amr_ecoli.csv` file and a visualization image.
## Data Visualization

Below is the comparative analysis of the retrieved *blaCTX-M* resistance genes, after filtering out whole-genome outliers:

![AMR Gene Lengths](Fifure_1.png)
