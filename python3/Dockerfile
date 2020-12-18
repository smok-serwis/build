FROM python:3.8

RUN apt-get update && \
    apt-get install -y patchelf zip && \
    apt-get clean

RUN pip install snakehouse satella twine auditwheel doctor-wheel sphinx grpcio-tools yapf

CMD ["bash"]
