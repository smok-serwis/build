FROM python:3.8

RUN apt-get update && \
    apt-get install -y patchelf zip && \
    apt-get clean

RUN pip install snakehouse>=1.4 satella>=2.14.32 twine auditwheel strip-docs doctor-wheel sphinx grpcio-tools yapf

CMD ["bash"]
