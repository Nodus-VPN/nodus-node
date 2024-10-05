create_wg_client = """
INSERT INTO clients (address, wg_id)
VALUES (:client_address, :client_wg_id)
RETURNING id;
"""