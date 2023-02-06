# OCP9: LITreview

Application de critique de livre en ligne.

## Fonctionnalités

* se connecter et s’inscrire – le site ne doit pas être accessible à un utilisateur non connecté
* consulter un flux contenant les derniers tickets et les commentaires des utilisateurs qu'il suit, classés par ordre chronologique, les plus récents en premier ; 
* créer de nouveaux tickets pour demander une critique sur un livre/article ;
* créer des critiques en réponse à des tickets ;
* créer des critiques qui ne sont pas en réponse à un ticket. Dans le cadre d'un processus en une étape, 
* l'utilisateur créera un ticket puis un commentaire en réponse à son propre ticket ;
* voir, modifier et supprimer ses propres tickets et commentaires ; 
* suivre les autres utilisateurs en entrant leur nom d'utilisateur ;
* voir qui il suit et suivre qui il veut ;
* cesser de suivre un utilisateur. 


## Installation & lancement

Récupérez le dépôt localement
```
git clone https://github.com/nopalpite/OCP9.git
```
Placez vous dans le dossier OCP9, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Installez ensuite les packages requis:
```
pip install -r requirements.txt
```
Ensuite, placez vous dans le sous-dossier LITreview et lancez les commandes suivantes:
```
python manage.py makemigrations
```
Puis: 
```
python manage.py migrate
```
Lancez le serveur: 
```
python manage.py runserver
```
Connectez vous à l'adresse suivante dans un navigateur: http://localhost:8000

## paramètre de tests

Pour les besoins de tests, 4 utilisateurs sont déjà présent dans la base de données ainsi que des ticket et des critiques pré-rédigées:

| utilisateur   | Mot de passe  |
| ------------- | ------------- |
| user1         | UserPassword! |
| user2         | UserPassword! |
| user3         | UserPassword! |
| user4         | UserPassword! |

Vous pouvez également accéder à l'interface d'administration à l'adresse suivante : 
http://localhost:8000/admin

login: admin/mdp: admin (A changer impérativement pour sécuriser l'application)