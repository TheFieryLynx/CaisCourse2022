#!/usr/bin/env python3

import sys, json

keyAddress = 'address'
keyHexDump = 'hexDump'
keyText = 'text'
keyIsBranch = 'isBranch'
keyIsForeignBranch = 'isForeignBranch'
keyForeignTargetAddress = 'foreignTargetAddress'
keyForeignTargetName = 'foreignTargetName'

class block:
	def __init__(self, ti = 0, size = -1, b_prev = [], b_next = []):
		self.size = size
		self.b_prev = [b_prev]
		self.b_next = [b_next]
		self.trace_i = ti
	
	def add_b_prev(self, b):
		self.b_prev.append(b)
	
	def add_b_next(self, b):
		self.b_next.append(b)
	
class dot:
	def __init__(self, fill_i = False):
		self.result = 'strict digraph {\n'
		self.file = open("results.dot", "w+")
		self.fill = fill_i
	
	def add_a_to_b(self, a, b):
		if self.fill:
			if s[a].trace_i != -1:
				self.result += '\"' + a + '\" [ shape = box, label = \"' + a + '\n'
				for k in range(s[a].trace_i - s[a].size + 1, s[a].trace_i + 1):
					self.result += trace[k][keyText]
					if k != s[a].trace_i:
						self.result += '\n'
			else:
				self.result += '\"' + a + '\" [ label = \"' + a
			self.result += '\" ];\n'
			
		self.result += '\"' + a + '\"' + ' -> ' + '\"' + b + '\"\n'
		
		if self.fill:
			if s[b].trace_i + 1 == len(trace):
				self.result += '\"' + b + '\" [ shape = box, label = \"' + b + '\n'
				if s[b].trace_i != -1:
					for k in range(s[b].trace_i - s[b].size + 1, s[b].trace_i + 1):
						self.result += trace[k][keyText]
						if k != s[b].trace_i:
							self.result += '\n'
				self.result += '\" ];\n'
	
		
	def __str__(self):
		self.result += '}\n'
		return self.result
	
	def print_to_file(self):
		self.file.write(self.result + '}\n')
		self.file.close()

# приведем к нужному виду десятичный адрес в 16-ый
def convertAddressToHex(address):
	zero_cnt = 16 - (len(hex(address)) -  2)
	return zero_cnt * '0' + hex(int(address))[2:].upper()

# нам не нужен адрес внешней функции - лишь имя
def getBranchAddressOrForeignName(trace_i):
	if keyIsForeignBranch not in trace_i:
		return convertAddressToHex(trace_i[keyAddress])
	else:
		return trace_i[keyForeignTargetName]
	
def search_duplicates(j, dot, i_start, i_start_idx, b_prev, trace):
	while j < len(trace):
		i_start = getBranchAddressOrForeignName(trace[j])
		i_start_idx = j
		if i_start not in s:
			break
		else:
			if i_start not in s[b_prev].b_next:
				s[b_prev].add_b_next(i_start)
				s[i_start].add_b_prev(b_prev)
				dot.add_a_to_b(b_prev, i_start)
			b_prev = i_start
			j += s[i_start].size
			i_start = getBranchAddressOrForeignName(trace[j])
			i_start_idx = j
	return j, dot, i_start, i_start_idx, b_prev
	
def foreignBranchCheck(trace_i, dot, b_prev):
	if keyIsForeignBranch in trace_i:
		addressOrName = getBranchAddressOrForeignName(trace_i)
		# ставим для внешней функции предыдущую b_prev
		if addressOrName in s:
			s[addressOrName].add_b_prev(b_prev)
		else:
			s[addressOrName] = block(-1, 1, b_prev)
		# ставим внешнюю функцию как следующую для b_prev
		dot.add_a_to_b(b_prev, addressOrName)
		s[b_prev].add_b_next(addressOrName)
		s[b_prev].size -= 1
		b_prev = addressOrName
	return b_prev, dot

fillInstructionsFlag = False
if len(sys.argv) == 1:
	print('No input file')
	exit(0)
if len(sys.argv) == 2:
	filename = sys.argv[1]
if len(sys.argv) == 3:
	filename = sys.argv[1]
	if sys.argv[2] != '--fill':
		exit(0)
	fillInstructionsFlag = True
fi = open(filename)
trace = json.load(fi)
s = dict()
dot = dot(fillInstructionsFlag)
instructions = dict()

# соберем все инструкции, осуществляющие передачу управления НЕ за пределы программы
isBranches = set()
for i in range(len(trace) - 1):
	if keyIsBranch in trace[i] and trace[i][keyIsBranch]:
		if keyIsForeignBranch in trace[i] and not trace[i][keyIsForeignBranch] or keyIsForeignBranch not in trace[i]:
			isBranches.add(getBranchAddressOrForeignName(trace[i + 1]))

# объявление переменных
i_start_idx = 0
i_start = getBranchAddressOrForeignName(trace[0])
b_prev = ''
i = 0

# основной цикл
while i < len(trace):
	# если содержит метку или инструкцию передачи управления
	# (проверка что текущая инструкция передает управление, а следующая является началом)
	if keyIsBranch in trace[i] or getBranchAddressOrForeignName(trace[i + 1]) in isBranches:
		if b_prev == '':
			# если B-prev пуст, то инициализируем первый блок
			s[i_start] = block(i, i - i_start_idx + 1)
		else:
			# если b-prev не пуст => присваиваем его как предыдущий
			s[i_start] = block(i, i - i_start_idx + 1, b_prev)
			# а для предыдущего текущий как следующий
			s[b_prev].add_b_next(i_start)
			dot.add_a_to_b(b_prev, i_start)
		b_prev = i_start
		
		# случай когда это trade[i] передаёт управление за пределы программы
		b_prev, dot = foreignBranchCheck(trace[i], dot, b_prev)

		# проверка повторного использования 
		i, dot, i_start, i_start_idx, b_prev = search_duplicates(i + 1, dot, i_start, i_start_idx, b_prev, trace)
	else:
		i += 1
		
fi.close()
print('result of the program in results.dot file.')
dot.print_to_file()