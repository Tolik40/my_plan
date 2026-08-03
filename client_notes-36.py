# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ClientNotes
def check_and_repair_data(data, repair_log):
    issues = []
    
    if not isinstance(data, dict):
        return data, ["Top-level is not a dictionary"]
    
    if "contacts" not in data or not isinstance(data["contacts"], list):
        if "contacts" not in data:
            issues.append("Missing 'contacts' key")
        else:
            issues.append("'contacts' is not a list")
        return data, issues
    
    for i, contact in enumerate(data["contacts"]):
        if not isinstance(contact, dict) or "name" not in contact:
            issues.append(f"Contact {i}: missing name or not a dict")
    
    if "meetings" not in data or not isinstance(data["meetings"], list):
        if "meetings" not in data:
            issues.append("Missing 'meetings' key")
        else:
            issues.append("'meetings' is not a list")
        return data, issues
    
    for i, meeting in enumerate(data["meetings"]):
        required = {"date": str, "client": (str, int)}
        if not isinstance(meeting, dict):
            issues.append(f"Meeting {i}: not a dict")
            continue
        missing_keys = [k for k, v in required.items() if k not in meeting or not isinstance(meeting[k], v)]
        if missing_keys:
            issues.append(f"Meeting {i}: missing keys - {missing_keys}")
    
    if "tasks" not in data or not isinstance(data["tasks"], list):
        if "tasks" not in data:
            issues.append("Missing 'tasks' key")
        else:
            issues.append("'tasks' is not a list")
        return data, issues
    
    for i, task in enumerate(data["tasks"]):
        required = {"title": str, "status": (str, int)}
        if not isinstance(task, dict):
            issues.append(f"Task {i}: not a dict")
            continue
        missing_keys = [k for k, v in required.items() if k not in task or not isinstance(task[k], v)]
        if missing_keys:
            issues.append(f"Task {i}: missing keys - {missing_keys}")
    
    return data, issues

def repair_simple_problems(data):
    repaired = dict(data)
    
    if "contacts" in repaired and not isinstance(repaired["contacts"], list):
        repaired["contacts"] = []
    
    if "meetings" in repaired and not isinstance(repaired["meetings"], list):
        repaired["meetings"] = []
    
    if "tasks" in repaired and not isinstance(repaired["tasks"], list):
        repaired["tasks"] = []
    
    return repaired
