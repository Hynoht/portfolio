#!/bin/bash

if [ ! -p /dev/stdin ]; then
    echo "Ce script doit être exécuté via 'curl -s URL | bash'"
    rm -- "$0"
    exit 1
fi

get_target_timestamp() {
    date -d "2025-09-24 10:00:00" +%s
}

get_current_timestamp() {
    date +%s
}

wait_until_target() {
    target_ts=$(get_target_timestamp)
    while true; do
        current_ts=$(get_current_timestamp)
        if [ $current_ts -ge $target_ts ]; then
            echo "C'est l'heure ! Clonage du repository..."
            clone_repository
            break
        fi
        sleep 60
        echo -n "."
    done
}

clone_repository() {
	git clone git@github.com:Hynoht/blind_42.git
    echo "Repository cloné avec succès !"
    exit 0
}

target_ts=$(get_target_timestamp)
current_ts=$(get_current_timestamp)

if [ $current_ts -lt $target_ts ]; then
    echo "Il n'est pas encore l'heure. La date cible est le 24 septembre 2025 à 10h00."
    echo "Que souhaitez-vous faire ?"
    echo "1) Attendre jusqu'à la date/heure exacte"
    echo "2) Quitter le script"
    read -p "Votre choix (1 ou 2): " choice < /dev/tty

    case $choice in
        1)
            echo "En attente de la date cible..."
            wait_until_target
            ;;
        2)
            echo "Au revoir !"
            exit 0
            ;;
        *)
            echo "Choix invalide. Au revoir !"
            exit 1
            ;;
    esac
else
    echo "La date cible est passée. Clonage du repository..."
    clone_repository
fi
