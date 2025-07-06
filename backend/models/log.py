import re
from datetime import datetime, timedelta
from collections import defaultdict

# Example list of known malicious IPs
MALICIOUS_IPS = {"192.168.1.100", "10.0.0.66"}

# Store login attempts by IP
failed_logins = defaultdict(list)

def parse_log(log_text: str):
    results = []
    lines = log_text.splitlines()

    for i, line in enumerate(lines, start=1):
        threat = None

        # Brute force detection
        if "Failed password" in line:
            ip = extract_ip(line)
            time = extract_time(line)
            if ip and time:
                failed_logins[ip].append(time)
                recent_attempts = [
                    t for t in failed_logins[ip] if time - t < timedelta(minutes=1)
                ]
                if len(recent_attempts) > 5:
                    threat = f"⚠️ Brute Force Suspected from {ip}"

        # Suspicious login time
        if "Accepted password" in line:
            time = extract_time(line)
            if time and (time.hour < 4 or time.hour > 22):
                threat = f"⚠️ Suspicious Login Time: {time.strftime('%H:%M')}"

        # Privilege escalation detection
        if re.search(r'\bsudo\b|\bsu\b|chmod\s+777|passwd|root', line):
            threat = "⚠️ Possible Privilege Escalation Attempt"

        # Known malicious IPs
        if any(ip in line for ip in MALICIOUS_IPS):
            threat = "❌ Known Malicious IP Detected"

        results.append({
            "line": i,
            "content": line,
            "threat": threat
        })

    return results

def extract_ip(line):
    match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
    return match.group(0) if match else None

def extract_time(line):
    try:
        match = re.search(r'\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}', line)
        if match:
            now = datetime.now()
            full_time_str = f"{now.year} {match.group(0)}"
            return datetime.strptime(full_time_str, "%Y %b %d %H:%M:%S")
    except:
        return None
