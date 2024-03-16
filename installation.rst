Installation
============

Clonage du dépôt
----------------

Clonez le dépôt de code avec la commande suivante :

.. code-block:: bash

   git clone https://github.com/AlexianeBA/Python-OC-Lettings-FR

.. note::

   Vous pouvez également télécharger le code en tant qu'archive zip.

Navigation vers le répertoire du projet
---------------------------------------

Depuis un terminal, naviguez vers la racine du répertoire `Python-OC-Lettings-FR` avec la commande suivante :

.. code-block:: bash

   cd python-oc-lettings-fr

Création de l'environnement virtuel
----------------------------------

Créez un environnement virtuel pour le projet avec la commande suivante :

.. code-block:: bash

   # Windows
   python -m venv env

   # MacOS ou Linux
   python3 -m venv env

Activation de l'environnement virtuel
-------------------------------------

Activez l'environnement virtuel avec la commande suivante :

.. code-block:: bash

   # Windows
   env\Scripts\activate

   # MacOS ou Linux
   source env/bin/activate

Installation des dépendances
----------------------------

Installez les dépendances du projet avec la commande suivante :

.. code-block:: bash

   pip install -r requirements.txt