FROM smokserwis/build:latest
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
    apt-get install -y libfontconfig nodejs zipalign && \
    apt-get clean
    
RUN npm install -g --unsafe-perm bower gulp cordova@6.5.0 karma

RUN wget http://mail.dms-serwis.com.pl/jdk-8u121-linux-x64.tar.gz && \
    mv jdk-8u121-linux-x64.tar.gz /usr/jdk-8u121-linux-x64.tar.gz && \
    cd /usr && \
    tar -xvf jdk-8u121-linux-x64.tar.gz && \
    rm jdk-8u121-linux-x64.tar.gz && \
    ls -la /usr/ && \
    mkdir /usr/adk

RUN update-alternatives --install /usr/bin/java java /usr/jdk1.8.0_121/bin/java 100 && \
    update-alternatives --install /usr/bin/javac javac /usr/jdk1.8.0_121/bin/javac 100 && \
    update-alternatives --install /usr/bin/jar jar /usr/jdk1.8.0_121/bin/jar 100 && \
    update-alternatives --install /usr/bin/jarsigner jarsigner /usr/jdk1.8.0_121/bin/jarsigner 100
    
RUN cd /usr/adk && \
    wget http://mail.dms-serwis.com.pl/tools_r25.2.3-linux.zip && \
    unzip tools_r25.2.3-linux.zip && \
    rm tools_r25.2.3-linux.zip
    
ENV ANDROID_HOME=/usr/adk

RUN mkdir /usr/adk/licenses && \
    echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > /usr/adk/licenses/android-sdk-license && \
    echo -e "\n504667f4c0de7af1a06de9f4b1727b84351f2910" > /usr/adk/licenses/android-sdk-preview-license && \
    echo y | /usr/adk/tools/bin/sdkmanager "build-tools;25.0.1" "build-tools;24.0.0" "platforms;android-25" "platforms;android-24" "platforms;android-23" "platform-tools" "extras;android;m2repository" "extras;google;m2repository" "extras;google;google_play_services"

LABEL "Apache Cordova" "6.5.0"
LABEL "NodeJS" "5"
