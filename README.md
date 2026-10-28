Deploy on server with docker:
- git clone the repo
- install docker.io and docker-compose
- docker-compose up --build -d (if there're changes, git pull and use this command again)

without docker-compose:
- docker build -t help-oc .
- docker run -d -p 8080:80 help-oc
