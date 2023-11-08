https://hub.docker.com/repository/docker/eugene8pro/eupoetry/general

#bash

# build
docker build -t eupoetry:1.0 .

# logs 
docker logs 27e012f8f18b

# check
docker run -dp 8080:8008 eupoetry:1.0

#docker tag
docker tag eupoetry:1.0 eugene8pro/eupoetry:1.0

#docker push
docker login
docker push eugene8pro/eupoetry:1.0
