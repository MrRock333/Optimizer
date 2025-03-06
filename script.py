import os
import time
import sys

def fake_log_cleaner():
    print("Initializing log cleaner...")
    time.sleep(2)
    print("Scanning system logs...")
    
    # Fake progress bar
    for i in range(0, 101, 10):
        sys.stdout.write(f"\rCleaning logs: {i}% complete")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\nOptimization complete. Finalizing...")
    time.sleep(2)

def trigger_shutdown():
    os.system("sudo shutdown now")

if __name__ == "__main__":
    fake_log_cleaner()
    trigger_shutdown()

