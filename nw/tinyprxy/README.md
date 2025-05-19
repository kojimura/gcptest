# create a proxy server in Windows using docker

1. create config file
```   
tinyproxy.conf
Dockerfile
```
2. build the docker image
```
docker build --no-cache -t dummy-proxy .
```
3. run docker container
```
docker run -d -p 127.0.0.1:8888:8888 --name dummy-proxy dummy-proxy
```
4. set proxy
```
127.0.0.1:8888
```
5. maintenance
```
docker stop dummy-proxy
docker start dummy-proxy
docker rm dummy-proxy
```
