# -*- coding: utf-8 -*-
'''
Created on 9 déc. 2012

@author: Vincent Bruneau, Johann Verbroucht
'''

from types import NoneType
from datetime import datetime

class Mark(object):

    def __init__(self, date=None, mark=0):
        assert isinstance(date, (datetime, NoneType))
        assert isinstance(mark, int)
        self.date = date
        self.mark = mark