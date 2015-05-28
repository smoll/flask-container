# start with a base image
FROM python:3.4.3

# expose port app is running on
EXPOSE 5000

# install runtime dependencies
RUN apt-get -y update

# add code
ADD . /code

# install requirements.txt
RUN pip install -r /code/requirements.txt

# set working diretory
WORKDIR /code
