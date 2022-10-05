# Oracle Analytics


## Oracle Analytic Server
- Access URL: `http://<OAS_Public_IP_Address>:9502/analytics`

- 

- OAS is CPU-intensive

### Before you begin
Oracle Analytics Server needs access to a oracle database deployed on OCI 
[Set Up an Oracle Cloud Database](https://docs.oracle.com/en/middleware/bi/analytics-server/deploy-oas-cloud/deploy-oracle-analytics-server-oracle-cloud.html#GUID-C8C5D819-5EB5-4EE2-98EF-F6093E850B0E)
- Oracle Analytics Server can install various required database schemas on that DB
- The ODB must be deployed in the same region as Oracle Analytics Server
- The ODB must be accessible from the VCN where you plan to deploy Oracle Analytics Server.
- The ODB version must be 12.1, 12.2, 18+, or 19+.
- The database must be a pluggable database (PDB)
  - DB connection string must be in format <hostname or IP address>:<port>:<PDB_name>.<DB_domain>
  - Please test database connection and database administrator credentials before deployment. OAS will not do dry-run in deploy stack. 
- Prepare an existing user with database administration privileges for OAS Domain Configuration

Oracle Analytics Server Domain Configuration is a must for new OAS deployment
- Skip only when creating an additional Oracle Analytics Server compute instance to scale out an existing Oracle Analytics Server deployment.

