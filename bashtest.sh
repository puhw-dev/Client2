#!/bin/bash
MONITOR="10.0.0.4:8898"
SENSOR="System%20Load"
METRIC="cpuUtilization"
COUNT="100"
HOSTS=$(curl --silent $MONITOR/hosts/ | tr , '\n' | sed -nre 's/^.*"hostname":"([^"]*)".*$/\1/pg')

for HOST in $HOSTS; do
	curl --silent http://$MONITOR/hosts/$HOST/sensors/$SENSOR/metrics/$METRIC/data?n=$COUNT \
		| tr -d '\n' \
		| sed -re 's/^.*"data":\[([^]]*)].*$/\1/;s/"\},\{"/\n/g;s/:/ /g;s/[\{\}"]//g' \
		| sort -n \
		| gnuplot -p -e 'plot "-"'
done
