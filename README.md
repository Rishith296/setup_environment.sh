# German Weather Big Data ML Pipeline

## Predicting Precipitation Events in Germany Using Machine Learning

### Project Overview
This project applies Big Data machine learning techniques to predict precipitation
events across Germany using historical hourly weather observations from the German
Weather Service (Deutscher Wetterdienst — DWD) Climate Data Center (CDC).

The pipeline demonstrates end-to-end Big Data processing: Spark-based ingestion,
Parquet storage, distributed feature engineering, PySpark MLlib model training,
uncertainty quantification, scalability analysis, and Tableau visualization.

### Dataset
- **Source**: DWD Climate Data Center (CDC) — German Federal Government Open Data
- **URL**: https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/
- **Size**: >1GB (combined hourly observations across 500+ stations, 8 parameters)
- **Features**: 15+ meteorological variables (temperature, humidity, wind, pressure, etc.)
- **Target**: Binary — has_precipitation (1 if precipitation > 0mm, else 0)
- **License**: Open Data — freely available for all purposes (DWD Terms of Use)
- **NOT Kaggle**: German government official source

### Project Structure
german-weather-bigdata-ml/
├── notebooks/ # Jupyter notebooks
│ ├── 1_data_ingestion.ipynb
│ ├── 2_feature_engineering.ipynb
│ ├── 3_model_training.ipynb
│ └── 4_evaluation.ipynb
├── tableau/ # Tableau dashboard files
├── scripts/ # Pipeline scripts
├── config/ # Spark and Tableau configuration
├── data/ # Schemas and samples
├── tests/ # Unit tests
├── results/ # Figures, models, metrics
├── docs/ # Documentation
├── environment.yml # Conda environment
├── Dockerfile # Container setup
└── README.md

text


### Algorithms Implemented
| # | Algorithm                  | Framework          | Role                    |
|---|----------------------------|--------------------|-------------------------|
| 1 | Logistic Regression        | PySpark MLlib      | Interpretable baseline  |
| 2 | Random Forest              | PySpark MLlib      | Bagging ensemble        |
| 3 | Gradient-Boosted Trees     | PySpark MLlib      | Boosting ensemble       |
| 4 | Support Vector Machine     | scikit-learn       | Single-node baseline    |

### Quick Start
1. All data accessed online — no local download needed

### Links
- **Github  [https://github.com/Rishith296/setup_environment.sh.git]
- **Tableau Public**: [https://public.tableau.com/app/profile/s.a2263/viz/GermanWeatherBigDataMLPipeline/Dashboard2?publish=yes]

### Author
[Karmudi Rishith Reddy] — [ID-16718535]
Coventry University — 7006SCN Machine Learning and Big Data
