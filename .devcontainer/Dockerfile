FROM python:3.8-slim

# Make sure we don't get notifications we can't answer during building.
ENV DEBIAN_FRONTEND noninteractive

#
# Default config
#
RUN groupadd -g 9999 dev \
    && useradd -m -r -u 9999 -g dev dev

#
# Add module and packages
#
RUN apt-get update \
    && apt-get install -y git procps \
    && apt-get clean \
    && pip install black mypy pylint pytest pytest-xdist

USER dev

