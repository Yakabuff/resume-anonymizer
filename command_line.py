

import argparse

from anonymizer import resume_anonymizer


class resumeAnonymizerCLI(object):
    def __init__(self):
        self.output = None
        self.input = None
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
            help = "manually anonymize fields"
        )
        self.parser.add_argument(
            '-i',
            '--input',
            # action='store_true',
            help = "input file path"
        )

        # self.parser.add_argument(
        #     '-o',
        #     '--output',
        #     # action='store_true',
        #     help = "output file path"
        # )

    def extract_resume_data(self):
        args = self.parser.parse_args()
        if args.input:
            # print("input")
            self.input = args.input
            # print(input)
        if (args.manual and args.auto):
            self.parser.error('Cant have both')
        if args.manual:
            # print("List of items: {}".format(args.alist))
            # import resume_anonymizer
            secret_fields = args.manual
            resume_anonymizer.anonymize(self.input, self.output, secret_fields)


        if args.auto:
            print("auto not complete yet")
        if not(args.manual or args.auto):
            self.parser.error('Must have either manual or auto')


if __name__ == '__main__':

    cli_obj = resumeAnonymizerCLI()
    cli_obj.extract_resume_data()