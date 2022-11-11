# Remote Data Gateway (RDG)
- Installation binary cannot be executed as root or super user
  - `# SEVERE [1] com.oracle.cie.nextgen.launcher.Launcher - The current user is root or has superuser privilege. The Oracle Universal Installer cannot continue.`
- If `-invPtrLoc` not specified, it defaults to `/etc/oraInst.loc`

## Docker build
```
cd analytic/RDG/
docker build -t rdg:latest . 
```


- system check will failed on docker when `Checking swap space: must be greater than 512 MB.   Actual 0 MB    Failed <<<< `
  - We use flag `-ignoreSysPrereqs` to skip this checking. 