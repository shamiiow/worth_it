notes = [11,7,5]
coef = [1,1,1]

def moyenne(tab1, tab2):
	n,d = 0,0
	for i in range(len(tab1)):
		n += tab1[i]
		d += tab2[i]
	return (n/d)

def remove_less(tab, tab2):
	a = 0
	ntab, ntab2 = [],[]
	for i in range(len(tab)):
		if tab[i] == min(tab):
			a = i
	for i in range(len(tab)):
		if i != a:
			ntab.append(tab[i])
			ntab2.append(tab2[i])
	return ntab, ntab2

def m_bac(a,b):
	return (a*3 + b)/(3+1)
			

def test_note(without):
	w = without
	for i in range(0,21):
		if w< m_bac(moyenne(notes, coef), i):
			return m_bac(moyenne(notes, coef), i), i


a,b = remove_less(notes, coef)
without = m_bac(moyenne(a,b), min(notes))
moyenne, note = test_note(without)

print(f"Si tu ne rends rien                                       : {without} \nSi tu as {note} ou plus alors ta moyenne augmentera et sera a : {moyenne}")
