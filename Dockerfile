FROM python:3.7-slim-buster

LABEL "com.github.actions.name"="Release Calendar GitHub Action"
LABEL "com.github.actions.description"="Check whether release allowed or not based on release calendar."
LABEL "com.github.actions.icon"="calendar"
LABEL "com.github.actions.color"="green"

WORKDIR /opt/app

COPY . .

RUN pip install -r requirements.txt \
  && chmod +x entrypoint.sh

ENTRYPOINT ["/opt/app/entrypoint.sh"]
