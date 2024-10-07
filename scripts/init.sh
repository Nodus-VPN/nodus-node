#!/bin/bash

if ! [ -x "$(command -v docker)" ]; then
  apt update -y && apt upgrade -y
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
  sudo install -m 0755 -d /etc/apt/keyrings
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
  sudo chmod a+r /etc/apt/keyrings/docker.asc
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt update -y
  apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
fi

echo ""
echo "-----------------------------------"
echo ""
echo -n "Введите ваш адрес кошелька ERC20: "
read owner_address
OWNER_ADDRESS=$owner_address
echo ""
echo "-----------------------------------"
echo ""

echo ""
echo "-----------------------------------"
echo ""
echo -n "Введите private key от вашего кошелька $OWNER_ADDRESS: "
read owner_private_key
OWNER_PRIVATE_KEY=$owner_private_key
echo ""
echo "-----------------------------------"
echo ""

echo ""
echo "-----------------------------------"
echo ""
NODE_IP=$(wget -q -4 -O- http://icanhazip.com)
echo "Ваш IP: $NODE_IP"
echo ""
echo "-----------------------------------"
echo ""

export OWNER_ADDRESS
export OWNER_PRIVATE_KEY
export NODE_IP

docker compose -f docker/docker-compose.yml up nodus-init --build

if [ $? -ne 0 ]; then
  echo ""
  echo "-----------------------------------"
  echo ""
  echo "Инициализация не удалось,
   не хватает средств для совершения транзакции на запись вашего IP в блокчейн.
   Пополните баланс"
  exit 1
  echo ""
  echo "-----------------------------------"
  echo ""
else
  echo ""
  echo "-----------------------------------"
  echo ""
  echo "Инициализация прошла успешно."
  echo ""
  echo "-----------------------------------"
  echo ""
fi

docker compose -f docker/docker-compose.yml up --build
