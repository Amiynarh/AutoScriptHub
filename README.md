# AutoScriptHub
Welcome to AutoScriptHub, a collection of Python scripts designed to automate a variety of tasks, streamlining your workflow and increasing efficiency. Each script in this repository serves a unique purpose, from encoding secrets for secure storage to handling data processing tasks automatically.

## Featured Scripts

### Secret Encoder
- **Description**: This script, `encode_secrets.py`, automates the process of encoding sensitive configuration data. It reads secrets from a plain text file, encodes each secret's value using base64, and saves the results back to a new file. This ensures that sensitive information is stored securely and ready for safe transmission or configuration management.
- **Usage**:
  1. Place all your secrets in `secrets.txt`, formatted as `KEY=value`.
  2. Run the script with `python3 encode_secrets.py`.
  3. Encoded secrets will be saved in `encoded_secrets.txt`.
