class batave():
    def __init__():
        pass
    def calc(hits, atbat):
        import math, random, time, numpy
        import matplotlib.pyplot as m
        p = atbat / hits
        points = numpy.array([p, p])
        m.plot(points, marker="x")
        m.savefig("Batave.png")
    def Possible(hits, atbat):
        if hits > atbat:
            return "Not possible"
        else:
            return True
hit_bats = [5, 10]
t = batave
if t.Possible(hit_bats[0], hit_bats[1]) == True:
    t.calc(hit_bats[0], hit_bats[1])
else:
    print(ValueError)
