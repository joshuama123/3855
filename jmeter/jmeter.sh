JMETER_DIR="${HOME}/Desktop/Term4/3885/KDproject/jmeter"

rm -rf ${JMETER_DIR}/results.jtl
rm -rf ${JMETER_DIR}/report

echo ${1:-10} threads, ${2:-10} loops

/Library/Java/JavaVirtualMachines/temurin-26.jdk/Contents/Home/bin/java  \
    -jar /opt/homebrew/Cellar/jmeter/5.6.3/libexec/bin/ApacheJMeter.jar \
    -t ${JMETER_DIR}/3855.jmx \
    -Jthreads=${1:-10} \
    -Jloops=${2:-10} \
    -n -l ${JMETER_DIR}/results.jtl -e -o ${JMETER_DIR}/report

    #