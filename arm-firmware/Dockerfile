FROM openjdk:11-jre-slim

RUN apt-get -y update || true && \
	apt-get -y install wget make zip lbzip2 && \
	wget -q https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.07/gcc-arm-none-eabi-10.3-2021.07-x86_64-linux.tar.bz2 -O gcc-arm-none-eabi.tar.bz2 && tar xf gcc-arm-none-eabi.tar.bz2 && rm gcc-arm-none-eabi.tar.bz2 && \
	wget -q "https://mirror.dkm.cz/eclipse/technology/epp/downloads/release/2021-09/R/eclipse-cpp-2021-09-R-linux-gtk-x86_64.tar.gz" -O eclipse.tar.gz && tar xvf eclipse.tar.gz && rm eclipse.tar.gz && \
	eclipse/eclipse -application org.eclipse.equinox.p2.director -noSplash -repository 'https://download.eclipse.org/embed-cdt/updates/v6/' -installIU org.eclipse.embedcdt.managedbuild.cross.arm.feature.group,org.eclipse.embedcdt.packs.feature.group,org.eclipse.embedcdt.feature.group
