FROM python:3.6-alpine

RUN adduser -D translate_api

WORKDIR /home/translate_api

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY translate.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP translate.py

RUN chown -R translate_api:translate_api ./
USER translate_api

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]