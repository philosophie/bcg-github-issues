List github issues for the facebook/react repository.

## Requirements
- [Docker](https://docs.docker.com/install/)

#### Github Access Token
- In Github go to Settings -> Developer settings -> Personal access tokens
- No permissions need to be selected

## Local Development
- Copy `config.example.cfg` to `config.local.cfg`
- Set GITHUB_ACCESS_TOKEN to your access token
- Run Docker with `docker-compose up`

## Staging Deployment
- Ensure `config.example.cfg` is defined in the `app/` directory. This would typically be stored in 1password or ansible vault.
- `docker-compose -f docker-compose-staging.yml build`