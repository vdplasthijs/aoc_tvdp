def read_txt_file_lines(folder='day1', filename='input.txt'):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]
    