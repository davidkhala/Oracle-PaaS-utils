set +x
cleanup(){
  #  delete the domain configuration file biconfig.rsp. This file contains sensitive configuration information
  sudo su oracle
  cd /u01/data
  rm biconfig.rsp
}


$@
