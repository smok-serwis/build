FROM smokserwis/build:base

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    clean-apt-install --no-install-recommends docker-ce

RUN clean-pip-install docker-compose>=1.27.0
ADD docker-it.py /usr/bin/docker-it
ADD strip-docs.py /usr/bin/strip-docs
ADD check-syntax.py /usr/bin/check-syntax
ADD configure.py /usr/bin/configure
RUN chmod ugo+x /usr/bin/check-syntax /usr/bin/docker-it /usr/bin/strip-docs /usr/bin/configure

