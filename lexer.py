from Tokens import Token, TokenType

WHITESPACE = ' \t\n'
DIGITS = '1234567890'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.currentchar = next(self.text)
        except StopIteration:
            self.currentchar = None

    def generate_tokens(self):
        while self.currentchar is not None:
            if self.currentchar in WHITESPACE:
                self.advance()
            elif self.currentchar == '.' or self.currentchar in DIGITS:
                yield self.generate_number()
            elif self.currentchar == '+':
                yield Token(TokenType.PLUS)
                self.advance()
            elif self.currentchar == '-':
                yield Token(TokenType.MINUS)
                self.advance()
            elif self.currentchar == '*':
                yield Token(TokenType.MULTIPLY)
                self.advance()
            elif self.currentchar == '/':
                yield Token(TokenType.DIVIDE)
                self.advance()
            elif self.currentchar == '(':
                yield Token(TokenType.LPAREN)
                self.advance()
            elif self.currentchar == ')':
                yield Token(TokenType.RPAREN)
                self.advance()
            else:
                raise Exception(f"Illegal Char '{self.currentchar}'")

    def generate_number(self):
        dec_point = 0
        num_str = self.currentchar
        self.advance()
        while self.currentchar is not None and (self.currentchar == '.' or self.currentchar in DIGITS):
            if self.currentchar == '.':
                dec_point += 1
                if dec_point > 1:
                    break
            num_str += self.currentchar
            self.advance()
        if num_str.startswith('.'):
            num_str = '0' + num_str
        if num_str.endswith('.'):
            num_str += '0'
        return Token(TokenType.NUMBER, float(num_str))
