# OAS Installation

### Product Schemas

Oracle Analytics Server installs several schemas on the RCU Database and uses them to store various product metadata.

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


## post deploy
- install `sudo yum install -y libgfortran` if you want to use automated machine learning features





