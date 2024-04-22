FROM nginx:latest

RUN apt-get update && \
    apt-get install -y procps

COPY default.conf /etc/nginx/conf.d/default.conf

COPY index.html /usr/share/nginx/html/index.html

COPY log-observe.sh /usr/local/bin/

COPY log-observe.py /usr/local/bin/

RUN chmod +x /usr/local/bin/log-observe.sh

RUN chmod +x /usr/local/bin/log-observe.py

EXPOSE 80

CMD service nginx start && /usr/local/bin/log-observe.sh

