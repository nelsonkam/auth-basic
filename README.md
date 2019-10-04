### ADD STAGING REMOTE
  git remote add dokku-staging dokku@staging.letsjist.com:staging-api

### Add PROD remote
  git remote add dokku-prod dokku@api.letsjist.com:api
  
## ENV VARIABLES
See `.env.example`

## Run in development
Before running the app make sure you have `.env` file with all the environment variables set as shown
in `.env.example`.

```
$ pipenv install
$ pipenv shell
$ flask run --host=0.0.0.0
```

## Migrations

See https://orator-orm.com/docs/0.9/migrations.html

### Make migration
```
orator make:migration name_of_migration
```

### Migration status
```
orator migrate:status -c config.py
```

### Run status
```
orator migrate -c config.py
```

## Workers
This app uses huey as it's task queue. All worker tasks are in the `workers` module.

To run the workers, make sure you have Redis installed on your machine and run the following command:
```
huey_consumer.py workers.huey -k process
```