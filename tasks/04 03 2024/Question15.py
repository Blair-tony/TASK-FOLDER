#  Copy odd lines of one file to another file in Python 


def copy_odd_lines(input_file, output_file):
    with open(input_file, 'r') as f_input:
        with open(output_file, 'w') as f_output:
            lines = f_input.readlines()
            odd_lines = [line for idx, line in enumerate(lines) if idx % 2 == 0]
            f_output.writelines(odd_lines)

# Example usage:
input_file = 'sample.txt'
output_file = 'output2.txt'
copy_odd_lines(input_file, output_file)
