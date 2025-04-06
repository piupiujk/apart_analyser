#!/bin/bash

source .venv/.env || { echo "Ошибка: Не удалось загрузить .env файл"; exit 1; }

if [ -z "$SSH_HOST" ] || [ -z "$SSH_USER" ]; then
  echo "Ошибка: SSH_HOST или SSH_USER не заданы в .env"
  exit 1
fi

ssh -t "$SSH_USER@$SSH_HOST" "
cd ~/apart_analyser || { echo '❌ Ошибка: Директория apart_analyser не найдена'; exit 1; }

echo '🔄 Принудительная синхронизация с GitHub...'
git fetch --all
git reset --hard origin/main
git clean -fd
docker compose down
tmux kill-session -t apart_analyser 2>/dev/null
./autostart.sh
"