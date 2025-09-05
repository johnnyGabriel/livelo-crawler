FROM --platform=$BUILDPLATFORM python:3.13-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["flask", "run"]