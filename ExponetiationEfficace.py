
# coding: utf-8

# In[4]:


#Projet du module Outils de programmation : Ce projet est fait par : 
#AJEMMAA Selma! Section A! Groupe 3! 201400007141 
#DOUALANE Issaac! Secction A! Groupe 3! 201400007004 
#REZKALLAH Soumia! Section A! Groupe 3! 201500008657 
#TAMZAIT Narimane! Section A! Groupe 3! 201500008843


# coding : utf-8
def s_w(m, k):
       
        n = bin(m)  # converition en binaire 
        n = n[2:]   # se debarasse du '0b' de depart
        n = n[::-1] # on renverse la chaine de charactere pour faciliter son traitement
    
        # Les puissance impaire
      
        x = { 1:2, 2:4 }
        
        for i in range(1, 2**(k-1) ) :
            x[2*i+1] = 2**(2*i+1)
        
        # nombre de multiplications effectuees jusqu'ici
        etape = len( range(1, 2**(k-1) ) ) + 1
    
        y, i = 1, len(n)-1
        max_utile = 0   # Elle servie à enlever le coups des valeurs precalculee non utile du total
    
        while i > -1 :
            if n[i] == '0': 
                
                y = y**2
                i -= 1
                etape += 1
                
            else :
                # retrouve la chaine de longeur < k et qui se termine par 1 
                for j in range(k):
                    lower = max(i-j,0)
                    if n[lower] == '1':
                        d = int ( n[ lower : i+1], 2)
                        e = lower
    
                y = y**(2**(i-e+1))
                
                # comptabilise le nombre de multiplication qui vient d'etre effectue
                if y > 1 :
                    etape += i-e+1
               
                y = y*x[d]
    
                # max_utile reçoit le plus grand index utilise jusqu'ici
                max_utile = max(d, max_utile)
                i = e-1
    
                # ne comptabilise pas la multiplication si c'est fois 1
                if y > x[ d ] :
                    etape += 1
        
        # on soustrait au coups le nombre des elements precalculer non utile
        non_utile = [ 1 for i in x.keys() if i > max_utile ]
        etape -= sum(non_utile)
    
        return etape
  
 
def minProd(k):       
    somme = 0  # initialisation de la somme
        
    for a in range(2, k+1) :
        max_window = len( bin(a) )-2        # longeur de maximal de la fenetre = longueur de a en binaire
        etapes = [ s_w(a, b) for b in range(1, max_window ) ]
        somme += min( etapes )
    
        print( "Sommes du nombre de multiplications necessaires à l'exponenetiation pour chauque n de ( 1 à", k,") =", somme )
   

