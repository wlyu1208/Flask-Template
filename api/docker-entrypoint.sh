dockerize -wait tcp://db:5432 -timeout 20s

if [ $IS_INIT -eq 1 ]
then
    flask storage init
    flask db init
    env IS_INIT=0
    flask db migrate
    flask db upgrade
elif [ $IS_INIT -eq 2 ]
then
    flask db migrate
    flask db upgrade
fi

gunicorn -b 0.0.0.0:5000 -w 2 --timeout=30 "flaskapp:create_app()"
