from os import system
from timeit import time

def getTime(cmd):
  start_time = time.time()
  system(cmd)
  end_time = time.time()
  elapsed = end_time - start_time
  return elapsed

def runPattern(pattern, text_file, max_error, algorithm):
  return getTime('./bin/pmt "{}" {} -c -e {} -a {} > /dev/null'.format(
      pattern, text_file, max_error, algorithm))

def runGrep(pattern, text_file):
  return getTime('grep -c "{}" {} > /dev/null'.format(pattern, text_file))

text_files = [
  'english',
  'dna'
]

patterns = {}

patterns['english'] = [
  'I',
  'blue',
  'hello',
  'church',
  'thinking',
  'specially',
  'engagement',
  'marshmallow',
  'exaggeration',
  'thunderstruck',

  'I haven\'t got',
  'And I tried it',
  'O King of the Age',
  'light and darkness'
  'a three hundred and',
  'The journey to Chester',
  'pen pineapple apple pen',
  'making these observations',
  'four quarters of the globe',
  'from the Russian proletariat',
  'washing themselves was sounded'
]

patterns['dna'] = [
  'C'
  'CT'
  'GAC'
  'TTGA'
  'ATAGG'
  'ACTCTC'
  'CTTATCC'
  'AAGCTAAA'
  'TAGTGCGGT'
  'GTAGAGGTGT'
  'GTCAGTAGTGC'
  'GCGACGGGCTAT'
  'CCCCATTACGCTT'
  'GTCGCAGCGGTTTA'
  'CGGTTATCCGTAGGC'
  'GTATACTGCATATCAA'
  'CTCGAACTGATTTCAAC'
  'GGCCGTGGTTTGAATGCA'
  'CGAATCACGAAGACAGCAT'
  'GGAGCGGCCGACTCACCGCG'
  'TAGTCACTTTCTAGCGTAGTA'
  'GCGCAACATCACCCGGTGCCAG'
  'GCTATACGTTCTGTCCGGCGGTG'
  'TCCTGCTTCACTTCAAGAACGTCG'
  'GATGATGTGGTGTCGCAACTCTTCC'
  'ACATTCACCACGCTATGTCACTAGCG'
  'CGATGGTCAAACATATGATTTGGGATT'
  'CGCGCCTTCCGTGGCTACCCCCGCTGTC'
  'GGGTTGGAATTCGTATTGCAGTGTCTGGC'
  'ATCTTTGCCCTCAGGGAAACTGGCGTCTTG'
  'CGAATGATACAGAATTACCATAACTATTATC'
  'TGGGAAGTGCTTTCAATTGCTCACCCTCGGAC'
  'CTGGCCCCTGACATTACCGTGAATATGTTCCTC'
  'TCCGCCAACTTGAATATGATCGCAACGCCCCAGA'
  'CAACTACCCAGGAGGTCTTATCTCTGCGTACACAT'
  'CCTTTAATTGATACGTGAGCGGGTAGATTAGTCTCT'
  'AAGCTAAACCGTGTAGCATCGGAGCCGCGTTTAGGCT'
  'TGGCAGAGTTGGGTATCGTGCCTTGCCGGTCCATAGGG'
  'GCCCGCCAGCAGCCGCGTAAAACCCATTGCTGCCGATTC'
  'CCGGGTCTGCTGGGGTTAGACTAGTCAATCTAGATGACGC'
  'TACGTAGCATTCGCCCTTACAACATTAGAGCGAGGTACCAT'
  'CCGCTTGAATTGAGTACGCGAACTCCCCCCCGGCCCTTTCCT'
  'GCCAACGTCTAGGCCGTCGGCTTGAAAGTGTCTGGTCATATTG'
  'GAGGCGTTTCGTAAAGGAACCCTGATATTGGGATTGTAGCAGAT'
  'TTAGTACGAAGGCGCATCGCCCCTCCAATCGGTTCCCCAAATTCA'
  'AGTAAACTAGGGGCCCTTGAGCTTTCCTAAGCGAGATACTCTGACA'
  'CCCTAAGGGGTTCGGTCCTTGACTCGCTGGGATAGAAGCTTGATGTG'
  'CTACCGGACTGGGGTCTACCTGAGGCAACTCCTTAATCAGAAGGTTCC'
  'CAAGAATATTCGTAGCACCCTTATAGACGCCCCCGATGGACGGGTCAGC'
  'TAGCGTCCGGCTACGACACCTCCGTGTCTCGTGAGCTTCGTTATGAACGT'
]

algo_types = ['exact', 'aprox']

algos = {}

algos['exact'] = [
  'grep',
  'naive',
  'kmp',
  'aho',
  'so',
  'bm'
]

algos['aprox'] = [
  'sellers',
  'ukkonen',
  'wm'
]

def main():
  
  base = 'data/'
  system('make')
  for alg_type in algo_types:
    for txt in text_files:
      for pat in patterns[txt]:
        if alg_type == 'exact':
          errors = [0]
        else:
          errors = [1, len(pat)-1]
        for alg in algos[alg_type]:
          for err in errors:
            time = 0.0
            no_repetitions = 3
            for _ in range(no_repetitions):
              if alg != 'grep':
                time += runPattern(pat, base + txt, err, alg)
              else:
                time += runGrep(pat, base + txt)
            time /= no_repetitions
            print('{:30} {:5} {:5} {:10} {:5.4f}'.format(alg_type + '_' + txt + ('1' if err < 2 else 'M'), len(pat), err, alg, time))

if __name__ == '__main__':
  main()
