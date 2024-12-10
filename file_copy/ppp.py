def read_file_to_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

# Usage
file_content = read_file_to_list('hehe.txt')
print(file_content)
