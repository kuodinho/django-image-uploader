Migrations have been already applied, to that it is possible to fetch thumbnails from the start.

There are two way to start the app using the virual environement or Docker. This README describes only how to start the app using:
A) Docker:

1. Install [docker](https://docs.docker.com/desktop/install/mac-install/).
2. Using the terminal navigate to the repository and run:
```
docker-compose build
```
3. After the build is finished run:
```
docker-compose run
```

Now you have a running Docker container with the application.

B) GitHub:
1. Clone the repository
2. Create a virtual environment to isolate our package dependencies locally in terminal:
```
python3 -m venv env
```
```
source env/bin/activate
```
3. Install requirements.txt
```
pip install -r requirements.txt
```

To list the already added thumbnails you can use:

```
curl --location 'localhost:8000/thumbnails/' -u login:password
```

Post a new one:
```
curl --location 'localhost:8000/thumbnails/' \
--form 'title="test from postman"' \
--form 'image=@"{{path/to/image}}"' \
-u login:password
```

Available users (login:password):
- `admin:admin`
- `user:asdzxcqwe`
