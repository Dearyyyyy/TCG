# coding=utf-8
while True:
	string = input()
	score = 0       #得分
	rebound = 0     #抢断
	assists = 0     #助攻
	steal = 0       #偷球
	block = 0       #篮板
	shots = 0       #投篮次数（不包括罚球）
	hits = 0        #投篮命中（不包括罚球）
	freethrows = 0  #发球次数
	Yfreethrows = 0 #发球命中次数
	turnovers = 0   #失误
	for i in range(len(string)):
		if string[i] == 'Y':
			tmp = int(string[i-1])
			score += tmp
			if tmp == 1:
				freethrows += 1
				Yfreethrows += 1
			else:
				shots += 1
				hits += 1
		
		elif string[i] == 'N':
			tmp = int(string[i-1])
			if tmp == 1:
				freethrows += 1
			else:
				shots += 1

		else:
			if string[i] == 'R':
				rebound += 1
			elif string[i] == 'A':
				assists += 1
			elif string[i] == 'S':
				steal += 1
			elif string[i] == 'B':
				block += 1
			elif string[i] == 'T':
				turnovers += 1

	value = (score + rebound + assists + steal + block) - (shots - hits) - (freethrows - Yfreethrows) - turnovers
	print(value)