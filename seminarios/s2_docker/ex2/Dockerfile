FROM alpine
RUN apk add --update py3-pip
RUN pip install -U Flask

COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/ 

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]
