#!/usr/bin/env python3

import sys, json

results = []

# -----------------------------------------------------------------------

class registersClass:
	def __init__(self):
		self.info = {
			'rax': {'reg_name': 'rax', 'offset': 0, "size": 8 },
			'rbx': {'reg_name': 'rbx', 'offset': 0, "size": 8 },
			'rcx': {'reg_name': 'rcx', 'offset': 0, "size": 8 },
			'rdx': {'reg_name': 'rdx', 'offset': 0, "size": 8 },
			'rdi': {'reg_name': 'rdi', 'offset': 0, "size": 8 },
			'rsi': {'reg_name': 'rsi', 'offset': 0, "size": 8 },
			'rbp': {'reg_name': 'rbp', 'offset': 0, "size": 8 },
			'rsp': {'reg_name': 'rsp', 'offset': 0, "size": 8 },
			
			'r8': {'reg_name': 'r8', 'offset': 0, "size": 8 },
			'r9': {'reg_name': 'r9', 'offset': 0, "size": 8 },
			'r10': {'reg_name': 'r10', 'offset': 0, "size": 8 },
			'r11': {'reg_name': 'r11', 'offset': 0, "size": 8 },
			'r12': {'reg_name': 'r12', 'offset': 0, "size": 8 },
			'r13': {'reg_name': 'r13', 'offset': 0, "size": 8 },
			'r14': {'reg_name': 'r14', 'offset': 0, "size": 8 },
			'r15': {'reg_name': 'r15', 'offset': 0, "size": 8 },
			
			'rflags': {'reg_name': 'rflags', 'offset': 0, "size": 8 },
			
			'eax': {'reg_name': 'rax', 'offset': 0, "size": 4 },
			'ebx': {'reg_name': 'rbx', 'offset': 0, "size": 4 },
			'ecx': {'reg_name': 'rcx', 'offset': 0, "size": 4 },
			'edx': {'reg_name': 'rdx', 'offset': 0, "size": 4 },
			'edi': {'reg_name': 'rdi', 'offset': 0, "size": 4 },
			'esi': {'reg_name': 'rsi', 'offset': 0, "size": 4 },
			'ebp': {'reg_name': 'rbp', 'offset': 0, "size": 4 },
			'esp': {'reg_name': 'rsp', 'offset': 0, "size": 4 },
			
			'r8d': {'reg_name': 'r8', 'offset': 0, "size": 4 },
			'r9d': {'reg_name': 'r9', 'offset': 0, "size": 4 },
			'r10d': {'reg_name': 'r10', 'offset': 0, "size": 4 },
			'r11d': {'reg_name': 'r11', 'offset': 0, "size": 4 },
			'r12d': {'reg_name': 'r12', 'offset': 0, "size": 4 },
			'r13d': {'reg_name': 'r13', 'offset': 0, "size": 4 },
			'r14d': {'reg_name': 'r14', 'offset': 0, "size": 4 },
			'r15d': {'reg_name': 'r15', 'offset': 0, "size": 4 },
	
			'eflags': {'reg_name': 'rflags', 'offset': 0, "size": 4 },
				
			'ax': {'reg_name': 'rax', 'offset': 0, "size": 2 },
			'bx': {'reg_name': 'rbx', 'offset': 0, "size": 2 },
			'cx': {'reg_name': 'rcx', 'offset': 0, "size": 2 },
			'dx': {'reg_name': 'rdx', 'offset': 0, "size": 2 },
			'di': {'reg_name': 'rdi', 'offset': 0, "size": 2 },
			'si': {'reg_name': 'rsi', 'offset': 0, "size": 2 },
			'bp': {'reg_name': 'rbp', 'offset': 0, "size": 2 },
			'sp': {'reg_name': 'rsp', 'offset': 0, "size": 2 },
			
			'r8w': {'reg_name': 'r8', 'offset': 0, "size": 2 },
			'r9w': {'reg_name': 'r9', 'offset': 0, "size": 2 },
			'r10w': {'reg_name': 'r10', 'offset': 0, "size": 2 },
			'r11w': {'reg_name': 'r11', 'offset': 0, "size": 2 },
			'r12w': {'reg_name': 'r12', 'offset': 0, "size": 2 },
			'r13w': {'reg_name': 'r13', 'offset': 0, "size": 2 },
			'r14w': {'reg_name': 'r14', 'offset': 0, "size": 2 },
			'r15w': {'reg_name': 'r15', 'offset': 0, "size": 2 },

			'al': {'reg_name': 'rax', 'offset': 0, "size": 1 },
			'bl': {'reg_name': 'rbx', 'offset': 0, "size": 1 },
			'cl': {'reg_name': 'rcx', 'offset': 0, "size": 1 },
			'dl': {'reg_name': 'rdx', 'offset': 0, "size": 1 },
			
			'ah': {'reg_name': 'rax', 'offset': 1, "size": 1 },
			'bh': {'reg_name': 'rbx', 'offset': 1, "size": 1 },
			'ch': {'reg_name': 'rcx', 'offset': 1, "size": 1 },
			'dh': {'reg_name': 'rdx', 'offset': 1, "size": 1 },
			
			'dil': {'reg_name': 'rdi', 'offset': 0, "size": 1 },
			'sil': {'reg_name': 'rsi', 'offset': 0, "size": 1 },
			'bpl': {'reg_name': 'rbp', 'offset': 0, "size": 1 },
			'spl': {'reg_name': 'rsp', 'offset': 0, "size": 1 },
		
				 
			'r8b': {'reg_name': 'r8', 'offset': 0, "size": 1 },
			'r9b': {'reg_name': 'r9', 'offset': 0, "size": 1 },
			'r10b': {'reg_name': 'r10', 'offset': 0, "size": 1 },
			'r11b': {'reg_name': 'r11', 'offset': 0, "size": 1 },
			'r12b': {'reg_name': 'r12', 'offset': 0, "size": 1 },
			'r13b': {'reg_name': 'r13', 'offset': 0, "size": 1 },
			'r14b': {'reg_name': 'r14', 'offset': 0, "size": 1 },
			'r15b': {'reg_name': 'r15', 'offset': 0, "size": 1 },
			
			'memory': {'reg_name': 'memory', 'offset': 0, "size": 0 },
			'flags': {'reg_name': 'rflags', 'offset': 0, "size": 2 },
			'rip' : {'reg_name': 'rip', 'offset': 0, "size": 0 }
		}
		self.res = {
			'rax': [0 for i in range(8)],
			'rbx': [0 for i in range(8)],
			'rcx': [0 for i in range(8)],
			'rdx': [0 for i in range(8)],
			'rdi': [0 for i in range(8)],
			'rsi': [0 for i in range(8)],
			'rbp': [0 for i in range(8)],
			'rsp': [0 for i in range(8)],
			
			'r8': [0 for i in range(8)],
			'r9': [0 for i in range(8)],
			'r10': [0 for i in range(8)],
			'r11': [0 for i in range(8)],
			'r12': [0 for i in range(8)],
			'r13': [0 for i in range(8)],
			'r14': [0 for i in range(8)],
			'r15': [0 for i in range(8)],
			
			'rflags': [0 for i in range(8)],
			'memory': set()
		}
		self.children_dependency = {
			'rax': ['rax', 'eax', 'ax', 'ah', 'al'],
			'rbx': ['rbx', 'ebx', 'bx', 'bh', 'bl'],
			'rcx': ['rcx', 'ecx', 'cx', 'ch', 'cl'],
			'rdx': ['rdx', 'edx', 'dx', 'dh', 'dl'],
			
			'rdi': ['rdi', 'edi', 'di', 'dil'],
			'rsi': ['rsi', 'esi', 'si', 'sil'],
			'rbp': ['rbp', 'ebp', 'bp', 'bpl'],
			'rsp': ['rsp', 'esp', 'sp', 'spl'],
			
			'r8': ['r8', 'r8d', 'r8w', 'r8b'],
			'r9': ['r9', 'r9d', 'r9w', 'r9b'],
			'r10': ['r10', 'r10d', 'r10w', 'r10b'],
			'r11': ['r11', 'r11d', 'r11w', 'r11b'],
			'r12': ['r12', 'r12d', 'r12w', 'r12b'],
			'r13': ['r13', 'r13d', 'r13w', 'r13b'],
			'r14': ['r14', 'r14d', 'r14w', 'r14b'],
			'r15': ['r15', 'r15d', 'r15w', 'r15b'],
			
			'rflags': ['rflags', 'eflags', 'flags']
		}
	
	
	def getRegInfo(self, reg):
		if reg in self.info:
			return self.info[reg]
		return {'reg_name': 'reg', 'offset': 0, "size": 0 }
	
	def setRegByte(self, reg, i):
		self.res[reg][i] = 1
	
	def rmRegByte(self, reg, i):
		self.res[reg][i] = 0
	
	def setMemory(self, i):
		self.res['memory'].add(i)
	
	def rmMemory(self, i):
		if i in self.res['memory']:
			self.res['memory'].remove(i)
	
	def checkTaintMem(self, i):
		if i in self.res['memory']:
			return True
		return False
	
	def checkTaintReg(self, reg, i):
		if self.res[reg][i] == 1:
			return True
		return False
		
registers = registersClass()

# -----------------------------------------------------------------------

class testsClass:
	def __init__(self):
		self.sources = dict()
		self.sinks = []
	
	def add_source(self, tests_row):
		self.sources[tests_row['step']] = tests_row['taint']
	
	def add_sink(self, tests_row):
		self.sinks.append(tests_row['step'])
		
tests = testsClass()

# -----------------------------------------------------------------------

def process_source(register, offset, size):
	info = registers.getRegInfo(register)
	left = offset + info['offset']
	right = left + size
	for i in range(left, right):
		if info['reg_name'] == 'memory':
			registers.setMemory(i)
		else:
			registers.setRegByte(info['reg_name'], i)
			
def process_source_rm(register, offset, size):
	info = registers.getRegInfo(register)
	left = offset + info['offset']
	right = left + size
	for i in range(left, right):
		if info['reg_name'] == 'memory':
			registers.rmMemory(i)
		else:
			registers.rmRegByte(info['reg_name'], i)
			
def check_tainted(register, offset, size):
	info = registers.getRegInfo(register)
	left = offset + info['offset']
	right = left + size
	for i in range(left, right):
		if info['reg_name'] == 'memory':
			return registers.checkTaintMem(i)
		else:
			return registers.checkTaintReg(info['reg_name'], i)
	return False

def mem(k, v):
	ret = []
	memory = sorted(list(v))
	size = len(memory)
	cnt = 1
	for i in range(1, size):
		if memory[i] == memory[i - 1] + 1:
			cnt += 1
		else:
			if k == 'memory':
				ret.append((memory[i - cnt], cnt))
			else:
				ret.append((k, memory[i - cnt], cnt))
			cnt = 1
			
	if cnt > 0 and size > 0:
		if k == 'memory':
			ret.append((memory[size - cnt], cnt))
		else:
			ret.append((k, memory[size - cnt], cnt))
	return ret

def sink():
	res = []
	for k, v in registers.res.items():
		
		v = v.copy()
		res1 = []
		if k in registers.children_dependency:
			
			tmp = []
			for i in registers.children_dependency[k]:
				info = registers.getRegInfo(i)
				flag = True
				for j in range(info['offset'], info['offset'] + info['size']):
					if v[j] != 1:
						flag = False
						break
				if flag:
					tmp.append(i)
					for j in range(info['offset'], info['offset'] + info['size']):
						v[j] = 0

			tmp2 = set()
			for l in range(len(v)):
				if v[l] == 1:
					tmp2.add(l)
		
			res1 = tmp
			for i in mem(k, tmp2):
				res1.append(i)
		else:
			res1 = mem(k, v)
			
		for i in res1:
			res.append(i)
	return res
			
# -----------------------------------------------------------------------

def source_processing(step):
	for i in tests.sources[step]:
		if type(i) == list: 		# [140721559695000, 8] or ["rax", 8]
			if type(i[0]) != str: 	# [140721559695000, 8]
				process_source('memory', i[0], i[1])
			else: 					#["rax", 8, 1]
				process_source(i[0], i[1], i[2])
		elif type(i) == str:		# "ax"
			info = registers.getRegInfo(i)
			process_source(info['reg_name'], info['offset'], info['size'])

	
def sink_processing(step):
	results.append({"step": step, "answer": sink()})
			
def distribute(trace_i):
	flag = False
	
	if "readRegs" in trace_i:
		for i in trace_i["readRegs"]:
			info = registers.getRegInfo(i)
			flag |= check_tainted(info['reg_name'], info['offset'], info['size'])
	if "readMem" in trace_i and not flag:
		for i in trace_i["readMem"]:
			flag |= check_tainted('memory', i[0], i[1])
	if flag:
		if "writeRegs" in trace_i:
			for i in trace_i["writeRegs"]:
				info = registers.getRegInfo(i)
				process_source(info['reg_name'], info['offset'], info['size'])
		if "writtenMem" in trace_i:
			for i in trace_i["writtenMem"]:
				process_source('memory', i[0], i[1])
	elif trace_i["text"].startswith("cmov") or trace_i["text"].startswith("mov"):
		if "writeRegs" in trace_i:
			for i in trace_i["writeRegs"]:
				info = registers.getRegInfo(i)
				process_source_rm(info['reg_name'], info['offset'], info['size'])
		if "writtenMem" in trace_i:
			for i in trace_i["writtenMem"]:
				process_source_rm('memory', i[0], i[1])
	
# -----------------------------------------------------------------------


if len(sys.argv) < 4:
	print('incorrect params')
	exit(0)
if len(sys.argv) == 4:
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	output_filename = sys.argv[3]

fi_trace = open(filename1)
fi_tests = open(filename2)
fo = open(output_filename, 'w+')

trace_json = json.load(fi_trace)
tests_json = json.load(fi_tests)

for i in tests_json:
	if i['type'] == 'source':
		tests.add_source(i)
	else:
		tests.add_sink(i)

for step, trace_i in enumerate(trace_json):
	if step in tests.sources:
		source_processing(step)
	if step in tests.sinks:
		sink_processing(step)
	distribute(trace_i)
#print(results)
	
json.dump(results, fo)	

fi_trace.close()	
fi_tests.close()
fo.close()