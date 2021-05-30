rebuild server and run (detached)
```shell
sudo docker-compose up --build -d
```

make migrations
```shell
sudo docker-compose run server bash -c "server/manage.py makemigrations"
```

migrate
```shell
sudo docker-compose run server bash -c "server/manage.py migrate"
```

create superuser
```shell
sudo docker-compose run server bash -c "server/manage.py createsuperuser"
```