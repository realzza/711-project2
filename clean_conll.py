"""
Remove the extra two columns in the CONLL2003 format
"""

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str)
    return parser.parse_args()


def main():
    args = get_args()

    with open(args.input, encoding='utf-8') as inf, open(args.output, 'w', encoding='utf-8') as outf:
        for line in inf:
            tokens = line.strip('\n').split()
            if len(tokens) < 4:  # skip '-DOCSTART-' at the top, and keep the empty lines
                if len(tokens) == 0:
                    outf.write(f'\n')
            else:
                col1 = tokens[0]
                col2 = tokens[3]
                outf.write(f'{col1} {col2}\n')


if __name__ == '__main__':
    main()
