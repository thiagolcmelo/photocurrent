#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="""
        CLI tool for launching photocurrent calculator
    """)
    return parser

if __name__ == '__main__':
    parser = create_parser()
    print(parser.parse_args())