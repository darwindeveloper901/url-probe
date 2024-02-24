# 🌐 URL Probe 

This Python script provides a tool for checking HTTP status codes of URLs listed in a wordlist file.

## 🚀 Usage

### Prerequisites
- Python 3.x
- Requests library (install using `pip install requests`)

### Usage
```bash
python status.py -w <wordlist_file_path> -u <target_url>
```

## 📋 Parameters
- -w, --wordlist: Path to the wordlist file 📄
- -u, --url: Target URL to check 🎯

<img src = "https://github.com/darwindeveloper901/url-probe/blob/main/assets/image.png">

## 🛠️ Features

- Supports both HTTP and HTTPS URLs.
- Customizable user-agent headers for requests.
- Saves results to a timestamped text file.
