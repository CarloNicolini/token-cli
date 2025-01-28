#!/usr/bin/env python3
import sys
import tiktoken

def count_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

if __name__ == "__main__":
    # Check if there's input from stdin
    if not sys.stdin.isatty():
        # Read from stdin
        text = sys.stdin.read().strip()
    elif len(sys.argv) > 1:
        # If no stdin, use command line arguments
        text = " ".join(sys.argv[1:])
    else:
        print("Usage: cli-tokenizer-counter.py <text>")
        print("   or: cat file.txt | cli-tokenizer-counter.py")
        sys.exit(1)
    
    token_count = count_tokens(text)
    print(f"Token count: {token_count}")