class TuringMachine:
    def __init__(self, tp, tbl, start_state='q0', end_state='q0'):
        self.tape = tp
        self.table = tbl
        self.state = start_state
        self.end_state = end_state
        self.index = 0

    def read(self):
        return self.tape[self.index]

    def write(self, value):
        self.tape[self.index] = value

    def move(self, direction):
        if direction == 'R':
            self.index += 1
        elif direction == 'L':
            self.index -= 1

    def execute(self):
        while self.state != self.end_state:
            symbol, direction, state = self.table[self.state][self.read()]
            self.write(symbol)
            self.move(direction)
            self.state = state
        return self.tape


if __name__ == '__main__':
    tape = list(input())
    table = {
        'q0': {' ': [' ', 'R', 'q0'], '2': ['2', 'R', 'q0'], '1': ['1', 'R', 'q0'], '0': ['0', 'R', 'q0'],
               '+': ['+', 'R', 'q1'], '-': ['-', 'R', 'q2']},
        'q1': {'2': ['2', 'L', 'q3'], '1': ['1', 'L', 'q4'], '0': ['0', 'N', 'q10']},
        'q2': {'2': ['2', 'L', 'q5'], '1': ['1', 'L', 'q6'], '0': ['0', 'N', 'q10']},
        'q3': {'+': ['+', 'L', 'q3'], '-': ['-', 'L', 'q3'], '2': ['1', 'L', 'q4'], '1': ['0', 'L', 'q4'],
               '0': ['2', 'N', 'q10']},
        'q4': {'+': ['+', 'L', 'q4'], '-': ['-', 'L', 'q4'], '2': ['0', 'L', 'q4'], '1': ['2', 'N', 'q10'],
               '0': ['1', 'N', 'q10'], ' ': ['1', 'N', 'q10']},
        'q5': {'+': ['+', 'L', 'q5'], '-': ['-', 'L', 'q5'], '2': ['0', 'N', 'q10'], '1': ['2', 'L', 'q6'],
               '0': ['1', 'L', 'q6']},
        'q6': {'+': ['+', 'L', 'q6'], '-': ['-', 'L', 'q6'], '2': ['1', 'N', 'q10'], '1': ['0', 'L', 'q7'],
               '0': ['2', 'L', 'q6']},
        'q7': {'0': ['0', 'N', 'q10'], '1': ['1', 'N', 'q10'], '2': ['2', 'N', 'q10'], ' ': [' ', 'R', 'q8']},
        'q8': {'0': [' ', 'R', 'q8'], '1': ['1', 'N', 'q10'], '2': ['2', 'N', 'q10'], '-': ['-', 'L', 'q9']},
        'q9': {' ': ['0', 'N', 'q10']}
    }

    turing_machine = TuringMachine(tape, table, start_state='q0', end_state='q10')
    print("".join(turing_machine.execute()))
