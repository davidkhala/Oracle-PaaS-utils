start() {
    $Oracle_Home/domain/bin/startJetty.sh
}

stop() {
    $Oracle_Home/domain/bin/stopJetty.sh
}
status() {
    $Oracle_Home/domain/bin/status.sh
}
install() {
    ./DataGateway_Linux64.bin -silent -responseFile ./silentInstall.response -invPtrLoc ./oraInst.loc
}
$@
