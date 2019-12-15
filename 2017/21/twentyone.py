input = """../.. => ###/##./##.
#./.. => .##/###/...
##/.. => ##./###/#..
.#/#. => .##/#.#/###
##/#. => .#./###/#..
##/## => .../#.#/...
.../.../... => .#../#.#./..##/.###
#../.../... => ...#/#..#/#.../#.#.
.#./.../... => .###/..##/.#.#/..#.
##./.../... => ##.#/#.##/..#./...#
#.#/.../... => .##./####/..../..#.
###/.../... => ...#/..../..../##.#
.#./#../... => ##../#..#/..##/#.##
##./#../... => ###./...#/#..#/#.#.
..#/#../... => .##./#.../.###/#.#.
#.#/#../... => ...#/#.##/####/##.#
.##/#../... => ####/..../..#./....
###/#../... => ..##/..##/.###/..#.
.../.#./... => ..../.#../.#.#/...#
#../.#./... => ..#./#.../####/#...
.#./.#./... => ...#/##../#.../.#..
##./.#./... => ####/..../#.../#..#
#.#/.#./... => #.##/#.#./##../.##.
###/.#./... => ###./...#/#.##/#.##
.#./##./... => ..##/#.##/###./#.#.
##./##./... => ..../..##/.###/#..#
..#/##./... => ####/...#/##../####
#.#/##./... => ##../.#.#/.#../.#.#
.##/##./... => ..#./.#../.#../###.
###/##./... => #.../.###/..##/.#..
.../#.#/... => ...#/##../.##./....
#../#.#/... => .#../..../..#./###.
.#./#.#/... => ##../#.#./#.../...#
##./#.#/... => .##./...#/#.##/#.##
#.#/#.#/... => #.../#.##/#..#/...#
###/#.#/... => ..##/#.##/...#/###.
.../###/... => #.../#.##/.#.#/...#
#../###/... => ..#./###./.#.#/#.#.
.#./###/... => ###./.#.#/.##./.#.#
##./###/... => .###/#.##/##../.##.
#.#/###/... => .#../..##/..../..#.
###/###/... => ...#/.#../.#.#/#...
..#/.../#.. => ...#/.#.#/..#./...#
#.#/.../#.. => ##.#/###./####/##.#
.##/.../#.. => .###/.##./..##/....
###/.../#.. => ..../.#.#/...#/#..#
.##/#../#.. => #.##/.#.#/##../##..
###/#../#.. => ..../..##/####/#.#.
..#/.#./#.. => #.#./##.#/##../##..
#.#/.#./#.. => #.##/.##./##.#/#.##
.##/.#./#.. => ##.#/#.../.#../####
###/.#./#.. => ###./..##/####/.##.
.##/##./#.. => #.##/..#./...#/.#..
###/##./#.. => ##.#/#.#./#.../..#.
#../..#/#.. => ####/...#/..../#.#.
.#./..#/#.. => ##../.###/.###/.#..
##./..#/#.. => #.#./###./...#/.##.
#.#/..#/#.. => #.#./.###/..##/..##
.##/..#/#.. => .#../#..#/##../#...
###/..#/#.. => ####/#.##/#.../...#
#../#.#/#.. => ##../.###/#.../....
.#./#.#/#.. => ..../#.#./##../..#.
##./#.#/#.. => #..#/...#/##../##..
..#/#.#/#.. => ####/#..#/..##/##.#
#.#/#.#/#.. => .#../..##/###./.#..
.##/#.#/#.. => #..#/#.../..../####
###/#.#/#.. => ..../.##./.#.#/...#
#../.##/#.. => #.#./#.##/#.../#...
.#./.##/#.. => #.##/###./.##./####
##./.##/#.. => ###./.###/##.#/#..#
#.#/.##/#.. => ##../####/####/#.#.
.##/.##/#.. => ####/#.#./###./.##.
###/.##/#.. => ##.#/#..#/.##./..#.
#../###/#.. => ...#/####/#.#./#.#.
.#./###/#.. => ..##/.##./.###/..#.
##./###/#.. => ..#./##.#/####/##..
..#/###/#.. => ###./.###/..../###.
#.#/###/#.. => ##.#/###./..../..#.
.##/###/#.. => .##./##.#/#.##/.##.
###/###/#.. => .#.#/####/#.##/##..
.#./#.#/.#. => ..##/..##/#.##/#.#.
##./#.#/.#. => #.##/#.##/..#./..##
#.#/#.#/.#. => .#.#/..../#.#./..#.
###/#.#/.#. => #.#./..##/###./#.##
.#./###/.#. => .#../.###/..##/##..
##./###/.#. => ##.#/..#./#.#./#...
#.#/###/.#. => ##../###./.#.#/...#
###/###/.#. => ###./##.#/..../###.
#.#/..#/##. => #.#./##.#/#.#./.##.
###/..#/##. => .#.#/#.../####/.##.
.##/#.#/##. => ##.#/#.#./#.#./.#..
###/#.#/##. => ...#/..##/###./#.##
#.#/.##/##. => #.##/##.#/#..#/..##
###/.##/##. => .###/.#.#/#.##/.#..
.##/###/##. => #..#/#..#/#.##/.#..
###/###/##. => ..##/.##./####/###.
#.#/.../#.# => ##../#.##/##../.##.
###/.../#.# => ###./#.#./##.#/####
###/#../#.# => ###./#.#./#..#/...#
#.#/.#./#.# => ###./###./.#.#/.#..
###/.#./#.# => ..#./...#/..#./##..
###/##./#.# => .###/#..#/#.##/.#.#
#.#/#.#/#.# => ####/#.../##../....
###/#.#/#.# => ##../...#/..##/..#.
#.#/###/#.# => .##./#.../#..#/#..#
###/###/#.# => .#.#/#.../..../#..#
###/#.#/### => #.#./.##./##../.###
###/###/### => ###./.#../####/..##"""

input2 = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""

def parse_pattern(p):
	lines = p.split("/")
	return [[1 if c == "#" else 0 for c in l] for l in lines]

def pat_string(p):
	return "".join("".join(str(c) for c in l) for l in p)
	
def parse_line(l):
	pat, out = l.split(" => ")
	return parse_pattern(pat), parse_pattern(out)

def rot270(m):
	l = len(m)
	return [[m[i][-(j+1)] for i in range(l)] for j in range(l)]

def rot180(m):
	l = len(m)
	return [[m[-(j+1)][-(i+1)] for i in range(l)] for j in range(l)]

def rot90(m):
	l = len(m)
	return [[m[-(i+1)][j] for i in range(l)] for j in range(l)]

def flipx(m):
	l = len(m)
	return [[m[j][-(i+1)] for i in range(l)] for j in range(l)]

def flipy(m):
	l = len(m)
	return [[m[-(j+1)][i] for i in range(l)] for j in range(l)]

rules = {}
for pat, out in map(parse_line, input.splitlines()):
	variants = [pat, rot90(pat), rot180(pat), rot270(pat)]
	for var in variants:
		rules[pat_string(var)] = out
		rules[pat_string(flipx(var))] = out
		rules[pat_string(flipy(var))] = out

start = [[0,1,0], [0,0,1], [1,1,1]]

def split_sub_matrices(m, size):
	n = int(len(m)/size)
	return [[[m[j][ni*size:(ni+1)*size] for j in range(nj*size, (nj+1)*size)] for ni in range(n)] for nj in range(n)]

def join_sub_matrices(m, size):
	l = len(m)*size
	return [[m[int(j/size)][int(i/size)][j % size][i % size] for i in range(l)] for j in range(l)]
	
def stepn(m, n):
	pieces = split_sub_matrices(m, n)
	expanded = [[rules[pat_string(pieces[j][i])] for i in range(len(pieces))] for j in range(len(pieces))]
	return join_sub_matrices(expanded, n+1)
	
def step(m):
	if len(m) % 2 == 0:
		return stepn(m, 2)
	else:
		return stepn(m, 3)

m = start
for i in range(5):
	m = step(m)

print(sum(sum(l) for l in m))

m = start
for i in range(18):
	m = step(m)

print(sum(sum(l) for l in m))