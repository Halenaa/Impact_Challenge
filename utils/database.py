from __future__ import annotations

import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


DB_PATH = Path(__file__).resolve().parents[1] / "submissions.db"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with _connect() as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                nickname TEXT NOT NULL,
                email_optional TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS profiles (
                profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                q1_answer TEXT,
                q2_answer TEXT,
                q3_answer TEXT,
                q4_answer TEXT,
                q5_answer TEXT,
                q6_answer TEXT,
                pre_belonging_score INTEGER NOT NULL,
                challenge_type TEXT NOT NULL,
                identity_id TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            );

            CREATE TABLE IF NOT EXISTS submissions (
                submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                identity_id TEXT NOT NULL,
                challenge_type TEXT NOT NULL,
                task_id TEXT NOT NULL,
                reflection_text TEXT NOT NULL,
                location_text TEXT,
                pass_forward_note TEXT,
                post_belonging_score INTEGER NOT NULL,
                recommendation_score INTEGER,
                consent_for_wall INTEGER NOT NULL DEFAULT 0,
                approved_for_wall INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            );
            """
        )


def save_user(nickname: str, email_optional: str = "") -> str:
    user_id = uuid.uuid4().hex
    with _connect() as connection:
        connection.execute(
            """
            INSERT INTO users (user_id, nickname, email_optional, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, nickname.strip(), email_optional.strip(), _now_iso()),
        )
    return user_id


def save_profile(
    user_id: str,
    answers: dict[str, str],
    pre_belonging_score: int,
    challenge_type: str,
    identity_id: str,
) -> int:
    with _connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO profiles (
                user_id,
                q1_answer,
                q2_answer,
                q3_answer,
                q4_answer,
                q5_answer,
                q6_answer,
                pre_belonging_score,
                challenge_type,
                identity_id,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                answers.get("q1_answer", ""),
                answers.get("q2_answer", ""),
                answers.get("q3_answer", ""),
                answers.get("q4_answer", ""),
                answers.get("q5_answer", ""),
                answers.get("q6_answer", ""),
                pre_belonging_score,
                challenge_type,
                identity_id,
                _now_iso(),
            ),
        )
    return int(cursor.lastrowid)


def save_submission(
    user_id: str,
    identity_id: str,
    challenge_type: str,
    task_id: str,
    reflection_text: str,
    location_text: str,
    pass_forward_note: str,
    post_belonging_score: int,
    recommendation_score: int,
    consent_for_wall: bool,
) -> int:
    with _connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO submissions (
                user_id,
                identity_id,
                challenge_type,
                task_id,
                reflection_text,
                location_text,
                pass_forward_note,
                post_belonging_score,
                recommendation_score,
                consent_for_wall,
                approved_for_wall,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?)
            """,
            (
                user_id,
                identity_id,
                challenge_type,
                task_id,
                reflection_text.strip(),
                location_text.strip(),
                pass_forward_note.strip(),
                post_belonging_score,
                recommendation_score,
                int(consent_for_wall),
                _now_iso(),
            ),
        )
    return int(cursor.lastrowid)


def get_public_wall_posts() -> pd.DataFrame:
    with _connect() as connection:
        return pd.read_sql_query(
            """
            SELECT
                submission_id,
                identity_id,
                challenge_type,
                location_text,
                reflection_text,
                pass_forward_note,
                created_at
            FROM submissions
            WHERE consent_for_wall = 1
              AND approved_for_wall = 1
            ORDER BY created_at DESC
            """,
            connection,
        )


def get_dashboard_data() -> dict[str, pd.DataFrame]:
    with _connect() as connection:
        return {
            "users": pd.read_sql_query("SELECT * FROM users ORDER BY created_at DESC", connection),
            "profiles": pd.read_sql_query("SELECT * FROM profiles ORDER BY created_at DESC", connection),
            "submissions": pd.read_sql_query(
                "SELECT * FROM submissions ORDER BY created_at DESC",
                connection,
            ),
        }


def approve_submission(submission_id: int, approved: bool = True) -> None:
    with _connect() as connection:
        connection.execute(
            """
            UPDATE submissions
            SET approved_for_wall = ?
            WHERE submission_id = ?
            """,
            (int(approved), submission_id),
        )
