FROM python:3.7-slim-buster

WORKDIR /opt/app

COPY . .

RUN pip install -r requirements.txt \
  && chmod +x entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]
