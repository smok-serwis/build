FROM smokserwis/build:base

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    clean-apt-install --no-install-recommends docker-ce

RUN clean-pip-install docker-compose>=1.19.0

