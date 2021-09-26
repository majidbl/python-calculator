from Calculator import *


def calculator():
    import sys
    evaluator = Evaluator()
    while True:
        try:
            line = input('>>> ')
            if line.strip() == 'quit':
                return
            result = evaluator.eval(line)
            if result:
                print(result)
        except EOFError:
            return
        except KeyboardInterrupt:
            sys.stdout.write('\nYou need use quit to exit!\n')
            continue
        except Exception as err:
            sys.stderr.write(err.args[0] + '\n')


if __name__ == '__main__':
    calculator()
