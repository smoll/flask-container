# flask-container [![Circle CI](https://circleci.com/gh/smoll/flask-container.svg?style=svg)](https://circleci.com/gh/smoll/flask-container)

Following along with [this](https://realpython.com/blog/python/docker-in-action-fitter-happier-more-productive/) RealPython article...

## Usage

Start flask app and redis db with

```
$ docker-compose up
```

View the site at [http://localhost:80/](http://localhost:80/) if running Docker natively (i.e. on a Linux host) or, if running remote docker on a VM (e.g. boot2docker) do `$ echo $DOCKER_HOST` or `$ boot2docker ip` to get host, it will probably be [http://192.168.59.103:80/](http://192.168.59.103:80/)

## Tests

Run tests on your dev env with

```
$ docker-compose run web python tests.py
```

## Debugging

In order for a `pdb` breakpoint to work, start the web container with

```
docker-compose run --service-ports web
```
