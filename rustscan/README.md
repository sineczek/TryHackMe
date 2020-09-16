# Rustscan
**better, faster nmap

## HP: https://github.com/Rustscan

###rustscan -h
```Fast Port Scanner built in Rust. WARNING Do not use this program against sensitive infrastructure since the specified
server may not be able to handle this many socket connections at once. - Discord https://discord.gg/GFrQsGy - GitHub
https://github.com/RustScan/RustScan

USAGE:
    rustscan [FLAGS] [OPTIONS] [addresses]... [-- <command>...]

FLAGS:
        --accessible    Accessible mode. Turns off features which negatively affect screen readers
    -h, --help          Prints help information
    -n, --no-config     Whether to ignore the configuration file or not
        --no-nmap       Turns off Nmap
    -q, --quiet         Quiet mode. Only output the ports. No Nmap. Useful for grep or outputting to a file
    -V, --version       Prints version information

OPTIONS:
    -b, --batch-size <batch-size>    The batch size for port scanning, it increases or slows the speed of scanning.
                                     Depends on the open file limit of your OS.  If you do 65535 it will do every port
                                     at the same time. Although, your OS may not support this [default: 4500]
    -p, --ports <ports>...           A list of comma separed ports to be scanned. Example: 80,443,8080
    -r, --range <range>              A range of ports with format start-end. Example: 1-1000
        --scan-order <scan-order>    The order of scanning to be performed. The "serial" option will scan ports in
                                     ascending order while the "random" option will scan ports randomly [default:
                                     serial]  [possible values: Serial, Random]
    -t, --timeout <timeout>          The timeout in milliseconds before a port is assumed to be closed [default: 1500]
    -u, --ulimit <ulimit>            Automatically ups the ULIMIT with the value you provided

ARGS:
    <addresses>...    A list of comma separated CIDRs, IPs, or hosts to be scanned
    <command>...      The Nmap arguments to run. To use the argument -A, end RustScan's args with '-- -A'. Example:
                      'rustscan -t 1500 127.0.0.1 -- -A -sC'. This command adds -Pn -vvv -p $PORTS automatically to
                      nmap. For things like --script '(safe and vuln)' enclose it in quotations marks \"'(safe and
                      vuln)'\"")
```

