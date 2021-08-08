FROM python:3.7

ENV PYTHONIOENCODING utf-8
ENV TZ='Asia/Tokyo'

WORKDIR /app

RUN mkdir /app/src
RUN mkdir /app/data

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y apt-utils
RUN pip install --upgrade pip

RUN pip install requests
RUN pip install requests_oauthlib
RUN pip install pandas
RUN pip install python-dotenv

RUN export LANG=C.UTF-8
RUN export LANGUAGE=en_US:

CMD ["python", "src/main.py"]
