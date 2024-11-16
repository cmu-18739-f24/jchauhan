FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS base
RUN mkdir /challenge && chmod 700 /challenge
WORKDIR /app/
RUN apt-get update && apt-get install -y \
python3 \
socat \
build-essential \
gcc-multilib \
libc6-dev-i386

#RUN apt update && apt install -y build-essential gdb
#&& apt install gcc-multilib && apt install libc6-dev-i386


COPY flag.txt .
COPY format_vuln.c .
#COPY flag.txt . 
RUN gcc -m32 -g -w -o format_vuln -z execstack format_vuln.c
#RUN rm format_vuln.c
COPY setup-challenge.py .
#COPY format_vuln.c format_vuln setup-challenge.py /app/
#CMD ["app/.format_vuln"]

COPY start.sh /opt/
RUN chmod +x /opt/start.sh

# WORKDIR /app/
RUN tar czvf /challenge/artifacts.tar.gz format_vuln format_vuln.c

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

# # The start.sh script starts a socat listener on port 5555, that connects to the
# # python script.
EXPOSE 5555
# # PUBLISH 5555 AS socat
CMD ["/opt/start.sh"]



#sudo docker build -t ctf-problem --build-arg FLAG="picoCTF{sample}" .
#sudo docker run -it --rm ctf-problem
#%x.%x.%x.%x.%x.%x.%x.%x.%n