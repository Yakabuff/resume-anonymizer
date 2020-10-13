

import argparse


# import resume_anonymizer
class resumeAnonymizerCLI(object):
    def __init__(self):
        # self.output = None
        # self.input = None
        # self.fields = None

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            '-a',
            '--auto',

            action = 'store_true',
            help = "automatically anonymize fields"
        )
        self.parser.add_argument(
            '-m',
            '--manual',
            nargs = "+",
            default = [],
            # action='store',

            help = "manually anonymize fields"
        )
        self.parser.add_argument(
            '-o',
            '--output',

            action='store_true',
            help = "export file path"
        )

        self.parser.add_argument(
            '-i',
            '--input',

            action='store_true',
            help = "select input path"
        )

    def extract_resume_data(self):
        args = self.parser.parse_args()
        if args.output:
            print("output")
            output = args.output
        if args.input:
            print("input")
            input = args.input
        if (args.manual and args.auto):
            self.parser.error('Cant have both')
        if args.manual:
            # print("List of items: {}".format(args.alist))
            secret_fields = args.manual
            print(secret_fields)

        if args.auto:
            print("auto")






if __name__ == '__main__':
    print("hi")
    cli_obj = resumeAnonymizerCLI()
    cli_obj.extract_resume_data()