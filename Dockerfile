FROM --platform=$BUILDPLATFORM python:3.13-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=8000
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8000

CMD ["flask", "run"]