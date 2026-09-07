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
|2. KPI Dashboard|Built around one central flag: the overall late-delivery rate, broken down by Shipping Mode (revealed the core finding) and Market/Region (checked for concentration, found none). A world map was deliberately avoided for the regional view: since late rate is uniform across all 5 continents, a map would visually imply a geographic story that isn't actually there, adding noise without aiding any decision.|Tableau|
|3. Demand Forecasting|Category-level time series forecast of order volume|Python (statsmodels / Prophet-style decomposition)|
|4. Late-Delivery Risk Model|Built a baseline XGBoost classifier using two features surviving filter-method testing (Shipping Mode, payment Type), after excluding several strong-looking but invalid candidates: two data-leakage columns (Days for shipping (real), Delivery Status - both only knowable after an order ships) and one fraud-contaminated column (Order Status). Achieved 70% accuracy, 87% precision, 55% recall on the late class. Verified this is near the theoretical ceiling achievable with these two features (69.64%, calculated via majority-vote-per-group), confirming the model isn't undertrained - meaningful recall improvement requires new features, not further tuning. Noted as a scoped area for future iteration.|Python (scikit-learn, XGBoost) + SHAP for feature importance|
|5. Inventory Optimization|Calculated safety stock recommendations at the category level using the formula safety stock equals Z times standard deviation of daily demand times the square root of lead time, with Z set to 1.65 for a 95 percent service level. True supplier lead time data is not available in this dataset, so average customer facing shipping time was used as a directional proxy, clearly flagged as an imperfect substitute rather than a validated input. Demand variability was measured at the daily level per category to keep units consistent with the lead time figure.|Python|

## Key Visuals

!\[On-time delivery dashboard](reports/figures/dashboard\_overview.png)
!\[Late delivery feature importance](reports/figures/feature\_importance.png)
!\[Demand forecast by category](reports/figures/demand\_forecast.png)

!\[Top 10 categories by safety stock](reports/figures/safety\_stock\_top10.png)

## Key Findings *(fill in once analysis is complete)*

* Late-delivery rate: \*\***54.8%\*\*** overall after data is cleaned; highest in \*\***First class (95.3%)\*\* and \*\*Second class (76.6%)\*\* consistent across all region**
* Primary driver: not fulfillment speed, but \*\*miscalibrated shipping promises\*\* — First Class (promised 1 day, actual \~2) and Second Class (promised 2 days, actual \~4) both consistently run \*\*\~2x\*\* their promised window, uniformly across all 5 markets
* The delivery-risk model correctly flags 87% of its "late" predictions, but only catches 55% of orders that are truly late -> a conservative model that under-flags real risk. Using the dataset's own profit gap (\~$0.78/order), the \~9,000 missed late orders in the test set represent an estimated $7,040 in direct margin impact, likely an underestimate given the larger real cost is probably customer retention, which this dataset can't measure directly.
* Confirmed via a theoretical ceiling calculation that the model is already near-optimal given its current features (69.64% ceiling vs. 70% achieved) -> the constraint is feature richness, not model quality.
* Coefficient of variation and recommended safety stock do not rank categories the same way, and this is expected rather than contradictory. Cameras has the highest coefficient of variation in the dataset at about 1.33, meaning its demand is highly erratic relative to its own size, yet its recommended safety stock, about 53 units, is similar in absolute terms to Cleats, about 51 units, despite Cleats selling roughly 8 times more units per day. This is because safety stock depends on the actual size of demand swings in real units, not on relative variability alone. Books, Cameras, and Music require the largest absolute safety stock buffers in the dataset, driven by a combination of moderate to high variability and meaningful sales volume together, not by either factor alone.

## Business Recommendations *(fill in once analysis is complete)*

1. DataCo has two viable paths forward, with a real trade-off between them:

   1. Option A — Reset the promise to match reality. Cheap and fast to implement, but doesn't improve actual delivery speed — it only changes what counts as "on time." Risk: customers paying a premium for "expedited" shipping may notice it no longer outpaces Standard Class, undermining trust in the tier itself.
   2. Option B — Investigate and fix the fulfillment bottleneck. Addresses the root cause rather than the label, but is more expensive and slower to implement — and since the \~2x gap holds identically across all 5 continents, the fix likely isn't regional logistics, but something structural in fulfillment or carrier processes, which may be costly to change globally.

      1. Given the evidence, a reasonable starting point is Option A as a short-term fix (immediately reduces the reported late-rate crisis) paired with Option B as a longer-term investigation — rather than treating them as mutually exclusive.
   3. Prioritize safety stock investment for Books, Cameras, DVDs, and Music, the four categories with the largest calculated buffers, since these represent the greatest real risk of stockouts under current demand patterns. Treat these numbers as directional estimates rather than precise targets, since true supplier lead time data was not available and was approximated using outbound shipping time. A natural next step, outside the scope of this project, would be to repeat this calculation once real supplier lead time data is available, to validate or adjust these estimates.

## Setup \& Reproduction

```bash
git clone https://github.com/<your-username>/supply-chain-analytics.git
cd supply-chain-analytics
python -m venv venv \\\\\\\&\\\\\\\& source venv/bin/activate    # or venv\\\\\\\\Scripts\\\\\\\\activate on Windows
pip install -r requirements.txt
```

Download the dataset from
[Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)
and place `DataCoSupplyChainDataset.csv` into `data/raw/`. Then run the notebooks in `notebooks/` in
order, 01 through 04.

## Tools Used

Python (pandas, scikit-learn, XGBoost, SHAP, statsmodels) · Tableau · Excel · SQL

