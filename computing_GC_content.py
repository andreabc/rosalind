from __future__ import division
from collections import Counter, defaultdict
import sys

file_path = sys.argv[1]
id_dict = defaultdict(float)
with open(file_path, 'r') as input_file:
	for line in input_file:
		if line.startswith('>'):
			seq = ''
			key = line.strip()[1:]
		else:
			seq += line.strip()
			counts = Counter(seq)
			id_dict[key] = (counts['G'] + counts['C']) / len(seq) * 100, 4
max_gc = 0
max_id = ''
for key in id_dict:
	if id_dict[key] > max_gc:
		max_gc = id_dict[key]
		max_id = key

print max_id
print max_gc