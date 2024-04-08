# docker VPN server and client

    $ docker compose up -d server
    $ cp server/peer1/peer1.conf client/
    $ docker compose up -d client


# connect host as VPN client

    $ apt install wireguard
    $ cp server/peer2/peer2.conf .
    $ sudo wg-quick up ./peer2.conf

## disconnect

    $ sudo wg-quick down ./peer2.conf
