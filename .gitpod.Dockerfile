FROM python:3.7
RUN apt update -y && apt upgrade -y
RUN apt install zsh -y
RUN pip install pipenv
