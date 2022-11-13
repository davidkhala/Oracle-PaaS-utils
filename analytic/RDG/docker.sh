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
tail-log() {
    docker logs -f analytic-rdg
}

$@
