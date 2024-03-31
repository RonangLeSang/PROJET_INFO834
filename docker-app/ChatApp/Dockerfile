FROM alpine

# Définit le répertoire de travail
WORKDIR /home

COPY entrypoint.sh /
COPY . /home

RUN chmod +x /entrypoint.sh

RUN apk add --update --no-cache python3 && \
    apk add py3-pip &&\
    apk add --no-cache tzdata

RUN python3 -m venv venv  &&\ 
    source venv/bin/activate &&\
    pip install -r requirements.txt &&\
    deactivate

RUN apk add npm && \
    npm install -D tailwindcss && \
    npm install -g flowbite

EXPOSE 8000


ENTRYPOINT ["/entrypoint.sh"]



