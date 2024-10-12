# WG
create_wg_client = """
INSERT INTO clients (address, wg_id)
VALUES (:client_address, :client_wg_id)
RETURNING id;
"""

set_wg_client = """
UPDATE clients
SET wg_id = :client_wg_id
WHERE address = :client_address
"""

# OVPN
create_ovpn_client = """
INSERT INTO clients (address, ovpn_id)
VALUES (:client_address, :client_ovpn_id)
RETURNING id;
"""

set_ovpn_client = """
UPDATE clients
SET ovpn_id = :client_address
WHERE address = :client_address
"""


# GENERAl
delete_client_query = """
DELETE FROM clients
WHERE address = :client_address;
"""

client_by_address = """
SELECT * FROM clients
WHERE address = :client_address
"""