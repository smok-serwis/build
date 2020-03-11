FROM python:3.8

ENV DEBIAN_FRONTEND=noninteractive

ADD clean-apt-install.sh /usr/bin/clean-apt-install
ADD clean-pip-install.sh /usr/bin/clean-pip-install
RUN chmod ugo+x /usr/bin/clean-apt-install /usr/bin/clean-pip-install

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    clean-apt-install --no-install-recommends docker-ce

RUN clean-pip-install cython docker-compose>=1.19.0