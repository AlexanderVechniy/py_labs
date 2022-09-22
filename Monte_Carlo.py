def Experiment(N):
    from random import uniform
    p_b = [0.22, 0.06, 0.18, 0.11, 0.11, 0.21] # Вероятности выхода из строя приборов
    fail_ctr = 0    # Счётчик выходов из строя системы
    for n in range(N):
        t = [uniform(0, 1) for i in range(6)]
        # Проверка 1 прибора
        if t[0] < p_b[0]:
            fail_ctr += 1
            continue
        # Проверка 6 прибора
        if t[5] < p_b[5]:
            fail_ctr += 1
            continue     
        # Проверка 2 и 3 прибора       
        if (t[1] < p_b[1]) and (t[2] <= p_b[2]):
            fail_ctr += 1
            continue
        # Проверка 3, 4 и 5 приборов
        if (t[2] < p_b[2]) and (t[3] <= p_b[3]) and (t[4] <= p_b[4]):
            fail_ctr += 1
    print ("Вероятность выхода из строя для", N, "экспериментов:", fail_ctr / N)


Experiment(10)
Experiment(100)
Experiment(500)
Experiment(1000)
