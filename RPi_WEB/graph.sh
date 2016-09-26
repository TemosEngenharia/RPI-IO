#!/bin/bash
RRDTOOL=$(whereis -b rrdtool | awk '{print $2}')
HOME="/var/ramdisk/RPi-IO/RPi_WEB/static/graph"
$RRDTOOL graph $HOME/temp1.png \
--title="Temperatura Placa 1h" \
--vertical-label "ºC" \
-s 'now - 1 hour' -e 'now' \
-A -Y -X 0 \
DEF:temp=/var/ramdisk/var/temperature.rrd:temp:AVERAGE \
AREA:temp#FF0000:Temperatura \
GPRINT:temp:MAX:"Máxima\\: %3.2lf" \
GPRINT:temp:AVERAGE:"Media\\: %3.2lf" \
GPRINT:temp:MIN:"Mínima\\: %3.2lf"

$RRDTOOL graph $HOME/temp6.png \
--title="Temperatura Placa 6h" \
--vertical-label "ºC" \
-s 'now - 6 hour' -e 'now' \
-A -Y -X 0 \
DEF:temp=/var/ramdisk/var/temperature.rrd:temp:AVERAGE \
AREA:temp#FF0000:Temperatura \
GPRINT:temp:MAX:"Máxima\\: %3.2lf" \
GPRINT:temp:AVERAGE:"Media\\: %3.2lf" \
GPRINT:temp:MIN:"Mínima\\: %3.2lf"

$RRDTOOL graph $HOME/temp12.png \
--title="Temperatura Placa 12h" \
--vertical-label "ºC" \
-s 'now - 12 hour' -e 'now' \
-A -Y -X 0 \
DEF:temp=/var/ramdisk/var/temperature.rrd:temp:AVERAGE \
AREA:temp#FF0000:Temperatura \
GPRINT:temp:MAX:"Máxima\\: %3.2lf" \
GPRINT:temp:AVERAGE:"Media\\: %3.2lf" \
GPRINT:temp:MIN:"Mínima\\: %3.2lf"

$RRDTOOL graph $HOME/temp24.png \
--title="Temperatura Placa 24h" \
--vertical-label "ºC" \
-s 'now - 24 hour' -e 'now' \
-A -Y -X 0 \
DEF:temp=/var/ramdisk/var/temperature.rrd:temp:AVERAGE \
AREA:temp#FF0000:Temperatura \
GPRINT:temp:MAX:"Máxima\\: %3.2lf" \
GPRINT:temp:AVERAGE:"Media\\: %3.2lf" \
GPRINT:temp:MIN:"Mínima\\: %3.2lf"

$RRDTOOL graph $HOME/temp48.png \
--title="Temperatura Placa 48h" \
--vertical-label "ºC" \
-s 'now - 48 hour' -e 'now' \
-A -Y -X 0 \
DEF:temp=/var/ramdisk/var/temperature.rrd:temp:AVERAGE \
AREA:temp#FF0000:Temperatura \
GPRINT:temp:MAX:"Máxima\\: %3.2lf" \
GPRINT:temp:AVERAGE:"Media\\: %3.2lf" \
GPRINT:temp:MIN:"Mínima\\: %3.2lf"
