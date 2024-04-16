SERVER="vpn-server"
CLIENT="client1"

server-setup:
	docker compose run --rm server ovpn_genconfig -u udp://${SERVER}
	docker compose run --rm server ovpn_initpki

client1.ovpn:
	docker compose run --rm server easyrsa build-client-full ${CLIENT}
	docker compose run --rm server ovpn_getclient ${CLIENT} > ./docker/client/data/${CLIENT}.ovpn

nopass-client1.ovpn:
	docker compose run --rm server easyrsa build-client-full ${CLIENT} nopass
	docker compose run --rm server ovpn_getclient ${CLIENT} > ./docker/client/data/${CLIENT}.ovpn

revoke-client:
	docker compose run --rm server ovpn_revokeclient ${CLIENT}
	docker compose run --rm server ovpn_revokeclient ${CLIENT} remove

server-shell:
	docker compose exec -it server /bin/bash

client-shell:
	docker compose exec -it client /bin/bash
