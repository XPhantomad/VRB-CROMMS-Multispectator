# Dockerfile of the base image: https://github.com/IntEL4CoRo/jupyter-ros2/blob/main/Dockerfile
FROM intel4coro/jupyter-ros2:jazzy-py3.12


USER root
ENV PATH=$HOME/.local/bin:$PATH

# Set Working Directory
ENV REPO_DIR=/home/repo
RUN mkdir -p ${REPO_DIR}
WORKDIR ${REPO_DIR}


#============= Install extra software packages =============#

RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb 
EXPOSE 3004

# Change the default shell to Bash
SHELL [ "/bin/bash" , "-c" ]

EXPOSE 3004

USER root
# Install Requirements
RUN apt-get update && apt-get install -y git colcon cmake libfreeimage-dev libfreeimageplus-dev freeglut3-dev libxi-dev libxmu-dev liblua5.3-dev lua5.3 doxygen graphviz libgraphviz-dev asciidoc

USER root
RUN cd /usr/lib/x86_64-linux-gnu \
    && ln -s libglut.so.3.12.0 libglut.so.3

RUN git clone -b master https://github.com/XPhantomad/Context-Role-Oriented-Transport-Chain-Swarm.git

USER root
# Install ARGoS3
RUN cd Context-Role-Oriented-Transport-Chain-Swarm \
    # && git pull
    && cd Dependencies \
    && apt-get install -y ./argos3_simulator-3.0.0-x86_64-beta59.deb

# Install GSL for ARGoS3-ROS2-Bridge
RUN apt-get install -y libgsl-dev

RUN cd Context-Role-Oriented-Transport-Chain-Swarm \
    && cd Dependencies \
    && tar -zxf gsl-latest.tar.gz \
    && cd gsl-2.8 \
    && mkdir /root/gsl \
    && ./configure --prefix=/root/gsl \
    && make \
    && make check \
    && make install 

ENV LD_LIBRARY_PATH="/root/gsl/lib:$LD_LIBRARY_PATH"

# Build ARGoS3-ROS2-Bridge
RUN ln -s Context-Role-Oriented-Transport-Chain-Swarm/rosWorkspace ros_ws 

RUN cd ros_ws \
    && chmod +x build.sh \
    && ./build.sh 

RUN sudo apt install -y python3.12 python3.12-venv ros-dev-tools 

RUN wget https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.10-linux-x86_64.tar.gz \
    && tar xzf julia-1.10.10-linux-x86_64.tar.gz

ENV PATH="julia-1.10.10/bin:$PATH"

RUN julia -e 'using Pkg; Pkg.add.(["Sockets", "JSON", "Parameters"])'

RUN cd Context-Role-Oriented-Transport-Chain-Swarm/runtimemodel \
    && python3 -m venv . \
    && source bin/activate \
    && source /opt/ros/jazzy/setup.bash \
    && source ../rosWorkspace/install/setup.bash \
    && pip install pyyaml pyecore numpy 

RUN cd Context-Role-Oriented-Transport-Chain-Swarm/webapp \
    && python3 -m venv . \
    && source bin/activate \
    && source /opt/ros/jazzy/setup.bash \
    && source ../rosWorkspace/install/setup.bash \
    && pip install -r requirements.txt 
    
RUN cd Context-Role-Oriented-Transport-Chain-Swarm/startup \
    && python3 -m venv . \
    && source bin/activate \
    && source /opt/ros/jazzy/setup.bash \
    && source ../rosWorkspace/install/setup.bash \
    && pip install -r requirements.txt 

# Install python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#===========================================================#
# RUN apt update && apt install -y curl


# Copy content to the image
COPY . ${REPO_DIR}/
RUN git config --global --add safe.directory ${REPO_DIR}

# Set JupyterLab default directory
WORKDIR ${REPO_DIR}
# Set VSCODE default directory
ENV CODE_WORKING_DIRECTORY=${REPO_DIR}

# The entrypoint of the docker image
COPY binder/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]




