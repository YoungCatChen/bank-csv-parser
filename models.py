# -*- coding: utf8 -*-

import collections
import datetime


class Transaction(collections.namedtuple('Transaction',
                                         'date amount description type id_')):
  _global_id = 0
  def __new__(cls, date, amount, description, type=None, id_=None):
    cls._global_id += 1
    return super(Transaction, cls).__new__(
        cls, date, amount, description, type, id_ or cls._global_id)
