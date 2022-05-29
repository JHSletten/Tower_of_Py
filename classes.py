from random import *
from materials import *

#A document of all classes (and a function) used in the Tower of Py game
#Hero class, spell class, enemy class, (create_spells function)


def create_spells(spells, spell_list):
  for level in spells:
    for i in range(len(spells[level])):
      spell_list[level].append(Spell(spells[level][i][0], spells[level][i][1], spells[level][i][2], spells[level][i][3], spells[level][i][4]))
  #print(spell_list)

#The Hero class
#Defines the hero class with attributes for name, level, player_class, element, alive,
#spell_book, str, max_hp, max_mp, grit, and magic.
#Functions for representing, attacking, taking damage, healing, using MP, level up, etc.
class Hero:
  def __init__(self, name, player_class):
    self.name = name
    self.level = 1
    self.player_class = player_class

    self.element = 'Physical'
    self.alive = True
    self.spell_book = {1:[], 2:[], 3:[]}
    if self.player_class == 'Fighter':
      self.str = 6
      self.max_hp = 12
      self.max_mp = 0
      self.spell_book[1] = [Spell(fighter_source[0], fighter_source[1], fighter_source[2], fighter_source[3], fighter_source[4])]
      self.grit = [1, '+']
      self.magic = [0, '']
    elif self.player_class == 'Wizard':
      self.str = 4
      self.max_hp = 8
      self.max_mp = 10
      self.grit = [1, '']
      self.magic = [1, '+']
      create_spells(wizzard_source, self.spell_book)
    elif self.player_class == 'Paladin':
      self.str = 5
      self.max_hp = 10
      self.max_mp = 6
      self.grit = [1, '']
      self.magic = [1, '']
      create_spells(paladin_source, self.spell_book)
    else:
      self.player_class = 'Toad'
      self.str = 1
      self.max_hp = 1
      self.max_mp = 0
      self.grit = [0, '']
      self.magic = [0, '']
    self.temp_hp = self.max_hp
    self.temp_mp = self.max_mp

  def __repr__ (self):
     return ('{name}   (level {level} {player_class}) \nStrength: {strength}  Grit: {grit1}{grit2}  Magic: {magic1}{magic2}\nHP: {temp_hp}/{max_hp}  MP: {temp_mp}/{max_mp}'.format(name = self.name, level = self.level, player_class = self.player_class, strength = self.str, grit1 = self.grit[0], grit2 = self.grit[1], magic1 = self.magic[0], magic2 = self.magic[1], temp_hp = int(self.temp_hp), max_hp = self.max_hp, temp_mp = int(self.temp_mp), max_mp = self.max_mp))

  def level_up(self):
    self.level += 1
    if self.player_class == 'Fighter':
      self.str += 6
      self.max_hp += 6
      self.max_mp += 3
      self.grit[0] += 1
      self.magic[0] += 1
    elif self.player_class == 'Wizard':
      self.str += 3
      self.max_hp += 4
      self.max_mp += 5
      self.grit[0] += 1
      self.magic[0] += 1
    elif self.player_class == 'Paladin':
      self.str += 5
      self.max_hp += 5
      self.max_mp += 3
      self.grit[0] += 1
      self.magic[0] += 1
    else:
      self.player_class = 'Toad'
      self.str += 1
      self.max_hp += 1
    self.full_heal()

  def attack(self):
    return [round(self.str * 0.5 * uniform(0.5, 1.5), 0), self.element]

  def cast_spell(self, spell):
    target = spell.target
    if spell.MP_cost <= self.temp_mp:
      self.mana_drain(spell.MP_cost)
      if target == 'Self':
        self.heal(spell.damage)
        print ('You heal for', spell.damage, 'hp.')
        return('Healed') 
      else: return [spell.damage, spell.element]
    return 'Not enough MP'
  
  def heal(self, heal):
    self.temp_hp += heal
    if self.temp_hp > self.max_hp: self.temp_hp = self.max_hp
  
  def take_damage(self, damage):
    self.temp_hp -= damage
    if self.temp_hp <= 0: 
      self.temp_hp = 0
      self.alive = False
  
  def mana_gain(self, mana_add):
    self.temp_mp += mana_add
    if self.temp_mp > self.max_mp: self.temp_mp = self.max_mp

  def mana_drain(self, mana_loss):
    self.temp_mp -= mana_loss
    if self.temp_mp < 0: self.temp_mp = 0

  def new_turn(self):
    if self.player_class == 'Fighter':
      self.heal(round(uniform(1, self.level)))
      self.mana_gain(round(uniform(0, self.level-1)))
    elif self.player_class == 'Wizard':
      self.heal(round(uniform(0, self.level)))
      self.mana_gain(round(uniform(1, self.level)))
    elif self.player_class == 'Paladin':
      self.heal(round(uniform(0, self.level)))
      self.mana_gain(round(uniform(0, self.level)))
    else:
      self.heal(self.level)
  
  def full_heal(self):
    self.heal(self.max_hp)
    self.mana_gain(self.max_mp)


#Defines spell class (3 levels)
#Attributes: name, damage, element, target and level
#Funtions: representaion, cast spell
class Spell:
  def __init__(self, name, damage, element, level, target = 'Enemy'):
    self.name = name
    self.damage = damage
    self.element = element
    self.target = target
    self.level = level
    if self.level == 1: self.MP_cost = 3
    elif self.level == 2: self.MP_cost = 5
    elif self.level == 3: self.MP_cost = 10
    else: self.MP_cost = 999

  def __repr__(self):
    deal = 'deals'
    if self.target == 'Self': deal = 'heals'
    return ('{name}: A level {level} {element} spell that {deal} {damage} damage.\nMana cost: {mana} MP'.format(name = self.name, level = self.level, element = self.element, deal = deal, damage = self.damage, mana = self.MP_cost))

  def cast_spell(self):
    return([self.damage, self.element])


#Defines enemy class (challenge 1-3)
#Attributes: name, element, max_hp, temp_hp, level, str, alive
#Funtions: representation, take damage, attack, reset.
class Enemy:
  def __init__(self, name, element, hp, level):
    self.name = name
    self.element = element
    self.max_hp = hp
    self.temp_hp = self.max_hp
    self.level = level
    self.str = level*5
    self.alive = True
  
  def __repr__(self):
    return('{name} - a challenge {challenge} {element} creature. \nHP: ?/{max_hp}'.format(name = self.name, challenge = self.level, element = self.element, max_hp = self.max_hp))

  def take_damage(self, damage):
    self.temp_hp -= damage
    if self.temp_hp <= 0: 
      self.temp_hp = 0
      self.alive = False
  
  def attack(self):
    return [round(self.level * 2 * uniform(0.5, 1.5), 0), self.element]
    
  def reset(self):
    self.temp_hp = self.max_hp
    self.alive = True


######