# CLI Tokenizer Counter

A simple command-line tool for counting tokens in text using the `tiktoken` library. This tool can read text from standard input or from command-line arguments.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Installation

### Prerequisites

Ensure you have Python 3 and pip installed on your system. You can check their installation using:

```bash
python3 --version
pip3 --version
```

If either command is not found, please install Python 3 and pip first.

### Install tiktoken

Install the `tiktoken` library which is essential for counting tokens. You can do this manually or use the provided script.

To install manually, run:

```bash
pip3 install tiktoken
```

Alternatively, you can use the installation script provided:

```bash
./install.sh
```

This script checks for Python and pip, and installs `tiktoken` if it's not already installed.

## Usage

You can use the command-line tool in two ways:

1. **Pass text as command-line arguments:**

```bash
python3 cli-tokenizer-counter.py "your text here"
```

2. **Pipe text from a file or standard input:**

```bash
cat file.txt | python3 cli-tokenizer-counter.py
```

### Error Handling

If you do not provide any text, the script will display usage instructions:

```bash
Usage: cli-tokenizer-counter.py <text>
   or: cat file.txt | cli-tokenizer-counter.py
```

## Examples

1. **Count tokens from command-line arguments:**

```bash
python3 cli-tokenizer-counter.py "Hello, world!"
```
Output:
```
Token count: 4
```

2. **Count tokens from a file:**

```bash
cat example.txt | python3 cli-tokenizer-counter.py
```
Output:
```
Token count: X
```
Where `X` is the count of tokens present in `example.txt`.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

---

Feel free to contribute or report any issues you encounter!
