import requests
import re
import pyfiglet
from colorama import Fore, Style, init
from tqdm import tqdm  # Progress bar
from urllib.parse import urlparse

# Initialize colorama
init(autoreset=True)

# Constants
WAYBACK_URL = "https://web.archive.org/cdx/search/cdx"
FILE_EXTENSIONS = r'\.(xls|xml|xlsx|json|pdf|sql|doc|docx|pptx|txt|zip|tar\.gz|tgz|bak|7z|rar|log|cache|secret|db|backup|yml|gz|config|csv|yaml|md|md5|exe|dll|bin|ini|bat|sh|tar|deb|rpm|iso|img|apk|msi|dmg|tmp|crt|pem|key|pub|asc)'

# Functions
def fetch_wayback_urls(domain):
    """Fetch URLs from the Wayback Machine."""
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Fetching URLs from Wayback Machine for {domain}...")
    params = {
        "url": f"*.{domain}/*",
        "collapse": "urlkey",
        "output": "text",
        "fl": "original"
    }
    response = requests.get(WAYBACK_URL, params=params)
    if response.status_code == 200:
        urls = response.text.splitlines()
        print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Retrieved {Fore.RED}{len(urls)}{Style.RESET_ALL} URLs from Wayback Machine for {domain}.")
        return urls
    else:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Failed to fetch URLs from Wayback Machine for {domain}.")
        return []

def filter_urls_by_filetype(urls):
    """Filter URLs by specific file extensions."""
    filtered = [url for url in urls if re.search(FILE_EXTENSIONS, url, re.IGNORECASE)]
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Filtered {Fore.RED}{len(filtered)}{Style.RESET_ALL} URLs matching file types.")
    return filtered

def validate_urls(urls):
    """Check if URLs respond with a 200 OK."""
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Validating URLs...")
    valid_urls = []
    for url in tqdm(urls, desc="Checking URLs", unit="url"):
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                valid_urls.append(url)
        except requests.RequestException:
            pass
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Found {Fore.RED}{len(valid_urls)}{Style.RESET_ALL} valid URLs with a 200 OK response.")
    return valid_urls
def sanitize_domain(domain):
    """Extract and sanitize the domain name for file naming."""
    parsed_url = urlparse(domain)
    clean_domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path
    return clean_domain.replace("/", "_")  # Replace any slashes to avoid issues

def save_to_file(data, filename):
    """Save a list of URLs to a file."""
    with open(filename, "w") as f:
        f.write("\n".join(data))
    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Saved valid URLs to {Fore.YELLOW}{filename}{Style.RESET_ALL}.")

def process_domains(domains):
    """Process all domains and fetch URLs."""
    all_urls = []
    for domain in domains:
        print(f"\n{Fore.CYAN}[INFO]{Style.RESET_ALL} Processing domain: {Fore.YELLOW}{domain}{Style.RESET_ALL}")
        # Fetch URLs for each domain
        wayback_urls = fetch_wayback_urls(domain)
        # Filter URLs for each domain
        filtered_urls = filter_urls_by_filetype(wayback_urls)
        all_urls.extend(filtered_urls)

    # After processing all domains, validate URLs and save results
    valid_urls = validate_urls(all_urls)
    safe_domain = sanitize_domain(domain)                                                                                   
    filename = f"{safe_domain}_valid_urls.txt"                                                                              
    save_to_file(valid_urls, filename)
    print(f"{Fore.MAGENTA}[RESULT]{Style.RESET_ALL} Total valid URLs: {Fore.RED}{len(valid_urls)}{Style.RESET_ALL}.")

# Main function
def main():
    # Display ASCII Art Banner
    ascii_banner = pyfiglet.figlet_format("URL Extractor")
    print(Fore.LIGHTGREEN_EX + ascii_banner + Style.RESET_ALL)

    print(f"{Fore.RED}Made by shivangmauryaa{Style.RESET_ALL}")

    domain_input = input(f"{Fore.CYAN}Enter the domain (e.g., example.com), or press Enter to load from file: {Style.RESET_ALL}").strip()

    if not domain_input:
        # If the user presses Enter, ask for a file
        file_name = input(f"{Fore.CYAN}Enter the file name containing domains: {Style.RESET_ALL}").strip()
        try:
            with open(file_name, "r") as file:
                domains = [line.strip() for line in file if line.strip()]
            print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Found {Fore.RED}{len(domains)}{Style.RESET_ALL} domains in {file_name}.")
            # Process all domains together
            process_domains(domains)
        except FileNotFoundError:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} File {file_name} not found. Please try again.")
    else:
        # Process a single domain
        process_domains([domain_input])

if __name__ == "__main__":
    main()
