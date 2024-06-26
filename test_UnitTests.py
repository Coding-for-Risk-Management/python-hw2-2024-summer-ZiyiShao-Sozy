#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 00:00:36 2024

@author: shaoziyi
"""

import WhoAmI_File
def test_WhoAmI():
    assert WhoAmI_File.WhoAmI() != 'djr2132'
        
import BondPrice_File
def test_getBondPrice():
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  1)) == 2170604
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  2)) == 2171686

import BondDuration_File
def test_getBondDuration():
    assert round(BondDuration_File.getBondDuration(.03, 2000000, .04, 10,1),2) == 8.51

import FizzBuzz_File
def test_FizzBuzz():
    x = FizzBuzz_File.FizzBuzz(40,45)
    assert x[0] == "buzz"
    assert x[1] == 41
    assert x[5] == "fizzbuzz"