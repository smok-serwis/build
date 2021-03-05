FROM python:3.9

RUN apt-get update && \
    apt-get install -y libsnappy-dev libgflags-dev liblz4-dev libbz2-dev zlib1g-dev patchelf

RUN pip install https://mail.dms-serwis.com.pl/rapid/cffi-1.14.1-cp39-cp39-linux_armv7l.whl && \
	pip install pip install https://mail.dms-serwis.com.pl/rapid/cryptography-3.2.1-cp39-cp39-linux_armv7l.whl

RUN pip install satella snakehouse doctor-wheel auditwheel twine strip-docs
