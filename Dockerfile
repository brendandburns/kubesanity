FROM python:3.6-alpine

RUN pip install kubernetes

COPY *.py /

CMD python /kube_sanity.py 
