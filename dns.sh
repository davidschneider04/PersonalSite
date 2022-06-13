#!/bin/bash

export LOGIN=$DDNS_USER
export PASSWORD=$DDNS_PW
export DOMAIN="davidschneiderprojects.com"

cd /var/www/davidschneiderprojects.com/
source /home/www-data/environment/bin/activate
python -m dnsexitUpdate
