import argparse as argp
import re

class app():

    def __init__(self) -> None:

        self.parser = argp.ArgumentParser(prog = "calcylator",
                                            description = "Resolve arimethics polynomials",
                                            epilog = "Superbus et Hedonistic~")
        self.parser.add_argument("operation",
                                metavar = "OPERATION",
                                type = str,
                                help = "the arimethic operation (Ex.: 1+2-3*4/(5**6))")
        # self.parser.add_argument("-a",
        #                         "--add",
        #                         action = "store_true",
        #                         help = "set that only gonna add 2 numbers")
        # self.parser.add_argument("-s",
        #                         "--subtraction",
        #                         action = "store_true",
        #                         help = "set that only gonna subtract 2 numbers")

        # self.parser.add_argument("-m",
        #                         "--multiplication",
        #                         action = "store_true",
        #                         help = "set that only gonna multiply 2 numbers")

        # self.parser.add_argument("-d",
        #                         "--division",
        #                         action = "store_true",
        #                         help = "set that only gonna divide 2 numbers")

        # self.parser.add_argument("-p",
        #                         "--power",
        #                         action = "store_true",
        #                         help = "set that only gonna power a number")

    def exec(self) -> None:

        argument = self.parser.parse_args()
        operation = self.refine(argument.operation)
        print(eval(operation))

    def refine(self, argument) -> bool:

        operation = argument.translate(str.maketrans("{}[],", "()()."))

        regex_sub = {
            "^/|^\*|[a-zA-Z]|[^+*-/\.\^()\d]": "",
            "\^" : "\*\*",
            "/{2,}" : "/",
            "\+{2,}" : "+",
            "-{2,}" : "-",
            "\*{3,}" : "**",
            "\.{2,}" : "."
        }

        for subs in regex_sub.items(): operation = re.sub(subs[0], subs[1], operation)     

        return operation

app().exec()