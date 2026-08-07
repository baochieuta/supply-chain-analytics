# End-to-End Supply Chain Analytics: Demand Forecasting, Delivery Risk \& Inventory Optimization

**Author:** Ta Bao Chieu | [LinkedIn](https://www.linkedin.com/in/baochieu) | baoct@uci.edu

## Business Problem

Supply chain teams routinely lose margin and customer trust to two linked problems: **shipments that
arrive late**, and **inventory that's either too thin (stockouts) or too thick (working capital tied up
in safety stock)**. This project simulates the analysis a supply chain/operations analyst would run to
diagnose both problems and recommend fixes, using the [DataCo Smart Supply Chain
dataset](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)
— \~180k real order-level transactions spanning shipping mode, delivery status, product category,
customer segment, and geography.

**Guiding questions:**

1. Which orders are at risk of arriving late, and what drives that risk?
2. How does product demand vary over time by category, and what's a reasonable forecast?
3. Given that demand variability, what safety stock / reorder point keeps service levels up without
over-investing in inventory?
4. What would an ops team actually do differently based on this?

## Repo Structure

```
supply-chain-analytics/
├── data/
│   ├── raw/              # original Kaggle CSV (not committed — see Setup)
│   └── processed/        # cleaned datasets used by notebooks
├── notebooks/            # analysis notebooks, run in order (01 → 04)
├── src/                  # reusable Python functions (cleaning, features, models)
├── dashboards/           # Tableau workbook(s) / exported dashboard images
├── reports/
│   └── figures/          # key charts embedded below
├── models/                # saved model artifacts
├── requirements.txt
└── README.md
```

## Methodology

|Stage|What|Tools|
|-|-|-|
|1. Data Cleaning \& ETL|Deduplication, type fixes, handling missing/inconsistent geography and date fields, building an analysis-ready order table|Python (pandas)|
|2. KPI Dashboard|On-time delivery rate, profit by region/category, order cycle time, late-delivery trend|Tableau|
|3. Demand Forecasting|Category-level time series forecast of order volume|Python (statsmodels / Prophet-style decomposition)|
|4. Late-Delivery Risk Model|Classification model predicting late delivery from shipping mode, distance, category, order size|Python (scikit-learn, XGBoost) + SHAP for feature importance|
|5. Inventory Optimization|Safety stock / reorder point recommendations using demand variability and lead-time assumptions|Python|

## Key Visuals

*(Embedded directly, not just linked — replace these placeholders as each notebook is finished)*

!\[On-time delivery dashboard](reports/figures/dashboard\_overview.png)
!\[Late delivery feature importance](reports/figures/feature\_importance.png)
!\[Demand forecast by category](reports/figures/demand\_forecast.png)

## Key Findings *(fill in once analysis is complete)*

* Late-delivery rate: \*\***54.8%\*\*** overall after data is cleaned; highest in \*\***First class (95.3%)\*\* and \*\*Second class (76.6%)\*\* consistent across all region**
* Primary driver: not fulfillment speed, but \*\*miscalibrated shipping promises\*\* — First Class (promised 1 day, actual \~2) and Second Class (promised 2 days, actual \~4) both consistently run \*\*\~2x\*\* their promised window, uniformly across all 5 markets
* Forecasted demand for **\[category]** shows **\[trend/seasonality]**
* Recommended safety stock adjustment: **\[+/- X%]** for **\[category]**, projected to reduce stockout
risk from **X% → Y%**

## Business Recommendations *(fill in once analysis is complete)*

1. ...
2. ...
3. ...

## Setup \& Reproduction

```bash
git clone https://github.com/<your-username>/supply-chain-analytics.git
cd supply-chain-analytics
python -m venv venv \&\& source venv/bin/activate    # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
```

Download the dataset from
[Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)
and place `DataCoSupplyChainDataset.csv` into `data/raw/`. Then run the notebooks in `notebooks/` in
order, 01 through 04.

## Tools Used

Python (pandas, scikit-learn, XGBoost, SHAP, statsmodels) · Tableau · Excel · SQL

