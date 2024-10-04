def get_status(is_busy):
    status = {}
    status["status"] = "busy" if is_busy else "available"
    return status
