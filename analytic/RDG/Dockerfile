FROM oraclelinux:9
ENV ORACLE_HOME=/home/opc/Oracle/Middleware/Analytic/RDG
ENV CREDENTIALS_PAGE_ADMIN_USERNAME=admin
ENV CREDENTIALS_PAGE_PASSWORD=Admin123
ENV INVENTORY_LOCATION=${ORACLE_HOME}/oraInventory
RUN curl https://objectstorage.ap-singapore-1.oraclecloud.com/n/cn9yc2hk0gzg/b/e-delivery/o/analytic%2FDataGateway_september2022_Linux64.bin > DataGateway_Linux64.bin
RUN chmod +x DataGateway_Linux64.bin
RUN ./DataGateway_Linux64.bin -silent ORACLE_HOME=${ORACLE_HOME} CREDENTIALS_PAGE_ADMIN_USERNAME=${CREDENTIALS_PAGE_ADMIN_USERNAME} CREDENTIALS_PAGE_PASSWORD=${CREDENTIALS_PAGE_PASSWORD} SELECT_RD_VERSION_RADIO_V1=false INVENTORY_LOCATION=${INVENTORY_LOCATION}}


