import os
from math import ceil
def cls():os.system('cls' if os.name =='nt' else 'clear')
def h1(text): print('\n##{0}##\n# {1} #\n##{0}##'.format('#'*len(text), text))
def h2(text): print('\n{}\n{}'.format(text, '‾'*len(text)))
def columns(text):
    size = os.get_terminal_size()
    x = size.columns
    y = size.lines
    lines = text.split('\n')
    number_of_lines = len(lines)
    max_line_len = max([len(line) for line in lines])
    if number_of_lines > y:
        max_cols = x//(max_line_len+4) -1
    elif len(lines)/y > 0.5:
        if max_line_len < x//3:
            max_cols = 3
        elif max_line_len < x//2:
            max_cols = 2
    if max_cols:
        total_rows = ceil(number_of_lines / max_cols)
        new_lines = ['' for x in range(total_rows)]
        current_row = 0
        current_column = 1
        for line in lines:
            new_lines[current_row] += '{}{}{}'.format(
                line,
                ' '*(max_line_len - len(line)),
                '        ' if current_column < max_cols else '\n'
            )
            current_row +=1
            if current_row == total_rows:
                current_row = 0
                current_column += 1
        print(''.join(new_lines))
    else:print(text)
if __name__ == '__main__':
    print('cls test before')
    cls()
    print('cls test after')
    h1('h1 test')
    h2('h2 test')