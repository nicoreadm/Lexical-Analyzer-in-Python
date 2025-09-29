# Lexical-Analyzer-in-Python
Basic Lexical Analyzer in Python

This project implements a simple lexical analyzer that reads an input text from the terminal or .txt and splits it into tokens (keywords, identifiers, numbers, operators, etc.).
It’s designed to demonstrate the first stage of a compiler or interpreter in a straightforward way, without relying on complex external libraries.

# Project Overview

This project contains three different implementations of a lexical analyzer, each illustrating a different approach:

1. analizador lexico.py
A basic, from-scratch implementation that manually reads operators, numbers, identifiers, and other tokens.
Goal: demonstrate the most fundamental way to build a lexer without external libraries.

2. lexical analyzer – PLY
Uses the PLY library (Python Lex & Yacc) to create the same lexical analyzer with far fewer lines of code.
Advantage: PLY simplifies token definitions, provides built-in regular expression handling, and produces more maintainable code.

3. lexical analyzer – PLY + .txt
Extends the PLY version to read source code directly from .txt files, making it easier to test different input programs.

These three steps show the evolution from a fully manual solution to a concise, library-assisted implementation capable of handling external input files.

# Features

Reads code or plain text from cmd and .txt.

# Basic recognition of:

Predefined keywords

Identifiers

Numbers

Operators and punctuation symbols

Prints a clean, easy-to-read list of tokens and their types to the console.

# Requirements

Python 3.8+

Latest version of PLY

No additional dependencies.
