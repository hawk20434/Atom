# Atom - учебное консольное приложение 
Тестовое консольное приложение-симулятор для инвестиций выполненое в качестве небольшого учебного задания
- Основная цель: создать декстопное приложения для инвестиций
- Описание: в ходе работы был написани простой код на языке Python, который симулирует деятельность инвестиционного приложения
- Использованные технологии: Python + ООП



git clone https://github.com/abhioncbr/docker-superset.git

cd docker-superset

docker build -t abhioncbr/docker-superset:0.29.0rc4 --build-arg SUPERSET_VERSION=0.29.0rc4 -f docker-files/Dockerfile .

docker run -p 8088:8088 abhioncbr/docker-superset:0.29.0rc4





apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
docker --version
