FROM debian:jessie
RUN apt-get update
RUN apt-get install -y \
        avr-libc \
        avrdude \
        usbutils \
        sudo \
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
	debconf-utils
	
        
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade cffi
RUN pip install google-api-python-client wheel cassandra-driver nose mock coverage
RUN apt-get clean
 
