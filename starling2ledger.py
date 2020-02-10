#!/usr/bin/env python3

import csv
import codecs
import datetime
import re

def parse_datetime(date_time_str):
    """
    Parses datetime string in 01-01-2000 format.
    """
    try:
        date_time_obj = datetime.datetime.strptime(date_time_str, "%d/%m/%Y")
    except ValueError as error:
        print(error)
    return date_time_obj.date()


def parse(raw_data):
    output = ""
    csv_reader = csv.reader(raw_data.splitlines())
    next(csv_reader, None)
    for row in csv_reader:
        if row[0] == "":
            continue
        date = parse_datetime(row[0]).strftime("%Y/%m/%d")
        payee = row[1]
        description = re.sub("\s\s+", " ", row[2])
        amount = row[4]
        output += "{} {}\n".format(date, payee)
        if (float(amount) >= 0):
            output += "  Assets:Monzo:Checking  £{}\n".format(amount)
            output += "  X:X\n"
        else:
            output += "  Expenses:X  £{}\n".format(amount[1:])
            output += "  Assets:Monzo:Checking\n"
            output += "  ;; Reference: {}\n\n".format(description)
    return output


with codecs.open('input.csv', encoding='utf-8', errors='ignore') as csv_file, open('output.ldg', 'w') as output_file:
    reader = csv.reader(csv_file, delimiter=',')
    output_file.write(parse(csv_file.read()))
