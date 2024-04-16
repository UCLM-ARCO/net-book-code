# setup dockerized VPN server

    $ make server-setup
    $ make server-shell
    $ ip a

# setup dockerized VPN client

    $ make client-setup
    $ make client-shell
    vpn-client$ wg-quick up /config/wg_confs/peer1.conf
    vpn-client$ ip a

# connect host as VPN client

    $ apt install wireguard
    $ sudo wg-quick up server/peer2/peer2.conf

## disconnect

    $ sudo wg-quick down ./peer2.conf
