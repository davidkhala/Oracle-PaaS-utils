#!/bin/bash
export DISABLE_RDC_METADATA_SECURITY=1
export PUBLIC_KEY_FOLDER=/home/opc/Oracle/Middleware/Oracle_Home/domain/rdc_keys
export JAVA_HOME=/home/opc/Oracle/Middleware/Oracle_Home/oracle_common/jdk1.8.0_333
export PATH=$JAVA_HOME/bin:$PATH
export JETTY_HOME=/home/opc/Oracle/Middleware/Oracle_Home/jetty
export DOMAIN_HOME=/home/opc/Oracle/Middleware/Oracle_Home/domain
export JETTY_BASE=/home/opc/Oracle/Middleware/Oracle_Home/domain/jettybase
cd $JETTY_BASE
java -DSTOP.PORT=35997 -DSTOP.KEY=stop_jetty  -DDOMAIN_HOME=$DOMAIN_HOME -DPUBLIC_KEY_FOLDER=/home/opc/Oracle/Middleware/Oracle_Home/domain/rdc_keys -DRDC_VERSION=V2  -Djetty.home=$JETTY_HOME -Djetty.base=$JETTY_BASE  -Djetty.http.port=8080 -Djetty.ssl.port=8443 -Dlog4j.configurationFile=$DOMAIN_HOME/config/log4j2.xml -Duser.timezone=GMT  -jar $JETTY_HOME/start.jar 