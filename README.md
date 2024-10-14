------------------------------
# 1 - Explication:
------------------------------

### **Démonstration avec un seul alpha (α = 0.5)**

---

Ce code est une démonstration d'un agent Q-Learning qui apprend à résoudre l'environnement **MountainCar-v0** en utilisant **une seule valeur de paramètre alpha (α)**, ici **α = 0.5**. L'agent est formé pendant 2000 épisodes, et ensuite évalué sur 10 essais.

#### 💡 **Alpha (α = 0.5)**

---

### **Explication du code :**

1. **Environnement de simulation :**  
   L'environnement **MountainCar-v0** de **OpenAI Gym** est utilisé. Dans cet environnement, une voiture doit apprendre à gravir une colline en prenant de l'élan.

2. **Agent Q-Learning (avec α = 0.5) :**  
   - L'agent Q-Learning est créé avec un taux d'apprentissage (alpha) de **0.5**.  
   - L'agent apprend à sélectionner des actions optimales pour maximiser ses récompenses. 
   - La table Q est mise à jour en fonction des récompenses reçues après chaque action.

3. **Phases du programme :**

   - **Phase d'apprentissage :**  
     L'agent s'entraîne pendant **2000 épisodes**. Pendant cette phase, il explore différentes actions pour apprendre à maîtriser l'environnement.
   
   - **Phase d'évaluation :**  
     Après l'apprentissage, l'agent est évalué sur **10 essais**. Pendant chaque essai, vous verrez la voiture se déplacer en temps réel dans une fenêtre **gym**. L'objectif de l'agent est de monter la colline en **moins de 200 pas de temps**.
   
   - **Suivi des résultats :**  
     Pour chaque essai, le nombre de **pas de temps** est enregistré, ainsi que le **succès** ou l'**échec** de l'agent (réussir à monter la colline en moins de 200 pas). Les résultats sont affichés à la fin sous forme de graphiques.

4. **Affichage des résultats :**
   - **Graphique des succès/échecs** : Un graphique montre si l'agent a réussi ou échoué pour chaque essai.
   - **Graphique du nombre de pas** : Un autre graphique montre le nombre de pas nécessaires pour chaque essai.
   - **Statistiques globales** : Le taux de succès, la moyenne et la médiane des pas sont calculés et affichés en bas des graphiques.

### **Détails des paramètres :**
- **Episodes d'entraînement :** 2000
- **Nombre d'actions possibles :** 3 (aller à gauche, ne rien faire, aller à droite)
- **Nombre d'essais d'évaluation :** 10
- **Alpha (lr - taux d'apprentissage) :** 0.5

### **Ce que vous verrez dans ce code :**
- Pendant la phase d'évaluation, la voiture se déplacera en **temps réel** dans l'environnement **MountainCar-v0** pendant que l'agent essaie d'appliquer ce qu'il a appris. Après chaque essai, les performances de l'agent sont collectées, et vous verrez :
  - **Un graphique des succès et échecs** (l'agent a-t-il réussi ou échoué à chaque essai ?).
  - **Un graphique du nombre de pas nécessaires** pour chaque essai.

### **Exécution finale :**
- À la fin des essais, vous obtiendrez un résumé des performances de l'agent avec un taux de succès et des statistiques de pas de temps.

---

💡 **Conclusion** : Ce code est une démonstration simple avec un seul **alpha**. Il montre comment un agent peut apprendre et appliquer les concepts de **Q-Learning** pour résoudre un problème de type **MountainCar** en ajustant un seul paramètre clé, le **taux d'apprentissage (alpha)**.



------------------------------
# 2 - Démonstration
------------------------------

```
git clone https://github.com/hrhouma/RLCode2-1.git
cd RLCode2-1
python3 -m venv mountain_car_env (ici python3 et non python)
mountain_car_env\Scripts\activate
python nom_du_script.py  (Ici python et non python3)
pip install -r requirements.txt
python main.py
deactivate
```


# 1. Cloner le projet

Commencez par cloner le projet depuis le dépôt GitHub :

```bash
git clone https://github.com/hrhouma/RLCode2.git
```

Accédez au dossier du projet :

```bash
cd RLCode2
code .
```

# 2. Création de l'environnement virtuel

Créez un environnement virtuel nommé `mountain_car_env` :

```bash
python3 -m venv mountain_car_env
```

# 3. Activation de l'environnement virtuel

Activez l'environnement :

- Sur macOS et Linux :
  ```bash
  source mountain_car_env/bin/activate
  ```

- Sur Windows :
  ```bash
  mountain_car_env\Scripts\activate
  ```

# 4. Installation des dépendances

Installez les packages nécessaires :

```bash
pip install -r requirements.txt
```

# 5. Structure du projet

Le projet est déjà organisé dans le dépôt que vous avez cloné. Il comprend les fichiers suivants :

- `helpers.py`
- `QLearning.py`
- `main.py`

# 6. Exécution du projet

Avec l'environnement virtuel activé, exécutez le fichier `main.py` pour lancer le projet :

```bash
python main.py
```

# 7. Désactivation de l'environnement virtuel

Une fois que vous avez terminé, vous pouvez désactiver l'environnement avec la commande suivante :

```bash
deactivate
```

---------------------------
# 3 - Annexe :
---------------------------



## 1. Création de l'environnement virtuel

Ouvrez un terminal et naviguez vers le dossier de votre projet. Créez un environnement virtuel nommé "mountain_car_env" :

```bash
python3 -m venv mountain_car_env
```

## 2. Activation de l'environnement virtuel

Activez l'environnement :

- Sur macOS et Linux :
```bash
source mountain_car_env/bin/activate
```

- Sur Windows :
```bash
mountain_car_env\Scripts\activate
```

## 3. Installation des dépendances

Installez les packages nécessaires :

```bash
pip install numpy pandas gym
```

## 4. Création du fichier requirements.txt

Créez un fichier `requirements.txt` à la racine de votre projet avec le contenu suivant :

```
numpy==1.23.5
pygame
pandas
gym
matplotlib
```

Alternativement, vous pouvez générer ce fichier automatiquement :

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

## 5. Structure du projet

Organisez votre projet avec trois fichiers Python :

- `helpers.py`
- `QLearning.py`
- `main.py`


## 6. Exécution du projet

Dans le terminal, avec l'environnement virtuel activé, exécutez :

```bash
python main.py
```

## 7. Désactivation de l'environnement virtuel

Une fois terminé, désactivez l'environnement :

```bash
deactivate
```

## 8. Partage du projet

Pour partager ou reproduire l'environnement sur un autre système :

1. Incluez le fichier `requirements.txt` dans votre projet.
2. L'autre personne peut créer un nouvel environnement virtuel et installer les dépendances avec :

```bash
python3 -m venv mountain_car_env
source mountain_car_env/bin/activate  # ou mountain_car_env\Scripts\activate sur Windows
pip install -r requirements.txt
```

En suivant ces étapes, vous aurez un projet bien structuré, utilisant un environnement virtuel, avec toutes les corrections nécessaires pour faire fonctionner le code de l'agent Q-Learning pour le problème Mountain Car.

----------------------------
# Annexe 
----------------------------

- Le code que vous avez ci-haut met en œuvre un **agent d'apprentissage par renforcement basé sur le Q-Learning** pour résoudre le problème **MountainCar-v0** proposé par OpenAI Gym. 
- Je vous propose une description étape par étape de ce que fait le code et ce que vous verrez en l'exécutant :

### 1. **Problème à résoudre : MountainCar-v0**
Le problème **MountainCar** est un environnement classique où une voiture doit atteindre le sommet d'une colline. Cependant, la voiture n'a pas assez de puissance pour monter directement la pente, donc elle doit d'abord reculer pour prendre de l'élan avant d'avancer.

- **Objectif** : Amener la voiture au sommet de la colline.
- **Actions possibles** : La voiture peut aller à gauche, ne rien faire (aucune poussée), ou aller à droite.
- **États** : Chaque état correspond à la position et à la vitesse de la voiture.

### 2. **Composants clés du code :**

#### a) **QLearning.py :** Implémente l'agent Q-Learning
- **Classe QLAgent** : Représente l'agent de Q-Learning, qui apprend les actions optimales à prendre dans chaque état. Il utilise une **table de Q-valeurs** pour stocker les valeurs de récompense pour chaque paire (état, action).
  - **Méthodes principales :**
    - `act(state, episode)` : Choisit l'action optimale à partir de l'état actuel.
    - `updateQ(s, a, r, s_dash)` : Met à jour la table de Q-valeurs après chaque action.
    - `learn(episodes)` : Entraîne l'agent sur un certain nombre d'épisodes.
  
#### b) **helpers.py :** Gère la discrétisation des états continus
- Les états du problème MountainCar (position et vitesse) sont continus. Ce fichier contient des fonctions pour transformer ces états continus en états discrets, ce qui permet à l'algorithme de Q-Learning de les manipuler.
  - `discretize(state)` : Prend un état continu (position, vitesse) et le transforme en un numéro d'état discret.

#### c) **main.py :** Entraîne et évalue l'agent Q-Learning
- **Entraînement** : L'agent est entraîné pendant 2000 épisodes sur l'environnement **MountainCar-v0**. Pendant chaque épisode, il choisit des actions, met à jour ses Q-valeurs et tente de résoudre le problème en atteignant le sommet de la colline.
- **Évaluation** : Après l'entraînement, l'agent est évalué sur 10 essais pour voir combien de fois il réussit à atteindre le sommet dans moins de 200 pas de temps.

#### d) **requirements.txt :** Contient les dépendances nécessaires pour exécuter le projet
- Ce fichier liste les bibliothèques Python requises : `numpy`, `gym`, `pandas`, `matplotlib`, etc.

### 3. **Ce que vous allez voir en l'exécutant :**

- **Visualisation graphique** : Lorsque vous exécuterez le projet, vous verrez une fenêtre graphique montrant l'environnement **MountainCar-v0**, où une voiture essaie de monter une colline en oscillant d'avant en arrière.
  - Pendant l'entraînement, l'environnement n'est pas affiché, mais lors des essais d'évaluation, vous verrez la voiture essayer de grimper la colline en se balançant.

- **Statistiques finales** :
  - Vous verrez un graphique avec deux sous-graphiques :
    1. **Succès/Échecs des essais** : Chaque point indique si l'agent a réussi (1) ou échoué (0) à atteindre le sommet lors de chaque essai d'évaluation.
    2. **Nombre de pas de temps par essai** : Le nombre de pas de temps nécessaires pour terminer chaque essai (plus le nombre est petit, plus l'agent est performant).
  - Un texte montrera également les statistiques globales, comme le taux de succès et la moyenne des pas de temps.

### 4. **Résultats attendus :**
- Si l'agent apprend correctement, vous verrez un **taux de succès** élevé lors des essais d'évaluation après l'entraînement.
- Vous devriez également voir une **réduction progressive** du nombre de pas de temps nécessaires pour atteindre le sommet, indiquant que l'agent apprend à résoudre le problème plus efficacement.

### 5. **Détails supplémentaires :**
- **Exploration vs Exploitation** : Au début de l'entraînement, l'agent ajoutera du bruit à ses décisions pour explorer différentes actions. À mesure que l'entraînement progresse, il deviendra plus sûr de ses décisions et explorera moins.
  
- **Utilisation d'un environnement virtuel** : Le fichier `requirements.txt` vous permet d'installer facilement les dépendances nécessaires dans un environnement virtuel, pour assurer une exécution sans conflit de bibliothèques.

En résumé, ce code met en œuvre un agent Q-Learning pour résoudre le problème MountainCar, avec des visualisations à la fin pour évaluer ses performances.
