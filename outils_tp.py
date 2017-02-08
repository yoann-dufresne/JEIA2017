# renvoie une liste de lecture séquencées
def lecture_donnees(donnees):
    sequences = []
    for ligne in open(donnees):
        if ligne.startswith('>'):
            continue
        sequence = ligne.strip()
        sequences += [sequence]
    return sequences

# renvoie un dictionnaire de la forme:
# organisme : séquence ADN de son gène 16s/18s
def lecture_base():
    import glob
    base = dict()
    for fichier in glob.glob('16s-18s/*.fasta'):
        organisme = fichier[:-6].split('/')[-1]
        sequence = ""
        for ligne in open(fichier):
            if ligne.startswith('>'):
                continue
            sequence += ligne.strip()
        base[organisme]=sequence
    return base