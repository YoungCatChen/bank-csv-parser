import csv
import line_parsers
import models
import re
import StringIO


def Parse(csv_content, line_parser=None):
  line_parser = line_parser or line_parsers.FindLineParser(csv_content)
  csv_content = line_parser.StripNonCsvData(csv_content)
  csv_mem_file = StringIO.StringIO(csv_content)
  # dialect = csv.Sniffer().sniff(csv_content)
  dialect = 'excel'
  has_header = _HasHeader(csv_content)

  if has_header:
    reader = csv.DictReader(csv_mem_file, dialect=dialect)
  else:
    reader = csv.reader(csv_mem_file, dialect=dialect)

  transactions = []

  for line_item in reader:
    tran = line_parser.ParseLine(line_item)
    if tran:
      transactions.append(tran)

  return transactions


def _HasHeader(csv_content):
  first_line = csv_content.split('\n')[0]
  has_date_1 = re.search(r'\d\d\d\d[/-]\d\d?[/-]\d\d?', first_line)
  has_date_2 = re.search(r'\d\d?[/-]\d\d?[/-]\d\d\d\d', first_line)
  has_amount = re.search(r'\d\.\d\d', first_line)
  actual_content = has_amount and (has_date_1 or has_date_2)
  return not actual_content
