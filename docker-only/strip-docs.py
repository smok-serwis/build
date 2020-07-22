#!/usr/bin/python
# coding=UTF-8
"""
Strip comments and docstrings from a file.
"""
import io
import sys
import token
import tokenize
import os


def do_file(fname):
    """ Run on just one file.

    """
    mod = io.BytesIO()
    with open(fname, "r") as source:

        prev_toktype = token.INDENT
        first_line = None
        last_lineno = -1
        last_col = 0

        tokgen = tokenize.generate_tokens(source.readline)
        for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
            if 0:   # Change to if 1 to see the tokens fly by.
                print('%10s %-14s %-20r %r' % (
                    tokenize.tok_name.get(toktype, toktype),
                    '%d.%d-%d.%d' % (slineno, scol, elineno, ecol),
                    ttext, ltext
                    ))
            if slineno > last_lineno:
                last_col = 0
            if scol > last_col:
                mod.write(" " * (scol - last_col))
            if toktype == token.STRING and prev_toktype == token.INDENT:
                # Docstring
                mod.write("#--")
            elif toktype == tokenize.COMMENT:
                # Comment
                mod.write("##\n")
            else:
                mod.write(ttext)
            prev_toktype = toktype
            last_col = ecol
            last_lineno = elineno

    with open(fname, 'w') as f_out:
        f_out.write(mod.getvalue())


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('''Use as:
        
strip-docs <name of directory with py, pyx and pyd files>
''')
        sys.exit(0)

    for rootdir, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            if file.endswith('.py') or file.endswith('.pyx') or file.endswith('.pyd'):
                path = os.path.join(rootdir, file)
                print ('Doing %s' % (path, ))
                do_file(path)
