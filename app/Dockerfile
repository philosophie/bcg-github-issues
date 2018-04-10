FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

ENV FLASK_CONFIG_FILE config.local.cfg

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]