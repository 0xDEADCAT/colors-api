# colors-api
## Deployment

You can run the application in a container or in your local environment.

### Use the container image from Docker Hub
1. Install `podman`, if it's not already installed
2. Run the container `podman run -dp 8080:8080 docker.io/0xdeadcat/colors-api:v1`
3. In your browser, navigate to `localhost:8080`

### Build the container image using podman

1. Install `podman`, if it's not already installed
2. Clone the repository: `git clone https://github.com/0xDEADCAT/colors-api.git`
3. Navigate inside the cloned repository: `cd colors-api`
4. Using the command `podman build -t colors-api .` build the container
5. Run the container `podman run -dp 8080:8080 colors-api`
6. In your browser, navigate to `localhost:8080`

### Use your host OS

1. Install `python3.9`, if it's not already installed
2. Install pipenv using pip `pip install pipenv`
3. Clone the repository: `git clone https://github.com/0xDEADCAT/colors-api.git`
4. Navigate inside the cloned repository: `cd colors-api`
5. Run `pipenv install`
6. Once all dependencies are installed, run `pipenv shell`
7. Run the database setup script `python database_setup.py`
8. Start the application  `uwsgi --ini uwsgi.ini`
9. In your browser, navigate to `localhost:8080`

## REST API documentation
The documentation of the REST API is available inside the Swagger UI provided by the application.
Once the application is running, simply navigate to `localhost:8080` using your browser to view it.