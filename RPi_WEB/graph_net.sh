#!/bin/bash
RRDTOOL=$(whereis -b rrdtool | awk '{print $2}')
HOME="/var/ramdisk/RPi-IO/RPi_WEB/static/graph"
$RRDTOOL graph $HOME/net1.png \
--title="Lantência 1h (IP 8.8.8.8)" \
--vertical-label "ms" \
-s 'now - 1 hour' -e 'now' \
-A -Y -X 0 \
DEF:temp=/var/ramdisk/var/net.rrd:temp:AVERAGE \
CDEF:dispo=temp,100,0,IF \
VDEF:dispo_por=dispo,AVERAGE \
AREA:temp#0000FF:Latência \
GPRINT:temp:MAX:"Máxima\\: %3.2lf" \
GPRINT:temp:AVERAGE:"Media\\: %3.2lf" \
GPRINT:temp:MIN:"Mínima\\: %3.2lf\n" \
GPRINT:dispo_por:"Disponibilidade\\: %3.2lf"

$RRDTOOL graph $HOME/net24.png \
--title="Lantência 24h (IP 8.8.8.8)" \
--vertical-label "ms" \
-s 'now - 24 hour' -e 'now' \
-A -Y -X 0 \
DEF:temp=/var/ramdisk/var/net.rrd:temp:AVERAGE \
CDEF:dispo=temp,100,0,IF \
VDEF:dispo_por=dispo,AVERAGE \
AREA:temp#0000FF:Latência \
GPRINT:temp:MAX:"Máxima\\: %3.2lf" \
GPRINT:temp:AVERAGE:"Media\\: %3.2lf" \
GPRINT:temp:MIN:"Mínima\\: %3.2lf\n" \
GPRINT:dispo_por:"Disponibilidade\\: %3.2lf"

$RRDTOOL graph $HOME/net48.png \
--title="Lantência 48h (IP 8.8.8.8)" \
--vertical-label "ms" \
-s 'now - 48 hour' -e 'now' \
-A -Y -X 0 \
DEF:temp=/var/ramdisk/var/net.rrd:temp:AVERAGE \
CDEF:dispo=temp,100,0,IF \
VDEF:dispo_por=dispo,AVERAGE \
AREA:temp#0000FF:Latência \
GPRINT:temp:MAX:"Máxima\\: %3.2lf" \
GPRINT:temp:AVERAGE:"Media\\: %3.2lf" \
GPRINT:temp:MIN:"Mínima\\: %3.2lf\n" \
GPRINT:dispo_por:"Disponibilidade\\: %3.2lf"
