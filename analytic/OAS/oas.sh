set +x

create-domain() {
  /u01/app/oas-scripts/create_oas_domain.sh
}

start() {
  # /u01/data/domains/bi does not exist if installation doesn't success.
  sudo su oracle
  /u01/data/domains/bi/bitools/bin/start.sh
}
update-config() {
  vi /u01/data/biconfig.rsp
}
cleanup() {
  #  delete the domain configuration file biconfig.rsp. This file contains sensitive configuration information
  sudo su oracle
  rm /u01/data/biconfig.rsp

  sudo yum install -y libgfortran # Enable automated machine learning features
}
domain-status() {

  cat /var/log/oas_cloudinit.log
  cat /var/log/oas_create_domain.log
}

$@
