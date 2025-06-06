FROM python:3.11-slim-bullseye

WORKDIR /workspace

# COPY src(your host device) destination(in container)
COPY . /workspace

ENV TZ=Asia/Taipei
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

RUN apt-get update -y
RUN apt-get install curl vim wget procps git -y
RUN apt-get install -y zsh \
    && echo "Y" | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN pip install --upgrade pip
RUN pip install flask

CMD ["flask", "run"]
