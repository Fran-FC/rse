# our base image
FROM alpine

# Install python and pip
RUN apk add --update py3-pip

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
RUN pip install -U paho-mqtt

# copy files required for the app to run
COPY sisub.py /usr/src/app/

# run the application
CMD ["python3", "/usr/src/app/sisub.py"]
