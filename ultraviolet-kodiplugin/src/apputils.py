__author__ = 'developer'


def cleanString( str):
    if not str is None:
        return str.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)")


