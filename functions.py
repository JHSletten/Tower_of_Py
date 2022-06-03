from random import *
from classes import *

#A document with all the functoins for the Tower of Py game
    #Creating hero, spells, and enemies
    #Attacking and calculating damage
    #Defining a combat function
    #Defining the three stages

def create_hero():
  print('First, let\'s start by making a character')
  a = input('What is the name of your character? \n>>>')
  hero_class = ['Giga Chad', 'Fighter', 'Wizard', 'Paladin']
  c = False
  while c == False:
    b = input('What class do you want to play as? \nFighter: 1 \nWizard: 2 \nPaladin: 3 \n>>>')
    if b in ['0', '1', '2', '3']:
      b = int(b)
      c = True
      break
    input('Invalid input! Try again. \n>')
  return Hero(a, hero_class[b]) 

def create_enemies(enemies, stage):
  for enemy in enemies:
    stage.append(Enemy(enemy[0], enemy[1], enemy[2], enemy[3]))

def calculate_damage(attack_list, target_element):
  damage = attack_list[0]
  attack_element = attack_list[1]
  damage_calculation = damage
  if target_element in elements_more[attack_element]:
     damage_calculation = round(damage*1.5, 0)
  elif target_element in elements_less[attack_element]:
    damage_calculation = round(damage*0.5, 0)
  # print('{dmg_type} damage is effective against {weakness} and weak against {resistence}'.format(dmg_type = attack_element, weakness = elements_more[attack_element], resistence = elements_less[attack_element]))
  return damage_calculation

def attack(attacker, enemy):
  hit = False
  if attacker.str > enemy.str: hit = uniform(0, 1) > 0.15
  else: hit = uniform(0, 1) > 0.3 
  return hit

def combat(hero, enemy):
  input('\nEncounter: \n{enemy}\n>'.format(enemy = enemy))
  while enemy.alive and hero.alive:
    action = 'x'
    while action not in ['a', 'A', 'S', 's']:
      action = input('It\'s your turn! \n\n{stats} \nAttack: a \nCast Spell: s \n>>>'.format(stats = hero))
      if action.upper() == 'A':
        hero.print_attack_text(enemy)
        if attack(hero, enemy):
          damage = calculate_damage(hero.attack(), enemy.element)
          enemy.take_damage(damage)
          print('You hit', enemy.name, 'for', int(damage), 'damage.')
        else:
          print('You missed!')
      elif action.upper() == 'S':
        print('\nAvailable spells:')
        for i in range(1, hero.level+1):
          print('\nLevel {level} spells:'.format(level = i))
          for spell in hero.spell_book[i]:
            print(spell)
        action = input('\nCast a spell: spell_name \nBack to menu: x \n>>>')
        if action not in ['x', '']:
          for level in hero.spell_book: 
            for spell in hero.spell_book[level]:
              if spell.name.upper() == action.upper():
                spell_status = hero.cast_spell(spell)
                if spell_status == 'Not enough MP':
                  print('You fail to cast {spell} due to insuficient mana. \nMana cost: {mana_cost} \nMP: {mana_level} '.format(spell = spell.name, mana_cost = spell.MP_cost, mana_level = hero.temp_mp))
                elif spell_status == 'Healed':
                  print('HP: {tempHP}/{maxHP}'.format(tempHP = int(hero.temp_hp), maxHP= hero.max_hp))
                else:
                  damage = calculate_damage(spell_status, enemy.element)
                  enemy.take_damage(damage)
                  print('You cast {spell} at {target} and deal {damage} {element} damage'.format(spell = spell.name, target = enemy.name, damage = int(damage), element = spell.element))
                action = 's'
        if action not in ['s', 'x']: print('Invalid spell name')  
      else: print('Invalid input, try again!')
      input('>')
    if not enemy.alive: break 
    else:
      if attack(enemy, hero):
        print(enemy.name, 'attacks you.')
        damage = calculate_damage(enemy.attack(), hero.element)
        hero.take_damage(damage)
        print(enemy.name, 'attack and hit you for', int(damage), enemy.element, 'damage.')
          #calculate damage
      else:
        print(enemy.name,'attack and miss!')
    input('>')
    if not hero.alive: break
    hero.new_turn()
  if hero.alive:
    input('You defeat the {enemy}\n>'.format(enemy = enemy.name))
    hero.new_turn()
    hero.increase_score(enemy.level * 100)
  else:
    input('\n{name} was slain by a mighty {enemy}\nNext>'.format(name = hero.name, enemy = enemy.name))
    print('', hero, '', sep='\n')
    input('Restart by ending this program \n\nEnd>')
    raise SystemExit(0)

def stage_1(hero):
  input('\nYou make your way towards the base of the Tower of Py.\n>') 
  input('By the large brown door which marks the entrance, you spot your first enemy.\n>')
  hero.full_heal()
  create_enemies(stage_1_enemies, stage_1_list)
  combat(hero, stage_1_list[0])
  input('After defeating that dreadful hound you make your way inside the tower.\n>')
  input('You stand in a large grass field under a light gray sky. In the middle of the field you see a great red oak tree. There is no sign of the door behind you.\n>') 
  input('As you make your way towards the red oak you feel the ground trembling...\n>')
  combat(hero, stage_1_list[1])  
  input('Your foe slowly falls over and you notice a stone hatch where the oak guardian once stood.\n>')
  input('As you pull up the heavy stone slab, you see a wooden staircase leading down into darkness.\n>')
  input('You make your way down the stairs. In the dark you glimpse a milky white creature charging towards you.\n>')
  combat(hero, stage_1_list[2])
  input('Bones clatter against the walls and floor of the small room you are standing in. You sigh deeply and lay down to rest among the scattered remains of the skelletal guard. \n>')
  hero.level_up()
  input('\nYou level up! \n\n{stats}\n\nContinue to next stage\n>'.format(stats = hero))

def stage_2(hero):
  hero.full_heal()
  create_enemies(stage_2_enemies, stage_2_list)
  input('\nYou wake up from your brief rest. In the middle of the previously dark room you see a column of bright orange light. \n>')
  input('A voice erupts from the radiating pillar. \n>')
  input('\"Welcome to the Tower of Py! Your anmusing attempt at climbing this spire will soon come to an end. My collegues will dispose of you with ease. Now answer their challenge!\"\n>')
  input('You enter the glowing orange light and feel your body accelerate upwards. There is an abrupt stop and you find yourself in a smoke filled chamber. You hear the crackling of a fire.\n>')
  combat(hero, stage_2_list[0])
  input('You quickly put out the small fire that your foe inflicted on your cloak. \n>')
  input('Looking for a way to advance further up the tower, you make your way up a spiral staircase. \n>')
  input('At the top of the staircase you attempt to push open a heavy wooden door. \n>')
  input('As the door finaly gives in, you feel heavy humid air hit your face. \n>')
  combat(hero, stage_2_list[1])  
  input('\"Seems like i have to deal with you myself...\"\n>')
  input('As you turn to identify the source of the voice, the room around you dissapears.\n>')
  input('You are engulfed in complete white, you can see neither walls nor celing. \n>')
  combat(hero, stage_2_list[2])
  input('When you deal your final blow to the Archmage, her body is flung up in the air and contorts and pushes itself into the size of child\'s doll. \n>') 
  input('The white floor around you crumbles and is pulled towards the remains of the Void Wizard. \n>')
  input('You feel the air being pushed out of your lungs, and everything turns to black. \n>')
  hero.level_up()
  input('\nYou level up! \n\n{stats}\n\nContinue to next stage\n>'.format(stats = hero))

def stage_3(hero):
  hero.full_heal()
  create_enemies(stage_3_enemies, stage_3_list)
  input('\nYou come to, lying in a soft bed in a warm room of aristochratic standards. Your wounds are tended to and your dirty rags have been replaced by light gray robes. \n>')
  input('You get out of the bed to find your gear nicely sorted next to your bedside. You equip your gear. \n>')
  input('You feel a strong magnetic like attraction comming from an open doorway at the oposite end of the room. You make your way thorugh this doorway into a long corridor.\n>')
  input('The corridor exits into a large gray room. The room reminds you of that of your local temple with several rows of seating leading up to what seems like an altar. \n>')
  input('By the altar you see two towering figures. One with gray skin, dressed in dark brown garments, holding what looks like several large meat hooks in their left hand. \n>')
  input('This must be the Baron of Death. \n>')
  input('Besides the Baron stands a taller figure with feminin fetures. Her skin is white as snow and she is dressed in a loose silver robe. As you move closer you can see that she has seven fingers on each hand. \n>')
  input('This must be the Duchess of Halidom. \n>')
  input('The Baron steps towards you with dead eyes. A guteral sound escapes from his mouth, as he flings his collection of rusty hooks towards you. \n>')
  combat(hero, stage_3_list[0])
  input('The Baron stumbles, trying to catch himself on the nearby altar. \n>')
  input('When his hand hits the altar the tendons of his right arm gives in and the arm itself is torn off. \n>')
  input('As his rotten, maggot filled inside gets exposed, the Baron is reduced to a pile of decay wrapped in brown cloth.\n>')
  input('The Duchess grins. \n>')
  input('She folds her hands in prayer and sings. The song is beautiful and melancholic, sung in a celestial language you cannot comprehend.\n>')
  input('\"This is it\". You think to yourself, as the Duchess turn towards you with dark red blood running from her eyes. \n>')
  combat(hero, stage_3_list[1])  
  input('The Duchess falls to her knees. Her being glows in bright silver.\n>')
  input('A sudden gust of wind passes through the room, and the air fills with specs of silver and gold. \n>')
  input('The Duchess is gone. \n>')
  input('You have defeated your tyrants, the Baron of Death and the Duchess of Halidom. \n>')
  input('Your homeland is finally safe from the terror and suffering imposed by these draconic rulers. \n>')
  input('You hear a low whisper from the altar in front of you. \n>')
  input('darkness... \n>')
  input('darkness... \n>')
  input('void... \n>')
  combat(hero, stage_3_list[2])
  input('Congratualtions {player}!. You have fought your way through the Tower of Py, and have defeated the void despot, thon.\n>'.format(player = hero.name))
  input('After completing this feat of excellence, you are deserving of a life of rest ...\n')
  input('... but you also could try to scale the tower again with a different class! \n>')
  hero.increase_score(6100)
  print(hero)
