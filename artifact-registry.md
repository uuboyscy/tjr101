# Artifact Registry

## Login
1. Create service account with Artifact Registry permission on GCP console
2. Download JSON key
3. Login with JSON key:
    ```shell
    cat artifact-registry-user.json | docker login -u _json_key --password-stdin https://asia-east1-docker.pkg.dev
    ```
    Or
    ```powershell
    Get-Content artifact-registry-user.json | docker login -u _json_key --password-stdin https://asia-east1-docker.pkg.dev
    ```

## Build and push image to your Artifact Registry
- app.py
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "<h1>Hello!</h1>"

    if __name__ == "__main__":
        app.run()
    ```

- flask.Dockerfile
    ```dockerfile
    FROM python:3.11-slim-bullseye

    WORKDIR /workspace

    # COPY src(your host device) destination(in container)
    # COPY . /workspace
    COPY app.py /workspace

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
    ```

- Command to build an image
  ```shell
  docker build -f flask.Dockerfile -t <region>-docker.pkg.dev/<project-id>/<artifact-registry-name>/<image-name>:<image-tag> .
  ```
