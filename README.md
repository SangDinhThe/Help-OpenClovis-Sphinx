Deploy on server with docker:
- git clone the repo
- install docker: apt install docker.io
- build docker image: docker build -t help-oc .
- start container: docker run -d -p 80:80 help-oc


Update if there're changes:
- git pull
- docker compose up --build -d
