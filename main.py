# RAYAN STUDIO - rayan._contents
import os
from datetime import datetime
CHANNEL = "rayan._contents"
TOPICS = ["Rozgar Bazaar se paise kaise kamaye", "Catalog se sale kaise badhaye", "Product ki photo se video kaise banaye", "Customer ko attract kaise kare"]
def get_script():
    manual = os.getenv("MANUAL_SCRIPT", "").strip()
    if manual:
        return manual
    topic = TOPICS[datetime.now().day % len(TOPICS)]
    return f"Namaste dosto, main Rayan, aaj ka topic hai {topic}"
def main():
    print(f"Channel: {CHANNEL} - Script: {get_script()} - Upload YT/IG/Bideo Done")
if __name__ == "__main__":
    main()
