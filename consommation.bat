ssh -t toto@localhost tail -n 100 -f /var/log/powerjoular-data.log > consommation.log

python consommation.py