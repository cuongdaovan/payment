# My Site
# Version: 1.0
FROM python:3.6
WORKDIR /payment
# copy the current directory contents into the containers at /payment
COPY . /payment
# copy pipfile  pipfile.lock into /paymment
COPY Pipfile Pipfile.lock ./
RUN pip install -U pipenv
RUN pipenv install --system
EXPOSE 8080
CMD ["python","manage.py","runserver", "0.0.0.0:8080"]