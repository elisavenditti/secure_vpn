sudo ip a a 10.0.16.2/30 dev enp0s3
sudo ip a a 10.23.1.1/24 dev enp0s8
sudo ip r a default via 10.0.16.1
sudo -s
echo 1 > /proc/sys/net/ipv4/ip_forward
