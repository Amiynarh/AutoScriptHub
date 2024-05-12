import base64

def encode_secret(secret):
    # Convert string to bytes, encode it in base64, and then decode back to string
    return base64.b64encode(secret.encode()).decode()

def process_secrets(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove any trailing whitespace or new lines
            line = line.strip()
            if line:  # Make sure line is not empty
                # Split the line into variable name and value
                if '=' in line:
                    variable_name, secret_value = line.split('=', 1)
                    # Encode only the value
                    encoded_secret = encode_secret(secret_value)
                    # Write the variable name and encoded value
                    outfile.write(variable_name + '=' + encoded_secret + '\n')
                else:
                    # Handle the case where there's no '=' to split on
                    outfile.write(line + '\n')

# File names can be changed to whatever is required
input_filename = 'secrets.txt'
output_filename = 'encoded_secrets.txt'

# Call the function with the filenames
process_secrets(input_filename, output_filename)

print("Secrets have been encoded and saved to", output_filename)
