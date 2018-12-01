<img alt="Open book logo" src="https://snag.gy/yWbLr1.jpg" width="200">

[![CircleCI](https://circleci.com/gh/OpenbookOrg/openbook-api.svg?style=svg&circle-token=b41cbfe3c292a3e900120dac5713328b1e754d20)](https://circleci.com/gh/OpenbookOrg/openbook-api) [![Maintainability](https://api.codeclimate.com/v1/badges/5e6ae40e9d945cad0591/maintainability)](https://codeclimate.com/repos/5bbf4878e46c0d3b620000a2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/5e6ae40e9d945cad0591/test_coverage)](https://codeclimate.com/repos/5bbf4878e46c0d3b620000a2/test_coverage) [![gitmoji badge](https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square)](https://github.com/carloscuesta/gitmoji)


The API server for Openbook.

## Table of contents

- [Requirements](#requirements)
- [Project overview](#project-overview)
- [Contributing](#contributing)
    + [Code of Conduct](#code-of-conduct)
    + [License](#license)
    + [Other issues](#other-issues)
    + [Git commit message conventions](#git-commit-message-conventions)
- [Getting started](#getting-started)
  + [Docker](#docker)
- [FAQ](#faq)
    + [Double logging in console](#double-logging-in-console)

## Requirements

* [Pipenv](https://github.com/pypa/pipenv)

## Project overview

The project is a [Django](https://www.djangoproject.com/start/) application. 

## Contributing

There are many different ways to contribute to the website development, just find the one that best fits with your skills and open an issue/pull request in the repository.

Examples of contributions we love include:

- **Code patches**
- **Bug reports**
- **Patch reviews**
- **Translations**
- **UI enhancements**

#### Code of Conduct

Please read and follow our [Code of Conduct](https://github.com/OpenBookOrg/openbook-api/blob/master/CODE_OF_CONDUCT.md).

#### License

Every contribution accepted is licensed under [AGPL v3.0](http://www.gnu.org/licenses/agpl-3.0.html) or any later version. 
You must be careful to not include any code that can not be licensed under this license.

Please read carefully [our license](https://github.com/OpenBookOrg/openbook-org-backend/blob/master/LICENSE.txt) and ask us if you have any questions.

#### Responsible disclosure

Cyber-hero? Check out our [Vulnerability Disclosure page](https://www.open-book.org/en/vulnerability-report).

#### Other issues

We're available almost 24/7 in the Openbook slack channel. [Join us!](https://join.slack.com/t/openbookorg/shared_invite/enQtNDI2NjI3MDM0MzA2LTYwM2E1Y2NhYWRmNTMzZjFhYWZlYmM2YTQ0MWEwYjYyMzcxMGI0MTFhNTIwYjU2ZDI1YjllYzlhOWZjZDc4ZWY)

#### Git commit message conventions

Help us keep the repository history consistent 🙏!

We use [gitmoji](https://gitmoji.carloscuesta.me/) as our git message convention.

If you're using git in your command line, you can download the handy tool [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli).

## Getting started

#### Clone the repository

```sh
git clone git@github.com:OpenbookOrg/openbook-api.git
```

#### Create and configure your .env file

```bash
cp .env.sample .env
nano .env
```

#### Install the dependencies
```bash
pipenv install
```

#### Activate the pipenv environment
```bash
pipenv shell
```

#### Run the database migrations
```bash
python manage.py migrate
```

#### Load the fixtures
```bash
python manage.py loaddata circles.json emoji-groups.json emojis.json
```

#### Serve with hot reload at http://127.0.0.1:8000
```bash
python manage.py runserver
```

<br>

## Docker
If you love containerization and you want to keep your local environment clean you can run Openbook API server inside Docker! <br>
The `docker-compose.yml` contains two services: one mysql container and one python container. <br>
Your local copy of Openbook API it's mirrored inside the container, this means you can work from your favourite IDE and check immediatly the results. <br>
Add inside the `.env` file created above, the following lines in order to have the mysql container properly configured:
```text
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_PASSWORD=changeMe
MYSQL_USER=openbookuser
MYSQL_ROOT_PASSWORD=changeMe
MYSQL_DATABASE=openbook_api_db
```
To build/start/stop the containers use the `Makefile` corresponding task: <br>
```makefile
build_openbook_api
start_openbook_api
stop_openbook_api
clean_openbook_api
logs_openbook_api
```
Example:
```commandline
make build_openbook_api
```
**NB**: To execute any python command against the running container you should connect to the container. <br>
Example:
```commandline
docker exec -i -t openbook-api_web_1 /bin/bash 
root@c770f4607a97:/code# python manage.py migrate
```
## FAQ

### Double logging in console

The local development server runs a separate process for the auto-reloader. You can turn off the auto-reload process by passing the --noreload flag.

````bash
python manage.py runserver --noreload
````

#### Happy coding 🎉!

