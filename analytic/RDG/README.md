# Remote Data Gateway (RDG)
[wiki](https://github.com/davidkhala/oracle-PaaS-collection/wiki/Analyic:-Remote-Data-Gateway-(RDG))

## Docker containerize
Tech notes
- We read, understand and migrate $Oracle_Home/domain/bin/startJetty.sh to a Dockerfile Entrypoint, in order to
  - Make it running in front, to fit container design
  - Make it share the context of Dockerfile, to reuse Env variables
- system check will failed on docker when `Checking swap space: must be greater than 512 MB.   Actual 0 MB    Failed <<<< `
  - We use flag `-ignoreSysPrereqs` to skip this checking. 
- Please make sure your hostPost ${hostPort} is opened in host firewall, to make docker service available to external access.
- We find a trick to skip website Basic Auth: leave `CREDENTIALS_PAGE_PASSWORD` blank in `silentInstall.response` config file.


Docker build
```
export hostPort=8080
./docker.sh build
```
Docker run
```
./docker.sh run
```

# License
Downloading or using Remote Data Gateway indicates you have read the [Oracle Technology Network License Agreement
](https://www.oracle.com/downloads/licenses/distribution-license.html) carefully and accept the agreement.

