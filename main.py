from pathlib import Path
from fastapi import FastAPI
import requests
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()
app.mount("/.well-known", StaticFiles(directory=".", html=True), name="static")
TENANT_ACCESS_TOKEN = "t-g10477kLUF2P4PIQZ272AER64CUOHIRMJ6M57RN2"
SHEET_TOKEN = "QSMTsNDDEhvm00txBpycTG6ZnBh"

@app.get("/read_feishu_sheet")
def read_feishu_sheet():
    url = f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{SHEET_TOKEN}/"
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
@app.get("/openapi.yaml", include_in_schema=False)
def get_openapi_yaml():
    filepath = os.path.join(os.path.dirname(__file__), "openapi.yaml")
    return FileResponse(filepath, media_type="application/yaml")

# @app.get("/read_feishu_doc")
# def read_feishu_doc():
#     doc_id = "WuApw0ktqipZsHk7JIrctRtrnef"
#     url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/content"
#     headers = {
#         "Authorization": f"Bearer {TENANT_ACCESS_TOKEN}"
#     }

#     response = requests.get(url, headers=headers)

#     content_type = response.headers.get("Content-Type", "")
#     if "application/json" in content_type:
#         return response.json()
#     else:
#         return JSONResponse(
#             status_code=500,
#             content={"error": "Non-JSON response", "raw": response.text}
#         )
