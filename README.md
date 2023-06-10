# cv
visualiser ton cv en ligne

# pre-requis
vous devez savoir configurer les serveur suivants: 
- nginx
- uwsgi

## installation 
```
git clone https://github.com/makan-dianka/cv.git
cd cv
```

# création de .env
Pour laisser certains informations secretes comme la clé secrete de django, il faut les stocké dans les variables d'environnement. Pour cela créer un fichier ```.env``` et y mettre toutes les variables d'environnement.
Pour ce projet l'exemple sera 

```touch .env```

Mettre ces variables dans le .env

```
SECRET_KEY='votre cle secret de django ici'
DEBUG=0
ALLOWED_HOSTS="192.0.0.0,192.0.0.0" #vos adresse ip ou nom de domain ici separer par virgule ,
username='votre nom d'utilisateur de django admin'
```

# création d'environnement virtuel
Pour isoler les packages utilisé dans un projet django. Il faut les installer dans un environnement virtuel (c'est recommandé).
Pour créer un environnement virtuel taper ```python -m venv .venv```. Notre environnement virtuel est crééé et on l'a appelé ```.venv```  . Maintenant il faut l'activé pour installer les packages qui se trouver dans le fichier requirements.txt.
pour l'activé taper ```. .venv/bin/activate``` et pour y installer les packages dans le fichier ```requirements.txt``` taper
```
pip install --upgrade pip 
pip install -r requirements.txt
```

# uwsgi emperor
uwsgi emperor permet de redemarrer notre application en cas de panne, crash ou redemarrage de notre serveur ou pour même arreter et redemarrer votre application.
Pour le mettre en place, suivez les configurations suivantes.

Créer un dossier ```vassals``` dans votre dossier d'environnement virtuel

```mkdir .venv/vassals``` 
puis créer un lien symbolique vers le fichier uwsgi.ini avec cette commande (donner le chemin absolue au lieu de relatif)
```sudo ln -s uwsgi.ini .venv/vassals```


### créer le services emperor dans systemd
créer et ouvrir le fichier ```emperor.uwsgi.service```  dans le dossier ```/etc/systemd/system/``` puis ajouter les contenus suivants

```sudo vim /etc/systemd/system/emperor.uwsgi.service```

```
[Unit]
Description=uwsgi emperor for app website
After=network.target
[Service]
User=pydev #system user
Restart=always
ExecStart=/home/pydev/www/cv/.cv_env/bin/uwsgi --emperor /home/pydev/www/cv/.cv_env/vassals
[Install]
WantedBy=multi-user.target
```

### activer uwsgi emperor
```sudo systemctl enable emperor.uwsgi.service```

### demarrer, arreter ou redemarrer le service emperor
```
sudo systemctl start emperor.uwsgi.service
sudo systemctl stop emperor.uwsgi.service
sudo systemctl restart emperor.uwsgi.service
```

