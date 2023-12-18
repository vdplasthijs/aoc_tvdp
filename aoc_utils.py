def read_txt_file_lines(filename='input.txt', read_arg='r'):
    with open(filename, read_arg) as f:
        return [line.strip() for line in f.readlines()]
    
def read_txt_file_without_escape(filename='input.txt', read_arg='r'):
    with open(filename, read_arg) as f:
        return f.read().strip()
    
def gcd(a, b):
    """find common divisor of all diffs"""   
    while b:
        a, b = b, a % b
    return a