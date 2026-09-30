import argparse
from modules.ping import ping_target
from modules.scan import port_scanner
from modules.brute_force import brute_force_login
from modules.dir_fuzzer import dir_fuzzer
from modules.download import parse
from modules.XSS_SQLi_Scanner import scan_vulnerabilities
from modules.http_logger import start_logger
from modules.sniffer import start_sniff
from modules.spoof import simulate_dns_spoof

parser=argparse.ArgumentParser(description="Advanced InfoGather & Attack Tool")
parser.add_argument("--ping",help="pinging a target (IP,Domain)")
parser.add_argument("--scan",help="scan port on a target")
parser.add_argument("--brute",help="brute force loginwith wordlist.txt")
parser.add_argument("--fuzz",help="Directory fuzzer for hidden paths")
parser.add_argument("--parse",help="Download and extract title from a webpage")
parser.add_argument("--xss",help="scan for (XSS,SQLi) vulnerability")
parser.add_argument("--log",action="store_true",help="Start http rrequest logger")
parser.add_argument("--sniff",action="store_true",help="Start netword sniffer")
parser.add_argument("--spoof",action="store_true",help="simulate DNS spoof (testing only)")

args=parser.parse_args()
if args.ping:
    ping_target(args.ping)
elif args.scan:
    port_scanner(args.scan)
elif args.brute:
    brute_force_login(args.brute)
elif args.fuzz:
    dir_fuzzer(args.fuzz)
elif args.parse:
    parse(args.parse)
elif args.xss:
    scan_vulnerabilities(args.xss)
elif args.log:
    start_logger()
elif args.sniff:
    start_sniff()
elif args.spoof:
    simulate_dns_spoof()
else:
    print("no valid option provided. Use --help to see available commands")