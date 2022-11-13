build() {
    docker build -t rdg:latest .
}
run() {
    local hostPort=${hostPort:-8080}
    local host=${host:-localhost}
    docker run -d -p=${hostPort}:8080 --name=analytic-rdg rdg:latest $@
    echo "Please make sure your hostPost ${hostPort} is opened in host firewall..."
    echo "URL: http://${host}:${hostPort}/obiee/config.jsp"
}
run-jdbc() {
    hostPort=80
    local driverJar=$1
    local filename=$(basename $driverJar)
    run --volume=$driverJar:/home/opc/Oracle/Middleware/Oracle_Home/domain/jettybase/thirdpartyDrivers/$filename
}
run-mariaDB() {
    run-jdbc ./drivers/mariadb-java-client-3.0.9.jar
}
tail-log() {
    docker logs -f analytic-rdg
}

$@
