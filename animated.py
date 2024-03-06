import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

matplotlib.use('TkAgg')  # ou 'Qt5Agg' ou un autre backend supporté


# Création de la figure et du subplot
fig, ax = plt.subplots()

# Initialisation des données
x = []
y = []


# Fonction pour mettre à jour les données
def update_data():
    # Ajout d'une nouvelle donnée
    x.append(time.time())  # Temps écoulé
    y.append(np.random.rand())  # Valeur aléatoire

    # Limite le nombre de données affichées
    max_display = 50
    if len(x) > max_display:
        x.pop(0)
        y.pop(0)


# Fonction d'animation pour mettre à jour le graphique
def animate(i):
    update_data()
    ax.clear()
    ax.plot(x, y)
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Real-time Data Plot')


# Animation du graphique
ani = animation.FuncAnimation(fig, animate, interval=1000)

# Affichage du graphique
plt.show()
