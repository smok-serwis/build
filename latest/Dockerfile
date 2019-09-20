FROM smokserwis/build:docker-only

RUN clean-apt-install debconf-utils apt-utils \
        sudo \
        binutils \
        wget \
        build-essential \
        gcc \
        make

RUN clean-apt-install  \
        openssh-client \
        gettext \
        libyaml-dev \
        libffi-dev \
        libev4 \
        libev-dev \
        libpq-dev \
	    ccrypt \
        sshpass \
        avr-libc \
        avrdude \
        postgresql-client-9.6 \
        usbutils

RUN clean-pip-install cassandra-driver

RUN clean-pip-install google-api-python-client wheel nose mock coverage kazoo monotonic

RUN clean-pip-install setproctitle \
	pint \
	pytz \
	gunicorn

ADD check-syntax.py /usr/bin/check-syntax
RUN chmod ugo+x /usr/bin/check-syntax

