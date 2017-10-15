from os import system
import matplotlib.pyplot as plt

def sortByFirst(a, b):
  return zip(*sorted(zip(a, b)))

def plot(results_per_alg, pid, fig_name):
  fig, ax = plt.subplots()
  for alg in results_per_alg:
    x, y = results_per_alg[alg]
    x, y = sortByFirst(x, y)
    ax.plot(x, y, '-x', label=alg)
  ax.set_xlabel('Pattern(s) size')
  ax.set_ylabel('Execution time')

  ax.legend(loc='best', fancybox=True, framealpha=0.5)
  # fig.suptitle(pid)

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

def main():
  results = getResults()

  system('mkdir -p figs')
  for pid in results:
    plot(results[pid], pid, 'figs/{}.png'.format(pid))

if __name__ == '__main__': main()
