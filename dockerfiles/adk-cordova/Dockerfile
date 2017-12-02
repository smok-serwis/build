FROM smokserwis/build:latest

RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
    clean-apt-install libfontconfig nodejs zipalign

RUN wget https://services.gradle.org/distributions/gradle-4.0.2-bin.zip && \
    mkdir /opt/gradle && \
    unzip -d /opt/gradle gradle-4.0.2-bin.zip && \
    update-alternatives --install /usr/bin/gradle gradle /opt/gradle/gradle-4.0.2/bin/gradle 100

RUN npm install -g --unsafe-perm bower gulp cordova karma

ADD http://mail.dms-serwis.com.pl/jdk-8u131-linux-x64.tar.gz /usr
RUN mkdir /usr/adk

RUN update-alternatives --install /usr/bin/java java /usr/jdk1.8.0_131/bin/java 100 && \
    update-alternatives --install /usr/bin/javac javac /usr/jdk1.8.0_131/bin/javac 100 && \
    update-alternatives --install /usr/bin/jar jar /usr/jdk1.8.0_131/bin/jar 100 && \
    update-alternatives --install /usr/bin/jarsigner jarsigner /usr/jdk1.8.0_131/bin/jarsigner 100

RUN cd /usr/adk && \
    wget http://mail.dms-serwis.com.pl/tools_r25.2.3-linux.zip && \
    unzip tools_r25.2.3-linux.zip && \
    rm tools_r25.2.3-linux.zip

ENV ANDROID_HOME=/usr/adk

RUN mkdir /usr/adk/licenses && \
    echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb78af6dfcb131a6481e" > /usr/adk/licenses/android-sdk-license && \
    echo -e "\n504667f4c0de7af1a06de9f4b1727b84351f2910" > /usr/adk/licenses/android-sdk-preview-license && \
    echo y | /usr/adk/tools/bin/sdkmanager "build-tools;25.0.1" "build-tools;24.0.0" "platforms;android-25" "platforms;android-24" "platforms;android-23" "platform-tools" "extras;android;m2repository" "extras;google;m2repository" "extras;google;google_play_services"

LABEL ApacheCordova 6.5.0
LABEL NodeJS 5
