def Experiment(N):
    from random import uniform
    hit_ctr = 0
    for n in range(N):
        x = uniform(0, 3)
        y = uniform(0, 4)
        if x*x/5 <= y and 5/x >= y:
            hit_ctr += 1
    result = round(hit_ctr / N * 3 * 4, 5)
    print("Площадь фигуры равна ", result, "Для ", N, "экспериментов.")

Experiment(100)
Experiment(200)
Experiment(1000)
Experiment(5000)