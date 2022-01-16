FROM ubuntu:focal
RUN apt-get update
RUN apt-get install python3-pip -y
WORKDIR /usr/app
COPY . .
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate --noinput
CMD python3 manage.py runserver 0.0.0.0:8000
