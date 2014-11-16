#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import graken, Parser


__version__ = (2014, 11, 15, 13, 55, 57, 5)

__all__ = [
    'colinoParser',
    'colinoSemantics',
    'main'
]


class colinoParser(Parser):
    def __init__(self, whitespace=None, nameguard=True, **kwargs):
        super(colinoParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            **kwargs
        )

    @graken()
    def _configuration_(self):

        def block1():
            self._rule_()
        self._positive_closure(block1)

        self.ast['rules'] = self.last_node
        self._check_eof()

        self.ast._define(
            ['rules'],
            []
        )

    @graken()
    def _rule_(self):
        self._token('rule')
        self._identifier_()
        self.ast['name'] = self.last_node
        self._condition_list_()
        self.ast['conditions'] = self.last_node
        self._action_list_()
        self.ast['actions'] = self.last_node
        self._token('end')

        self.ast._define(
            ['name', 'conditions', 'actions'],
            []
        )

    @graken()
    def _condition_list_(self):

        def block0():
            self._condition_()
        self._positive_closure(block0)

    @graken()
    def _condition_(self):
        self._token('match')
        with self._optional():
            with self._optional():
                self._INTEGER_()
                self.ast['repeat'] = self.last_node
                self._token('times')
            self._token('within')
            self._time_limit_()
            self.ast['limit'] = self.last_node
        self._test_()
        self.ast['test'] = self.last_node
        with self._optional():
            self._token('set')
            self._assignment_list_()

        self.ast._define(
            ['repeat', 'limit', 'test'],
            []
        )

    @graken()
    def _time_limit_(self):
        self._INTEGER_()
        self.ast['value'] = self.last_node
        with self._group():
            with self._choice():
                with self._option():
                    self._token('s')
                with self._option():
                    self._token('m')
                with self._option():
                    self._token('h')
                self._error('expecting one of: h m s')
        self.ast['unit'] = self.last_node

        self.ast._define(
            ['value', 'unit'],
            []
        )

    @graken()
    def _test_(self):
        self._or_test_()

    @graken()
    def _or_test_(self):
        self._and_test_()
        self.ast.setlist('@', self.last_node)

        def block1():
            self._token('or')
            self._cut()
            self._and_test_()
            self.ast.setlist('@', self.last_node)
        self._closure(block1)

    @graken()
    def _and_test_(self):
        self._not_test_()
        self.ast.setlist('@', self.last_node)

        def block1():
            self._token('and')
            self._cut()
            self._not_test_()
            self.ast.setlist('@', self.last_node)
        self._closure(block1)

    @graken()
    def _not_test_(self):
        with self._choice():
            with self._option():
                self._token('not')
                self._not_test_()
                self.ast['not_'] = self.last_node
            with self._option():
                self._comparison_()
                self.ast['comparison'] = self.last_node
            self._error('no available options')

        self.ast._define(
            ['not', 'comparison'],
            []
        )

    @graken()
    def _comparison_(self):
        with self._choice():
            with self._option():
                self._identifier_()
                self.ast['left'] = self.last_node
                self._comp_op_()
                self.ast['op'] = self.last_node
                self._expr_()
                self.ast['right'] = self.last_node
            with self._option():
                self._identifier_()
                self.ast['left'] = self.last_node
                self._token('~')
                self.ast['op'] = self.last_node
                self._REGEX_()
                self.ast['right'] = self.last_node
            with self._option():
                self._identifier_()
                self.ast['left'] = self.last_node
                self._token('!~')
                self.ast['op'] = self.last_node
                self._REGEX_()
                self.ast['right'] = self.last_node
            self._error('no available options')

        self.ast._define(
            ['left', 'op', 'right'],
            []
        )

    @graken()
    def _comp_op_(self):
        with self._choice():
            with self._option():
                self._token('<')
            with self._option():
                self._token('>')
            with self._option():
                self._token('=')
            with self._option():
                self._token('>=')
            with self._option():
                self._token('<=')
            with self._option():
                self._token('!=')
            with self._option():
                self._token('in')
            with self._option():
                self._token('not')
                self._token('in')
            self._error('expecting one of: != < <= = > >= in not')

    @graken()
    def _expr_(self):
        with self._choice():
            with self._option():
                self._INTEGER_()
            with self._option():
                self._STRING_()
            with self._option():
                self._identifier_()
            self._error('no available options')

    @graken()
    def _assignment_list_(self):

        def block0():
            self._assignment_()
            self.ast.setlist('@', self.last_node)
        self._closure(block0)

    @graken()
    def _assignment_(self):
        self._identifier_()
        self._token('=')
        self._expr_()

    @graken()
    def _action_list_(self):

        def block0():
            self._action_()
            self.ast.setlist('@', self.last_node)
        self._positive_closure(block0)

    @graken()
    def _action_(self):
        self._token('action')
        self._identifier_()
        self.ast['@'] = self.last_node

    @graken()
    def _identifier_(self):
        self._IDENTIFIER_()

    @graken()
    def _IDENTIFIER_(self):
        self._pattern(r'[a-zA-Z][a-zA-Z0-9]*')

    @graken()
    def _SCOPED_IDENTIFIER_(self):
        self._pattern(r'[a-zA-Z][a-zA-Z0-9]*(\.[a-zA-Z][a-zA-Z0-9]*)+')

    @graken()
    def _INTEGER_(self):
        self._pattern(r'[0-9]+')

    @graken()
    def _STRING_(self):
        with self._choice():
            with self._option():
                self._token('"')

                def block1():
                    with self._choice():
                        with self._option():
                            self._pattern(r'[^"\n\\]')
                        with self._option():
                            self._ESC_()
                        self._error('expecting one of: [^"\\n\\\\]')
                self._closure(block1)
                self.ast['@'] = self.last_node
                self._token('"')
            with self._option():
                self._token("'")

                def block4():
                    with self._choice():
                        with self._option():
                            self._pattern(r"[^'\n\\]")
                        with self._option():
                            self._ESC_()
                        self._error("expecting one of: [^'\\n\\\\]")
                self._closure(block4)
                self.ast['@'] = self.last_node
                self._token("'")
            self._error('expecting one of: " \'')

    @graken()
    def _REGEX_(self):
        with self._choice():
            with self._option():
                self._token('?/')
                self._cut()
                self._pattern(r'(.|\n)+?(?=/\?)')
                self.ast['@'] = self.last_node
                self._pattern(r'/\?+')
                self._cut()
            with self._option():
                self._token('/')
                self._cut()
                self._pattern(r'(.|\n)+?(?=/)')
                self.ast['@'] = self.last_node
                self._token('/')
                self._cut()
            self._error('expecting one of: / ?/')

    @graken()
    def _ESC_(self):
        with self._choice():
            with self._option():
                self._pattern(r'\\[\'"\\nrtbfv]')
            with self._option():
                self._pattern(r'\\u[a-fA-F0-9]{4}')
            self._error('expecting one of: \\\\[\'"\\\\nrtbfv] \\\\u[a-fA-F0-9]{4}')


class colinoSemantics(object):
    def configuration(self, ast):
        return ast

    def rule(self, ast):
        return ast

    def condition_list(self, ast):
        return ast

    def condition(self, ast):
        return ast

    def time_limit(self, ast):
        return ast

    def test(self, ast):
        return ast

    def or_test(self, ast):
        return ast

    def and_test(self, ast):
        return ast

    def not_test(self, ast):
        return ast

    def comparison(self, ast):
        return ast

    def comp_op(self, ast):
        return ast

    def expr(self, ast):
        return ast

    def assignment_list(self, ast):
        return ast

    def assignment(self, ast):
        return ast

    def action_list(self, ast):
        return ast

    def action(self, ast):
        return ast

    def identifier(self, ast):
        return ast

    def IDENTIFIER(self, ast):
        return ast

    def SCOPED_IDENTIFIER(self, ast):
        return ast

    def INTEGER(self, ast):
        return ast

    def STRING(self, ast):
        return ast

    def REGEX(self, ast):
        return ast

    def ESC(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = colinoParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in colinoParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for colino.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )

