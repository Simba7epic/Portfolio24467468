# Simple Threat Intelligence Module

threat_signatures = {
    "port_scan": {
        "keywords": ["nmap", "SYN scan", "port scan"],
        "severity": "MEDIUM"
    },
    "brute_force": {
        "keywords": ["failed login", "multiple attempts", "authentication failure"],
        "severity": "HIGH"
    },
    "suspicious_traffic": {
        "keywords": ["unusual traffic", "multiple requests", "bot-like"],
        "severity": "MEDIUM"
    },
    "malware_indicator": {
        "keywords": ["unknown executable", "suspicious file", "hash mismatch"],
        "severity": "HIGH"
    }
}

def analyse_log(event):
    event_lower = event.lower()

    alerts = []

    for threat_type, data in threat_signatures.items():
        for keyword in data["keywords"]:
            if keyword in event_lower:
                alerts.append({
                    "threat": threat_type,
                    "severity": data["severity"],
                    "matched_keyword": keyword,
                    "original_event": event
                })

    if not alerts:
        return [{
            "threat": "clean",
            "severity": "LOW",
            "message": "No threats detected",
            "original_event": event
        }]

    return alerts


# ------------------------
# TEST CASES (SIMULATED LOGS)
# ------------------------

logs = [
    "Multiple failed login attempts detected from IP 192.168.1.10",
    "User executed nmap SYN scan against server",
    "Normal user login successful",
    "Unusual traffic pattern detected with multiple requests per second",
    "File download with unknown executable signature"
]

for log in logs:
    results = analyse_log(log)
    print("\nEvent:", log)
    for r in results:
        print(" ->", r)