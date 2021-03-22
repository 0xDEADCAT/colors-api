FROM python:3
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy
RUN python database_setup.py
EXPOSE 8080
CMD ["uwsgi", "--ini", "uwsgi.ini"]