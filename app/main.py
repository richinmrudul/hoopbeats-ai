from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .nba_data import get_recent_games
import os

app = FastAPI()

# Mount the /assets route to serve audio files
app.mount("/assets", StaticFiles(directory=os.path.join("frontend", "assets")), name="assets")

@app.get("/")
def root():
    return FileResponse("frontend/index.html")

@app.get("/games")
def fetch_games():
    return {"games": get_recent_games()}

@app.get("/generate_track")
def generate_track(mood: str = Query(..., enum=["Hype", "Chill", "Lo-fi"])):
    track_map = {
        "Hype": "epic_buzzer_beater_track.mp3",
        "Chill": "confident_blowout_win.mp3",
        "Lo-fi": "gritty_defense_low_scoring.wav"
    }
    return {
        "mood": mood,
        "generated_track": track_map[mood]
    }
