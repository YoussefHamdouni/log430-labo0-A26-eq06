# Annexe 1 : commandes Docker utiles

```bash
# Construire l'image à partir du Dockerfile du répertoire courant
docker build -t log430-labo0:latest .

# Lister les images présentes sur votre machine
docker images

# Lister les conteneurs en cours d'exécution (ajoutez -a pour voir aussi les arrêtés)
docker ps

# Démarrer les services décrits dans docker-compose.yml
docker compose up -d

# Arrêter les services (ajoutez -v pour supprimer aussi les volumes)
docker compose down

# Ouvrir un terminal interactif dans un conteneur en cours d'exécution
docker compose exec calculator bash

# Voir les logs d'un service (-f pour suivre en continu)
docker compose logs -f calculator

# Supprimer une image locale
docker rmi log430-labo0:latest

# Faire le ménage : images, conteneurs et réseaux inutilisés
docker system prune
```

# Annexe 2 : commandes GitHub Container Registry (GHCR)

```bash
# S'authentifier au registre (le token doit avoir la portée write:packages)
echo <VOTRE_TOKEN> | docker login ghcr.io -u <votre-username> --password-stdin

# Construire une image en respectant la convention de nommage du registre
# ATTENTION : le nom doit être entièrement en minuscules
docker build -t ghcr.io/<votre-username>/log430-labo0:latest .

# Publier l'image
docker push ghcr.io/<votre-username>/log430-labo0:latest

# Récupérer l'image depuis le registre
docker pull ghcr.io/<votre-username>/log430-labo0:latest

# Ajouter une étiquette de version à une image existante
docker tag ghcr.io/<votre-username>/log430-labo0:latest ghcr.io/<votre-username>/log430-labo0:v1.0

# Se déconnecter du registre
docker logout ghcr.io
```

# Annexe 3 : observer les ressources

```bash
# Consommation CPU/RAM/réseau de tous les conteneurs, vue de l'hôte
docker stats

# Processus en cours à l'intérieur du conteneur
docker compose exec calculator top

# Utilisation de la RAM à l'intérieur du conteneur
docker compose exec calculator free -h

# Espace disque disponible
docker compose exec calculator df -h

# Détail des couches d'une image et de leur taille
docker image history log430-labo0:latest
```
