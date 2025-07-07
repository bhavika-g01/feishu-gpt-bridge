from pathlib import Path
from fastapi import FastAPI
import requests
from fastapi.responses import JSONResponse

app = FastAPI()

TENANT_ACCESS_TOKEN = "t-g10477fL2IQWIESOEDPKVD46KGONNJ5SLSUCD243"
SHEET_TOKEN = "QSMTsNDDEhvm00txBpycTG6ZnBh"

@app.get("/read_feishu_sheet")
def read_feishu_sheet():
    url = f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{SHEET_TOKEN}/values?range=订单信息Order%20delivery%20information!A1:Z100"
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
