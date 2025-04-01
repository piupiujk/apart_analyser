#!/bin/bash

if ! tmux has-session -t apart_analyser 2>/dev/null; then
  tmux new-session -d -s apart_analyser
  tmux send-keys -t apart_analyser 'cd apart_analyser' C-m
  tmux send-keys -t apart_analyser './rebuild.sh' C-m
fi
