set -e
install() {
    # The agent is only certified with Oracle JDK Version 11
    wget https://objectstorage.ap-seoul-1.oraclecloud.com/n/cn9yc2hk0gzg/b/java/o/jdk-11_linux-x64_bin.rpm
    wget https://objectstorage.ap-seoul-1.oraclecloud.com/n/cn9yc2hk0gzg/b/oci-material/o/oic_conn_agent_installer.zip
    unzip oic_conn_agent_installer.zip -d oic_conn_agent_installer
    rm oic_conn_agent_installer.zip jdk-11_linux-x64_bin.rpm
    # Modify property `oic_URL` and `agent_GROUP_IDENTIFIER`
    vi oic_conn_agent_installer/InstallerProfile.cfg

}
log-dir() {
    cd oic_conn_agent_installer/agenthome/logs
    ll
}

_start() {
    cd oic_conn_agent_installer
    nohup java -jar connectivityagent.jar &>>nohup.out &
    cd -
}

_stop() {
    pid=$(ps -fC "java" | grep "connectivityagent.jar" | awk '{ print $2; }')

    if [ -n "$pid" ]; then
        kill $pid
    fi

}
_restart() {
    _stop
    echo "Waiting for 45 seconds is required before next start..."
    sleep 45
    _start
}

$1
