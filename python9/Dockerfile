FROM python:3.9

RUN apt-get update && \
    apt-get install -y libsnappy-dev libgflags-dev liblz4-dev libbz2-dev zlib1g-dev patchelf

RUN pip install cffi cryptography && \
    pip install satella snakehouse doctor-wheel auditwheel twine && \
    pip install strip-docs install sphinx
