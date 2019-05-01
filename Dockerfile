FROM python:3.6-alpine

RUN adduser -D quiltpos

WORKDIR /home/quiltpos

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY pos.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP pos.py

RUN chown -R quiltpos:quiltpos ./
USER quiltpos

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]