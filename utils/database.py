from __future__ import annotations

import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


DB_PATH = Path(__file__).resolve().parents[1] / "submissions.db"


DEMO_RECORDS = [
    {
        "nickname": "Demo Student 01",
        "challenge_type": "Connection Challenge",
        "identity_id": "shared_kitchen_host",
        "task_id": "shared_kitchen_host_task",
        "pre_belonging_score": 4,
        "post_belonging_score": 6,
        "recommendation_score": 8,
        "q1_answer": "Less than 1 month",
        "q2_answer": "I want to meet people, but I do not know how to begin.",
        "q3_answer": "More chances to meet people without pressure.",
        "q4_answer": "Starting conversations with people I do not know well.",
        "q5_answer": "A small interaction with another person.",
        "q6_answer": "Some social contact is okay if it is low pressure.",
        "location_text": "Campus common room",
        "reflection_text": (
            "What I did: I asked someone in the common room where they usually get coffee.\n\n"
            "What I noticed: The conversation stayed small, but it made the room feel less closed.\n\n"
            "How I felt: A little less invisible afterward."
        ),
        "pass_forward_note": "Ask about something practical first. It feels easier than trying to be interesting.",
        "consent_for_wall": True,
        "approved_for_wall": True,
    },
    {
        "nickname": "Demo Student 02",
        "challenge_type": "Connection Challenge",
        "identity_id": "bike_messenger",
        "task_id": "bike_messenger_task",
        "pre_belonging_score": 5,
        "post_belonging_score": 7,
        "recommendation_score": 9,
        "q1_answer": "1-3 months",
        "q2_answer": "I want to meet people, but I do not know how to begin.",
        "q3_answer": "More chances to meet people without pressure.",
        "q4_answer": "Starting conversations with people I do not know well.",
        "q5_answer": "A small interaction with another person.",
        "q6_answer": "Some social contact is okay if it is low pressure.",
        "location_text": "Route between campus and De Pijp",
        "reflection_text": (
            "What I did: I mapped a calmer bike route and wrote down one crossing to avoid.\n\n"
            "What I noticed: Knowing one safer route made the city feel more readable.\n\n"
            "How I felt: More confident moving around alone."
        ),
        "pass_forward_note": "Stop before you write anything down. Amsterdam makes more sense when you pause.",
        "consent_for_wall": True,
        "approved_for_wall": True,
    },
    {
        "nickname": "Demo Student 03",
        "challenge_type": "Belonging Challenge",
        "identity_id": "canal_letter_writer",
        "task_id": "canal_letter_writer_task",
        "pre_belonging_score": 3,
        "post_belonging_score": 6,
        "recommendation_score": 8,
        "q1_answer": "3-12 months",
        "q2_answer": "I feel like everyone already belongs except me.",
        "q3_answer": "A feeling that this place can become mine too.",
        "q4_answer": "Feeling emotionally at home in familiar places.",
        "q5_answer": "A reflective walk or quiet city ritual.",
        "q6_answer": "I would prefer something quiet and independent.",
        "location_text": "Near Prinsengracht",
        "reflection_text": (
            "What I did: I sat by the canal for ten minutes and wrote one sentence.\n\n"
            "What I noticed: The city felt calmer when I stopped trying to use it efficiently.\n\n"
            "How I felt: More connected, even without talking to anyone."
        ),
        "pass_forward_note": "Go when it is quiet. You do not need to perform belonging.",
        "consent_for_wall": True,
        "approved_for_wall": True,
    },
    {
        "nickname": "Demo Student 04",
        "challenge_type": "Belonging Challenge",
        "identity_id": "city_signal_collector",
        "task_id": "city_signal_collector_task",
        "pre_belonging_score": 4,
        "post_belonging_score": 5,
        "recommendation_score": 7,
        "q1_answer": "More than 1 year",
        "q2_answer": "I feel like everyone already belongs except me.",
        "q3_answer": "A feeling that this place can become mine too.",
        "q4_answer": "Feeling emotionally at home in familiar places.",
        "q5_answer": "A reflective walk or quiet city ritual.",
        "q6_answer": "I would prefer something quiet and independent.",
        "location_text": "OBA Oosterdok",
        "reflection_text": (
            "What I did: I found three small signs that people share public space here.\n\n"
            "What I noticed: The library felt like a place where I did not need permission to stay.\n\n"
            "How I felt: Quieter, but in a good way."
        ),
        "pass_forward_note": "Look for benches, notice boards, and places where nobody asks why you are there.",
        "consent_for_wall": True,
        "approved_for_wall": True,
    },
    {
        "nickname": "Demo Student 05",
        "challenge_type": "Value Challenge",
        "identity_id": "museum_apprentice",
        "task_id": "museum_apprentice_task",
        "pre_belonging_score": 5,
        "post_belonging_score": 8,
        "recommendation_score": 9,
        "q1_answer": "1-3 months",
        "q2_answer": "I am not sure what value I bring here.",
        "q3_answer": "A clearer sense that I have something to contribute.",
        "q4_answer": "Trusting that my presence matters in groups or projects.",
        "q5_answer": "A task that lets me observe, choose, or make meaning.",
        "q6_answer": "I want something that helps me notice my own point of view.",
        "location_text": "Rijksmuseum garden",
        "reflection_text": (
            "What I did: I chose one public artwork and wrote what I noticed first.\n\n"
            "What I noticed: My first reaction was specific to me, not wrong.\n\n"
            "How I felt: More willing to trust my own perspective."
        ),
        "pass_forward_note": "Do not search for the correct interpretation. Start with what catches you.",
        "consent_for_wall": True,
        "approved_for_wall": True,
    },
    {
        "nickname": "Demo Student 06",
        "challenge_type": "Value Challenge",
        "identity_id": "second_hand_explorer",
        "task_id": "second_hand_explorer_task",
        "pre_belonging_score": 4,
        "post_belonging_score": 7,
        "recommendation_score": 8,
        "q1_answer": "Less than 1 month",
        "q2_answer": "I am not sure what value I bring here.",
        "q3_answer": "A clearer sense that I have something to contribute.",
        "q4_answer": "Trusting that my presence matters in groups or projects.",
        "q5_answer": "A task that lets me observe, choose, or make meaning.",
        "q6_answer": "I want something that helps me notice my own point of view.",
        "location_text": "Episode thrift store",
        "reflection_text": (
            "What I did: I found an old scarf and imagined who owned it before.\n\n"
            "What I noticed: Objects can move between lives without losing meaning.\n\n"
            "How I felt: Less temporary in the city."
        ),
        "pass_forward_note": "Pick something small. You do not have to buy it for the story to work.",
        "consent_for_wall": True,
        "approved_for_wall": True,
    },
    {
        "nickname": "Demo Student 07",
        "challenge_type": "Connection Challenge",
        "identity_id": "shared_kitchen_host",
        "task_id": "shared_kitchen_host_task",
        "pre_belonging_score": 6,
        "post_belonging_score": 7,
        "recommendation_score": 7,
        "q1_answer": "3-12 months",
        "q2_answer": "I want to meet people, but I do not know how to begin.",
        "q3_answer": "More chances to meet people without pressure.",
        "q4_answer": "Starting conversations with people I do not know well.",
        "q5_answer": "A small interaction with another person.",
        "q6_answer": "Some social contact is okay if it is low pressure.",
        "location_text": "Student housing kitchen",
        "reflection_text": (
            "What I did: I offered leftover pasta to someone in the kitchen.\n\n"
            "What I noticed: Sharing food made the interaction feel natural.\n\n"
            "How I felt: Warm, but also relieved that it could stay simple."
        ),
        "pass_forward_note": "Offer something with no pressure attached.",
        "consent_for_wall": False,
        "approved_for_wall": False,
    },
    {
        "nickname": "Demo Student 08",
        "challenge_type": "Belonging Challenge",
        "identity_id": "canal_letter_writer",
        "task_id": "canal_letter_writer_task",
        "pre_belonging_score": 2,
        "post_belonging_score": 5,
        "recommendation_score": 8,
        "q1_answer": "Less than 1 month",
        "q2_answer": "I feel like everyone already belongs except me.",
        "q3_answer": "A feeling that this place can become mine too.",
        "q4_answer": "Feeling emotionally at home in familiar places.",
        "q5_answer": "A reflective walk or quiet city ritual.",
        "q6_answer": "I would prefer something quiet and independent.",
        "location_text": "Canal near Jordaan",
        "reflection_text": (
            "What I did: I wrote a note to someone arriving after me.\n\n"
            "What I noticed: I had more to say than I expected.\n\n"
            "How I felt: Still new, but less alone in being new."
        ),
        "pass_forward_note": "Write to someone newer than you. It changes how you see yourself.",
        "consent_for_wall": True,
        "approved_for_wall": False,
    },
    {
        "nickname": "Demo Student 09",
        "challenge_type": "Value Challenge",
        "identity_id": "museum_apprentice",
        "task_id": "museum_apprentice_task",
        "pre_belonging_score": 6,
        "post_belonging_score": 8,
        "recommendation_score": 10,
        "q1_answer": "More than 1 year",
        "q2_answer": "I am not sure what value I bring here.",
        "q3_answer": "A clearer sense that I have something to contribute.",
        "q4_answer": "Trusting that my presence matters in groups or projects.",
        "q5_answer": "A task that lets me observe, choose, or make meaning.",
        "q6_answer": "I want something that helps me notice my own point of view.",
        "location_text": "Street art near NDSM",
        "reflection_text": (
            "What I did: I chose a mural and wrote down what I thought it was asking from me.\n\n"
            "What I noticed: My interpretation connected to where I come from.\n\n"
            "How I felt: Like my background was useful, not extra."
        ),
        "pass_forward_note": "Let your first memory be part of the task.",
        "consent_for_wall": True,
        "approved_for_wall": True,
    },
    {
        "nickname": "Demo Student 10",
        "challenge_type": "Connection Challenge",
        "identity_id": "bike_messenger",
        "task_id": "bike_messenger_task",
        "pre_belonging_score": 5,
        "post_belonging_score": 6,
        "recommendation_score": 7,
        "q1_answer": "1-3 months",
        "q2_answer": "I want to meet people, but I do not know how to begin.",
        "q3_answer": "More chances to meet people without pressure.",
        "q4_answer": "Starting conversations with people I do not know well.",
        "q5_answer": "A small interaction with another person.",
        "q6_answer": "Some social contact is okay if it is low pressure.",
        "location_text": "Wibautstraat",
        "reflection_text": (
            "What I did: I noticed a route with fewer crowded intersections.\n\n"
            "What I noticed: Helpful knowledge can be small and still worth sharing.\n\n"
            "How I felt: More like I had something practical to pass on."
        ),
        "pass_forward_note": "Notice one crossing, one landmark, and one place to stop.",
        "consent_for_wall": False,
        "approved_for_wall": False,
    },
]


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


def create_demo_records() -> int:
    created_count = 0
    with _connect() as connection:
        for record in DEMO_RECORDS:
            user_id = f"demo_{record['nickname'].lower().replace(' ', '_')}"
            already_exists = connection.execute(
                "SELECT 1 FROM users WHERE user_id = ?",
                (user_id,),
            ).fetchone()
            if already_exists:
                continue

            connection.execute(
                """
                INSERT INTO users (user_id, nickname, email_optional, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, record["nickname"], "", _now_iso()),
            )
            connection.execute(
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
                    record["q1_answer"],
                    record["q2_answer"],
                    record["q3_answer"],
                    record["q4_answer"],
                    record["q5_answer"],
                    record["q6_answer"],
                    record["pre_belonging_score"],
                    record["challenge_type"],
                    record["identity_id"],
                    _now_iso(),
                ),
            )
            connection.execute(
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
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    record["identity_id"],
                    record["challenge_type"],
                    record["task_id"],
                    record["reflection_text"],
                    record["location_text"],
                    record["pass_forward_note"],
                    record["post_belonging_score"],
                    record["recommendation_score"],
                    int(record["consent_for_wall"]),
                    int(record["approved_for_wall"]),
                    _now_iso(),
                ),
            )
            created_count += 1
    return created_count
