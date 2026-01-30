import os
import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# 設定路徑
BASE_DIR = Path(__file__).resolve().parent
MUSIC_DIR = BASE_DIR / "music"
TEMPLATES_DIR = BASE_DIR / "templates"

# 確保資料夾存在
MUSIC_DIR.mkdir(exist_ok=True)
TEMPLATES_DIR.mkdir(exist_ok=True)

# 掛載靜態檔案 (讓前端可以讀到音樂檔)
app.mount("/music", StaticFiles(directory=MUSIC_DIR), name="music")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """回傳前端頁面"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/songs")
async def get_songs():
    """列出所有音樂檔案"""
    files = []
    for f in os.listdir(MUSIC_DIR):
        if f.endswith(('.mp3', '.flac', '.wav', '.m4a')):
            # 嘗試從檔名解析 歌手 - 歌名
            name_part = os.path.splitext(f)[0]
            if " - " in name_part:
                artist, title = name_part.split(" - ", 1)
            else:
                artist, title = "未知歌手", name_part
            
            files.append({
                "filename": f,
                "artist": artist,
                "title": title,
                "url": f"/music/{f}"
            })
    return files

@app.get("/api/lyrics")
async def get_lyrics(title: str, artist: str):
    """去 LRCLIB 抓歌詞"""
    url = "https://lrclib.net/api/get"
    params = {"track_name": title, "artist_name": artist}
    
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, params=params, timeout=10.0)
            data = resp.json()
            # 優先回傳逐字歌詞，沒有就回傳純文字
            return {"lyrics": data.get("syncedLyrics", "") or data.get("plainLyrics", "")}
        except Exception as e:
            print(f"Error fetching lyrics: {e}")
            return {"lyrics": ""}

if __name__ == "__main__":
    import uvicorn
    print("啟動伺服器... 請打開瀏覽器輸入 http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)