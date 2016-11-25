FROM ubuntu:16.04
ENV USER user

RUN apt-get update -qq \
    && apt-get install -qq -y python-setuptools \
        pkg-config \
        zlib1g-dev \
        cython \
        default-jdk \
        build-essential \
        ccache \
        git \
        lib32stdc++6 \
        lib32z1 \
        lib32z1-dev \
        python2.7 \
        python2.7-dev \
        unzip \
        zlib1g-dev \
        wget \
        libtool  \
        autoconf  \
        automake \
        zlib1g-dev \
        python-dev \
        python-pip \
    && rm -rf /var/cache/apt/* /var/lib/apt/lists/*

RUN pip install buildozer
RUN adduser --disabled-password --gecos "" ${USER}

ADD demo /home/${USER}/demo
RUN chown -R ${USER} /home/${USER}/demo
USER ${USER}
WORKDIR /home/${USER}

RUN cd demo && buildozer android debug
