FROM python:3.8

ENV DEBIAN_FRONTEND=noninteractive

ADD clean-apt-install.sh /usr/bin/clean-apt-install
ADD clean-pip-install.sh /usr/bin/clean-pip-install

RUN chmod ugo+x /usr/bin/clean-apt-install /usr/bin/clean-pip-install

RUN clean-apt-install lsb-release software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
      "deb [arch=armhf] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable" && \
    clean-apt-install --no-install-recommends docker-ce zip docker-compose patchelf

RUN clean-pip-install https://mail.dms-serwis.com.pl/rapid/cffi-1.14.1-cp38-cp38-linux_armv7l.whl && \
    clean-pip-install https://mail.dms-serwis.com.pl/rapid/ujson-3.2.0-cp38-cp38-linux_armv7l.whl && \
    clean-pip-install https://mail.dms-serwis.com.pl/rapid/cryptography-3.2.1-cp38-cp38-linux_armv7l.whl

RUN clean-pip-install cython satella>=2.14.32 snakehouse>=1.3 auditwheel doctor-wheel twine strip-docs

CMD ["bash"]
