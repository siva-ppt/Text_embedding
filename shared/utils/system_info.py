import platform
import psutil

def get_system_info():
    return {
        "platform": platform.platform(),
        "cpu": platform.processor(),
        "ram": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
        "python_version": platform.python_version(),
    }
