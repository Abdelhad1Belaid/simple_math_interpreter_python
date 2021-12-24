from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter


def main():
    while True:
        try:
            text = input("Math_Interpreter >>>")
            lex = Lexer(text)
            tokens = lex.generate_tokens()
            # print(list(tokens))
            parser = Parser(tokens)
            tree = parser.parse()
            # print(tree)
            if not tree:
                continue
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            print(value)
        except EOFError:
            break


if __name__ == "__main__":
    main()
