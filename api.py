import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import *

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Nachricht(BaseModel):
    nachricht: str

@app.post("/verarbeitung")
async def verarbeitung(msg: Nachricht):

    text = msg.nachricht

    main = Main()
    text = main.verarbeitung(text)

    return {"nachricht": text}

if __name__ == "__main__":
    # Startet den Server automatisch, wenn das Skript direkt ausgeführt wird
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
