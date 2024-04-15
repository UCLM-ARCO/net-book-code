# setup dockerized VPN server

    $ docker compose up -d server
    $ docker compose exec -it server /bin/bash
    $ ip a

# setup dockerized VPN client

    $ cp server/peer1/peer1.conf client/
    $ docker compose up -d client
    $ docker compose exec -it client /bin/bash
    vpn-client$ wg-quick up /config/wg_confs/peer1.conf
    vpn-client$ ip a

# connect host as VPN client

    $ apt install wireguard
    $ cp server/peer2/peer2.conf .
    $ sudo wg-quick up ./peer2.conf

## disconnect

    $ sudo wg-quick down ./peer2.conf
