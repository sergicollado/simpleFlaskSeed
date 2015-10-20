install
-------

    # create a virtual env
    mkvirtualenv envName
    workon envName

    # install requeriments
    pip install -d config/requeriments/dev.txt

migrations
----------

    python manage.py db init        #create database
    python manage.py db migrate     #create migrations
    python manage.py db upgrade     #make database changes with last migrations

run app
-------

    python run.py
