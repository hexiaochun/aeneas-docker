FROM ubuntu

RUN apt-get update
RUN apt-get install -y ffmpeg 
RUN apt-get install -y espeak espeak-data libespeak1 libespeak-dev 
RUN apt-get install -y festival* 
RUN apt-get install -y build-essential 
RUN apt-get install -y flac libasound2-dev libsndfile1-dev vorbis-tools 
RUN apt-get install -y libxml2-dev libxslt-dev zlib1g-dev 
RUN apt-get install -y python3-dev python3-pip
RUN apt-get install -y git file htop screen vim unzip 
RUN pip3 install numpy boto3 requests tgt youtube-dl Pillow 
RUN pip3 install aeneas 
RUN apt-get clean

RUN mkdir /app
WORKDIR /app

ENV PYTHONIOENCODING=UTF-8

COPY ./ /app/

# Add new steps here to clone the espeak git repo and compile it
RUN git clone https://github.com/nvaccess/espeak.git && \
    cd espeak/dictsource && \
    espeak --compile=zh

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./main.py /app/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

