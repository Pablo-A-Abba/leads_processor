FROM python3.11

RUN apt-get update && apt-get upgrade -y

ENV PORT=8080

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 --capture-output "app:create_app()"