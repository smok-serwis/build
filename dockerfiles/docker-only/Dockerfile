FROM debian:stretch-slim

ENV DEBIAN_FRONTEND=noninteractive

ADD clean_apt_install.sh /usr/bin/clean-apt-install
ADD clean_pip_install.sh /usr/bin/clean-pip-install
RUN chmod ugo+x /usr/bin/clean-apt-install /usr/bin/clean-pip-install

RUN mkdir -p /usr/share/man/man1 /usr/share/man/man7 && \
    clean-apt-install --no-install-recommends \
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

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    clean-apt-install --no-install-recommends docker-ce

RUN clean-pip-install --upgrade wheel setuptools pip

RUN clean-pip-install docker-compose
