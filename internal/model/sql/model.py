create_clients_table_query = """
CREATE TABLE IF NOT EXISTS clients (
id SERIAL PRIMARY KEY,

wg_id TEXT UNIQUE DEFAUlT NONE,
ovpn_id TEXT UNIQUE DEFAUlT NONE,
address TEXT NOT NULL,
traffic INTEGER DEFAULT 0,

latest_handshake TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

create_on_update_table_func_query = """
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';
"""

on_update_clients_query = """
CREATE TRIGGER update_updated_at_trigger
BEFORE UPDATE ON clients
FOR EACH ROW
EXECUTE PROCEDURE update_updated_at();
"""

create_queries = [
    create_clients_table_query,
    create_on_update_table_func_query,
    on_update_clients_query,
]
