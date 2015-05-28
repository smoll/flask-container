# TODO: move this to web/Dockerfile-dev when the 'dockerfile' keyword makes it into a stable docker-compose release
# i.e. https://github.com/docker/compose/blob/1.3.0rc1/docs/yml.md#dockerfile
# same as web Dockerfile, but with additional test dependencies
FROM python:3.4.3

# expose port app is running on
EXPOSE 5000

# install runtime dependencies
RUN apt-get -y update

# install dev dependencies
RUN apt-get install -y \
	iceweasel \
	xvfb

# for xvfb to work
ENV DISPLAY :1

# add code
ADD web /code

# install requirements.txt
RUN pip install -r /code/requirements.txt

# install dev-requirements.txt
RUN pip install -r /code/dev-requirements.txt

# set working diretory
WORKDIR /code
