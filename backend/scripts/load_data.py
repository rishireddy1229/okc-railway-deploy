import json
import psycopg2
import os

with open('raw_data/teams.json') as f:
    teams_data = json.load(f)

with open('raw_data/players.json') as f:
    players_data = json.load(f)

with open('raw_data/games.json') as f:
    games_data = json.load(f)


conn = psycopg2.connect(
    dbname="okc",
    user="okcapplicant",
    password="rishi@db1",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cur.execute("SET search_path TO app;")

cur.execute("DELETE FROM games;")
cur.execute("DELETE FROM players;")
cur.execute("DELETE FROM teams;")

for team in teams_data:
    print("Inserting team:", team)
    cur.execute("""
        INSERT INTO teams (team_id, name)
        VALUES (%s, %s)
    """, (
        team['team_id'],
        team['name']
    ))


for player in players_data:
    print("Inserting player:", player)
    cur.execute("""
    INSERT INTO players (player_id, name, team_id)
    VALUES (%s, %s, %s)
""", (
    player['player_id'],
    player['name'],
    player['team_id']
))


for game in games_data:
    print("Inserting game:", game)
    cur.execute("""
        INSERT INTO games (game_id, date)
        VALUES (%s, %s)
    """, (
        game['id'],
        game['date']
    ))

    for stat in game.get('player_stats', []):
        print("Inserting stat:", stat)
        cur.execute("""
            INSERT INTO player_stats (
                id, game_id, player_id, points, assists, rebounds,
                steals, blocks, turnovers, minutes
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            stat['id'],
            game['id'],
            stat['player_id'],
            stat['points'],
            stat['assists'],
            stat['rebounds'],
            stat['steals'],
            stat['blocks'],
            stat['turnovers'],
            stat['minutes']
        ))


conn.commit()
cur.close()
conn.close()

print("Data loaded successfully.")
