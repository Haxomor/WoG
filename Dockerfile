FROM python:3.8-slim-buster

WORKDIR /python-docker
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["src/app.py"]
