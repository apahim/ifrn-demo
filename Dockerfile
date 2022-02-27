FROM        centos/python-36-centos7

WORKDIR     /cloudy

COPY        . ./

RUN         pip install .

ENTRYPOINT  ["gunicorn", "cloudy.app:APP", "--bind", "0.0.0.0:8080"]
CMD         ["--workers", "1", "--threads",  "1"]
