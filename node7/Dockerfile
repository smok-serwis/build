FROM smokserwis/build:latest

RUN clean-apt-install libfontconfig1 libfontconfig1-dev libfontconfig1 libfontconfig1-dev chrpath libxft-dev

ENV PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
ADD https://bitbucket.org/ariya/phantomjs/downloads/${PHANTOM_JS}.tar.bz2 /usr/local/share
RUN ln -sf /usr/local/share/${PHANTOM_JS}/bin/phantomjs /usr/local/bin/phantomjs

RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - && \
    clean-apt-install nodejs

RUN npm cache clean
RUN npm install -g bower gulp gulp-cli
RUN npm install -g wrench minimatch express connect
