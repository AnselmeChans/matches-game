# Jeux des allumettes

### A Python game

#### Author: Hans CERIL

#### License: MIT


# overview
 On commence le jeu avec 13 allumettes et celui qui tire la dernière allumette
 a perdu

##   2 joueurs : Player Vs Computer

##   Plusieurs niveaux de jeux possibles :

      ```
      Naif  : Choisir au hasard le nombre d'allumettes qu'il prend

      Distrait : choisir au hasard le nombre d’allumettes entre 1 et 3, sans tenir
                compte de celles qui sont dans le tas

      Rapide : Prend systématiquement le plus grand nombre d’allumettes possible.

      Expert : Niveau où l’ordinateur joue du mieux possible.

      ```
# execute the game

go to src/ and then type python3 main_menu.py

#                       Début du jeu ==> Ordinateur sera l'arbitre :

##    -- Nom de l'utilisateur

##    -- Niveau de l'ordinateur : "n", "d", "r", "e"
###       En cas de réponse différente c'est le niveau expert qui sera choisit

##     -- Affiche le niveau choisit

##     -- Demande au joueur humain s’il veut commencer ou non.
###       Le joueur humain commence si et seulement s’il répond ’o’ ou ’O’.

##      -- Vérifie que les joueurs respectent les règles du jeu :
###          ** si un joueur essaie de tricher, son coup est annulé et il doit recommencer:
              ```
              ++ un joueur doit nécessairement retirer entre 1 et 3 allumettes
                   du tas quand c’est à son tour de jouer.
              ```

##      -- En fin de partie, l’ordinateur dit qui a gagné.

#                                 Affichage
  ```
   Avant de demander à un joueur combien il veut prendre d’allumettes, les allumettes
   restantes sont affichées à l’écran sous la forme de barres verticales (trois
   l’une sous l’autre pour représenter une allumette)
  ```
   ```
   Pour faciliter leur comptage, les allumettes sont groupées par cinq.
   L’exemple suivant spécifie l’interface avec l’utilisateur à respecter impérativement.
   ```

   ```

    ||||| ||||| |||
    ||||| ||||| |||

    ```
