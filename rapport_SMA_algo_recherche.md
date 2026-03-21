Voici la version enrichie du mémoire avec, pour chaque algorithme, sa **présentation formelle** (pseudo-code, structure de données, complexité). J'ai conservé l'intégralité de votre texte original et ajouté les sections algorithmiques manquantes.

---

# Mémoire détaillé : Algorithmes de graphes et méthodes de recherche

# Introduction générale

L’algorithmique et la théorie des graphes occupent une place centrale dans les sciences informatiques modernes. Les graphes constituent un outil mathématique extrêmement puissant permettant de modéliser une grande variété de systèmes réels caractérisés par des relations entre entités. Ces relations peuvent représenter des routes entre villes, des connexions dans un réseau informatique, des interactions dans un réseau social ou encore des dépendances dans un système logiciel.

La capacité à analyser efficacement ces structures repose sur l’utilisation d’algorithmes spécialisés capables d’explorer, d’optimiser et de transformer ces graphes. Parmi ces algorithmes, on retrouve notamment les méthodes de parcours de graphes, les algorithmes de plus court chemin, ainsi que les techniques d’optimisation heuristique.

Dans ce mémoire, nous étudions en profondeur plusieurs concepts fondamentaux :

* la complexité algorithmique
* la recherche locale
* les parcours de graphes (BFS et DFS)
* les algorithmes de plus court chemin (Dijkstra et A*)
* les structures de représentation des graphes (matrice d’adjacence)
* les problèmes de coloration de graphes

Chaque section développe non seulement les principes théoriques, mais également les implications pratiques et les applications concrètes de ces méthodes dans les systèmes informatiques modernes.

---

# 1. Complexité algorithmique

## 1.1 Importance de l'analyse de complexité

Dans le domaine de l’informatique, un problème peut souvent être résolu par plusieurs algorithmes différents. Cependant, tous ces algorithmes ne présentent pas la même efficacité.

Par exemple, un algorithme qui fonctionne correctement sur une petite quantité de données peut devenir totalement inutilisable lorsque la taille de l’entrée augmente.

L’analyse de la complexité algorithmique permet de répondre à plusieurs questions fondamentales :

* Combien d’opérations un algorithme nécessite-t-il ?
* Comment ce nombre d’opérations évolue-t-il lorsque la taille de l’entrée augmente ?
* L’algorithme est-il scalable ?

Cette analyse constitue donc un outil indispensable pour la conception d’algorithmes efficaces.

---

## 1.2 Complexité temporelle

La complexité temporelle correspond au nombre d’opérations élémentaires exécutées par l’algorithme.

Prenons un exemple simple :

```
pour i = 1 à n
    afficher(i)
```

Nombre d’opérations ≈ n

Complexité :

O(n)

---

### Exemple plus complexe

```
pour i = 1 à n
    pour j = 1 à n
        afficher(i,j)
```

Nombre d’opérations :

n × n = n²

Complexité :

O(n²)

---

## 1.3 Complexité spatiale

La complexité spatiale correspond à la quantité de mémoire nécessaire pour exécuter l’algorithme.

Elle dépend notamment :

* des structures de données utilisées
* de la taille des variables
* de l’espace utilisé par les appels récursifs

---

# 2. Recherche locale

## 2.1 Principe général

La recherche locale constitue une approche heuristique permettant de résoudre des problèmes d’optimisation complexes.

Plutôt que d’explorer l’ensemble de l’espace des solutions — ce qui serait souvent impossible en pratique — la recherche locale consiste à améliorer progressivement une solution existante en explorant ses voisins.

---

## 2.2 Schéma conceptuel détaillé

```
              Solution initiale
                     |
                     v
           Evaluation de la solution
                     |
                     v
         Génération des solutions voisines
              /        |         \
             v         v          v
         Solution1  Solution2  Solution3
              |         |         |
              v         v         v
           Evaluation des solutions
                     |
                     v
           Choix de la meilleure solution
                     |
                     v
               Nouvelle solution
                     |
                     v
                Itération
```

## 2.3 Présentation formelle de l'algorithme de recherche locale (Hill Climbing)

```
Algorithme RechercheLocale (Problème P)
Entrée : Un problème d'optimisation P
Sortie : Une solution optimale locale S

Début
    S ← SolutionInitiale(P)
    Tant que (ConditionArrêt non satisfaite) Faire
        V ← GénérerVoisins(S)
        S' ← Meilleur(V)  // Solution voisine améliorant la fonction objectif
        Si f(S') ≥ f(S) Alors  // Pour un problème de maximisation
            S ← S'
        Sinon
            Sortir de la boucle
        Fin Si
    Fin Tant que
    Retourner S
Fin
```

**Structures de données utilisées :**
- Représentation de la solution (tableau, liste, graphe selon le problème)
- Fonction d'évaluation f(S)

**Complexité :**
- Temporelle : O(k × g) où k est le nombre d'itérations et g le coût de génération des voisins
- Spatiale : O(taille de la solution courante)

---

# 3. Parcours en largeur (BFS)

## 3.1 Principe théorique

Le parcours en largeur est un algorithme d’exploration systématique des graphes.

Son principe fondamental consiste à explorer les sommets selon leur distance au sommet initial.

Autrement dit, les sommets situés à une distance d’une arête sont visités avant ceux situés à deux arêtes.

---

## 3.2 Schéma de graphe détaillé

Considérons le graphe suivant :

```
            A
         /     \
        B       C
       / \     / \
      D   E   F   G
           \
            H
```

---

## 3.3 Ordre de parcours BFS

```
Niveau 0 : A

Niveau 1 : B C

Niveau 2 : D E F G

Niveau 3 : H
```

Ordre BFS :

A → B → C → D → E → F → G → H

---

## 3.4 Structure de données utilisée

BFS utilise une **file (queue)**.

Principe :

```
File :

[A]

on explore A
ajout B,C

[B,C]

on explore B
ajout D,E
```

## 3.5 Présentation formelle de l'algorithme BFS

```
Algorithme BFS (Graphe G, Sommet source s)
Entrée : Un graphe G = (S, A), un sommet de départ s ∈ S
Sortie : Marquage des sommets visités dans l'ordre BFS

Début
    Pour chaque sommet u ∈ S Faire
        visité[u] ← FAUX
        parent[u] ← NUL
    Fin Pour
    
    visité[s] ← VRAI
    File F ← Vide
    Enfiler(F, s)
    
    Tant que (F non vide) Faire
        u ← Défiler(F)
        Traiter(u)  // Action spécifique (affichage, calcul, etc.)
        
        Pour chaque voisin v de u dans G Faire
            Si visité[v] = FAUX Alors
                visité[v] ← VRAI
                parent[v] ← u
                Enfiler(F, v)
            Fin Si
        Fin Pour
    Fin Tant que
Fin
```

**Structures de données utilisées :**
- File (Queue) : implémentée par liste chaînée ou tableau circulaire
- Tableau visité[1..n] : booléen
- Tableau parent[1..n] : pour reconstruire les chemins

**Complexité :**
- Temporelle : O(|S| + |A|) où |S| est le nombre de sommets et |A| le nombre d'arêtes
- Spatiale : O(|S|)

---

# 4. Parcours en profondeur (DFS)

## 4.1 Principe

Le parcours en profondeur explore un graphe en suivant un chemin aussi loin que possible avant de revenir en arrière.

---

## 4.2 Schéma de graphe

```
           A
         /   \
        B     C
       / \
      D   E
```

---

## 4.3 Parcours possible

```
A → B → D
retour
B → E
retour
A → C
```

## 4.4 Présentation formelle de l'algorithme DFS (version itérative)

```
Algorithme DFS_Itératif (Graphe G, Sommet source s)
Entrée : Un graphe G = (S, A), un sommet de départ s ∈ S
Sortie : Marquage des sommets visités dans l'ordre DFS

Début
    Pour chaque sommet u ∈ S Faire
        visité[u] ← FAUX
    Fin Pour
    
    Pile P ← Vide
    Empiler(P, s)
    
    Tant que (P non vide) Faire
        u ← Dépiler(P)
        
        Si visité[u] = FAUX Alors
            visité[u] ← VRAI
            Traiter(u)
            
            // Empiler les voisins dans l'ordre inverse pour respecter l'ordre classique
            Pour chaque voisin v de u (dans l'ordre inverse) Faire
                Si visité[v] = FAUX Alors
                    Empiler(P, v)
                Fin Si
            Fin Pour
        Fin Si
    Fin Tant que
Fin
```

## 4.5 Présentation formelle de l'algorithme DFS (version récursive)

```
Algorithme DFS_Récursif (Graphe G, Sommet u)
Entrée : Un graphe G = (S, A), un sommet courant u
Sortie : Marquage des sommets visités (variable globale)

Début
    visité[u] ← VRAI
    Traiter(u)
    
    Pour chaque voisin v de u dans G Faire
        Si visité[v] = FAUX Alors
            DFS_Récursif(G, v)
        Fin Si
    Fin Pour
Fin
```

**Structures de données utilisées :**
- Pile (Stack) pour la version itérative
- Tableau visité[1..n]
- (Optionnel) Tableau des temps d'entrée/sortie pour analyse plus poussée

**Complexité :**
- Temporelle : O(|S| + |A|)
- Spatiale : O(|S|) (pile d'appel récursif ou pile explicite)

---

# 5. Algorithme de Dijkstra (explication complète)

## 5.1 Objectif

Trouver le plus court chemin depuis une source vers tous les autres sommets dans un graphe pondéré.

Condition :

les poids doivent être **positifs**.

---

# 5.2 Exemple de graphe

```
        (4)
   A -------- B
   | \        |
 (2)|  \1     |(5)
   |   \      |
   C----D-----E
      (8)  (2)
```

---

# 5.3 Étape 0 : initialisation

Source = A

Tableau des distances

```
Sommet   Distance
A        0
B        ∞
C        ∞
D        ∞
E        ∞
```

---

# 5.4 Étape 1

On explore A.

Voisins :

C = 2
D = 1
B = 4

```
Sommet   Distance
A        0
B        4
C        2
D        1
E        ∞
```

---

# 5.5 Étape 2

Sommet minimum non visité :

D = 1

Voisins :

E via D

distance :

1 + 2 = 3

```
Sommet   Distance
A        0
B        4
C        2
D        1
E        3
```

---

# 5.6 Étape 3

Sommet minimum :

C = 2

C → D = 8

mais :

2 + 8 > 1

pas d'amélioration.

---

# 5.7 Étape 4

Sommet minimum :

E = 3

E → B

3 + 5 = 8

mais B = 4 donc pas d’amélioration.

---

# 5.8 Résultat final

```
A = 0
D = 1
C = 2
E = 3
B = 4
```

## 5.9 Présentation formelle de l'algorithme de Dijkstra

```
Algorithme Dijkstra (Graphe G, Sommet source s)
Entrée : Un graphe pondéré G = (S, A, poids), une source s ∈ S
         (∀ (u,v) ∈ A, poids(u,v) ≥ 0)
Sortie : Distances minimales de s vers tous les sommets

Début
    // Initialisation
    Pour chaque sommet v ∈ S Faire
        dist[v] ← ∞
        parent[v] ← NUL
        visité[v] ← FAUX
    Fin Pour
    dist[s] ← 0
    
    // File de priorité (tas min) contenant (distance, sommet)
    FP ← FilePrioritéVide()
    Insérer(FP, (0, s))
    
    Tant que (FP non vide) Faire
        (d, u) ← ExtraireMin(FP)
        
        Si visité[u] = VRAI Alors
            Continuer  // Déjà traité via un meilleur chemin
        Fin Si
        
        visité[u] ← VRAI
        
        // Relaxation des arêtes sortantes
        Pour chaque voisin v de u tel que (u,v) ∈ A Faire
            nouvelle_distance ← dist[u] + poids(u,v)
            Si nouvelle_distance < dist[v] Alors
                dist[v] ← nouvelle_distance
                parent[v] ← u
                Insérer(FP, (nouvelle_distance, v))
            Fin Si
        Fin Pour
    Fin Tant que
    
    Retourner dist, parent
Fin
```

**Structures de données utilisées :**
- File de priorité (tas binaire, tas de Fibonacci)
- Tableaux dist[1..n], parent[1..n], visité[1..n]

**Complexité :**
- Avec tas binaire : O((|S| + |A|) log |S|)
- Avec tas de Fibonacci : O(|A| + |S| log |S|)
- Spatiale : O(|S|)

---

# 6. Algorithme A* (explication détaillée)

## 6.1 Principe

A* combine :

* coût réel
* estimation heuristique

Formule :

f(n) = g(n) + h(n)

---

## 6.2 Exemple de carte

```
   S ---- A ---- C
    \     |     /
     \    |    /
      B---D---G
```

S = départ
G = objectif

---

## 6.3 Valeurs heuristiques

```
Sommet    h(n)
S         7
A         6
B         4
C         2
D         1
G         0
```

---

# 6.4 Étape 1

OPEN = {S}

```
g(S) = 0
f(S) = 0 + 7 = 7
```

---

# 6.5 Étape 2

Explorer S

Voisins :

A

```
g(A) = 1
f(A) = 1 + 6 = 7
```

B

```
g(B) = 4
f(B) = 4 + 4 = 8
```

OPEN :

A,B

---

# 6.6 Étape 3

Choisir plus petit f :

A

Explorer A.

Voisins :

C

```
g(C) = 1 + 2 = 3
f(C) = 3 + 2 = 5
```

D

```
g(D) = 1 + 3 = 4
f(D) = 4 + 1 = 5
```

---

# 6.7 Étape 4

Choisir C

Explorer C.

Voisin :

G

```
g(G) = 3 + 2 = 5
f(G) = 5 + 0 = 5
```

---

# 6.8 Chemin final

```
S → A → C → G
```

## 6.9 Présentation formelle de l'algorithme A*

```
Algorithme A* (Graphe G, Sommet source s, Sommet but t)
Entrée : Un graphe G = (S, A, poids), source s, but t,
         une fonction heuristique h: S → ℝ (estimée, consistante)
Sortie : Plus court chemin de s à t (ou échec)

Début
    // Ensembles OPEN et CLOSED
    OPEN ← EnsemblePrioritéVide()  // Trié par f
    CLOSED ← EnsembleVide()
    
    // Initialisation
    g[s] ← 0
    f[s] ← h(s)
    parent[s] ← NUL
    Ajouter(OPEN, s)
    
    Tant que (OPEN non vide) Faire
        // Choisir le nœud avec le plus petit f
        n ← ExtraireMin(OPEN)
        
        Si n = t Alors
            Retourner ReconstruireChemin(parent, s, t)
        Fin Si
        
        Ajouter(CLOSED, n)
        
        Pour chaque successeur m de n dans G Faire
            Si m ∈ CLOSED Alors
                Continuer  // Déjà exploré
            Fin Si
            
            g_tentative ← g[n] + poids(n, m)
            
            Si m ∉ OPEN Alors
                // Premier passage
                parent[m] ← n
                g[m] ← g_tentative
                f[m] ← g[m] + h(m)
                Ajouter(OPEN, m)
            Sinon Si g_tentative < g[m] Alors
                // Meilleur chemin trouvé
                parent[m] ← n
                g[m] ← g_tentative
                f[m] ← g[m] + h(m)
                MettreÀJour(OPEN, m)  // Re-trier si nécessaire
            Fin Si
        Fin Pour
    Fin Tant que
    
    Retourner Échec  // Aucun chemin trouvé
Fin
```

**Structures de données utilisées :**
- File de priorité pour OPEN (triée par f)
- Ensemble (hash set) pour CLOSED
- Tables de hachage pour g, f, parent

**Complexité :**
- Temporelle : O(b^d) dans le pire cas, mais bien meilleure en pratique avec une bonne heuristique (b = facteur de branchement, d = profondeur)
- Spatiale : O(nombre de nœuds explorés)

**Propriété :** Si l'heuristique h est admissible (ne surestime jamais le coût réel) et consistante, A* est optimal et complet.

---

# 7. Matrice d’adjacence

## 7.1 Définition

Une matrice d’adjacence est une matrice carrée représentant les relations entre les sommets d’un graphe.

---

## 7.2 Exemple

Graphe :

```
A → B
A → C
B → D
C → D
```

Matrice :

```
    A B C D
A [ 0 1 1 0 ]
B [ 0 0 0 1 ]
C [ 0 0 0 1 ]
D [ 0 0 0 0 ]
```

## 7.3 Présentation formelle

```
Définition : Soit G = (S, A) un graphe avec S = {1, 2, ..., n}.
La matrice d'adjacence M est une matrice carrée n × n telle que :

M[i][j] = 1 si (i, j) ∈ A (arête ou arc de i vers j)
M[i][j] = 0 sinon

Pour un graphe pondéré, on stocke le poids :
M[i][j] = poids(i, j) si (i, j) ∈ A
M[i][j] = ∞ (ou 0) sinon
```

**Complexité :**
- Espace : O(n²)
- Accès à une arête : O(1)
- Parcours des voisins d'un sommet : O(n)

---

# 8. Coloration des sommets

## 8.1 Définition

La coloration des sommets consiste à attribuer une couleur à chaque sommet de manière à ce que deux sommets adjacents aient des couleurs différentes.

---

## 8.2 Exemple détaillé

Graphe :

```
       A
     /   \
    B     C
     \   /
       D
```

Coloration possible :

```
A = rouge
B = bleu
C = bleu
D = vert
```

## 8.3 Présentation formelle (algorithme glouton)

```
Algorithme ColorationGloutonne (Graphe G)
Entrée : Un graphe G = (S, A) non orienté
Sortie : Une coloration des sommets (pas nécessairement optimale)

Début
    // Initialisation : aucune couleur attribuée
    Pour chaque sommet v ∈ S Faire
        couleur[v] ← -1
    Fin Pour
    
    // Parcourir les sommets dans un ordre donné
    Pour chaque sommet v ∈ S (dans l'ordre choisi) Faire
        // Marquer les couleurs interdites
        Pour chaque couleur c dans [0, |S|-1] Faire
            utilisé[c] ← FAUX
        Fin Pour
        
        Pour chaque voisin u de v Faire
            Si couleur[u] ≠ -1 Alors
                utilisé[couleur[u]] ← VRAI
            Fin Si
        Fin Pour
        
        // Choisir la plus petite couleur disponible
        c ← 0
        Tant que utilisé[c] = VRAI Faire
            c ← c + 1
        Fin Tant que
        
        couleur[v] ← c
    Fin Pour
    
    Retourner couleur
Fin
```

**Structures de données utilisées :**
- Tableau couleur[1..n]
- Tableau temporaire utilisé[1..n] pour les couleurs interdites

**Complexité :**
- Temporelle : O(|S|²) dans le pire cas (si le graphe est dense)
- Spatiale : O(|S|)

**Propriété :** Cet algorithme glouton utilise au plus Δ+1 couleurs, où Δ est le degré maximum du graphe. Il ne garantit pas le nombre chromatique optimal (problème NP-difficile).

---

# Conclusion générale

L’étude des algorithmes de graphes constitue une composante essentielle de l’informatique moderne. Les méthodes présentées dans ce mémoire illustrent différentes approches permettant de résoudre efficacement des problèmes complexes de recherche, d’optimisation et de modélisation de réseaux.

Les algorithmes tels que BFS, DFS, Dijkstra ou A* jouent aujourd’hui un rôle central dans de nombreuses applications technologiques, notamment dans les systèmes de navigation, les réseaux de communication, l’intelligence artificielle et les systèmes distribués.

La maîtrise de ces techniques permet non seulement de comprendre les mécanismes fondamentaux de l’exploration de graphes, mais également de concevoir des solutions efficaces pour une grande variété de problèmes computationnels.

