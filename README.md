# flask-container

Following along with [this](https://realpython.com/blog/python/docker-in-action-fitter-happier-more-productive/) RealPython article...

## Usage

Start flask app and redis db with

```
$ docker-compose up
```

View the site at [http://localhost:5000/](http://localhost:5000/) if running Docker natively (i.e. on a Linux host) or, if running remote docker on a VM (e.g. boot2docker) do `$ echo $DOCKER_HOST` or `$ boot2docker ip` to get host, will probably be http://192.168.59.103:5000/