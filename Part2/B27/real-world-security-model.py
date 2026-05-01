# =========================================================
# B27 - Real-World Application of RBAC + Threat Detection
# =========================================================

# -------------------------
# USER ROLE DATABASE
# -------------------------
users = {
    "alice": "admin",
    "bob": "staff",
    "charlie": "student"
}

# -------------------------
# ROLE PERMISSIONS (RBAC)
# -------------------------
permissions = {
    "admin": ["view_logs", "delete_user", "view_dashboard", "edit_settings"],
    "staff": ["view_dashboard", "view_logs"],
    "student": ["view_dashboard"]
}

# -------------------------
# SIMPLE THREAT INTELLIGENCE RULES
# -------------------------
threat_rules = {
    "brute_force": ["failed login", "incorrect password", "authentication failure"],
    "suspicious_activity": ["multiple attempts", "unusual login", "new device"],
    "enumeration": ["user not found", "invalid username"]
}

# -------------------------
# THREAT DETECTION ENGINE
# -------------------------
def detect_threat(event):
    event_lower = event.lower()

    for threat_type, keywords in threat_rules.items():
        for keyword in keywords:
            if keyword in event_lower:
                return f"THREAT DETECTED: {threat_type.upper()}"

    return "No threats detected"


# -------------------------
# ACCESS CONTROL FUNCTION
# -------------------------
def access_system(username, action, event_log):
    print("\n--- LOGIN EVENT ---")
    print("User:", username)
    print("Action:", action)

    # Step 1: Threat detection
    threat_result = detect_threat(event_log)
    print("Security Scan:", threat_result)

    if "THREAT DETECTED" in threat_result:
        return "ACCESS BLOCKED: Suspicious activity detected"

    # Step 2: RBAC check
    role = users.get(username)

    if not role:
        return "ACCESS DENIED: Unknown user"

    if action in permissions[role]:
        return f"ACCESS GRANTED: {username} performed {action}"
    else:
        return f"ACCESS DENIED: {username} not authorised for {action}"


# -------------------------
# TEST SCENARIOS (REAL-WORLD SIMULATION)
# -------------------------

# 1. Normal admin access
print(access_system(
    "alice",
    "delete_user",
    "normal login successful"
))

# 2. Student trying admin action
print(access_system(
    "charlie",
    "delete_user",
    "normal login successful"
))

# 3. Suspicious login attempt (brute force)
print(access_system(
    "bob",
    "view_dashboard",
    "multiple failed login attempts detected from IP"
))

# 4. Unknown user attempt
print(access_system(
    "hacker123",
    "view_dashboard",
    "user not found during login attempt"
))