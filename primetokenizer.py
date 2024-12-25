def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def prime_tokenizer_from_file(file_path, output_file=None):
    try:
        # Read text from file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Split text into words
        words = text.split()
        
        # Generate prime numbers
        primes = generate_primes(len(words))
        
        # Create tokenized dictionary
        tokenized = {prime: word for prime, word in zip(primes, words)}
        
        # Handle output
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                for prime, token in sorted(tokenized.items()):
                    f.write(f"{prime}: '{token}'\n")
        
        return tokenized
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your file path
    output_file = "tokenized_output.txt"  # Optional output file
    
    result = prime_tokenizer_from_file(input_file, output_file)
    if result:
        # Print results to console
        for prime, token in sorted(result.items()):
            print(f"{prime}: '{token}'")