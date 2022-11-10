FROM ubuntu

ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y curl


USER $USERNAME

WORKDIR /home/$USERNAME
ADD ./oraInst.loc /home/$USERNAME
ADD ./silentInstall.response /home/$USERNAME

RUN curl https://objectstorage.ap-singapore-1.oraclecloud.com/n/cn9yc2hk0gzg/b/e-delivery/o/analytic%2FDataGateway_september2022_Linux64.bin > ~/DataGateway_Linux64.bin
RUN chmod +x ~/DataGateway_Linux64.bin
RUN ~/DataGateway_Linux64.bin -silent -ignoreSysPrereqs -responseFile ~/silentInstall.response -invPtrLoc ~/oraInst.loc
RUN rm ~/DataGateway_Linux64.bin

