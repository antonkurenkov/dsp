#Shell commands
___
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
___
#Obtain access token

_Request:_
```
POST /api/token/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Content-Length: 52

{
    "username": "admin",
    "password": "admin"
}
```
_Response:_
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMjQ2NTQ0MywianRpIjoiN2M0ZmI4OWI1MzhkNDJjODg1YWZiZmRjZjlkMDIwZTkiLCJ1c2VyX2lkIjoxfQ.cwl-DGEEu3IM4cDgEJXZC_TQ27W1Vmfrta4_lyWOfyo",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyMzc5MzQzLCJqdGkiOiJjMjZmMTlmODBhOTc0Zjc5OGNjZGI5ODY0NWIwYTU2YiIsInVzZXJfaWQiOjF9.WY_VtvVEfxNombCP8KZKUDWTCVl0RKQ4_Qdbwo3oQPA"
}
```

sudo ssh -i /home/antonkurenkov/.ssh/id_rsa ubuntu@52.59.214.105