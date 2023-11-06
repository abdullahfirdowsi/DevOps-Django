# DevOps-Django

[06/11, 8:10 am] ...: docker --version
[06/11, 8:10 am] ...: wsl --update
[06/11, 8:10 am] ...: docker pull monjo
[06/11, 8:10 am] ...: docker images
[06/11, 8:10 am] ...: docker run monjo
[06/11, 8:11 am] ...: docker run -d monjo
[06/11, 8:11 am] ...: docker ps
[06/11, 8:11 am] ...: docker ps -a
[06/11, 8:11 am] ...: docker stop 4____
[06/11, 8:12 am] ...: docker start 4_____
[06/11, 8:12 am] ...: docker logs 4_____
[06/11, 8:12 am] ...: docker pull mongo-express
[06/11, 8:13 am] ...: docker ps -a
[06/11, 8:13 am] ...: docker run --name skill -d mongo-express
[06/11, 8:13 am] ...: docker network create mongo-network
[06/11, 8:15 am] ...: docker run -p 27017:27017 -d -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=admin --name mongodb --net mongo-network mongo
[06/11, 8:18 am] ...: docker run --network mongo-network -e ME_CONFIG_MONGODB_SERVER=mongodb -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=admin -p 8081:8081 mongo-express
