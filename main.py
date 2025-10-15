from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from rembg import remove
from PIL import Image
import io
import os

app = FastAPI(title="Background Remover API")

# Serve thư mục static (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    try:
        # Đọc file upload
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes)).convert("RGBA")

        # Xóa nền bằng rembg
        result = remove(img)

        # Xuất ra buffer
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        buf.seek(0)

        return StreamingResponse(buf, media_type="image/png")

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
