import matplotlib.pyplot as plt


def analyseEnergy(log):
    # Ouvrir le fichier en lecture seule
    file = open(log, "r")

    # utiliser readlines pour lire toutes les lignes du fichier
    # La variable "lignes" est une liste contenant toutes les lignes du fichier
    lines = file.readlines()

    # fermez le fichier après avoir lu les lignes
    file.close()

    # Tableaux pour le tracé du graphe intensité=f(temps)
    times = []
    intensities = []

    # Iterer sur les lignes
    for line in lines:
        if line != "\n":
            result_of_extraction = line.split(",")

            # Recuperation de la date
            date = result_of_extraction[0]
            date_split = date.split(" ")
            time = date_split[1]
            times.append(time)

            # Recuperation de l'intensite
            intensity = 0
            for i in range(1, 4):
                intensity += float(result_of_extraction[i])
            intensities.append(intensity)

    moy = sum(intensities) / len(intensities)

    fig, axs = plt.subplots(2, 1, figsize=(30, 7))

    axs.plot(times, intensities, color='tab:red', label=f"Intensité relevées sur la machine")
    axs.plot(times, [moy for _ in range(len(times))], color='tab:green', label=f"moyenne = {moy}")

    axs.set_xlabel('temps')
    axs.set_ylabel('Intensité')
    axs.set_title('Intensité relevées sur la machine en fonction du temps')
    
    axs.set_xticks(times[::10])
    axs.set_xticklabels(times[::10], rotation=60)

    plt.tight_layout()
    
    axs.legend()

    plt.show()

    return None


if __name__ == '__main__':
    FICHIER_DE_LOG = "/var/log/powerjoular-data.log"
    analyseEnergy(FICHIER_DE_LOG)
