#!/bin/bash

tmux new-session -d -s session
tmux split-window -h
tmux send-keys -t session:0.0 './server.py 2000 | mplayer -quiet -' C-m
tmux send-keys -t session:0.1 'sleep 2; ./client.py localhost 2000 < audio.mp3' C-m
tmux attach-session -t session
