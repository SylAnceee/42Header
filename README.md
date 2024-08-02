
# 42header Usage Instructions

This script automatically inserts the 42 standard header into your source files.

## Setup

1. Make sure you have Python installed on your machine. You can check by running:
   ```bash
   python --version
   ```

2. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   ```

3. Navigate to the repository directory:
   ```bash
   cd <repository-directory>
   ```

4. Make the script executable (if necessary):
   ```bash
   chmod +x 42header.py
   ```

## Usage

1. Run the script with the filename you want to add a header to:
   ```bash
   ./42header.py your_file.c
   ```

2. Ensure the script is in your PATH to run it from anywhere. You can move it to `/usr/local/bin` on Unix-based systems:
   ```bash
   sudo mv 42header.py /usr/local/bin/42header
   ```

3. To use the script in a text editor, create a custom command or binding based on your editor's documentation.

## Customization

- Modify the `USERNAME` and `EMAIL` variables in the `42header.py` file to include your 42 credentials before running the script.
