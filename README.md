# IP WHOIS Lookup

A small Python script that reads IP addresses from a text file, performs a WHOIS lookup on each, and saves the results to a CSV file.


## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Create `input.txt` in the same folder, with one IP address per line:
   ```
   8.8.8.8
   1.1.1.1
   ```
2. Run the script:
   ```bash
   python lookup.py
   ```
3. Results are appended to `WhoIs_Look_Up.csv`.

## Notes

- IPs that fail to resolve are written as `Not Found`.

## License

MIT
