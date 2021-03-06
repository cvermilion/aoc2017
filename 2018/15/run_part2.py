input = open("input.txt"). readlines()


class Node (object):
	def __init__(self, loc, val, neighbors):
		self.loc = loc
		self.val = val
		self.neighbors = neighbors

class Fighter (object):
	def __init__(self, typ, loc, attack):
		self.typ = typ
		self.loc = loc
		self.hp = 200
		self.dead = False
		self.attack = attack

class State(object):
	def __init__(self, fs):
		self.fighters = fs
		self.ngoblins = len([f for f in fs if f.typ == "G"])
		self.nelfs = len(fs) - self.ngoblins
		
def neighbors(loc):
	i,j = loc
	return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
	
def make_state(elf_attack):
	fighters = []
	map = [[l[i] for l in input] for i in range(len(input[0]))]
	for j in range(len(map[0])):
		for i in range(len(map)):
			map[i][j] = Node((i,j), map[i][j], [])
	for j in range(1, len(map[0])-1):
		for i in range(1, len(map)-1):
			n = map[i][j]
			if n.val == "#":
				continue
			if n.val == "G" or n.val == "E":
				if n.val == "G":
					fighters.append(Fighter(n.val, n, 3))
				else:
					fighters.append(Fighter(n.val, n, elf_attack))
			for (ii, jj) in neighbors([i,j]):
				nn = map[ii][jj]
				if nn.val != "#":
					n.neighbors.append(nn)
	return State(fighters)

def is_attackable(f):
	for n in f.loc.neighbors:
		if n.val == ".":
			return True
	return False

def targets(state, f):
	other_type = [ff for ff in state.fighters if ff.typ != f.typ and not ff.dead]
	return [ff for ff in other_type if ff.loc in f.loc.neighbors or is_attackable(ff)]

def closest_target(loc, tgts):
	""" Finds the closest target Node in tgts to loc, returning a tuple of the first and last nodes in the path. """
	tgts = grid_sort(tgts)
	
	direct = [t for t in tgts if t.loc in loc.neighbors]
	if len(direct) > 0:
		return direct[0].loc, None, direct[0]
	
	tgt_locs = [t.loc for t in tgts]
	seen = set([loc])
	paths = set()
	for n in [n for n in loc.neighbors if n.val == "."]:
		seen.add(n)
		paths.add((n,n))
	possible_next = []
	while len(paths) > 0:	
		new_paths = set()
		new_seen = set()
		for p in paths:
			for l in [l for l in p[1].neighbors if not l in seen]:
				if l in tgt_locs:
					possible_next.append((p[0],l))
				else:
					new_seen.add(l)
					if l.val == ".":
						new_paths.add((p[0],l))
		seen = seen.union(new_seen)
		paths = new_paths
		if possible_next:
			return None, min(possible_next, key=lambda l:[list(reversed(l[1].loc)), list(reversed(l[0].loc))])[0], 1
	return None,None,None

def grid_sort(fs):
	return sorted(fs, key=lambda f:list(reversed(f.loc.loc)))
	
def take_turn(state, f):
	direct, next, tgt = closest_target(f.loc, targets(state, f))
	if tgt is None:
		return
	
	if next:
		old = f.loc
		f.loc = next
		old.val = "."
		next.val = f.typ
	
	# Find weakest neighbor
	attackable = [ff for ff in state.fighters if ff.loc in f.loc.neighbors and not ff.dead and ff.typ != f.typ]
	if not attackable:
		return
	tgt = min(grid_sort(attackable), key=lambda ff:ff.hp)
		
	# attack target
	tgt.hp -= f.attack
	if tgt.hp <= 0:
		tgt.dead = True
		tgt.loc.val = "."
		if tgt.typ == "G":
			state.ngoblins -= 1
		else:
			state.nelfs -= 1
	
def step(state):
	for f in state.fighters:
		if not f.dead:
			if f.typ == "G" and state.nelfs == 0:
				return False
			if f.typ == "E" and state.ngoblins == 0:
				return False
			take_turn(state, f)
	state.fighters = [f for f in state.fighters if not f.dead]
	state.fighters = grid_sort(state.fighters)
	return True

def show():
	print("\n".join("".join(map[i][j].val for i in range(len(map))) for j in range(len(map[0]))))

attack = 4
while True:
	steps = 0
	#show()
	state = make_state(attack)
	total_elfs = state.nelfs
	while True:
		if not step(state):
			break
		steps += 1
	
	if state.nelfs == total_elfs:
		print("success!", attack)
		
		rem_hp = sum(f.hp for f in state.fighters if not f.dead)
		print(rem_hp)
		print(steps * rem_hp)
		print([f.hp for f in state.fighters])
		break
	print(attack)
	attack += 1


#print(steps)
#show()


