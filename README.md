List github issues for the facebook/react repository.

## Requirements
- [Docker](https://docs.docker.com/install/)

#### Github Access Token
- In Github go to Settings -> Developer settings -> Personal access tokens
- No permissions need to be selected

## Local Development
- Copy `config.example.cfg` to `config.cfg`
- Set GITHUB_ACCESS_TOKEN to your access token
- Run Docker with `docker-compose up` or
```
cd app
docker build -t github-issues .
docker run -p 5000:5000 github-issues
```