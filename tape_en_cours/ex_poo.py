p1 = Personne(naissance=1990, nom="Matthieu")
p2 = Personne(naissance=2015, nom="Paul")
print(p1.est_majeur() == True)
print(p2.est_majeur() == False)
