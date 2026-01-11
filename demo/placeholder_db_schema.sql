-- Placeholder schema for demo purposes only
-- The full schema is included in the Pro version

CREATE TABLE leads (
    id INTEGER PRIMARY KEY,
    name TEXT,
    profile_url TEXT,
    source TEXT,
    status TEXT
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    lead_id INTEGER,
    message_type TEXT,
    sent_at TEXT
);
