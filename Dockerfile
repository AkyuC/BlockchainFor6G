FROM python:3.9

RUN apt-get update && apt-get install -y npm

RUN pip install flask && update-ca-certificates

WORKDIR /root/

COPY . .

EXPOSE 8080

# run application
CMD ["python", "app.py"]