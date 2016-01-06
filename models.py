# -*- coding: utf8 -*-

import collections
import datetime


class Transaction(collections.namedtuple('Transaction',
                                         'date amount description type')):
  def __new__(cls, date, amount, description, type=None):
    return super(Transaction, cls).__new__(cls, date, amount, description, type)
