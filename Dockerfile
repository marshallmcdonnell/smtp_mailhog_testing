FROM python:3.6

RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv install --dev
ENTRYPOINT ["pipenv", "run"]
CMD ["python"]
