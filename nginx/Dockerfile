FROM nginx

RUN apt update && apt install -y wget unzip

RUN wget https://github.com/twbs/bootstrap/releases/download/v5.1.0/bootstrap-5.1.0-dist.zip

RUN mkdir -p /var/django/static/vendor

RUN unzip bootstrap-5.1.0-dist.zip -d /var/django/static/vendor 
