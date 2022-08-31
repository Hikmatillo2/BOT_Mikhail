FROM ubuntu
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y nginx python3 python3-pip gunicorn sudo net-tools nano
COPY main /srv/main
WORKDIR /srv/main
RUN pip3 install -r requirements.txt
RUN service nginx stop
RUN cp /srv/main/nginx.conf /etc/nginx/sites-available/default
RUN python3 manage.py collectstatic --noinput
RUN chown -R www-data:www-data /srv/main
RUN chmod +x /srv/main/run.sh
EXPOSE 88:88
ENTRYPOINT /srv/main/run.sh
