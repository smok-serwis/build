FROM smokserwis/build:latest
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -
RUN apt-get install -y libfontconfig nodejs zipalign
RUN npm install -g --unsafe-perm bower gulp cordova@6.5.0 karma

ADD http://mail.dms-serwis.com.pl/jdk-8u121-linux-x64.tar.gz /usr/
RUN cd /usr; tar -xvf jdk-8u121-linux-x64.tar.gz; rm jdk-8u121-linux-x64.tar.gz
RUN ls -la /usr/
RUN mkdir /usr/adk
ADD http://mail.dms-serwis.com.pl/tools_r25.2.3-linux.zip /usr/adk/
RUN cd /usr/adk; unzip tools_r25.2.3-linux.zip
RUN update-alternatives --install /usr/bin/java java /usr/jdk1.8.0_121/bin/java 100
RUN update-alternatives --install /usr/bin/javac javac /usr/jdk1.8.0_121/bin/javac 100
RUN update-alternatives --install /usr/bin/jar jar /usr/jdk1.8.0_121/bin/jar 100
RUN update-alternatives --install /usr/bin/jarsigner jarsigner /usr/jdk1.8.0_121/bin/jarsigner 100
ENV ANDROID_HOME="/usr/adk"
RUN mkdir /usr/adk/licenses
RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > /usr/adk/licenses/android-sdk-license
RUN echo -e "\n504667f4c0de7af1a06de9f4b1727b84351f2910" > /usr/adk/licenses/android-sdk-preview-license
RUN ls /usr/adk
RUN echo y | /usr/adk/tools/bin/sdkmanager "build-tools;25.0.1" "build-tools;24.0.0" "platforms;android-25" "platforms;android-24" "platforms;android-23" "platform-tools" "extras;android;m2repository" "extras;google;m2repository" "extras;google;google_play_services"

RUN apt-get clean
LABEL "Apache Cordova" "6.5.0"
LABEL "NodeJS" "5"
