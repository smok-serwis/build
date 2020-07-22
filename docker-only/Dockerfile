FROM smokserwis/build:base-arm

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=armhf] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    clean-apt-install --no-install-recommends docker-ce

RUN clean-apt-install python-openssl libffi-dev libssl-dev python-cryptography

RUN clean-pip-install docker-compose>=1.19.0
ADD docker-it.py /usr/bin/docker-it
ADD strip-docs.py /usr/bin/strip-docs

RUN chmod ugo+x /usr/bin/docker-it /usr/bin/strip-docs

