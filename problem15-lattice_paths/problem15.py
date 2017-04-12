def find_ways_to_cross_mono_lattice(n):
	prev = [1]

	for j in range(1, n + 1):
		now = [1 for i in range(0,len(prev) + 1)]
		for i in reversed(range(1, len(prev))):
			now[i] = prev[i-1] + now[i+1]
		now[0] = 2 * now[1]
		prev = now
	return now[0]

print find_ways_to_cross_mono_lattice(2)
print find_ways_to_cross_mono_lattice(3)
print find_ways_to_cross_mono_lattice(10)
print find_ways_to_cross_mono_lattice(20)
