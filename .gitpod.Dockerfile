FROM python:3.7
RUN apt update -y && apt upgrade -y
RUN apt install zsh -y
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
RUN chsh -s $(which zsh)
RUN pip install pipenv
