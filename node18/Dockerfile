FROM smokserwis/build:latest

RUN clean-apt-install libfontconfig1 libfontconfig1-dev libfontconfig1 libfontconfig1-dev chrpath libxft-dev

RUN curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash - && \
    clean-apt-install nodejs build-essential

RUN npm cache clean --force
