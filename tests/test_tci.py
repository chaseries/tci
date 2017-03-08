import tci
import unittest

def test_add():
  assert tci.add(2, 2) == 4

def test_sub():
  assert tci.sub(2, 2) == 0

def test_mul():
  assert tci.mul(3, 3) == 9

def test_div():
  assert tci.div(2, 2) == 1
