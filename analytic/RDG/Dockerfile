FROM oraclelinux:9
RUN curl https://objectstorage.ap-singapore-1.oraclecloud.com/n/cn9yc2hk0gzg/b/e-delivery/o/analytic%2FDataGateway_september2022_Linux64.bin > DataGateway_Linux64.bin
RUN chmod +x DataGateway_Linux64.bin
RUN DataGateway_Linux64.bin -silent ORACLE_HOME=<TODO> CREDENTIALS_PAGE_ADMIN_USERNAME=admin CREDENTIALS_PAGE_PASSWORD=<TODO> SELECT_RD_VERSION_RADIO_V1=false


