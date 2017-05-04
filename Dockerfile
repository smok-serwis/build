FROM smokserwis/build:latest
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g --unsafe-perm bower gulp cordova@6.5.0 karma
LABEL "Apache Cordova" "6.5.0"
LABEL "NodeJS" "5"
