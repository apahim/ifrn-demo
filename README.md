# Cloudy

Demo Web Application

## Quickstart

To execute the application from Docker, run:

```bash
$ docker run --rm -it -p 8080:8080 docker.io/apahim/cloudy:ifrn
```

## Develop

Create a virtualenv and activate it:

```bash
$ python3 -v venv venv
$ source venv/bin/activate
```

Install the package in develop mode:

```bash
(venv) $ pip install -r requirements.txt
```

Run the service:

```bash
(venv) $ python cloudy/app.py 
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
INFO:werkzeug: * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 489-782-097
```

Send a GET request to the service:

```bash
(venv) $ curl localhost:8080
{
  "hostname": "t590"
}
```

## Build and Publish

The application is distributed as a Docker image. To build the image, run:

```bash
$ docker build -t <registry/repository/image:tag> .
``` 

To publish, run:

```bash
$ docker push <registry/repository/image:tag>
``` 