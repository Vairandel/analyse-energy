#!/bin/bash

echo "Extractions des valeurs d'analyse sur le Raspberry pi 2"

ssh -p 24 -t toto@pi-2 tail -n 250 /var/log/rpi.log > extractions.log

ssh -t toto@dd-8.inside.esipe-creteil.info tail -n 500 /var/log/rpi.log > stress.log

echo "Les données ont été extraites nous allons tracé le graphique correspondant"

python analyse.py log=extractions.log

echo "Tracé du graphique réussi"