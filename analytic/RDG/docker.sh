build() {
    docker build -t rdg:latest .
}
run() {
    docker run -d --name=analytic-rdg rdg:latest $@
    docker logs -f analytic-rdg
}

$@
