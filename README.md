# tjr101

# Docker
- [Docker Tutorial](https://docs.uuboyscy.dev/docs/category/docker-tutorial)
## Docker Commands
- Download a image
    - docker pull <image_name>:<tag>
- Start container
    - docker run -it -d --name <container_name> <image_name>:<tag> /bin/bash
- Enter a running container
    - docker exec -it <container_name> /bin/bash
- Exit a container (See cursor to check if you are in a container)
    - Press CTRL + D
- Check container status
    - docker ps
    - docker ps -a (-a means showing all containers)

## Dockerfile
If you want to customize your own image from base image. \
Write steps of commands in it, then execute following commands to build a new image.
```
docker build -f <dockerfile_name> -t <image>:<tag> .
```
Then follow the steps above (## docker) to run a container.

# Data Pipeline
- [What is ETL](https://docs.uuboyscy.dev/docs/Data%20Pipeline/What%20is%20ETL)
- [Pandas Tutorial](https://docs.uuboyscy.dev/docs/category/pandas-tutorial)

## MySQL connection
- Create a MySQL container
```
docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=passWord -p 3306:3306 mysql:latest
```

## CRUD
- C: Create -> INSERT
- R: Read -> SELECT
- U: Update -> UPDATE
- D: Delete -> DELETE

# Project Management
- [Poetry](https://docs.uuboyscy.dev/docs/Python/Project%20Management/Virtual%20Environment/Poetry)
