FROM django:python2
WORKDIR /musicwalletproject
COPY . /musicwalletproject
RUN pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver","0.0.0.0:8000", "--settings=musicwalletproject.settings.development" ]
