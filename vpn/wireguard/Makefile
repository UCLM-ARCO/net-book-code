server-setup:
	docker compose up -d server

client-setup:
	cp server/peer1/peer1.conf client/
	docker compose up -d client

server-shell:
	docker compose exec -it server /bin/bash

client-shell:
	docker compose exec -it client /bin/bash
