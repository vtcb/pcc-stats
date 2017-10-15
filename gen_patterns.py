import random

def genDna():
  no_patterns = 50
  print('[')
  for i in range(no_patterns):
    size = i + 1
    new_pattern = ''.join(random.choice("ACGT") for _ in range(size))
    print("  '{}'".format(new_pattern))
  print(']')

def main():
  genDna()

if __name__ == '__main__':
  main()