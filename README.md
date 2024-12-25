

# Prime Tokenizer

This Python script reads text from a file, splits it into words, and associates each word with a prime number. The result is a dictionary where the keys are prime numbers and the values are the corresponding words from the text.

## Functions

### `is_prime(n)`
Checks if a number `n` is a prime number.
- **Parameters**: `n` (int) - The number to check.
- **Returns**: `bool` - `True` if `n` is prime, otherwise `False`.

### `generate_primes(limit)`
Generates a list of prime numbers up to a specified limit.
- **Parameters**: `limit` (int) - The number of prime numbers to generate.
- **Returns**: `list` - A list of prime numbers.

### `prime_tokenizer_from_file(file_path, output_file=None)`
Reads text from a file, splits it into words, generates prime numbers, and creates a dictionary mapping primes to words.
- **Parameters**:
  - `file_path` (str) - The path to the input file.
  - `output_file` (str, optional) - The path to the output file where the tokenized dictionary will be saved. If not provided, the dictionary will not be saved to a file.
- **Returns**: `dict` - A dictionary with prime numbers as keys and words as values.

## Usage

To use the script, provide the path to the input file and optionally the path to the output file. The script will read the text from the input file, tokenize it using prime numbers, and print the result to the console. If an output file is specified, the result will also be saved to that file.

### Example

```python
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your file path
    output_file = "tokenized_output.txt"  # Optional output file
    
    result = prime_tokenizer_from_file(input_file, output_file)
    if result:
        # Print results to console
        for prime, token in sorted(result.items()):
            print(f"{prime}: '{token}'")
```

## Error Handling

The script handles the following errors:
- `FileNotFoundError`: If the input file is not found, an error message is printed, and `None` is returned.
- Other exceptions: Any other exceptions are caught, an error message is printed, and `None` is returned.


