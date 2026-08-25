import os
import psycopg2
import requests
from flask import Flask, jsonify

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
HELIUS_API_KEY = os.environ.get("HELIUS_API_KEY")


def get_conn():
    return psycopg2.connect(DATABASE_URL)


def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS dev_history_cache (
            deployer_wallet TEXT PRIMARY KEY,
            past_tokens JSONB,
            checked_at TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    c.close()
    conn.close()


def get_token_creator(mint):
    """Find the closest identifiable deployer wallet for a token."""
    # Placeholder — needs real Helius call to find mint authority
    # and/or first significant supply recipient
    pass


@app.route("/")
def home():
    return "HolderScore bot running"


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
