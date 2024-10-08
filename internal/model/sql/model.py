create_clients_table_query = """
CREATE TABLE IF NOT EXISTS clients (
id SERIAL PRIMARY KEY,

wg_id TEXT DEFAUlT NULL,
ovpn_id TEXT DEFAUlT NULL,
address TEXT NOT NULL,

created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
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

drop_clients_table_query = """
DROP TABLE IF EXISTS clients;
"""

drop_on_update_clients_trigger_query = """
DROP TRIGGER IF EXISTS update_updated_at_trigger ON clients;
"""

create_queries = [
    create_clients_table_query,
    create_on_update_table_func_query,
    on_update_clients_query,
]

drop_queries = [
    drop_clients_table_query,
    drop_on_update_clients_trigger_query,
]
