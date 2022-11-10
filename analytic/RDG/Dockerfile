FROM oraclelinux:9
COPY . /root/
RUN curl https://objectstorage.ap-singapore-1.oraclecloud.com/n/cn9yc2hk0gzg/b/e-delivery/o/analytic%2FDataGateway_september2022_Linux64.bin > DataGateway_Linux64.bin
RUN chmod +x DataGateway_Linux64.bin
#11 33.70 The current user is root or has superuser privilege.
#11 33.70 The Oracle Universal Installer cannot continue.
RUN ./DataGateway_Linux64.bin -silent -responseFile ~/silentInstall.response 


