FROM debian:stretch-slim

ENV DEBIAN_FRONTEND=noninteractive

ADD clean-apt-install.sh /usr/bin/clean-apt-install
ADD clean-pip-install.sh /usr/bin/clean-pip-install
RUN chmod ugo+x /usr/bin/clean-apt-install /usr/bin/clean-pip-install

RUN clean-apt-install --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        apt-utils \
        debconf-utils \
        curl \
        gnupg2 \
        software-properties-common \
        python \
        git \
        tar \
        zip unzip \
        python-setuptools \
        python-dev \
        python-pip \
        gcc

RUN clean-pip-install --upgrade pip setuptools wheel
