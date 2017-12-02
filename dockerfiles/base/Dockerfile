FROM debian:stretch-slim

ENV DEBIAN_FRONTEND=noninteractive

ADD clean_apt_install.sh /usr/bin/clean-apt-install
ADD clean_pip_install.sh /usr/bin/clean-pip-install
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
        python-setuptools \
        python-dev \
        python-pip

RUN clean-pip-install --upgrade pip setuptools wheel
