import sqlite3
from models.memory import ConversationEntry
from typing import List
from datetime import datetime, UTC

DB_PATH = 'data/ai_companion.db'

def _get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    with _get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                message TEXT NOT NULL,
                response TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                mood TEXT
            )
        ''')
        conn.commit()

def save_conversation(entry: ConversationEntry):
    with _get_connection() as conn:
        conn.execute(
            '''
            INSERT INTO conversations (user_id, message, response, timestamp, mood)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (entry.user_id, entry.message, entry.response, entry.timestamp.isoformat(), entry.mood)
        )
        conn.commit()

def get_conversations(user_id: str, limit: int = 10) -> List[ConversationEntry]:
    with _get_connection() as conn:
        cursor = conn.execute(
            '''
            SELECT user_id, message, response, timestamp, mood
            FROM conversations
            WHERE user_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
            ''',
            (user_id, limit)
        )
        rows = cursor.fetchall()

    return [
        ConversationEntry(
            user_id=row['user_id'],
            message=row['message'],
            response=row['response'],
            timestamp=datetime.fromisoformat(row['timestamp']).astimezone(UTC),
            mood=row['mood']
        ) for row in rows
    ]

# Initialize DB at import time
initialize_database()

