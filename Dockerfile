FROM debian:jessie
RUN apt-get update
RUN apt-get install -y \
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
	debconf-utils
	
        

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install google-api-python-client wheel cassandra-driver nose mock coverage kazoo monotonic
RUN apt-get install -y docker-ce 
RUN pip install docker-compose
RUN apt-get clean
 
