FROM python
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip  install -r requirements.txt

RUN apt-get update && apt-get install -y unzip

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
	apt-get install -y google-chrome-stable

ADD https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome
ENTRYPOINT ["python","main.py"]
