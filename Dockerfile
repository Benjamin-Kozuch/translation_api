FROM python:3.6-alpine

RUN adduser -D translation_api

WORKDIR /home/translation_api

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY translation_api.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP translation_api.py

RUN chown -R translation_api:translation_api ./
USER translation_api

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]