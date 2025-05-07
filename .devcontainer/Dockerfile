# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary build dependencies and fonts
RUN apt-get update && \
    apt-get install -y \
    build-essential gdb cmake git python3 python3-pip python3-venv python3-pytest lsb-release software-properties-common \
    wget curl valgrind doxygen doxygen-latex graphviz default-jre \
    texlive-latex-base texlive-fonts-recommended latexmk \
    fonts-cantarell fonts-roboto fonts-ubuntu fonts-freefont-otf\
    texlive-xetex xindy tree

# Accept the MS Core Fonts EULA
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections

# Install the MS Core Fonts
RUN apt-get install -y ttf-mscorefonts-installer

# Set the working directory for plantuml
WORKDIR /plantuml
# Download PlantUML JAR
RUN wget https://netcologne.dl.sourceforge.net/project/plantuml/plantuml.jar

# Force Java into headless mode to fix PlantUML AWT error
ENV _JAVA_OPTIONS="-Djava.awt.headless=true"

# Create an alias for running PlantUML
RUN echo 'alias plantuml="java -jar /plantuml/plantuml.jar"' >> ~/.bashrc

# Create and activate a virtual environment for Python packages
RUN python3 -m venv /env
ENV PATH="/env/bin:$PATH"

# Install setuptools to resolve 'pkg_resources' issue
RUN pip install --upgrade pip setuptools

WORKDIR /tmp

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt within the virtual environment
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the locale environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN adduser vscode

# Define an entry point
ENTRYPOINT ["/bin/sh"]
