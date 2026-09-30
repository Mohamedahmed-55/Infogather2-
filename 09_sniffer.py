from scapy.all import sniff 
def process_packets(packet):
    print(f"packet {packet.summary()}")
def start_sniff():
    print("starting packet sniffer...")
    sniff(prn=process_packets,count=10)    
