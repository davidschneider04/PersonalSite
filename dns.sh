#!/bin/bash

export LOGIN=$DDNS_USER
export PASSWORD=$DDNS_PW
export DOMAIN="graniteturtle.com"

cd /var/www/graniteturtle.com/
source /home/www-data/environment/bin/activate
python -m dnsexitUpdate
