Basic math operation project
============================
This project deploys django application with nginx that allows to do math operations with API calls and view history of them stored in the Postgres DB.
(Only deployment is done and test endpoint)

## Deployment

1. Change env value in the: `operations_django/operations.env` 
2. Run docker compose: `docker-compose up`
