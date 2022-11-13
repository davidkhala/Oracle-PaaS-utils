set -e
Name=${Name:-analytic-rdg}
image=${image:-rdg}
USERNAME=opc
Oracle_Home=/home/${USERNAME}/RDG
build() {
    
    docker build -t rdg:latest --progress=plain --no-cache . 
}
run() {
    local hostPort=${hostPort:-8080}
    local host=${host:-localhost}
    docker run -d -p=${hostPort}:8080 --name=$Name $@ $image:latest 
    echo "Please make sure your hostPost ${hostPort} is opened in host firewall..."
    echo "URL: http://${host}:${hostPort}/obiee/config.jsp"
}
run-jdbc() {
    local driverJar=$1
    local filename=$(basename $driverJar)
    
    run --volume=$driverJar:/home/opc/RDG/domain/jettybase/thirdpartyDrivers/$filename

}
run-mariaDB() {
    run-jdbc $PWD/drivers/mariadb-java-client-3.0.9.jar
}

_test(){
    host=168.138.163.237
    set +e
    docker stop $Name
    set -e
    docker system prune --force
    build
    run-mariaDB
    docker logs -f analytic-rdg
}
$@
