FROM debian:stretch-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /usr/share/man/man1 /usr/share/man/man7 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        software-properties-common \
        python \
        git \
        tar \
        python-setuptools \
        python-dev \
        python-pip && \
    apt-get clean && \
    rm -rf /usr/share/man/*

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    apt-get update && \
    apt-get install -y --no-install-recommends docker-ce && \
    apt-get clean

RUN pip install --upgrade wheel setuptools pip && \
    rm -rf /root/.cache /tmp/pip-*

RUN pip install docker-compose && \
    rm -rf /root/.cache /tmp/pip-*
