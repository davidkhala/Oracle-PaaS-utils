set +x
cleanup(){
  #  delete the domain configuration file biconfig.rsp. This file contains sensitive configuration information
  sudo su oracle
  cd /u01/data
  rm biconfig.rsp
  
  sudo yum install -y libgfortran # Enable automated machine learning features
}
domain-status(){
  sudo su oracle
  cat /var/log/oas_cloudinit.log
  cat /var/log/oas_create_domain.log
}

$@
