FROM smokserwis/build:latest

RUN clean-apt-install libfontconfig1 libfontconfig1-dev libfontconfig1 libfontconfig1-dev chrpath libxft-dev

RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - && \
    apt-get install -y nodejs build-essential && \
    apt-get clean

RUN npm cache clean --force
RUN npm install -g bower gulp gulp-cli
RUN npm install -g wrench minimatch express connect
