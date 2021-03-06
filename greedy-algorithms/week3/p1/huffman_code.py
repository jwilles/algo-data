import heapq

def process_text(filename):
  f = open(filename, 'r').readlines()
  num_symbols = int(f[0][:-1])
  symbols = [(int(weight[:-1]), [ind]) for ind, weight in enumerate(f[1:])]
  symbols_dict = {ind: int(x[:-1]) for ind, x in enumerate(f[1:])}
#  symbols = {int(x[:-1]): ind  for ind, x in enumerate(f[1:])}
  return num_symbols, symbols, symbols_dict


def merge(symbols):

  sym1 = heapq.heappop(symbols)
  sym2 = heapq.heappop(symbols)
#  print "Merge"
#  print sym1[1]
#  print sym2[1]
  meta_sym = ( sym1[0]+sym2[0], [sym1[1], sym2[1]])
  heapq.heappush(symbols, meta_sym)

  return symbols


def max_depth(tree):
  if len(tree) == 1:
    return 0
  else:
    return 1 + max(max_depth(tree[0]), max_depth(tree[1]))

def min_depth(tree):
  if len(tree) == 1:
    return 0
  else:
    return 1 + min(min_depth(tree[0]), min_depth(tree[1]))

def main():

  filename = 'huffman.txt'
  num_symbols, symbols, symbols_dict = process_text(filename)

#  print num_symbols
#  print symbols_dict

  heapq.heapify(symbols)

#  print heapq.heappop(symbols)
#  print heapq.heappop(symbols)

  while len(symbols) > 1:
    symbols = merge(symbols)

  max_code_length = max_depth(symbols[0][1])
  min_code_length = min_depth(symbols[0][1])

#  print symbols[0][1][1]
  print max_code_length
  print min_code_length

#  print num_symbols
#  print weights

if __name__ == '__main__':
  main()
