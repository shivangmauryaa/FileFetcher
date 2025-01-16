# FileFetcher

**FileFetcher** is a Python tool that extracts and filters URLs from archived Wayback Machine data based on file types like `.pdf`, `.zip`, `.sql`, and more. It checks the availability of each URL, saving valid ones with a 200 OK response to a text file, ideal for research or web scraping.

---

## Features

- Fetch URLs from Wayback Machine for a given domain.
- Filter URLs by specific file extensions like `.pdf`, `.zip`, `.xls`, `.sql`, `.txt`, and more.
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
git clone https://github.com/yourusername/url-extractor.git
cd url-extractor
