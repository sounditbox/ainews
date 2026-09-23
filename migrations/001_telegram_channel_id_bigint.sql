-- Telethon channel IDs exceed the range of PostgreSQL INTEGER.
ALTER TABLE news_items
    ALTER COLUMN telegram_channel_id TYPE BIGINT;
