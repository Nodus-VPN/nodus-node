import docker

from internal import model


class OVPN(model.OVPNInterface):
    def __init__(self):
        self.docker = docker.from_env()
        self.container_name = "openvpn"

    def create_client(self, client_address: str):
        self.docker.containers.get(self.container_name).exec_run(
            f"easyrsa build-client-full {client_address} nopass"
        )

    def get_config(self, client_address: str) -> bytes:
        exit_code, config = self.docker.containers.get(self.container_name).exec_run(
            f"ovpn_getclient {client_address}"
        )
        return config

    def delete_client(self, client_address: str) -> None:
        exit_code, output = self.docker.containers.get(self.container_name).exec_run(
            f"easyrsa revoke {client_address}"
        )
        exit_code, output = self.docker.containers.get(self.container_name).exec_run(
            "easyrsa gen-crl"
        )
        client_files = [
            f"/etc/openvpn/pki/issued/{client_address}.crt",
            f"/etc/openvpn/pki/private/{client_address}.key",
            f"/etc/openvpn/pki/reqs/{client_address}.req"
        ]
        for file_path in client_files:
            self.docker.containers.get(self.container_name).exec_run(f"rm -f {file_path}")

