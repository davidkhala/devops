org() {
  pulumi org set-default ${1:-davidkhala}

}
logback() {
  pulumi logout && pulumi login
}
status() {
  # View backend, current stack, pending operations, and versions
  pulumi about
}
$@
