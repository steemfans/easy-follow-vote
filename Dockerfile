FROM ety001/steem-python:latest

WORKDIR /app
ADD run.py /app/run.py

CMD ["/app/run.py"]
