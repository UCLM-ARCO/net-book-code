Playing with TCP flow control
-----------------------------

- `server.py` is a receiver with forced maximum limited rate.
- `client.py` sends as much as possible. It pauses when sending buffer is full.
