FROM smokserwis/build:docker-only

RUN mkdir -p /usr/share/man/man1/ /usr/share/man/man7/ && \
    clean-apt-install debconf-utils apt-utils \
        sudo \
        binutils \
        wget \ 
        unzip \
        build-essential \
        gcc \
        make \
        zip \
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
 
ADD build_tools/docker-it.py /usr/bin/docker-it

RUN chmod ugo+x /usr/bin/docker-it
