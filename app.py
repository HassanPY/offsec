def vulnerable_function(input_string):
    buffer_size = 10
    buffer = ['\0'] * buffer_size

    # Simulate buffer overflow by copying the input string into the buffer without checking the length
    for i in range(len(input_string)):
        buffer[i] = input_string[i]

    return ''.join(buffer)

if __name__ == "__main__":
    # Input string that exceeds the buffer size
    malicious_input = "A" * 15  # This input will overflow the buffer
    print("Original buffer content:", ['\0'] * 10)
    print("Input string:", malicious_input)
    try:
        result = vulnerable_function(malicious_input)
        print("Buffer content after overflow:", result)
    except IndexError as e:
        print("Buffer overflow detected:", e)
