#Material for classes and functoins

#Elements - crits and resists
elements_more = {'Nature':['Death'], 'Death':['Life'], 'Life':['Void'], 'Void':['Water'], 'Water':['Fire'], 'Fire':['Nature'], 'Physical':['']}
elements_less = {'Nature':['Nature', 'Fire'], 'Death':['Death', 'Nature'], 'Life':['Life', 'Death'], 'Void':['Void', 'Life'], 'Water':['Water', 'Void'], 'Fire':['Fire', 'Water'], 'Physical':['Void']}

#Spell lists - wizzard, paladin, fighter
wizzard_source = {1:[['Quick Heal', 5, 'Life', 1, 'Self'],
['Rock Fling', 5, 'Physical', 1, 'Enemy'],
['Thorn Storm', 4, 'Nature', 1, 'Enemy'],
['Vacuum Orb', 4, 'Void', 1, 'Enemy'],
['Water Blade', 4, 'Water', 1, 'Enemy']], 
2:[['Radiant Blast', 7, 'Life', 2, 'Enemy'],
['Fire Ball', 8, 'Fire', 2, 'Enemy'],
['Pestulence', 7, 'Death', 2, 'Enemy'],
['Constricting Vines', 7, 'Nature', 2, 'Enemy']], 
3:[['Greater Healing', 15, 'Life', 3, 'Self'],
['Decay', 14, 'Death', 3, 'Enemy'],
['Miniature Black Hole', 15, 'Vacuum', 3, 'Enemy']]}

paladin_source = {1:[['Quick Heal', 5, 'Life', 1, 'Self'],
['Rock Fling', 5, 'Physical', 1, 'Enemy']],
2:[['Radiant Blast', 7, 'Life', 2, 'Enemy']], 
3:[['Greater Healing', 15, 'Life', 3, 'Self']]}

fighter_source = ['Quick Heal', 5, 'Life', 1, 'Self']

#Enemy lists
stage_1_enemies = [['Guard Wolf', 'Physical', 8, 1], ['Enchanted Tree', 'Nature', 10, 1], ['Skeleton Brute', 'Death', 12, 2]]
stage_2_enemies = [['Fire Mage', 'Fire', 14, 2], ['Water Mage', 'Water', 16, 2], ['Void Archmage', 'Void', 18, 3]]
stage_3_enemies = [['Death Baron, Clandzhuul', 'Death', 24, 3], ['Holy Duchess, Silnidiya', 'Life', 24, 3], ['Void Despot, thon', 'Void', 30, 3]]

stage_1_list = []
stage_2_list = []
stage_3_list = []

attack_dict = {'Fighter': 'heavy steel sword.', 'Wizard': 'Wizard staff.', 'Paladin': 'holy blade.', 'Giga Chad': 'massive muscles.'}