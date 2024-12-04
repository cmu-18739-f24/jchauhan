FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS base

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    socat

RUN mkdir /challenge && chmod 700 /challenge



COPY crt.py setup-challenge.py flag.txt /app/
COPY start.sh /opt/
WORKDIR /app/
RUN pip3 install pycryptodome

RUN tar czvf /challenge/artifacts.tar.gz crt.py

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

# # The start.sh script starts a socat listener on port 5555, that connects to the
# # python script.
EXPOSE 5555
#PUBLISH 5555 AS socat
CMD ["/opt/start.sh"]


#sudo docker build -t ctf-problem2 --build-arg FLAG="{abc}" .
#sudo docker run --rm -it ctf-problem2