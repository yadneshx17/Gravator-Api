import hashlib
import requests
import pyfiglet
import sys

BLUE_BOLD = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;35m"
RED = "\033[1;31m"
RESET = "\033[0m"

def get_gravatar_profile(email):
    cleanemail = email.strip().lower()
    email_hash = hashlib.md5(cleanemail.encode('utf-8')).hexdigest()
    url = f"https://gravatar.com/{email_hash}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(RED + "Error fetching Gravatar profile:" + RESET, e)
        return None

    return response.json()

def display_profile_data(profiledata):
    if not profiledata:
        print(RED + "No data to display." + RESET)
        return

    entry = profiledata.get("entry")
    if not entry or len(entry) == 0:
        print(RED + "No profile entry found." + RESET)
        return

    data = entry[0]
    
    displaynm = data.get("displayName", "N/A")
    preferreduname = data.get("preferredUsername", "N/A")
    profileurl = data.get("profileUrl", "N/A")
    thumbnailurl = data.get("thumbnailUrl", "N/A")
    aboutme = data.get("aboutMe", "N/A")
    currentloc = data.get("currentLocation", "N/A")

    print(GREEN + "\nGravatar Profile Information:" + RESET)
    print(YELLOW + "Display Name       :" + RESET, CYAN + displaynm + RESET)
    print(YELLOW + "Preferred Username :" + RESET, CYAN + preferreduname + RESET)
    print(YELLOW + "Profile URL        :" + RESET, CYAN + profileurl + RESET)
    print(YELLOW + "Thumbnail URL      :" + RESET, CYAN + thumbnailurl + RESET)
    print(YELLOW + "About Me           :" + RESET, CYAN + aboutme + RESET)
    print(YELLOW + "Current Location   :" + RESET, CYAN + currentloc + RESET)

    urls = data.get("urls")
    if urls:
        print(GREEN + "\nAdditional URLs:" + RESET)
        for url_entry in urls:
            print(MAGENTA + " - " + url_entry.get("value", "N/A") + RESET)
    else:
        print(RED + "No additional URLs found." + RESET)

if __name__ == "__main__":
    banner = pyfiglet.figlet_format("GRAVATON")
    print(BLUE_BOLD + banner + RESET)

    print(MAGENTA + "Developed by: Swayam Sopnic Nayak (https://www.linkedin.com/in/swayamsopnic/)\n" + RESET)
    print(GREEN + "Socials:" + RESET)
    print(" - Twitter: https://x.com/osintambition")
    print(" - LinkedIn: https://www.linkedin.com/company/osintambition/")
    print(" - GitHub: https://github.com/osintambition")
    print("\n")
    print(GREEN + "\nEmail: hi@osintambition.com\n" + RESET)
    
    # Accept email as a command-line argument or prompt the user
    if len(sys.argv) > 1:
        email = sys.argv[1]
    else:
        email = input(CYAN + "Enter your email address: " + RESET)
    
    profile = get_gravatar_profile(email)
    display_profile_data(profile)
