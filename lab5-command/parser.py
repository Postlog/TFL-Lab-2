#!/usr/bin/env python

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.

from __future__ import annotations

import sys

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu
from tatsu.parsing import leftrec, nomemo, isname # noqa
from tatsu.infos import ParserConfig
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {}  # type: ignore


class PDABuffer(Buffer):
    def __init__(self, text, /, config: ParserConfig = None, **settings):
        config = ParserConfig.new(
            config,
            owner=self,
            whitespace=None,
            nameguard=None,
            comments_re=None,
            eol_comments_re=None,
            ignorecase=False,
            namechars='',
            parseinfo=True,
        )
        config = config.replace(**settings)
        super().__init__(text, config=config)


class PDAParser(Parser):
    def __init__(self, /, config: ParserConfig = None, **settings):
        config = ParserConfig.new(
            config,
            owner=self,
            whitespace=None,
            nameguard=None,
            comments_re=None,
            eol_comments_re=None,
            ignorecase=False,
            namechars='',
            parseinfo=True,
            keywords=KEYWORDS,
            start='start',
        )
        config = config.replace(**settings)
        super().__init__(config=config)

    @tatsumasu()
    def _start_(self):  # noqa
        self._stmts_()
        self._check_eof()

    @tatsumasu()
    def _stmts_(self):  # noqa

        def block0():
            self._stmt_()
        self._closure(block0)

    @tatsumasu()
    def _stmt_(self):  # noqa

        def block0():
            with self._choice():
                with self._option():
                    self._single_edge_description_()
                with self._option():
                    self._single_node_description_()
                with self._option():
                    self._group_of_nodes_()
                self._error(
                    'expecting one of: '
                    '<group_of_nodes>'
                    '<single_edge_description>'
                    '<single_node_description>'
                )
        self._closure(block0)
        self._statement_separator_()

    @tatsumasu()
    def _single_node_description_(self):  # noqa
        self._node_id_()
        self._token('(')

        def block0():
            with self._choice():
                with self._option():
                    self._flag_()
                with self._option():
                    self._key_word1_()
                    self._node_label_()
                with self._option():
                    self._node_label_()
                self._error(
                    'expecting one of: '
                    '<flag> <key_word1> <node_label>'
                )
        self._closure(block0)
        self._token(')')

    @tatsumasu()
    def _single_edge_description_(self):  # noqa
        self._token('pass')

    @tatsumasu()
    def _group_of_nodes_(self):  # noqa
        self._token('pass')

    @tatsumasu()
    def _flag_(self):  # noqa
        with self._choice():
            with self._option():
                self._initial_flag_()
            with self._option():
                self._final_flag_()
            with self._option():
                self._trap_flag_()
            self._error(
                'expecting one of: '
                "'is_final' 'is_initial' 'is_trap'"
                '<final_flag> <initial_flag> <trap_flag>'
            )

    @tatsumasu()
    def _initial_flag_(self):  # noqa
        self._token('is_initial')

    @tatsumasu()
    def _final_flag_(self):  # noqa
        self._token('is_final')

    @tatsumasu()
    def _trap_flag_(self):  # noqa
        self._token('is_trap')

    @tatsumasu()
    def _node_id_(self):  # noqa
        self._string_literal_1_()

    @tatsumasu()
    def _node_label_(self):  # noqa
        self._string_literal_2_()

    @tatsumasu()
    def _statement_separator_(self):  # noqa
        self._token(';')

    @tatsumasu()
    def _key_word1_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('label=')
            with self._option():
                self._token('label:')
            with self._option():
                self._token('label')
            self._error(
                'expecting one of: '
                "'label' 'label:' 'label='"
            )

    @tatsumasu()
    def _key_word2_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('id=')
            with self._option():
                self._token('id')
            self._error(
                'expecting one of: '
                "'id' 'id='"
            )

    @tatsumasu()
    def _string_literal_1_(self):  # noqa

        def block0():
            self._pattern('[a-z0-9_]')
        self._positive_closure(block0)

    @tatsumasu()
    def _string_literal_2_(self):  # noqa

        def block0():
            self._pattern('[a-z0-9_]')
        self._positive_closure(block0)

    @tatsumasu()
    def _string_literal_3_(self):  # noqa

        def block0():
            self._pattern('[a-z0-9_]')
        self._positive_closure(block0)

    @tatsumasu()
    def _string_literal_4_(self):  # noqa

        def block0():
            self._pattern('[a-z0-9_]')
        self._positive_closure(block0)

    @tatsumasu()
    def _string_literal_5_(self):  # noqa

        def block0():
            self._pattern('[a-z0-9_]')
        self._positive_closure(block0)

    @tatsumasu()
    def _string_literal_6_(self):  # noqa

        def block0():
            self._pattern('[a-z0-9_]')
        self._positive_closure(block0)

    @tatsumasu()
    def _string_literal_7_(self):  # noqa

        def block0():
            self._pattern('[a-z0-9_]')
        self._positive_closure(block0)


class PDASemantics:
    def start(self, ast):  # noqa
        return ast

    def stmts(self, ast):  # noqa
        return ast

    def stmt(self, ast):  # noqa
        return ast

    def single_node_description(self, ast):  # noqa
        return ast

    def single_edge_description(self, ast):  # noqa
        return ast

    def group_of_nodes(self, ast):  # noqa
        return ast

    def flag(self, ast):  # noqa
        return ast

    def initial_flag(self, ast):  # noqa
        return ast

    def final_flag(self, ast):  # noqa
        return ast

    def trap_flag(self, ast):  # noqa
        return ast

    def node_id(self, ast):  # noqa
        return ast

    def node_label(self, ast):  # noqa
        return ast

    def statement_separator(self, ast):  # noqa
        return ast

    def key_word1(self, ast):  # noqa
        return ast

    def key_word2(self, ast):  # noqa
        return ast

    def string_literal_1(self, ast):  # noqa
        return ast

    def string_literal_2(self, ast):  # noqa
        return ast

    def string_literal_3(self, ast):  # noqa
        return ast

    def string_literal_4(self, ast):  # noqa
        return ast

    def string_literal_5(self, ast):  # noqa
        return ast

    def string_literal_6(self, ast):  # noqa
        return ast

    def string_literal_7(self, ast):  # noqa
        return ast


def main(filename, **kwargs):
    if not filename or filename == '-':
        text = sys.stdin.read()
    else:
        with open(filename) as f:
            text = f.read()
    parser = PDAParser()
    return parser.parse(
        text,
        filename=filename,
        **kwargs
    )


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, PDAParser, name='PDA')
    data = asjson(ast)
    print(json.dumps(data, indent=2))
