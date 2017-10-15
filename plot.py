import matplotlib.pyplot as plt

algos = [
  ('naive',   False),
  ('kmp',     False),
  ('aho',     False),
  ('so',      False),
  ('bm',      False),
  ('sellers', True),
  ('ukkonen', True)
]

def isApprox(alg):
  return alg in [alg for alg, isa in algos if isa]

def plot(results_per_alg, title, fig_name):
  fig, ax = plt.subplots()
  for alg in results_per_alg:
    results = results_per_alg[alg]
    ax.plot(results[0], results[1], '-x', label=alg)
  ax.set_xlabel('Pattern(s) size')
  ax.set_ylabel('Execution time')

  ax.legend(loc='best', fancybox=True, framealpha=0.5)
  fig.suptitle(title)

  fig.savefig(fig_name)
  plt.close(fig)

def getResults():
  results_per_plt = {}
  with open('stats/results.txt') as results_file:
    for line in results_file:
      if not line.strip(): continue
      pid, siz, err, alg, tim = line.split()
      siz = int(siz)
      err = int(err)
      tim = float(tim)

      if pid not in results_per_plt:
        results_per_plt[pid] = {}
      if alg not in results_per_plt[pid]:
        results_per_plt[pid][alg] = [[], []]

      results_per_plt[pid][alg][0].append(siz)
      results_per_plt[pid][alg][1].append(tim)
  return results_per_plt

results = getResults()

for pid in results:
  plot(results[pid], pid, '{}.png'.format(pid))
