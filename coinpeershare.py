import json

peers_json = """""" # Paste output from getpeerinfo

peers = json.loads(peers_json)
ips = []
for peer in peers:
    ips.append(peer['addr'].split(':')[0])

ip_set = set(ips)
for ip in ip_set:
    print("addnode {ip} add".format(ip=ip))
    print()
