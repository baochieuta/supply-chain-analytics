# Notebooks

Run in order:

1. `01_data_cleaning.ipynb` — load raw CSV, fix types/missing values, output to `data/processed/`
2. `02_kpi_eda.ipynb` — exploratory analysis feeding the Tableau dashboard (on-time rate, profit, cycle time)
3. `03_demand_forecasting.ipynb` — category-level demand forecast
4. `04_delivery_risk_inventory.ipynb` — late-delivery classification (+ SHAP) and safety stock recommendations
