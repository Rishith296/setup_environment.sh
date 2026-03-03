# Tableau Dashboards — German Weather ML Pipeline

## Tableau Public Link
**[TO BE ADDED AFTER PUBLICATION]**

---

## Dashboard 1: Data Quality & Pipeline Monitoring

### Purpose
Monitor data ingestion, validate quality, track pipeline performance.

### Visualizations
- **Missing Values Heatmap**: Features × Stations showing missing rates
- **Feature Distributions**: Histograms for temperature, humidity, wind, pressure
- **Pipeline Stage Timing**: Bar chart showing duration of each stage
- **Data Coverage Map**: Germany map showing station coverage and data availability
- **KPI Cards**: Total rows, stations, date range, overall quality score

### LOD Expressions
// Rows per station
{ FIXED [station_id] : COUNTD([datetime]) }

// Missing rate per feature
{ FIXED [feature_name] : AVG([is_missing]) }

text


### Filters
- Date range selector
- Station ID multi-select
- Bundesland (state) dropdown

---

## Dashboard 2: Model Performance & Feature Importance

### Purpose
Compare model performance, understand feature contributions, validate results.

### Visualizations
- **ROC Curves**: Overlaid curves for all 4 models
- **Metrics Comparison**: Grouped bar chart (AUC, Accuracy, F1, Precision, Recall)
- **Confusion Matrices**: Side-by-side for each model (with parameter to select)
- **Feature Importance**: Horizontal bar chart (top 15 features)
- **Learning Curves**: Line chart showing accuracy vs training size
- **Bootstrap Confidence Intervals**: Error bars on AUC estimates

### Parameters
- `select_model`: Dropdown to choose which model's confusion matrix to display
- `select_metric`: Choose primary metric for ranking

### Annotations
- "GBT achieves highest AUC at 0.XX"
- "Humidity and pressure are top predictors"

---

## Dashboard 3: Business Insights & Recommendations

### Purpose
Translate ML results into actionable geographic and temporal insights.

### Visualizations
- **Germany Map**: Station locations colored by prediction accuracy
- **Seasonal Heatmap**: Month × Hour showing precipitation probability
- **Threshold Optimization Curve**: Precision/Recall/F1/Profit vs threshold
- **Regional Performance**: Bar chart by Bundesland
- **Recommendations Table**: Sector-specific advice (agriculture, energy, transport)

### Parameters
- `select_threshold`: Slider (0.1 to 0.9) to adjust decision threshold
- `select_season`: Filter by season

### Annotations
- "Optimal threshold: 0.XX maximizes expected value"
- "Southern stations show higher accuracy"
- "Morning hours have highest precipitation uncertainty"

---

## Dashboard 4: Scalability & Cost Analysis

### Purpose
Analyze computational performance, justify Big Data approach.

### Visualizations
- **Strong Scaling Chart**: Training time vs data size (fixed resources)
- **Weak Scaling Chart**: Training time vs number of cores
- **Memory Usage**: Bar chart per algorithm
- **MLlib vs sklearn Comparison**: Grouped bar at different sample sizes
- **Cost-Performance Scatter**: X=time, Y=AUC, size=memory

### Annotations
- "MLlib outperforms sklearn beyond 100K rows"
- "GBT requires most memory but achieves best AUC"
- "Diminishing returns beyond 4 cores for this dataset size"

---

## Data Sources (Export from Colab)

| File | Dashboard | Content |
|------|-----------|---------|
| `data_quality_summary.csv` | 1 | Missing rates, distributions, validation |
| `pipeline_metrics.csv` | 1 | Stage timing, row counts |
| `model_metrics.csv` | 2 | AUC, accuracy, precision, recall, F1 per model |
| `feature_importance.csv` | 2 | Feature names and importance scores |
| `confusion_matrices.csv` | 2 | TP, TN, FP, FN per model |
| `roc_curve_data.csv` | 2 | FPR, TPR points for plotting |
| `learning_curves.csv` | 2 | Training size vs accuracy |
| `station_results.csv` | 3 | Per-station accuracy with lat/lon |
| `seasonal_patterns.csv` | 3 | Monthly/hourly precipitation rates |
| `threshold_analysis.csv` | 3 | Metrics at each threshold |
| `scalability_results.csv` | 4 | Training time at different scales |
| `resource_usage.csv` | 4 | Memory, CPU per task |
| `mllib_sklearn_comparison.csv` | 4 | Side-by-side framework comparison |

---

## Design Guidelines

### Colors
- Primary: `#1f77b4` (Tableau blue)
- Secondary: `#ff7f0e` (orange)
- Background: `#ffffff`
- Weather theme: blues and grays

### Typography
- Tableau Regular font
- Title: 14pt bold
- Axis labels: 10pt

### Best Practices Applied
- [x] Tableau extracts for large data performance
- [x] LOD expressions for station-level aggregations
- [x] Parameter controls for interactivity
- [x] Action filters connecting dashboards
- [x] Tooltips with detailed breakdowns
- [x] Annotations on key insights
- [x] Mobile-responsive layout consideration
- [x] Export/download functionality

---

## Publishing Checklist

1. [ ] Connect all data sources (CSV files from Colab)
2. [ ] Verify all visualizations render correctly
3. [ ] Test all filters and parameters
4. [ ] Add annotations and insights
5. [ ] Check mobile layout
6. [ ] Publish to Tableau Public
7. [ ] Copy public URL to README and report
