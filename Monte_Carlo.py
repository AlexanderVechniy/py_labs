t_p = 0.22+0.06*0.18+0.18*0.11*0.11+0.21 # 0.442978
print("Теор. вер. выхода из строя системы =", t_p)

from random import uniform

def Experiment(N):
	d = [[], [], [], [], [], []]
	d_p = [0.22, 0.06, 0.18, 0.11, 0.11, 0.21]
	not_working_counter = 0

	for i in range (N):
		for j in range (6):
			t = round(uniform(0, 1), 2)
			d[j].append([t, t <= d_p[j]])
		if d[0][i][1] or d[1][i][1] and d[2][i][1] or d[2][i][1] and d[3][i][1] and d[4][i][1] or d[5][i][1]:
			not_working_counter += 1

	return not_working_counter/N

print ("Вероятность выхода из строя для 10 экспериментов:", Experiment(10))
print ("Вероятность выхода из строя для 100 экспериментов:", Experiment(100))
print ("Вероятность выхода из строя для 1000 экспериментов:", Experiment(1000))