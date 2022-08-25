FROM fedora:36

RUN sudo dnf update -y \
    && sudo dnf upgrade -y \
    && sudo dnf install -y \
    passwd sudo curl \
    git make gcc bzip2-devel libffi-devel zlib-devel openssl-devel readline-devel sqlite-devel ncurses-devel libxml2-devel xz-devel lldb

RUN sudo adduser henryrocha --groups wheel \
    && sudo passwd -d henryrocha

USER henryrocha
WORKDIR /home/henryrocha
ENV USER henryrocha

# Install rustup
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > rustup.sh
RUN sh rustup.sh -y && rm -f rustup.sh
ENV PATH /home/henryrocha/.cargo/bin:$PATH

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh > install.sh
RUN sh install.sh --method=standalone
RUN rm -f install.sh
RUN sudo chown -R henryrocha:henryrocha /home/henryrocha/.local
ENV PATH /home/henryrocha/.local/bin:$PATH

# Install pyenv
RUN curl https://pyenv.run | bash && echo 'eval "$(pyenv init -)"' >> /home/henryrocha/.profile
ENV PATH /home/henryrocha/.pyenv/bin:$PATH
ENV PYENV_ROOT /home/henryrocha/.pyenv
RUN pyenv install 3.10.6
RUN pyenv global 3.10.6
RUN python3 -m ensurepip && python3 -m pip install --upgrade pip

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
ENV PYROOT_ROOT /home/henryrocha/.poetry
ENV PATH $PYROOT_ROOT/bin:$PATH
