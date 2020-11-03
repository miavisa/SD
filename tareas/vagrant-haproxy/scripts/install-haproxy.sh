#!/usr/bin/env bash

echo "Installing haproxy"
sudo apt update
sudo apt -y install haproxy

echo "Creating haproxy config"
mv /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.bk
cp /tmp/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg

sudo sh -c 'echo "ENABLED=1" >> /etc/default/haproxy'

echo "Starting haproxy"
sudo service haproxy start
