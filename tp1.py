

# modele tableau
# Numéro | Description            | Entrée | Résultat attendu | Résultat obtenu | Réussi?
# -------+------------------------+--------+------------------+-----------------+--------
#        |                        |        |                  |                 | 
#        |                        |        |                  |                 | 
#        |                        |        |                  |                 | 






import random
import time

SCORE_CIBLE: int = 11
LIMITE_CROUPIER: int = 9
MISE: int = 5
ARGENT_DEPART: int = 15
ARGENT_OBJECTIF: int = 30
DELAI_CROUPIER: float = 0.2

ANSI_RESET: str = "\u001B[0m"
ANSI_RED: str = "\u001B[31m"
ANSI_BLUE: str = "\u001B[34m"
ANSI_GREEN: str = "\u001B[32m"


def afficherRegles() -> None:
    """Affiche les règles du jeu au début d'une partie."""
    print("\n=== Bienvenue au blackjack des dés! ===")
    print(f"Le but : obtenir un score le plus près possible de {SCORE_CIBLE}, sans le dépasser.")
    print(f"Le croupier lance tant que son score est inférieur à {LIMITE_CROUPIER}.")
    print(f"Vous commencez avec {ARGENT_DEPART}$ et misez {MISE}$ à chaque manche.")
    print(f"La partie se termine si vous atteignez 0$ ou {ARGENT_OBJECTIF}$.")


def correcteur(texte: str) -> str:
    """Retourne le texte saisi en minuscules et sans espaces autour.

    Args:
        texte: le texte saisi par l'utilisateur
    Returns:
        le texte corrigé
    """
    return texte.strip().lower()

# Tests :
# Numéro | Description            | Entrée | Résultat attendu | Résultat obtenu | Réussi?
# -------+------------------------+--------+------------------+-----------------+--------
# 1      | Majuscule avec espaces | ' R '  | 'r'              | 'r'             | Oui
# 2      | Majuscule seule        | 'O'    | 'o'              | 'o'             | Oui
# 3      | Chaîne vide            | ''     | ''               | ''              | Oui


def lancerDe() -> int:
    """Retourne un nombre aléatoire entre 1 et 6 inclus."""
    return random.randint(1, 6)

# Tests :
# Numéro | Description                              | Entrée        | Résultat attendu | Résultat obtenu  | Réussi?
# -------+------------------------------------------+---------------+------------------+------------------+--------
# 1      | tester pour verifier si valeur aléatoire | enter         | 1, 2, 3, 4, 5, 6 | 1                | Oui
# 2      | tester pour verifier si valeur aléatoire | enter         | 1, 2, 3, 4, 5, 6 | 6                | Oui
# 3      | tester pour verifier si valeur aléatoire | enter         | 1, 2, 3, 4, 5, 6 | 3                | Oui


def aDepasse(score: int) -> bool:
    """Indique si un score dépasse le score cible.

    Args:
        score: le score à vérifier
    Returns:
        True si le score dépasse 11, False sinon
    """
    return score > SCORE_CIBLE

# Tests :
# Numéro | Description              | Entrée | Résultat attendu | Résultat obtenu | Réussi?
# -------+--------------------------+--------+------------------+-----------------+--------
# 1      | Sous le seuil            | 10     | False            | False           | Oui
# 2      | Exactement le seuil      | 11     | False            | False           | Oui
# 3      | Juste au-dessus du seuil | 12     | True             | True            | Oui


def validerActionJoueur() -> str:
    """Demande au joueur de lancer (Entrée) ou de rester (r ou R), redemande si invalide.

    Returns:
        "" pour lancer le dé, "r" pour rester
    """
    action: str = correcteur(input("Lancer le dé (Entrée) ou rester (r) ? "))
    while action != "" and action != "r":
        print("Saisie invalide. Appuyez sur Entrée sans rien taper pour lancer, ou tapez r pour rester.")
        action = correcteur(input("Lancer le dé (Entrée) ou rester (r) ? "))
    return action

# Tests :
# Numéro | Description                  | Entrée             | Résultat attendu  | Résultat obtenu   | Réussi?
# -------+------------------------------+--------------------+-------------------+-------------------+--------
# 1      | Lancer                       | Entrée             | ""                | ""                | Oui
# 2      | Rester (minuscule)           | "r"                | "r"               | "r"               | Oui
# 3      | Rester (majuscule)           | "R"                | "r"               | "r"               | Oui
# 4      | Rester avec espaces          | " r "              | "r"               | "r"               | Oui
# 5      | Saisie invalide, puis Entrée | "allo" puis Entrée | 1 erreur, puis "" | 1 erreur, puis "" | Oui


def tourTermine(action: str) -> bool:
    """Indique si le joueur a décidé de rester.

    Args:
        action: l'action validée du joueur
    Returns:
        True si le joueur reste, False s'il lance
    """
    return action == "r"

# Tests :
# Numéro | Description     | Entrée | Résultat attendu | Résultat obtenu | Réussi?
# -------+-----------------+--------+------------------+-----------------+--------
# 1      | Le joueur reste | "r"    | True             | True            | Oui
# 2      | Le joueur lance | ""     | False            | False           | Oui


def tourJoueur() -> int:
    """Gère le tour complet du joueur, jusqu'à ce qu'il reste ou dépasse 11.

    Returns:
        le score final du joueur
    """
    score: int = 0
    termine: bool = False

    print(f"Votre score: {score}")
    while not termine:
        action: str = validerActionJoueur()
        if tourTermine(action):
            print(f"Vous restez à {score}.")
            termine = True
        else:
            de: int = lancerDe()
            score += de
            print(f"Vous avez lancé un {de}.")
            print(f"Votre score: {score}")
            if aDepasse(score):
                print(f"{ANSI_RED}Vous avez dépassé {SCORE_CIBLE}!{ANSI_RESET}")
                termine = True
    return score

# Tests :
# Numéro | Description                     | Entrée                               | Résultat attendu | Résultat obtenu | Réussi?
# -------+---------------------------------+--------------------------------------+------------------+-----------------+--------
# 1      | Deux lancers puis rester        | Entrée, Entrée, r (dés 3, 4)         | 7 (3 saisies)    | 7 (3 saisies)   | Oui
# 2      | Rester dès le début             | r                                    | 0 (1 saisie)     | 0 (1 saisie)    | Oui
# 3      | Exemple de l'énoncé             | Entrée, Entrée, r (dés 5, 6)         | 11 (3 saisies)   | 11 (3 saisies)  | Oui
# 4      | Dépassement : arrêt automatique | Entrée, Entrée, Entrée (dés 6, 5, 2) | 13 (3 saisies)   | 13 (3 saisies)  | Oui


def tourCroupier() -> int:
    """Fait lancer le croupier tant que son score est inférieur à 9 et affiche chaque lancer.

    Returns:
        le score final du croupier
    """
    scoreCroupier: int = 0

    print("\nTour du croupier...")
    while scoreCroupier < LIMITE_CROUPIER:
        deCroupier: int = lancerDe()
        scoreCroupier += deCroupier
        time.sleep(DELAI_CROUPIER)
        print(f"Le croupier a lancé un {deCroupier}. Score du croupier: {scoreCroupier}")
        time.sleep(DELAI_CROUPIER)
    print("Le croupier s'arrête.")

    return scoreCroupier

# Tests :
# Numéro | Description            | Entrée      | Résultat attendu | Résultat obtenu | Réussi?
# -------+------------------------+-------------+------------------+-----------------+--------
# 1      | Arrêt au-dessus de 9   | dés 4, 6    | 10 (2 lancers)   | 10 (2 lancers)  | Oui
# 2      | Arrêt exactement à 9   | dés 3, 5, 1 | 9 (3 lancers)    | 9 (3 lancers)   | Oui
# 3      | Le croupier dépasse 11 | dés 6, 6    | 12 (2 lancers)   | 12 (2 lancers)  | Oui


def determinerResultat(score: int, scoreCroupier: int) -> int:
    """Détermine le résultat de la manche du point de vue du joueur.

    Args:
        score: le score final du joueur
        scoreCroupier: le score final du croupier
    Returns:
        1 si le joueur gagne, -1 s'il perd, 0 en cas d'égalité
    """
    if aDepasse(score):
        resultat: int = -1
    elif aDepasse(scoreCroupier):
        resultat = 1
    elif score > scoreCroupier:
        resultat = 1
    elif score < scoreCroupier:
        resultat = -1
    else:
        resultat = 0
    return resultat

# Tests :
# Numéro | Description         | Entrée | Résultat attendu | Résultat obtenu | Réussi?
# -------+---------------------+--------+------------------+-----------------+--------
# 1      | Victoire normale    | 11, 9  | 1                | 1               | Oui
# 2      | Le croupier dépasse | 9, 12  | 1                | 1               | Oui
# 3      | Défaite normale     | 8, 10  | -1               | -1              | Oui
# 4      | Le joueur dépasse   | 12, 0  | -1               | -1              | Oui
# 5      | Égalité             | 10, 10 | 0                | 0               | Oui


def afficherResultatManche(score: int, scoreCroupier: int, mise: int) -> None:
    """Affiche les scores finaux et le résultat de la manche avec la bonne couleur.

    Args:
        score: le score final du joueur
        scoreCroupier: le score final du croupier (ignoré si le joueur a dépassé)
        mise: le montant misé
    """
    if aDepasse(score):
        print(f"\nVotre score: {score} | Score du croupier: -")
    else:
        print(f"\nVotre score: {score} | Score du croupier: {scoreCroupier}")

    match determinerResultat(score, scoreCroupier):
        case 1:
            if aDepasse(scoreCroupier):
                print(f"{ANSI_BLUE}Le croupier a dépassé {SCORE_CIBLE}! Vous gagnez la manche. (+{mise}$){ANSI_RESET}")
            else:
                print(f"{ANSI_BLUE}Vous gagnez la manche! (+{mise}$){ANSI_RESET}")
        case -1:
            if aDepasse(score):
                print(f"{ANSI_RED}Vous avez dépassé {SCORE_CIBLE}! Vous perdez la manche. (-{mise}$){ANSI_RESET}")
            else:
                print(f"{ANSI_RED}Le croupier gagne la manche. (-{mise}$){ANSI_RESET}")
        case _:
            print("Égalité! Aucun changement à votre argent.")

# Tests :
# Numéro | Description         | Entrée    | Résultat attendu                                                                  | Résultat obtenu                                                                   | Réussi?
# -------+---------------------+-----------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+--------
# 1      | Victoire normale    | 11, 9, 5  | Vous gagnez la manche! (+5$) [bleu]                                               | Vous gagnez la manche! (+5$) [bleu]                                               | Oui
# 2      | Le croupier dépasse | 9, 12, 5  | Le croupier a dépassé 11! Vous gagnez la manche. (+5$) [bleu]                     | Le croupier a dépassé 11! Vous gagnez la manche. (+5$) [bleu]                     | Oui
# 3      | Défaite normale     | 8, 10, 5  | Le croupier gagne la manche. (-5$) [rouge]                                        | Le croupier gagne la manche. (-5$) [rouge]                                        | Oui
# 4      | Le joueur dépasse   | 12, 0, 5  | Score du croupier: - / Vous avez dépassé 11! Vous perdez la manche. (-5$) [rouge] | Score du croupier: - / Vous avez dépassé 11! Vous perdez la manche. (-5$) [rouge] | Oui
# 5      | Égalité             | 10, 10, 5 | Égalité! Aucun changement à votre argent. [sans couleur]                          | Égalité! Aucun changement à votre argent. [sans couleur]                          | Oui


def validerRejouer() -> bool:
    """Demande au joueur s'il veut recommencer une partie complète (o ou n), redemande si invalide.

    Returns:
        True si le joueur veut recommencer, False sinon
    """
    reponse: str = correcteur(input("\nVoulez-vous recommencer une partie complète? (o/n) "))
    while reponse != "o" and reponse != "n":
        print("Saisie invalide. Veuillez entrer o ou n.")
        reponse = correcteur(input("Voulez-vous recommencer une partie complète? (o/n) "))
    return reponse == "o"

# Tests :
# Numéro | Description               | Entrée               | Résultat attendu    | Résultat obtenu     | Réussi?
# -------+---------------------------+----------------------+---------------------+---------------------+--------
# 1      | Oui (minuscule)           | "o"                  | True                | True                | Oui
# 2      | Oui (majuscule)           | "O"                  | True                | True                | Oui
# 3      | Non (minuscule)           | "n"                  | False               | False               | Oui
# 4      | Non (majuscule)           | "N"                  | False               | False               | Oui
# 5      | Saisie invalide, puis oui | "peut-être" puis "o" | 1 erreur, puis True | 1 erreur, puis True | Oui


def calculerTauxVictoire(nbVictoires: int, nbManches: int) -> float:
    """Calcule le pourcentage de victoire.

    Args:
        nbVictoires: le nombre de manches gagnées
        nbManches: le nombre de manches jouées
    Returns:
        le pourcentage de victoire arrondi à 2 décimales (0.0 si aucune manche)
    """
    if nbManches == 0:
        taux: float = 0.0
    else:
        taux = round(nbVictoires / nbManches * 100, 2)
    return taux

# Tests :
# Numéro | Description           | Entrée | Résultat attendu | Résultat obtenu | Réussi?
# -------+-----------------------+--------+------------------+-----------------+--------
# 1      | Exemple 1 de l'énoncé | 3, 4   | 75.0%            | 75.0%           | Oui
# 2      | Exemple 2 de l'énoncé | 1, 3   | 33.33%           | 33.33%          | Oui
# 3      | Aucune manche jouée   | 0, 0   | 0.0%             | 0.0%            | Oui


def afficherStatistiques(nbManches: int, nbVictoires: int, nbDefaites: int) -> None:
    """Calcule et affiche le résumé final de la partie.

    Args:
        nbManches: le nombre de manches jouées
        nbVictoires: le nombre de manches gagnées
        nbDefaites: le nombre de manches perdues
    """
    nbEgalites: int = nbManches - nbVictoires - nbDefaites
    tauxVictoire: float = calculerTauxVictoire(nbVictoires, nbManches)

    print("\n--- Statistiques de la partie ---")
    print(f"Manches jouées: {nbManches}")
    print(f"Victoires: {nbVictoires}")
    print(f"Défaites: {nbDefaites}")
    print(f"Égalités: {nbEgalites}")
    print(f"Taux de victoire: {tauxVictoire}%")

# Tests :
# Numéro | Description        | Entrée   | Résultat attendu        | Résultat obtenu         | Réussi?
# -------+--------------------+----------+-------------------------+-------------------------+--------
# 1      | Égalités calculées | 10, 6, 3 | Égalités: 1             | Égalités: 1             | Oui
# 2      | Taux de victoire   | 10, 6, 3 | Taux de victoire: 60.0% | Taux de victoire: 60.0% | Oui


def jouerPartie() -> None:
    """Joue une partie complète jusqu'à 0$ ou 30$, puis affiche les statistiques."""
    argent: int = ARGENT_DEPART
    nbManches: int = 0
    nbVictoires: int = 0
    nbDefaites: int = 0

    afficherRegles()
    while argent > 0 and argent < ARGENT_OBJECTIF:
        print(f"\n=== Manche {nbManches + 1} ===")
        print(f"Argent: {argent}$ | Mise: {MISE}$")

        score: int = tourJoueur()
        scoreCroupier: int = 0
        if not aDepasse(score):
            scoreCroupier = tourCroupier()

        afficherResultatManche(score, scoreCroupier, MISE)

        resultat: int = determinerResultat(score, scoreCroupier)
        nbManches += 1
        argent += resultat * MISE
        match resultat:
            case 1:
                nbVictoires += 1
                print(f"{ANSI_GREEN}Votre argent: {argent}${ANSI_RESET}")
            case -1:
                nbDefaites += 1
                print(f"{ANSI_RED}Votre argent: {argent}${ANSI_RESET}")
            case _:
                print(f"Votre argent: {argent}$")

    if argent <= 0:
        print(f"\n{ANSI_RED}Vous n'avez plus d'argent. Vous avez perdu la partie!{ANSI_RESET}")
    else:
        print(f"\n{ANSI_BLUE}Vous avez atteint {ARGENT_OBJECTIF}$. Vous avez gagné la partie!{ANSI_RESET}")

    afficherStatistiques(nbManches, nbVictoires, nbDefaites)


def main() -> None:
    """Lance des parties complètes tant que le joueur veut recommencer."""
    rejouer: bool = True
    while rejouer:
        jouerPartie()
        rejouer = validerRejouer()
        if rejouer:
            print("Nouvelle partie! Votre argent est remis à {ARGENT_DEPART}$ et les statistiques à zéro.")
        else:
            print("Merci d'avoir joué. Au revoir!")


main()
