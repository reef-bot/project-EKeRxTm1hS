# Filename: settings.py

import sqlite3

# Function to initialize the database for logging moderation actions
def initialize_database():
    conn = sqlite3.connect('logs/moderation_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS moderation_actions (
                action_id INTEGER PRIMARY KEY,
                user_id TEXT NOT NULL,
                action TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

# Function to log moderation actions
def log_action(user_id, action):
    conn = sqlite3.connect('logs/moderation_logs.db')
    c = conn.cursor()
    c.execute('''INSERT INTO moderation_actions (user_id, action) 
                VALUES (?, ?)''', (user_id, action))
    conn.commit()
    conn.close()

# Function to fetch all moderation actions from the database
def get_all_actions():
    conn = sqlite3.connect('logs/moderation_logs.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM moderation_actions''')
    actions = c.fetchall()
    conn.close()
    return actions

# Function to clear all moderation actions from the database
def clear_all_actions():
    conn = sqlite3.connect('logs/moderation_logs.db')
    c = conn.cursor()
    c.execute('''DELETE FROM moderation_actions''')
    conn.commit()
    conn.close()

# Function to get the total number of moderation actions
def get_total_actions():
    conn = sqlite3.connect('logs/moderation_logs.db')
    c = conn.cursor()
    c.execute('''SELECT COUNT(*) FROM moderation_actions''')
    total_actions = c.fetchone()[0]
    conn.close()
    return total_actions

# Initialize the database when the bot starts
initialize_database()