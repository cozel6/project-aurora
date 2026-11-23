from statistics import mean, pstdev

FEATURE_SCHEMA_VERSION = "v1"

FEATURE_NAMES = [
    "proto_tcp", "proto_udp", "proto_icmp",      # 0-2
    "pkt_count", "byte_count",                   # 3-4
    "pkts_per_sec", "bytes_per_sec",             # 5-6
    "flow_duration",                             # 7
    "pkt_size_mean", "pkt_size_std",             # 8-9
    "iat_mean", "iat_std",                       # 10-11
    "syn_count", "ack_count", "fin_count", "rst_count",  # 12-15
    "syn_ack_ratio",                             # 16
    "distinct_dst_ports",                        # 17
]

def build_features(packets, window_seconds, distinct_dst_ports):
    """Un flow (>= 1) aceeasi fereastra -> vector de len(FEATURE_NAMES) float in ordinea FEATURE_NAMES"""
    protocol = packets[0]["protocol"]
    sizes = [p["size"] for p in packets]
    times = sorted(p["ts"] for p in packets)

    pkt_count = len(packets)
    byte_count = sum(sizes)
    flow_duration = times[-1] - times[0] # 0.0 daca 1 pachet

    iats = [b - a for a, b in zip(times, times[1:])]
    iat_mean = mean(iats) if iats else 0.0
    iat_std = pstdev(iats) if iats else 0.0

    syn_count = sum("S" in p["flags"] for p in packets)
    ack_count = sum("A" in p["flags"] for p in packets)
    fin_count = sum("F" in p["flags"] for p in packets)
    rst_count = sum("R" in p["flags"] for p in packets)

    vector = [
        float(protocol == "TCP"), float(protocol == "UDP"), float(protocol == "ICMP"),
        pkt_count, byte_count,
        pkt_count / window_seconds, byte_count / window_seconds,
        flow_duration,
        mean(sizes), pstdev(sizes),
        iat_mean, iat_std,
        syn_count, ack_count, fin_count, rst_count,
        syn_count / max(ack_count, 1),
        distinct_dst_ports,
    ]
    assert len(vector) == len(FEATURE_NAMES)
    return [float(x) for x in vector]

