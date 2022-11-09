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

