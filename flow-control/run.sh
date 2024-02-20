#!/bin/bash

tmux new-session -d -s session
tmux split-window -h
tmux send-keys -t session:0.0 './server.py 2000' C-m
tmux send-keys -t session:0.1 'sleep 1; ./client.py localhost 2000' C-m
tmux attach-session -t session
