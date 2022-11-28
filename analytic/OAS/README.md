# OAS Installation
Points need to know more than Launch stack from OCI MarketPlace
- [Setup RCU DB](https://github.com/davidkhala/oracle-PaaS-collection/blob/main/analytic/OAS/RCU.md#setup-on-oci)
-  Opt-in Oracle Analytics Server Domain Configuration is a must for new OAS deployment
    - Skip only when creating an additional Oracle Analytics Server compute instance to scale out an existing Oracle Analytics Server deployment.
- DB Admin user
    - it cannot be `sys`, `sys as sysdba`
- Troubleshoot domain server
    - Articulate user `oracle` to satisfy /u01/app/oas-scripts/create_oas_domain.sh
    - `sudo passwd oracle`. By default it is nopassword
    - `oracle is not in the sudoers file`
        
- Run [./oas.sh cleanup](https://github.com/davidkhala/oracle-PaaS-collection/blob/main/analytic/OAS/oas.sh) post deploy 


[create_oas_domain.sh](https://github.com/davidkhala/oci-oracle-analytics-server/blob/master/terraform/computeinstance/templates/create_oas_domain.sh#L&)
- -> `/u01/app/Oracle/Middleware/Oracle_Home/bi/bin/config.sh`, in line 98 it go into
  - -> `/u01/app/Oracle/Middleware/Oracle_Home/oui/mw/common/framework/bin/configinternal.sh`
  -  --> in line 141, it `java -cp /u01/app/Oracle/Middleware/Oracle_Home/oui/modules/installer-launch.jar oracle.as.install.configlauncher.GLCMConfigLauncher`
