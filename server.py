from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/analyze/")
async def analyze_audio(file: UploadFile = File(...)):
    audio_data = await file.read()
    # Заглушка анализа — просто вернём размер файла и имя
    result = {
        "filename": file.filename,
        "size_bytes": len(audio_data),
        "message": "Аудио получено, обработка в разработке"
    }
    return JSONResponse(content=result)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
