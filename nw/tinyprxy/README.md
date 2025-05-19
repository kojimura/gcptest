# create a proxy server in Windows using docker

1. create config file
```   
tinyproxy.conf
Dockerfile
```
2. build the docker image
```
docker build --no-cache -t idummy-proxy .
```
3. run docker container
```
docker run -d -p 127.0.0.1:8888:8888 --name dummy-proxy idummy-proxy
docker ps -a
docker image ls
docker logs -t <container-id>
docker run -it --entrypoint /bin/sh dummy-proxy
docker rm dummy-proxy
docker image rm <image:tag>
```
4. set proxy
```
127.0.0.1:8888
```
5. maintenance
```
docker stop dummy-proxy
docker start dummy-proxy
```
