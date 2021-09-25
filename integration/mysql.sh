set -e

install() {

    wget https://objectstorage.ap-seoul-1.oraclecloud.com/n/cn9yc2hk0gzg/b/MySQL/o/mysql-connector-java-8.0.26.jar
    cp mysql-connector-java-8.0.26.jar oic_conn_agent_installer/agenthome/thirdparty/lib/
    rm mysql-connector-java-8.0.26.jar
}
$1
