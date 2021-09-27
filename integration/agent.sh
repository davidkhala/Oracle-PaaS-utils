set -e
install() {
    # The agent is only certified with Oracle JDK Version 8
    sudo yum install -y jdk
    wget https://objectstorage.ap-seoul-1.oraclecloud.com/n/cn9yc2hk0gzg/b/oci-material/o/oic_conn_agent_installer.zip
    unzip oic_conn_agent_installer.zip -d oic_conn_agent_installer
    rm oic_conn_agent_installer.zip
    # Modify property `oic_URL` and `agent_GROUP_IDENTIFIER`
    vi oic_conn_agent_installer/InstallerProfile.cfg

}
log-dir(){
    cd oic_conn_agent_installer/agenthome/logs;
    ll
}

start() {
    cd oic_conn_agent_installer
    nohup java -jar connectivityagent.jar &
    tail -f nohup.out
}
terminate() {
    kill $(ps -fC "java" | grep "connectivityagent.jar" | awk '{ print $2; }')

}
$1
