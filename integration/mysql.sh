set -e

install() {

    wget https://objectstorage.ap-seoul-1.oraclecloud.com/n/cn9yc2hk0gzg/b/MySQL/o/mysql-connector-java-latest.jar
    cp mysql-connector-java-latest.jar oic_conn_agent_installer/agenthome/thirdparty/lib/
    rm mysql-connector-java-latest.jar
}
$1
