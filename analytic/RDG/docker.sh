build() {
    docker build -t rdg:latest .
}
run() {
    local hostPort=${hostPort:-8080}
    docker run -d -p=${hostPort}:8080 --name=analytic-rdg rdg:latest $@
    echo "Please make sure your hostPost ${hostPort} is opened..."
    docker logs -f analytic-rdg
}

$@
