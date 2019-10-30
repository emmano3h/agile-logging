FROM pypy:3-6

WORKDIR /usr/src/app

# Bundle app source
COPY python-app-test/ /usr/src/app


RUN apt-get update

RUN apt-get install -y supervisor

# install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p /var/log/supervisor
RUN mkdir -p /usr/src/logs
COPY python-app-test/src/conf/agilecx.conf /etc/supervisor/conf.d/supervisord.conf


EXPOSE 611

VOLUME ["/usr/src/app"]

# run supervisord

CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf