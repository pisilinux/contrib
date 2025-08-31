#!/bin/sh
/usr/bin/tailscaled --state=/var/lib/tailscale/tailscaled.state --socket=/run/tailscale/tailscaled.sock --port=41641 > /dev/null 2>&1 &
echo $! > /run/tailscale/tailscaled.pid
