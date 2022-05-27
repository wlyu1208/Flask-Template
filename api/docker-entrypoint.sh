dockerize -wait tcp://db:5432 -timeout 20s

if [ $DB_STATUS -eq 1 ]
then
    flask storage init
    flask db init
    env DB_STATUS=0
    flask db migrate
    flask db upgrade
elif [ $DB_STATUS -eq 2 ]
then
    flask db migrate
    flask db upgrade
fi

gunicorn -b 0.0.0.0:5000 -w 2 --timeout=30 --preload "flaskapp:create_app()"
