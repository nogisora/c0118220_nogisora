FROM python:3.6

WORKDIR ./app/copy 

RUN apt-get update && apt-get -y install vim

COPY . /app
RUN pip install -r /app/requirements.txt

ENV PORT 4000
EXPOSE 4000

CMD ["python3", "/app/test2.py"]
