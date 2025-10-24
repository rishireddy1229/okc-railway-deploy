import json
import os
import random

from app.dbmodels.models import Shot, Pass, Turnover, Player
from collections import defaultdict

def get_player_summary_stats(player_id: str):
    # TODO: Complete API response, replace placeholder below with actual implementation that sources data from database
    play_types = ['pickAndRoll', 'isolation', 'postUp', 'offBallScreen']

    result = defaultdict(lambda: {
        "totalShotAttempts": 0,
        "totalPoints": 0,
        "totalPasses": 0,
        "totalTurnovers": 0,
        "shots": [],
        "passes": [],
        "turnovers": []
    })

    shots = Shot.objects.filter(player_id=player_id)
    for shot in shots:
        play = shot.play_type
        if play not in play_types:
            continue
        result[play]["totalShotAttempts"] += 1
        result[play]["totalPoints"] += shot.points
        result[play]["shots"].append({"x": shot.x, "y": shot.y})

    
    passes = Pass.objects.filter(player_id=player_id)
    for pas in passes:
        play = pas.play_type
        if play not in play_types:
            continue
        result[play]["totalPasses"] += 1
        result[play]["passes"].append({"x": pas.x, "y": pas.y})


    turnovers = Turnover.objects.filter(player_id=player_id)
    for turnover in turnovers:
        play = turnover.play_type
        if play not in play_types:
            continue
        result[play]["totalTurnovers"] += 1
        result[play]["turnovers"].append({"x": turnover.x, "y": turnover.y})

    return result


def get_ranks(player_id: str, player_summary: dict):
    # TODO: replace with your implementation of get_ranks
    random.seed(player_id)
    return {
        "totalShotAttemptsRank": random.randint(1, 10),
        "totalPointsRank": random.randint(1, 10),
        "totalPassesRank": random.randint(1, 10),
        "totalPotentialAssistsRank": random.randint(1, 10),
        "totalTurnoversRank": random.randint(1, 10),
        "totalPassingTurnoversRank": random.randint(1, 10),
        'pickAndRollCountRank': random.randint(1, 10),
        'isolationCountRank': random.randint(1, 10),
        'postUpCountRank': random.randint(1, 10),
        'offBallScreenCountRank': random.randint(1, 10),
    }
