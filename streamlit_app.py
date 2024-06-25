def trier_mots_cles(mots_cles, mots_cles_pertinents):
    """
    Filtre les mots clés non pertinents à partir d'une liste de mots clés et d'une thématique.

    Args:
    - mots_cles: List of str, les mots clés à vérifier.
    - mots_cles_pertinents: List of str, les mots clés pertinents pour la thématique.

    Returns:
    - List of str, les mots clés pertinents.
    """
    # Convertir la liste des mots clés pertinents en ensemble pour une recherche rapide
    mots_cles_pertinents_set = set(mots_cles_pertinents)
    
    # Filtrer les mots clés pour ne conserver que ceux qui sont pertinents
    mots_cles_triees = [mot for mot in mots_cles if mot in mots_cles_pertinents_set]
    
    return mots_cles_triees

# Exemple d'utilisation
mots_cles_a_verifier = [
    "alternateur hydrolienne", "houlomotrice", "cagué definition", "énergie houlomotrice", 
    "houlomoteur", "centrale pelamis", "colonne d'eau oscillante", "comment mesurer la houle"
]

mots_cles_pertinents = [
    "houlomotrice", "énergie houlomotrice", "houlomoteur", "centrale pelamis",
    "colonne d'eau oscillante", "déferlement", "houle", "vague", "électricité"
]

mots_cles_filtrees = trier_mots_cles(mots_cles_a_verifier, mots_cles_pertinents)
print("Mots clés filtrés : ", mots_cles_filtrees)
