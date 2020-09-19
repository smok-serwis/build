FROM python:3.8-buster

ENV DEBIAN_FRONTEND=noninteractive

ADD clean-apt-install.sh /usr/bin/clean-apt-install
ADD clean-pip-install.sh /usr/bin/clean-pip-install
ADD strip-docs.py /usr/bin/strip-docs
ADD doctor-wheel.sh /usr/bin/doctor-wheel

RUN chmod ugo+x /usr/bin/clean-apt-install /usr/bin/clean-pip-install /usr/bin/strip-docs /usr/bin/doctor-wheel

RUN clean-apt-install lsb-release software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=armhf] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    clean-apt-install --no-install-recommends docker-ce zip docker-compose

RUN clean-pip-install cython satella snakehouse

