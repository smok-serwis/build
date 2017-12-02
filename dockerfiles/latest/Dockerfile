FROM smokserwis/build:docker-only

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        avr-libc \
        avrdude \
        usbutils \
        sudo \
        binutils \
        wget \ 
        unzip \
        build-essential \
        python-dev \
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
        postgresql-client-9.6 \
	    ccrypt \
        sshpass && \
    apt-get clean && \
    rm -rf /usr/share/man/*

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install google-api-python-client wheel cassandra-driver nose mock coverage kazoo monotonic && \
    rm -rf /root/.cache /tmp/pip-*

RUN pip install setproctitle \
	pint \
	pytz \
	gunicorn && \
    rm -rf /root/.cache /tmp/pip-*
 
ADD build_tools/docker-it.py /usr/bin/docker-it

RUN chmod ugo+x /usr/bin/docker-it
