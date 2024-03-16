Déploiement
===========

Le déploiement de l'application est automatisé avec CircleCI et Azure Web App. Le fichier `config.yml` dans le répertoire `.circleci` définit les étapes de déploiement.

Création d'une application sur Azure Web App
--------------------------------------------

1. Connectez-vous à Azure avec votre compte.
2. Naviguez vers "App Services".
3. Cliquez sur "Add" pour créer une nouvelle application.
4. Remplissez les détails de l'application, y compris le nom, l'abonnement, le groupe de ressources, le plan de service et le runtime stack.
5. Cliquez sur "Review + create" pour créer l'application.

Configuration de CircleCI
-------------------------

1. Connectez-vous à CircleCI avec votre compte GitHub.
2. Ajoutez votre projet à CircleCI.
3. Configurez les variables d'environnement suivantes dans les paramètres du projet CircleCI :

   - `DOCKERHUB_USERNAME` : Votre nom d'utilisateur DockerHub.
   - `DOCKERHUB_PASSWORD` : Votre mot de passe DockerHub.
   - `DOCKERHUB_REPO` : Le nom du dépôt DockerHub où l'image Docker de l'application sera poussée.

Processus de déploiement
------------------------

Le déploiement se fait en plusieurs étapes :

1. **Setup** : Cette étape prépare l'environnement de déploiement. Elle se connecte à DockerHub en utilisant les identifiants fournis.

2. **Build** : Cette étape est actuellement configurée pour afficher le message "this is the build job". Vous pouvez la modifier pour construire votre application si nécessaire.

3. **Build Docker and Push** : Cette étape construit une image Docker de l'application et la pousse à DockerHub. Elle supprime d'abord l'ancienne image Docker, si elle existe. Ensuite, elle construit une nouvelle image Docker avec le SHA du commit actuel comme tag. Enfin, elle pousse l'image Docker au dépôt DockerHub configuré.

4. **Push to Azure Container Registry** : Cette étape pousse l'image Docker à Azure Container Registry. Vous devez configurer CircleCI pour se connecter à Azure Container Registry en utilisant les identifiants fournis lors de la création du registre.

5. **Déploiement sur Azure Web App** : Une fois l'image Docker poussée à Azure Container Registry, Azure Web App la récupère et déploie l'application sur votre serveur Azure.

Workflow
--------

Le workflow `build_and_test` est configuré pour exécuter les jobs `setup`, `build`, `build-docker-push`, `push-to-azure-container-registry` et `deploy-to-azure-web-app` dans cet ordre.