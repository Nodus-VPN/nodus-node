#!/bin/bash

#apt update -y && apt upgrade -y
#
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
#sudo install -m 0755 -d /etc/apt/keyrings
#sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
#sudo chmod a+r /etc/apt/keyrings/docker.asc
#echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#sudo apt update -y
#apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

echo -n "Введите ваш адрес кошелька ERC20: "
read owner_address
OWNER_ADDRESS=owner_address
echo "Ваш кошелек: $OWNER_ADDRESS"

echo -n "Введите private key от вашего кошелька $owner_address: "
read owner_private_key
OWNER_PRIVATE_KEY=owner_private_key
echo "Private key от вашего кошелька $OWNER_ADDRESS: $OWNER_PRIVATE_KEY"

NODE_IP=$(wget -q -4 -O- http://icanhazip.com)
echo "Ваш IP: $NODE_IP"

export OWNER_ADDRESS
export OWNER_PRIVATE_KEY
export NODE_IP
docker compose -f docker/docker-compose.yml up nodus-init --build


#docker network create net
#docker run -d \
#  --name=wg-easy \
#  --network=net \
#  -e WG_HOST=$(wget -q -4 -O- http://icanhazip.com) \
#  -v ~/.wg-easy:/etc/wireguard \
#  -p 51820:51820/udp \
#  -p 51821:51821/tcp \
#  --cap-add=NET_ADMIN \
#  --cap-add=SYS_MODULE \
#  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
#  --sysctl="net.ipv4.ip_forward=1" \
#  --restart unless-stopped \
#  ghcr.io/wg-easy/wg-easy