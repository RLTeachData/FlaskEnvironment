FROM python:3.10.16-alpine

WORKDIR /mywork

RUN pip install --no-cache Flask

EXPOSE 8100

CMD ["python3", "main.py"]