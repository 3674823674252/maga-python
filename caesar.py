from sys import argv
from sys import exit
from string import ascii_lowercase
from string import ascii_uppercase
from collections import OrderedDict

def encdec(file, dict):
  cyph = ''
  file = open(file)
  char = file.read(1)

  while char:
    if char in dict.keys():
      cyph += dict[char]
    else:
      cyph += char
    char = file.read(1)

  print cyph

def encdecdict(dict):
  mdict = {}
  dict = open(dict).readlines()

  for line in dict:
    if enc:
      mdict[line.split(' ')[0]] = line.split(' ')[1][0]
    else:
      mdict[line.split(' ')[1][0]] = line.split(' ')[0]
  return mdict


def encdict(dict):
  return encdecdict(dict, True)

def decdict(dict):
  return encdecdict(dict, False)

def breakdict(file, text):
  freqs = {}
  ffreqs = {}

  text = open(text).read()
  for char in ascii_lowercase + ascii_uppercase:
    freqs[len(text.split(char))] = char
  
  freqs = OrderedDict(sorted(freqs.items()))

  file = open(file).read()
  for char in ascii_lowercase + ascii_uppercase:
    ffreqs[len(file.split(char))] = char

  dict = {}

  for afreq, char in ffreqs.items():
    for tfreq, tchar in freqs.items():
      if tfreq > afreq:
        print char, dict[char]
        break

      dict[char] = tchar

  return dict


def encode(file, dict):
  encdec(file, encdict(text))

def decode(file, dict):
  encdec(file, decdict(text))

def break_(file, text):
  encdec(file, breakdict(file, text))

if len(argv) != 4:
  print "format <-e|-d|-b> <file> <dict|text>"
  exit()

if len(argv) == 4 and argv[1] == '-e':
  encode(argv[2], argv[3])
if len(argv) == 4 and argv[1] == '-d':
  decode(argv[2], argv[3])
if len(argv) == 4 and argv[1] == '-b':
  break_(argv[2], argv[3])

