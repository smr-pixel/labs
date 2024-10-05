class Item:
    
    def __init__(self, name, description = '', rarity = 'common'):
        self._name = name
        self._rarity = rarity
        self._description = description
        self._ownership = ''
    
    def pick_up(self, character: str) -> str:
        self._ownership = character
        print(f"{self._name} is now owned by {self._ownership}")
    
    def throw_away(self) -> str:
        self._ownership = False
        print(f"{self._name} is now thrown away")
    
    def use(self) -> str:
        if self._ownership == '':
            pass
        else:
            print(f"The {self._name} is used.")


class Weapon(Item):
    
    def __init__(self, name, damage, type, description = '', rarity = 'common'):
        super().__init__(name, description, rarity)
        self._damage = damage
        self._type = type
        self._equip = False
        self._use = False

    def equip(self):
        self._equip = True
        print(f'{self._name} is equipped by {self._ownership}.')
        return self._equip

    def use(self):
        if self._equip == True and self._use == False and self._ownership != '':
            if self._rarity == 'legendary':
                attacking_power = self._damage * 1.15
            else:
                attacking_power = self._damage * 1
            print(f"{self._name} is used, dealing {attacking_power} damage")
            self._use = True
        else:
            pass

    

class Shield(Item):
    def __init__(self, name, defense, broken, description = '', rarity = 'common'):
        super().__init__(name, description, rarity)
        self._defense = defense
        self._broken = broken
        self._equip = False
        self._use = False
        if self._broken == True:
            broken_mod = 0.5
        elif self._broken == False:
            broken_mod = 1
        self._broken_mod = broken_mod
    
    def equip(self):
        self._equip = True
        print(f'{self._name} is equipped by Beleg.')
        return self._equip
    
    def use(self):
        if self._equip == True and self._use == False and self._ownership != '':
            if self._rarity == 'legendary;':
                defense_power = self._defense * 1.1 * self._broken_mod
            else:
                defense_power = self._defense * self._broken_mod
            print(f"{self._name} is used, blocking {defense_power} damage")
            self._use = True
        else:
            pass
    

class Potion(Item):
     
     def __init__(self, name, value, type, description = '', effective_time = 30, rarity = 'common'):
         super().__init__(name, description, rarity)
         self._value = value
         self._effective_time = effective_time
         self._empty = False
         self._type = type
     
     def use(self):
         if self._empty == False and self._ownership != '':
             print(f"{self._name} is consumed.")
             if self._type == 'attack':
                 print(f"{self._ownership} used {self._name}, and attack increases {self._value} for {self._effective_time}s")
             elif self._type == 'defense':
                 print(f"{self._ownership} used {self._name}, and defense increases {self._value} for {self._effective_time}s")
             elif self._type == 'HP':
                 print(f"{self._ownership} used {self._name}, and HP restores {self._value} health")
         elif self._empty == True or self._ownership == '':
             pass
         self._empty = True

     @classmethod
     def from_ability(cls, name, owner, type):
         potion = cls(name = name, value = 50, type = type, rarity = 'common', effective_time = 30)
         potion._ownership = owner
         return potion
         
         

long_bow = Weapon(name='Belthronding', rarity = 'legendary', damage=5000, type='bow')
long_bow.pick_up('Beleg')  # Belthronding is now owned by Beleg
long_bow.equip()            # Belthronding is equipped.
long_bow.use()              # Belthronding is used, dealing 5750 damage.

broken_pot_lid = Shield(name='wooden lid', defense=5, broken=True, description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield')
broken_pot_lid.pick_up('Beleg')  # wooden lid is now owned by Beleg
broken_pot_lid.equip()            # wooden lid is equipped.
broken_pot_lid.use()              # wooden lid is used, blocking 2.5 damage
broken_pot_lid.throw_away()       # wooden lid has been thrown away.
broken_pot_lid.use()              # NO OUTPUT

attack_potion = Potion.from_ability(name='atk potion temp', owner='Beleg', type='attack')
attack_potion.use()                # Beleg used atk potion temp, and attack increase 50 for 30s
attack_potion.use()                # NO OUTPUT

# Testing isinstance
print(isinstance(long_bow, Item))         # True
print(isinstance(broken_pot_lid, Shield)) # True
print(isinstance(attack_potion, Weapon))  # False
