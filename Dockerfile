FROM tiangolo/uwsgi-nginx-flask:python3.11
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app app
COPY ./migrations migrations
COPY ./config.py config.py
COPY ./app.db app.db
COPY ./.flaskenv .flaskenv
COPY ./main.py main.py
