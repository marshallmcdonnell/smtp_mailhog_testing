| CI | License |
|----|---------|
| [![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fmarshallmcdonnell%2Fsmtp_mailhog_testing%2Fbadge%3Fref%3Dmaster&style=flat)](https://actions-badge.atrox.dev/marshallmcdonnell/smtp_mailhog_testing/goto?ref=master) | [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) |
# smtp_mailhog_testing

Working examples of testing a Python mail client using SMTP (using [smtplib](https://docs.python.org/3.6/library/smtplib.html)  with the [MailHog](https://github.com/mailhog/MailHog) Web and API SMTP testing utility

## To test

0) Install [docker-comopse](https://docs.docker.com/compose/install/) and [pipenv](https://pipenv.readthedocs.io/en/latest/)
1) Install via: `pipenv install --dev`
2) Run docker compose via: `docker-compose up`

# Tutorial

Excellent RealPython [tutorial](https://realpython.com/python-send-email/) for sending emails with Python
