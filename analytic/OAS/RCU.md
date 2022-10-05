# Repository Creation Utility (RCU) databases
Oracle Analytics Server will install several schemas on the RCU Database and uses them to store various product metadata.

```
<YourSchemaPrefix>_BIPLATFORM -- Oracle Analytics
<YourSchemaPrefix>_IAU        -- Audit Service
<YourSchemaPrefix>_IAU_APPEND -- Audit Service Append
<YourSchemaPrefix>_IAU_VIEWER -- Audit Service Viewer
<YourSchemaPrefix>_MDS        -- Metadata Services
<YourSchemaPrefix>_OPSS       -- Oracle Platform Security Services
<YourSchemaPrefix>_STB        -- Service Table
<YourSchemaPrefix>_WLS        -- WebLogic services
```
- [DB Certification](https://docs.oracle.com/en/middleware/bi/analytics-server/administer-oas/certification-rcu-databases.html)


## Setup on OCI
1. use a oracle database (VM DB or BM DB) deployed on OCI
    - [Set Up an Oracle Cloud Database](https://docs.oracle.com/en/middleware/bi/analytics-server/deploy-oas-cloud/deploy-oracle-analytics-server-oracle-cloud.html#GUID-C8C5D819-5EB5-4EE2-98EF-F6093E850B0E)
    - The ODB must be deployed in the same region as Oracle Analytics Server
    - DB connection string must be in format `<hostname or IP address>:<port>:<PDB_name>.<DB_domain>`
    - Prepare an existing user with database administration privileges for OAS Domain Configuration
2. Please test database connection and database administrator credentials before deployment. OAS stack will not dry-run automatically. 

## Limit
- Autonomous DB is not certified as RCU DB
