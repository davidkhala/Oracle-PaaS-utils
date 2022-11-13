# Remote Data Gateway (RDG)
- Installation binary cannot be executed as root or super user
  - `# SEVERE [1] com.oracle.cie.nextgen.launcher.Launcher - The current user is root or has superuser privilege. The Oracle Universal Installer cannot continue.`
- If `-invPtrLoc` not specified, it defaults to `/etc/oraInst.loc`

## Docker build
```
export hostPort=8080
./docker.sh build
```
Tech notes
- We have changed the $Oracle_Home/domain/bin/startJetty.sh to make it running in front, to fit container design
- system check will failed on docker when `Checking swap space: must be greater than 512 MB.   Actual 0 MB    Failed <<<< `
  - We use flag `-ignoreSysPrereqs` to skip this checking. 
- Please make sure your hostPost ${hostPort} is opened in host firewall, to make docker service available to external access.