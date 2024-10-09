create_wg_client = """
INSERT INTO clients (address, wg_id)
VALUES (:client_address, :client_wg_id)
RETURNING id;
"""

delete_wg_client_query = """
DELETE FROM clients
WHERE client_wg_id = :client_wg_id;
"""

client_by_address = """
SELECT * FROM clients
WHERE address = :client_address
"""