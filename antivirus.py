import os

# List of known malware signatures (hexadecimal patterns)
malware_signatures = [
    "68656c6c6f6d616c77617265",  # "hellomalware" in hex for demo purposes
    "4d5a90000300000004000f00",  # Common PE file signature for potential Windows malware
]

def scan_file(file_path):
    """Scan a file for known malware signatures."""
    try:
        with open(file_path, "rb") as f:
            file_content = f.read().hex()
            for signature in malware_signatures:
                if signature in file_content:
                    print(f"[WARNING] Malware detected in {file_path}")
                    return True
    except Exception as e:
        print(f"[ERROR] Failed to scan {file_path}: {e}")
    return False

def scan_directory(directory):
    """Recursively scan a directory for malware."""
    infected_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if scan_file(file_path):
                infected_files.append(file_path)
    if infected_files:
        print("\nScan complete. Infected files found:")
        for file in infected_files:
            print(f"- {file}")
    else:
        print("\nScan complete. No infected files found.")

if __name__ == "__main__":
    directory_to_scan = input("Enter the directory to scan: ")
    if os.path.isdir(directory_to_scan):
        scan_directory(directory_to_scan)
    else:
        print("Invalid directory path. Please try again.")
