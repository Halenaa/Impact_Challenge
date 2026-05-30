from __future__ import annotations

import random

from data.identities import IDENTITIES_BY_CHALLENGE
from data.questions import CHALLENGE_TYPES, QUESTIONS


def calculate_scores(answers: dict[str, str]) -> dict[str, int]:
    scores = {challenge_type: 0 for challenge_type in CHALLENGE_TYPES}

    for question in QUESTIONS:
        answer = answers.get(question["id"])
        for challenge_type, points in question.get("scores", {}).get(answer, {}).items():
            scores[challenge_type] += points

    return scores


def get_challenge_type(scores: dict[str, int]) -> str:
    tie_break_order = {
        "Connection Challenge": 0,
        "Belonging Challenge": 1,
        "Value Challenge": 2,
    }
    return max(scores, key=lambda challenge_type: (scores[challenge_type], -tie_break_order[challenge_type]))


def match_identity(challenge_type: str) -> str:
    identity_ids = IDENTITIES_BY_CHALLENGE.get(challenge_type, [])
    if not identity_ids:
        raise ValueError(f"No identities configured for challenge type: {challenge_type}")
    return random.choice(identity_ids)
