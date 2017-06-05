#!/bin/bash

systemctl stop background-changer.service

cp -f template.service background-changer.service
dir=$PWD
sed -i "s#{dir}#$dir#g" background-changer.service

cp -f background-changer.service /etc/systemd/system
systemctl enable background-changer.service
systemctl daemon-reload
systemctl start background-changer.service