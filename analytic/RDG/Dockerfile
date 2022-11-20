FROM oraclelinux:9

ARG USERNAME=opc
ARG relative_Oracle_Home=RDG

RUN groupadd --gid 1000 $USERNAME && useradd --uid 1000 --gid 1000 -m $USERNAME
RUN echo inventory_loc=/home/${USERNAME}/oraInventory >> /etc/oraInst.loc
RUN echo inst_group=${USERNAME} >> /etc/oraInst.loc
USER $USERNAME 

WORKDIR /home/${USERNAME}/

ENV Oracle_Home=/home/${USERNAME}/${relative_Oracle_Home}

ADD ./silentInstall.response /home/${USERNAME}/silentInstall.response

RUN echo "ORACLE_HOME=${Oracle_Home}" >> /home/${USERNAME}/silentInstall.response

RUN curl https://objectstorage.ap-singapore-1.oraclecloud.com/n/cn9yc2hk0gzg/b/e-delivery/o/analytic%2FDataGateway_september2022_Linux64.bin > ~/DataGateway_Linux64.bin
RUN chmod +x ~/DataGateway_Linux64.bin
RUN ~/DataGateway_Linux64.bin -silent -ignoreSysPrereqs -responseFile ~/silentInstall.response
RUN rm ~/DataGateway_Linux64.bin
RUN mkdir -p ${Oracle_Home}/domain/jettybase/thirdpartyDrivers/

ENV DISABLE_RDC_METADATA_SECURITY=1
ENV PATH=$Oracle_Home/oracle_common/jdk1.8.0_333/bin:$PATH
ENV JETTY_HOME=$Oracle_Home/jetty
ENV DOMAIN_HOME=$Oracle_Home/domain
ENV JETTY_BASE=$Oracle_Home/domain/jettybase
WORKDIR $JETTY_BASE

ENTRYPOINT java -DSTOP.PORT=35997 -DSTOP.KEY=stop_jetty -DDOMAIN_HOME=$DOMAIN_HOME -DPUBLIC_KEY_FOLDER=$Oracle_Home/domain/rdc_keys -DRDC_VERSION=V2 -Djetty.home=$JETTY_HOME -Djetty.base=$JETTY_BASE  -Djetty.http.port=8080 -Djetty.ssl.port=8443 -Dlog4j.configurationFile=$DOMAIN_HOME/config/log4j2.xml -Duser.timezone=GMT -jar $JETTY_HOME/start.jar
