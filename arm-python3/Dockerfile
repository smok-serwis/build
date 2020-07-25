FROM python:3.8

ENV DEBIAN_FRONTEND=noninteractive

RUN pip install yapf satella snakehouse cython && \
    rm -rf /root/.cache /tmp/pip-*

RUN apt-get update && \
    apt-get install -y zip && \
    apt-get clean

ADD doctor-wheel.sh /usr/bin/doctor-wheel
ADD clean-pip-install.sh /usr/bin/clean-pip-install
ADD strip-docs.py /usr/bin/strip-docs
RUN chmod ugo+x /usr/bin/clean-pip-install /usr/bin/doctor-wheel /usr/bin/strip-docs


