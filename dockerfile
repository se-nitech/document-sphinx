FROM python:slim

RUN apt -y update && apt -y install git
RUN apt -y install locales
RUN pip install sphinx sphinx-autobuild myst-parser furo

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

WORKDIR /mnt
