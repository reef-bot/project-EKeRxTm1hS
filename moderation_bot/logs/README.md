README.md

# Moderation Logs

This file contains the logs of all moderation actions taken by the Discord bot. The bot logs all moderation activities to ensure transparency and accountability within the server.

The moderation logs are stored in a SQLite database named `moderation_logs.db`, located in the `logs` directory.

Each log entry includes the following information:
- Timestamp of the moderation action
- Action taken (e.g., message deleted, user warned)
- User responsible for the action
- Reason for the action (if provided)
- Additional details (e.g., message content, user ID)

The database schema for the moderation logs is designed to efficiently store and retrieve information about moderation actions. It includes tables for different types of actions and indexes for quick access to specific data points.

The moderation logs can be queried and analyzed to identify patterns, track user behavior, and assess the effectiveness of the bot's moderation strategies.

For any inquiries or issues related to moderation actions, please refer to the moderation logs for detailed information.