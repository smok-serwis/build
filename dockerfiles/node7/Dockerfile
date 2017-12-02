FROM smokserwis/build:latest

RUN apt-get update && \
    apt-get install -y libfontconfig1 libfontconfig1-dev libfontconfig1 libfontconfig1-dev chrpath libxft-dev && \
    apt-get clean

ENV PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
ADD https://bitbucket.org/ariya/phantomjs/downloads/${PHANTOM_JS}.tar.bz2 /usr/local/share
RUN ln -sf /usr/local/share/${PHANTOM_JS}/bin/phantomjs /usr/local/bin/phantomjs

RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - && \
    apt-get install -y nodejs && \
    apt-get clean

RUN npm install -g bower gulp
RUN npm install -g wrench minimatch express connect
