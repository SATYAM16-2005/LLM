def detect_intent(tokens):
    if any(word in tokens for word in ["show", "list", "get", "display"]):
        return "SELECT"
    return None
