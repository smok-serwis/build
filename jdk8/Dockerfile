FROM smokserwis/build:latest

RUN clean-apt-install libfontconfig zipalign

ADD http://mail.dms-serwis.com.pl/jdk-8u131-linux-x64.tar.gz /usr

RUN update-alternatives --install /usr/bin/java java /usr/jdk1.8.0_131/bin/java 100 && \
    update-alternatives --install /usr/bin/javac javac /usr/jdk1.8.0_131/bin/javac 100 && \
    update-alternatives --install /usr/bin/jar jar /usr/jdk1.8.0_131/bin/jar 100 && \
    update-alternatives --install /usr/bin/jarsigner jarsigner /usr/jdk1.8.0_131/bin/jarsigner 100
