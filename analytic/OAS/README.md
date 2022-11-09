# OAS Installation
Points need to know more than Launch stack from OCI MarketPlace
- [Setup RCU DB](https://github.com/davidkhala/oracle-PaaS-collection/blob/main/analytic/OAS/RCU.md#setup-on-oci)
-  Opt-in Oracle Analytics Server Domain Configuration is a must for new OAS deployment
    - Skip only when creating an additional Oracle Analytics Server compute instance to scale out an existing Oracle Analytics Server deployment.
- DB Admin user
    - it cannot be `sys`, `sys as sysdba`
- reset the password for OS user `Oracle`. By default it is nopassword
- Run [./oas.sh cleanup](https://github.com/davidkhala/oracle-PaaS-collection/blob/main/analytic/OAS/oas.sh) post deploy 

