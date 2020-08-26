FROM python:alpine
ADD . /code
WORKDIR /code

RUN pip install --upgrade pip && \
pip  install -r requirements.txt && \
apk add --no-cache chromium chromium-chromedriver

ENTRYPOINT ["python","main.py"]
