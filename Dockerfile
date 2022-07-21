# Here is the build image

FROM python:3.7

MAINTAINER  Phoenix Analytics


# upgrade pip
RUN pip install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /movie_app/requirements.txt

WORKDIR /movie_app

RUN pip install -r requirements.txt

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get install -y wget \
&& apt-get clean

COPY . /movie_app/

EXPOSE 9900
#RUN celery -A api.functions.article_metadata.celery worker --pool=solo -l info -E

#CMD [ "sh", "-c", "gunicorn app:app --bind localhost:9900" ]

#CMD [ "sh", "-c", "gunicorn app:app --bind 0.0.0.0:9900" ]

CMD [ "uwsgi", "app.ini" ]







# FROM python:3.7

# MAINTAINER  Demz Analytics

# # We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /image_scraper/requirements.txt

# WORKDIR /image_scraper

# RUN pip install -r requirements.txt
# # RUN pip install -r requirements.txt --no-cache-dir

# RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y

# COPY . /image_scraper

# RUN . /image_scraper/bash.sh

# EXPOSE 9000
# #RUN celery -A api.functions.article_metadata.celery worker --pool=solo -l info -E

# # CMD [ "sh", "-c", "gunicorn api.app:app --bind 0.0.0.0:9000" ]

# CMD [ "uwsgi", "app.ini" ]
