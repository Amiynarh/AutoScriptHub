# Secret Encoder

The Secret Encoder script is designed to securely encode sensitive configuration data, making it safer to store or transmit. It uses base64 encoding to convert plain text secrets into a non-readable format, while retaining the original structure of key-value pairs.

## Features

- **Secure Encoding**: Encodes secret values while keeping the keys visible for easy reference.
- **Batch Processing**: Process multiple secrets at once from a text file.
- **Easy to Integrate**: Can be incorporated into larger workflows for automated configurations and deployments.

## Prerequisites

Before you can run the script, make sure you have Python installed on your system. Python 3.x is recommended. You can download it from [python.org](https://www.python.org/downloads/).


## Usage

To use the Secret Encoder, you need to prepare a text file named `secrets.txt` in the `secret-encoder` directory. Each line should contain a secret in the form of `KEY=value`.

### Running the Script

1. Open your command line interface.
2. Ensure you are in the `secret-encoder` folder.
3. Run the script with the following command:
   ```bash
   python3 encode_secrets.py
   ```
4. Encoded secrets will be saved in `encoded_secrets.txt` in the same directory.

## Example

**Input** (`secrets.txt`):
```
API_KEY=abcdef12345
DB_PASSWORD=secret123
```

**Output** (`encoded_secrets.txt`):
```
API_KEY=YWJjZGVmMTIzNDU=
DB_PASSWORD=c2VjcmV0MTIz
```
