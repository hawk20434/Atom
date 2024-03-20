# Atom - учебное консольное приложение 
Тестовое консольное приложение-симулятор для инвестиций выполненое в качестве небольшого учебного задания
- Основная цель: создать декстопное приложения для инвестиций
- Описание: в ходе работы был написани простой код на языке Python, который симулирует деятельность инвестиционного приложения
- Использованные технологии: Python + ООП
- 
------------------------------------
Установка докера:

sudo apt update

sudo apt install apt-transport-https ca-certificates curl softwareproperties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo aptkey add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

sudo apt update

apt-cache policy docker-ce

sudo apt-get install docker-ce docker-ce-cli containerd.io dockerbuildx-plugin docker-compose-plugin

docker --version

sudo systemctl status docker

------------------------------------

Работа после установки докера

git clone https://github.com/abhioncbr/docker-superset.git

cd docker-superset

docker-compose up -d

docker build -t abhioncbr/docker-superset:0.28.0 --build-arg SUPERSET_VERSION=0.28.0 -f docker-files/Dockerfile .

docker pull abhioncbr/docker-superset

docker run -d -p 8088:8088 abhioncbr/docker-superset:0.28.

