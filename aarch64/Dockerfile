FROM python:3.8

RUN apt-get update && apt-get install -y patchelf

RUN pip install twine auditwheel doctor-wheel cython snakehouse satella strip-docs
