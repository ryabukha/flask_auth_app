FROM tiangolo/uwsgi-nginx-flask:python3.8
ENV STATIC_URL /static
ENV STATIC_PATH /app/static
COPY ./requirements.txt /var/www/requirements.txt
COPY ./app /app
RUN pip install -r /var/www/requirements.txt
RUN python3 init_database.py