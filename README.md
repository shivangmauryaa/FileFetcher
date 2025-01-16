# FileFetcher

**FileFetcher** is a Python tool that extracts and filters URLs from archived Wayback Machine data based on specific file types like `.pdf`, `.zip`, `.sql`, `.xls`, and more. It checks the availability of each URL, saving valid ones with a 200 OK response to a text file. Perfect for web scraping, research, or retrieving historical files from archived domains.

---

## Features

- Fetch URLs from Wayback Machine for a given domain.
- Filter URLs by specific file extensions such as `.pdf`, `.zip`, `.xls`, `.sql`, `.txt`, and more.
- Validate URLs by checking their response status (200 OK).
- Option to process multiple domains by providing a text file with domain names.
- Saves valid URLs to a text file.
- Progress bar to show the URL checking process.
- Clean, easy-to-read, colored output in the terminal.

---

## Requirements

- Python 3.6+
- `requests`
- `pyfiglet`
- `colorama`
- `tqdm`

---

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/shivangmauryaa/FileFetcher.git
cd FileFetcher
```

## Install dependencies
1.Install the required dependencies using pip

```bash
pip install -r requirements.txt
```

## Input Options

You can use the script in two ways:

1. **Single Domain**: 
   - When prompted, enter a domain (e.g., `example.com`).
   - The script will extract URLs related to the provided domain.

2. **Multiple Domains from a File**: 
   - Press Enter to load domains from a file.
   - Provide the file name containing domains, one per line.
   - Example input file:
     ```
     example1.com
     example2.com
     example3.com
     ```


## Author

- **Name**: Shivang Maurya
- **GitHub**: [ShivangMaurya](https://github.com/ShivangMaurya)
- **Email**: shivangmauryaa@gmail.com

