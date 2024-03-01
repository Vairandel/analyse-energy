import sys

import matplotlib.pyplot as plt


def analyseEnergy(log, stress):
    # Ouvrir le fichier en lecture seule
    logFile = open(log, "r")
    stressFile = open(stress, "r")

    # utiliser readlines pour lire toutes les lignes du fichier
    # La variable "lignes" est une liste contenant toutes les lignes du fichier
    logLines = logFile.readlines()
    stressLines = stressFile.readlines()

    # fermez le fichier après avoir lu les lignes
    logFile.close()
    stressFile.close()

    # Tableaux pour le tracé du graphe intensité=f(temps)
    logTimes = []
    logIntensities = []

    stressTimes = []
    stressIntensities = []

    # Iterer sur les lignes
    for line in logLines:
        if line != "\n":
            result_of_extraction = line.split(" ")

            # Recuperation de la date
            time = result_of_extraction[1]
            logTimes.append(time)

            # Recuperation de l'intensite
            intensity = result_of_extraction[2]
            logIntensities.append(float(intensity))

    for line in stressLines:
        if line != "\n":
            result_of_extraction = line.split(",")

            # Recuperation de la date
            date = result_of_extraction[0]
            date_split = date.split(" ")
            time = date_split[1]
            stressTimes.append(time)

            # Recuperation de l'intensite
            intensity = 0
            for i in range(1, 4):
                intensity += float(result_of_extraction[i])
            stressIntensities.append(intensity)

    logMoy = sum(logIntensities) / len(logIntensities)
    stressMoy = sum(stressIntensities) / len(stressIntensities)

    fig, axs = plt.subplots(2, 1, figsize=(30, 7))

    axs[0].plot(logTimes, logIntensities, color='tab:blue')
    axs[0].plot(logTimes, [logMoy for _ in range(len(logTimes))], color='tab:green', label=f"Moyenne = {logMoy}")
    axs[0].set_xlabel('temps')
    axs[0].set_ylabel('Intensité')
    axs[0].set_title(f'Intensité relevées sur le Raspberry Pi en fonction du temps')

    axs[1].plot(stressTimes, stressIntensities, color='tab:red', label=f"Intensité relevées lors du stress de la machine")
    axs[1].plot(stressTimes, [stressMoy for _ in range(len(stressTimes))], color='tab:green', label=f"moyenne = {stressMoy}")

    axs[1].set_xlabel('temps')
    axs[1].set_ylabel('Intensité')
    axs[1].set_title('Intensité relevées lors du stress de la machine en fonction du temps')

    axs[0].set_xticks(logTimes[::10])
    axs[0].set_xticklabels(logTimes[::10], rotation=60)
    axs[1].set_xticks(stressTimes[::10])
    axs[1].set_xticklabels(stressTimes[::10], rotation=60)

    plt.tight_layout()

    axs[0].legend()
    axs[1].legend()

    plt.show()

    return None


if __name__ == '__main__':
    FICHIER_DE_LOG = "rpi.log"
    FICHIER_DE_MACHINE_STRESS = "stress.log"
    for strParam in sys.argv:
        param = strParam.split("=")
        if param[0] == "log":
            FICHIER_DE_LOG = param[1]
        elif param[0] == "stress":
            FICHIER_DE_MACHINE_STRESS = param[1]

    analyseEnergy(FICHIER_DE_LOG, FICHIER_DE_MACHINE_STRESS)
