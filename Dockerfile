FROM ubuntu:latest

RUN <<EOF
	apt-get update
	apt-get install -y sudo vim nano git tmux
	apt-get install -y python3.11 python3-pip
EOF

# Install Python packages
RUN <<EOF
	pip3 install rocketpy
EOF

# Set Python 3.11 as default interpreter
RUN ln -s /usr/bin/python3.11 /usr/bin/python

# Create a user
RUN <<EOF
	useradd -ms /bin/bash antares
	echo 'antares:antarespwd' | chpasswd
	usermod -d /home/antares antares
	echo "PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /home/antares/.bashrc
EOF

# Switch to user antares
USER antares
WORKDIR /home/antares

