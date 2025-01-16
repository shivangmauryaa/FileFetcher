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

## Install dependencies
1.Install the required dependencies using pip

```bash
pip install -r requirements.txt
