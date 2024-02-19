Flow control for media stream play
----------------------------------

run server:

```
$ ./server.py 2000 | mplayer -quite -
```

run client:

```
$ ./client.py localhost 2000 < audio.mp3
```
