from pathlib import Path
from fastapi import FastAPI
import requests

app = FastAPI()

TENANT_ACCESS_TOKEN = "t-g10477e7BIKRYMEQMN5B7LTKXOO62CYXRZKNMTG6"
SPREADSHEET_TOKEN = "QSMTsNDDEhvm00txBpycTG6ZnBh"

@app.get("/read_feishu_sheet")
def read_feishu_sheet():
    url = f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{SHEET_TOKEN}/values"
    headers = {
        "Authorization": f"Bearer {TENANT_ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        return response.json()
    else:
        return JSONResponse(
            status_code=500,
            content={"error": "Non-JSON response", "raw": response.text}
        )
