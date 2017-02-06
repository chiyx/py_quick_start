#! python3

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batwoman')

# 贪心匹配 and 非贪心匹配
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
print(mo1.group())

greedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
print(mo1.group())