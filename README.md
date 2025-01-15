# Introduction
使用 Dockerfile 製作 Flask 開發環境
# Build step by step
- Build image with the dockerfile.
```bash
cd FlaskEnvironment
podman build -t flask .
```
- Run container with image.
```bash
podman run --name flaskservice -v .:/mywork -dp 8100:8100 flask
```
