import argparse as argp
import re
import pyperclip as pyc

class app():

    def __init__(self) -> None:

        self.parser = argp.ArgumentParser(prog = "calcylator",
                                            prefix_chars = "~",
                                            description = "Resolve arimethics polynomials",
                                            epilog = "Superbus et Hedonistic~")
        self.parser.add_argument("operation",
                                metavar = "OPERATION",
                                type = str,
                                help = "the arimethic operation (Ex.: 1+2-3*4/(5**6))")
        self.parser.add_argument("~a",
                                "~~absolute",
                                action = "store_true",
                                help = "set the output as an absolute value")
        self.parser.add_argument("~cp",
                                "~~copy",
                                action = "store_true",
                                help = "set the output value to be copied into the paperclip")
    def exec(self) -> None:

        try:

            argument = self.parser.parse_args()
            operation = self.refine(argument.operation, argument.absolute)
            result = eval(operation)
            if argument.copy: pyc.copy(result); pyc.paste()
            print(result)
        
        except SyntaxError:

            print("\nIllegal operation, please consult [~h] command\nEx.: calcylator ~h")

    def refine(self, argument, absolute) -> str:

        operation = argument.translate(str.maketrans("{}[],", "()()."))
                
        regex_subs = {
            "^/+|^\*+|[a-zA-Z]|[^+*-/%\.\^()\d]": "",
            "%" : "/100",
            "\^" : "**",
            "/{2,}" : "/",
            "\+{2,}" : "+",
            "-{2,}" : "-",
            "\*{3,}" : "**",
            "\.{2,}" : ".",
            "\.[0-9]\." : ""
        }

        for subs in regex_subs.items(): operation = re.sub(subs[0], subs[1], operation)

        checked = [re.match("^\d|^\.[0-9]|^\+[0-9]|^-[0-9]", operation) == None, len(operation) > 1]

        if all(checked): return self.refine(operation, absolute)

        if absolute: return f"abs({operation})"

        return operation

def run(): app().exec()

if __name__ == "__main__": run()