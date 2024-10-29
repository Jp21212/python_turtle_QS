colors =["Red", "orange", "yellow", "green", "blue", "Indigo", "purple"]

for i in range(5000):
  t.forward(i)
  t.color(colors[i % len(colors)])
  t.left(500)
