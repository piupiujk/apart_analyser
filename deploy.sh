#!/bin/bash

source .venv/.env || { echo "Ошибка: Не удалось загрузить .env файл"; exit 1; }

[ -z "$SSH_HOST" ] || [ -z "$SSH_USER" ] && {
  echo "Ошибка: SSH_HOST или SSH_USER не заданы в .env"
  exit 1
}

ssh -t "$SSH_USER@$SSH_HOST" "
cd ~/apart_analyser || { echo '❌ Ошибка: Директория apart_analyser не найдена'; exit 1; }

echo '🔄 Принудительная синхронизация с GitHub...'
git fetch --all
git reset --hard origin/main
git clean -fd

if tmux has-session -t apart_analyser 2>/dev/null; then
  tmux attach -t apart_analyser
  echo '♻️ Перезапускаем приложение (существующая tmux сессия)...'
  ./rebuild.sh
else
  echo '🚀 Запускаем новую сессию...'
  ./autostart.sh || { echo '❌ Ошибка при запуске autostart.sh'; exit 1; }
  tmux attach -t apart_analyser
fi

echo '✅ Основные команды выполнены!'
bash -l
"