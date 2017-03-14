# Run via: 
#   docker run -d --name rf_control -p 5000 -p 4040 -ti rf_control
#

# Pull base image
FROM resin/rpi-raspbian:jessie
MAINTAINER Mark Mester <mmester6016@gmail.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
	git \
	python3-pip \
	supervisor \
	unzip \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python3-dev \
    python-pip \
    python-virtualenv \
    python-rpi.gpio \
    libyaml-dev \
    libpython2.7-dev \
    libssl-dev \
    libffi-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
RUN git clone git://git.drogon.net/wiringPi
RUN cd wiringPi && ./build && cd ..
RUN pip install setuptools wiringpi2 pyserial pyaml flask flask-ask pyparsing appdirs
RUN pip3 install rpi-rf

# clone repo
RUN mkdir -p /opt
WORKDIR /opt
RUN git clone https://github.com/markmester/rf_control.git

# Install grok
RUN cd rf_control && unzip ngrok-stable-linux-arm.zip && rm -rf ngrok-stable-linux-arm.zip && chmod +x ngrok

# create logs
RUN mkdir /var/log/rf
RUN touch /var/log/rf/rf_control_stderr.log && touch /var/log/rf/rf_control_stdout.log
RUN touch /var/log/rf/ngrok_stderr.log && touch /var/log/rf/ngrok_stdout.log
RUN chmod 777 /var/log/rf/* 

# setup supervisor
RUN cp rf_control/config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Define working directory
# WORKDIR /data
# VOLUME /data

EXPOSE 5000 5000
EXPOSE 4040 4040

CMD ["/usr/bin/supervisord"]
