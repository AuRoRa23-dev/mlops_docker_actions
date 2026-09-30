# Student Management REST API

Simple Flask API for retrieving and adding student records. Data is stored in memory, so it resets whenever the server restarts.

## Run with Docker

Build and start the API from the project directory:

```powershell
docker build -t student-management-api .
docker run --rm -p 5000:5000 student-management-api
```

The API is available at `http://localhost:5000`. The container includes only
`app.py` and its runtime dependencies; `test_app.py` and local virtual
environments are excluded.

## Postman requests

### Check the API

- Method: `GET`
- URL: `http://127.0.0.1:5000/`

### Get all students

- Method: `GET`
- URL: `http://127.0.0.1:5000/students`

### Add a student

- Method: `POST`
- URL: `http://127.0.0.1:5000/students`
- Body: `raw` -> `JSON`

```json
{
  "name": "Chris Lee",
  "course": "Cybersecurity"
}
```

## Publish to Docker Hub with GitHub Actions

1. In Docker Hub, create an access token with read and write permissions.
2. In the GitHub repository, open **Settings > Secrets and variables > Actions** and add these repository secrets:
  - `DOCKERHUB_USERNAME`: your Docker Hub username.
  - `DOCKERHUB_TOKEN`: the Docker Hub access token. Do not commit the token to the repository.
3. Push to any branch, or run **Build and push Docker image** from the repository's **Actions** tab.

The workflow runs `test_app.py` before building, but the Docker image itself only
contains `app.py` and its runtime dependencies. On success, it publishes
`<dockerhub-username>/student-management-api:latest` and a tag matching the
commit SHA to Docker Hub.

## Run tests locally

```powershell
\.\venv\Scripts\python.exe -m unittest -v
```