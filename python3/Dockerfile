FROM python:3.8

RUN apt-get update && \
    apt-get install -y patchelf zip gcc-arm-linux-gnueabihf && \
    apt-get clean

RUN pip install snakehouse>=1.3 satella>=2.14.30 twine auditwheel strip-docs doctor-wheel sphinx grpcio-tools yapf

CMD ["bash"]
