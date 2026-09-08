from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Campaign Analysis API")

@app.get("/campaign-analysis")
def get_campaign_analysis():
    # Campaign analysis results data
    data = [
        {"Campaign_ID": "C001", "Channel": "Google Ads", "Spend": 1200.0, "Conversions": 150, "CPA": 8.0, "ROI": 3.2},
        {"Campaign_ID": "C002", "Channel": "Meta Ads", "Spend": 2500.0, "Conversions": 300, "CPA": 8.33, "ROI": 2.8},
        {"Campaign_ID": "C003", "Channel": "LinkedIn", "Spend": 1800.0, "Conversions": 90, "CPA": 20.0, "ROI": 1.5},
        {"Campaign_ID": "C004", "Channel": "Email Newsletter", "Spend": 300.0, "Conversions": 120, "CPA": 2.5, "ROI": 5.0}
    ]
    
    df = pd.DataFrame(data)[cite: 1]
    
    # Returns records in a tabular list format easily consumed by Power Query[cite: 1]
    return df.to_dict(orient="records")


# --- TABULAR JSON ENDPOINT ---
@app.get("/campaign-analysis/table")
def get_campaign_table_json():
    campaigns = [
        {"Campaign_ID": "C001", "Channel": "Google Ads", "Spend": 1200.0, "Conversions": 150, "CPA": 8.0, "ROI": 3.2},
        {"Campaign_ID": "C002", "Channel": "Meta Ads", "Spend": 2500.0, "Conversions": 300, "CPA": 8.33, "ROI": 2.8},
        {"Campaign_ID": "C003", "Channel": "LinkedIn", "Spend": 1800.0, "Conversions": 90, "CPA": 20.0, "ROI": 1.5},
        {"Campaign_ID": "C004", "Channel": "Email Newsletter", "Spend": 300.0, "Conversions": 120, "CPA": 2.5, "ROI": 5.0}
    ]
    
    df = pd.DataFrame(campaigns)
    
    # Returns the table layout including schema and data
    return df.to_dict(orient="table")