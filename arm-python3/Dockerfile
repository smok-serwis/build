FROM python:3.8-buster

ENV DEBIAN_FRONTEND=noninteractive

ADD clean-apt-install.sh /usr/bin/clean-apt-install
ADD clean-pip-install.sh /usr/bin/clean-pip-install
RUN chmod ugo+x /usr/bin/clean-apt-install /usr/bin/clean-pip-install

RUN clean-apt-install lsb-release software-properties-common

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=armhf] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    clean-apt-install --no-install-recommends docker-ce
RUN clean-apt-install --no-install-recommends zip

ADD strip-docs.py /usr/bin/strip-docs
ADD doctor-wheel.sh /usr/bin/doctor-wheel
RUN chmod ugo+x /usr/bin/strip-docs /usr/bin/doctor-wheel && \
    clean-pip-install --upgrade pip wheel setuptools
RUN clean-pip-install cython
RUN clean-apt-install docker-compose

