FROM debian:jessie-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /usr/share/man/man1 /usr/share/man/man7 && \
    apt-get update && \ 
    apt-get install -y \
        avr-libc \
        avrdude \
        usbutils \
        sudo \
	binutils \
	ca-certificates \
	software-properties-common \
        wget \ 
        curl \
        unzip \
        python \
        python-setuptools \
        python-pip \
        build-essential \
        python-dev \
        gcc \
        make \
        openssh-client \
        gettext \
        tar \
        apt-transport-https \
        git \
	libyaml-dev \
	libffi-dev \	
	apt-utils \
 	libev4 \
	libev-dev \
	libpq-dev \
	debconf-utils \
	postgresql-client \
	sshpass && \
    apt-get clean && \
    rm -rf /usr/share/man/*

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install google-api-python-client wheel cassandra-driver nose mock coverage kazoo monotonic && \
    rm -rf /root/.cache /tmp/pip-*

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    apt-get update && \
    apt-get install -y docker-ce && \
    apt-get clean
    
RUN pip install docker-compose \ 
        setproctitle \
	pint \
	pytz \
	gunicorn && \
    rm -rf /root/.cache /tmp/pip-*
 
