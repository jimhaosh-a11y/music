# Vutron Lite - 極簡主義者的動態歌詞播放器

> 「為什麼要為了看歌詞每個月付錢給串流平台？程式碼能解決的問題，就不該用錢解決。」



## 這是什麼？

這是一個用 Python 和現代網頁技術 (FastAPI + Tailwind CSS) 堆出來的本地音樂播放器。

它沒有複雜的資料庫，沒有使用者追蹤，也沒有廣告。它只做一件事：**播放你硬碟裡的 MP3，然後去 [LRCLIB](https://lrclib.net/) 把動態歌詞抓下來同步顯示。**

如果你受夠了 iTunes 的臃腫，或者不想為了聽幾首老歌去搞懂那些複雜的 Electron 專案，這個專案就是給你用的。

## 功能特點

- **零成本歌詞**：直接串接開源的 LRCLIB API，支援逐字歌詞 (Synced Lyrics)。
- **極簡架構**：後端 Python (FastAPI)，前端 HTML/JS，連 Node.js 都不用裝。
- **偽・Apple Music 介面**：用 Tailwind CSS 刻出來的玻璃擬態 (Glassmorphism) 風格，看起來很高級，但其實只是一堆 CSS class。
- **自動匹配**：只要你的檔名格式對了，它就會自動幫你找歌詞。

## 安裝需求

你只需要一台有安裝 Python 的電腦。

1. **Python 3.8+** (建議 3.10 以上)
2. 一些些耐心。

## 快速開始

### 1. 安裝依賴

打開你的終端機 (Terminal / CMD / PowerShell)，輸入以下指令來安裝必要的 Python 套件：

-pip install fastapi uvicorn httpx jinja2 aiofiles


2. 準備音樂
在專案根目錄下建立一個叫做 music 的資料夾，把你的 .mp3 檔案丟進去。

⚠️ 重要：檔名格式必須嚴格遵守！ 為了讓程式能自動搜尋，請將檔名命名為： 歌手 - 歌名.mp3

範例：

✅ 周杰倫 - 晴天.mp3

✅ NewJeans - Ditto.mp3

❌ track01.mp3 (程式會找不到是誰唱的)

3. 啟動伺服器
執行以下指令：
python main.py

如果看到 Uvicorn running on http://127.0.0.1:8000，恭喜，它活了。

4. 開始聽歌
打開瀏覽器，前往 http://127.0.0.1:8000。點擊左側的歌單，享受免費的動態歌詞。

技術堆疊 (給想改 Code 的人看)
Backend: FastAPI (比 Flask 快，比 Django 瘦)

Frontend: Vanilla JS + Tailwind CSS (透過 CDN 載入，省去 Webpack/Vite 的麻煩)

Lyrics Source: LRCLIB (感謝他們的無私奉獻)

常見問題 (FAQ)
Q: 為什麼網頁一片白？ A: 因為你的網路擋住了 Tailwind CSS 的 CDN，或者是你的瀏覽器太舊了。試著關掉 AdBlock 或換個網路。

Q: 為什麼找不到歌詞？ A:

LRCLIB 資料庫裡沒有這首歌。

你的檔名打錯字了（例如 周杰倫 - 晴天 多了空白）。

這首歌只有純文字歌詞 (Plain Lyrics)，不支援逐字滾動。
