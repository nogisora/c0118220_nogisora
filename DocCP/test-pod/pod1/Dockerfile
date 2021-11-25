FROM python:3.6

WORKDIR ./app/copy

RUN apt-get update && apt-get -y install vim

COPY . /app
RUN pip install -r /app/requirements.txt

ENV PORT 3100
EXPOSE 3100

CMD ["python3", "/app/main.py"]

