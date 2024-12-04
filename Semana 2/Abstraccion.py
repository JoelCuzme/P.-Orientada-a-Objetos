class Molde:
    def __init__(self,Nombre,Vida,Mana,Dano_Magico,Dano,Resistencia_Magica,Armadura):
        self.Nombre=Nombre
        self.Vida=Vida
        self.Mana=Mana
        self.Dano_Magico=Dano_Magico
        self.Dano=Dano
        self.Resistencia_Magica=Resistencia_Magica
        self.Armadura=Armadura

    def atributos(self):
        print("Nombre:", self.Nombre)
        print("Vida:",self.Vida)
        print("Mana:",self.Mana)
        print("Dano Magico:", self.Dano_Magico)
        print("Dano:",self.Dano)
        print("Resistencia Magico:",self.Resistencia_Magica)
        print("Armadura:",self.Armadura)

    def esta_vivo(self):
        return self.Vida > 0

    def morir (self):
        self.Vida = 0
        print (self.Nombre, "esta muerto.")

    def daño (self, Oponente):
        magia= self.Dano_Magico - Oponente.Resistencia_Magica
        normal= self.Dano - Oponente.Armadura
        daño= magia+normal
        return daño

    def combate (self, Oponente):
        daño= self.daño(Oponente)
        Oponente.Vida = Oponente.Vida-daño
        print (self.Nombre, "ha realizado ", daño," de daño a",  Oponente.Nombre)
        if Oponente.esta_vivo():
            print(Oponente.Nombre, "tienen", Oponente.Vida,"de vida." )
        else:
            Oponente.morir()



def pelea (personaje,personaje2):
    personaje.combate(personaje2)



personaje= Molde("Jayce",200,100,700,
                 40,400,20)
personaje2=Molde("Jhin",50,100,20,100,10,10 )


pelea(personaje,personaje2)