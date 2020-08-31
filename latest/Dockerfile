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
        postgresql-client-11 \
        usbutils \
        cmake

RUN clean-pip-install --upgrade pip
RUN clean-pip-install cassandra-driver \
        google-api-python-client wheel nose coverage kazoo monotonic \
        setproctitle \
    pint pytz gunicorn grpcio-tools nose2 coverage nose2[coverage_plugin]


