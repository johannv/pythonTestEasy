# -*- coding: utf-8 -*-
'''
Created on 9 déc. 2012

@author: Vincent Bruneau, Johann Verbroucht
'''

from types import StringTypes, NoneType


class People(object):

    def __init__(self, peopleid=None, lastname=None, firstname=None):
        '''
        Constructor
        '''
        assert isinstance(peopleid, (int, NoneType))
        assert isinstance(lastname, (StringTypes, NoneType))
        assert isinstance(lastname, (StringTypes, NoneType))
        self.peopleid = peopleid
        self.lastname = lastname
        self.firstname = firstname
        