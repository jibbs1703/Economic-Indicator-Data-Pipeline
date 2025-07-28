"""Economic APIs for ETL Pipeline."""

import json
import os
from datetime import UTC, datetime
from pprint import pprint

import dotenv
import requests

dotenv.load_dotenv()

BASE_URL = "https://api.stlouisfed.org/fred/series/observations?series_id="
INDICATOR = "MORTGAGE30US"
START_DATE="2025-06-17"
END_DATE=datetime.now(UTC).date
API_KEY=os.getenv("FRED_KEY")

# Weekly Refreshed
# 15-Year Mortgage Rates
# 30-Year Mortgage Rates

response = requests.get(
	f"{BASE_URL}{INDICATOR}"
	f"&observation_start={START_DATE}"
	f"&observation_end={END_DATE}"
	f"&api_key={API_KEY}"
    f"&file_type=json",
    timeout=5
)
result = json.loads(response.text)
pprint(result)