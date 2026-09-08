from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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


# --- NEW JSON TABULAR ENDPOINT ---
@app.get("/campaign-analysis/json-table")
def get_campaign_json_table():
    data = [
        {"Campaign_ID": "C001", "Channel": "Google Ads", "Spend": 1200.0, "Conversions": 150, "CPA": 8.0, "ROI": 3.2},
        {"Campaign_ID": "C002", "Channel": "Meta Ads", "Spend": 2500.0, "Conversions": 300, "CPA": 8.33, "ROI": 2.8},
        {"Campaign_ID": "C003", "Channel": "LinkedIn", "Spend": 1800.0, "Conversions": 90, "CPA": 20.0, "ROI": 1.5},
        {"Campaign_ID": "C004", "Channel": "Email Newsletter", "Spend": 300.0, "Conversions": 120, "CPA": 2.5, "ROI": 5.0}
    ]
    
    df = pd.DataFrame(data)
    
    # Returns the data in a JSON tabular format (Table Schema format with schema and data)
    return df.to_dict(orient="table")


# --- HTML TABLE ENDPOINT ---
@app.get("/campaign-analysis/table", response_class=HTMLResponse)
def get_campaign_table():
    # Use the same data source (or convert from your DataFrame)
    campaigns = [
        {"Campaign_ID": "C001", "Channel": "Google Ads", "Spend": 1200.0, "Conversions": 150, "CPA": 8.0, "ROI": 3.2},
        {"Campaign_ID": "C002", "Channel": "Meta Ads", "Spend": 2500.0, "Conversions": 300, "CPA": 8.33, "ROI": 2.8},
        {"Campaign_ID": "C003", "Channel": "LinkedIn", "Spend": 1800.0, "Conversions": 90, "CPA": 20.0, "ROI": 1.5},
        {"Campaign_ID": "C004", "Channel": "Email Newsletter", "Spend": 300.0, "Conversions": 120, "CPA": 2.5, "ROI": 5.0}
    ]
    
    # Generate table rows dynamically
    table_rows = "".join([
        f"<tr><td>{c['Campaign_ID']}</td><td>{c['Channel']}</td><td>${c['Spend']}</td><td>{c['Conversions']}</td><td>${c['CPA']}</td><td>{c['ROI']}</td></tr>"
        for c in campaigns
    ])
    
    # Build a clean HTML page with a styled table
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Campaign Analysis Table</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f8f9fa; }}
            h2 {{ color: #333; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            th, td {{ border: 1px solid #dee2e6; padding: 12px; text-align: left; }}
            th {{ background-color: #007bff; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h2>Campaign Analysis Table</h2>
        <table>
            <thead>
                <tr>
                    <th>Campaign ID</th>
                    <th>Channel</th>
                    <th>Spend</th>
                    <th>Conversions</th>
                    <th>CPA</th>
                    <th>ROI</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content, status_code=200)