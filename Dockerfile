FROM python:3.7-slim

RUN adduser bothub

WORKDIR /home/bothub

RUN apt update
RUN apt install git -y
RUN git clone https://github.com/gunthercox/chatterbot-corpus
COPY requirements.txt requirements.txt
RUN mkdir databases
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
RUN venv/bin/python -m spacy download en
RUN venv/bin/python -m spacy download pt


COPY app app
COPY migrations migrations
COPY bothub.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP bothub.py

RUN chown -R bothub:bothub ./
USER bothub

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
