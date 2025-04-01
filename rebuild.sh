if [[ $1 == "--nc" ]]; then
    echo "Пересборка с использованием --no-cache..."
    docker compose down
    docker compose build --no-cache
    docker compose up
else
    echo "Пересборка без --no-cache..."
    docker compose down
    docker compose build
    docker compose up
fi
