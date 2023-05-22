FROM tensorflow/tensorflow:latest-gpu

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt
CMD python index.py