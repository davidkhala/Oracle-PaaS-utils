# OAS in OCI MarketPlace

## Troubleshoot
Found end lines in `/var/log/oas_create_domain.log`
```
[VALIDATION] [ERROR]:Password contains invalid characters
[VALIDATION] [SUGGESTION]:Ensure password contains only alphanumeric, underscore (_), dollar ($) or pound (#) characters
```
- The password of Analytics Administrator cannot include others special characters than above

Found end lines in 
```
[VALIDATION] [ERROR]:Incorrect Oracle connect string.  Wrong number of : separated fields in '138.2.80.190:1521/DBSystem_pdb1.public.insecure.oraclevcn.com'
[VALIDATION] [SUGGESTION]:For a simple database use the format hostname:port:servicename 
For Application Cluster (RAC) Database use the format host1:port1^host2:port2@servicename
```
- The Oracle connect string cannot accept the typical connection string format. Please follow above guidelines. 
```
[VALIDATION] [ERROR]:PreReq Check for create new schema failed.
```

