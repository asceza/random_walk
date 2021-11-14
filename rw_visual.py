from random_walk import RandomWalk
import matplotlib.pyplot as plt


# Построение
rw = RandomWalk()
rw.fill_walk()

# Нанесение точек на график
plt.style.use("dark_background")
# plt.style.use("classic")

fiq, ax = plt.subplots(figsize=(10, 10))

# генерация списка для цветовой карты
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
point_numbers = range(rw.num_points)


ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.prism, edgecolors='none', s=5)

# начальная и конечная точка
ax.scatter(0, 0, c='black', edgecolors='none', s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='black', edgecolors='none', s=50)


# x_coord = [0, rw.x_values[-1]]
# y_coord = [0, rw.y_values[-1]]

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# ax.plot(x_coord, y_coord, '-r', linewidth=2)


# Убираем видимость осей
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
