from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

def get_recent_games():
    try:
        gamefinder = leaguegamefinder.LeagueGameFinder(season_type_nullable="Regular Season")
        games_df = gamefinder.get_data_frames()[0]

        recent_games = games_df.sort_values("GAME_DATE").tail(10)

        game_summaries = []
        for _, game in recent_games.iterrows():
            score = game["PTS"]
            matchup = game["MATCHUP"]
            margin = abs(game["PLUS_MINUS"])

            
            if margin <= 5:
                mood = "Hype"
            elif score < 90:
                mood = "Lo-fi"
            else:
                mood = "Chill"

            game_summaries.append({
                "game_id": game["GAME_ID"],
                "team": game["TEAM_ABBREVIATION"],
                "opponent": matchup.replace("vs. ", "").replace("@ ", ""),
                "team_score": score,
                "outcome": game["WL"],
                "date": game["GAME_DATE"],
                "mood": mood
            })

        return game_summaries

    except Exception as e:
        print(f"[ERROR] {e}")
        return [{"error": str(e)}]
