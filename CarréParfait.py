
# coding: utf-8

# In[ ]:


#Projet du module Outils de programmation : Ce projet est fait par : 
#AJEMMAA Selma! Section A! Groupe 3! 201400007141 
#DOUALANE Issaac! Secction A! Groupe 3! 201400007004 
#REZKALLAH Soumia! Section A! Groupe 3! 201500008657 
#TAMZAIT Narimane! Section A! Groupe 3! 201500008843


# coding : utf-8



def premier(a,b): 
        p = []
  
        for i in range( max(a,2) , b):
            for j in range(2, int(sqrt(i))+1 ):
                if i%j == 0 :
                    break
            else :
                p.append(i)
        return set(p)

def combinaison(a) :
        combo = [ [] ]
 
        for i in range (0,a):
            for sub_set in combo:
                combo = combo + [list(sub_set)+[i]]

            return combo[1:]


def C():
    a= input("Veuillez donner un chiffre ")
    b= input("Veuillez donner un autre chifftre ") 
    if type(a) != int or type(b) != int : 
            print('Veillez entrer des chiffres')
            return
   
    if a > b or min(a, b) < 0 :
            print("L'interval fourni est non valide")
                  
            return 
   
    interval = set( range(a, b+1) )
       
        # Pruning des éléments non necessaire
    if b > 2*a :
          interval = interval - premier(a*2, b)
    
    else :
            p = premier(b-a, a)
    
            for i in p :
                if b//i != i :
                    interval = interval - set( [(b//i)*i] )
    
            interval = interval - premier(a+1, b+1)
    
            interval = list(interval)
            sous_ensemble = combinaison(interval)
    
        #test des sous ensemble
            total = 0
        
            for i in sous_ensemble :
                produit = 1
    
                for j in i :
                    produit = produit*j
    
                if sqrt(produit)%1 == 0 :
                    total = total + 1
    
            print( "Nombre de carrées parfais issus du produit des éléments des sous-ensembles de l'interval",(a, b) ,"=", total)
C()

