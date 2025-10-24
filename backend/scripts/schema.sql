SET search_path TO app;

DROP TABLE IF EXISTS player_stats CASCADE;
DROP TABLE IF EXISTS games CASCADE;
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS teams CASCADE;

CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    team_id INT REFERENCES teams(team_id)
);

CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    date DATE
);

CREATE TABLE player_stats (
    stat_id SERIAL PRIMARY KEY,
    game_id INT REFERENCES games(game_id),
    player_id INT REFERENCES players(player_id),
    points INT,
    assists INT,
    rebounds INT,
    steals INT,
    blocks INT,
    turnovers INT,
    minutes FLOAT
);
