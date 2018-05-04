import random 
class Pokemon(object):
	def __init__(self,name,hp,type):
		self.name = name 
		self.hp = hp
		#it defines each type 
		if type == 'fire':
			self.type = {
			'fireball': random.randint(240, 300),
			'blaze claw': random.randint(150, 180),
			'tail slash': random.randint(90, 100),
			}

		elif type == 'water':
			self.type = {
			'water jet': random.randint(220, 260),
			'water whip': random.randint(160,180),
			'hydrate': random.randint(-200,-1),
			}

		else:
			print ('not a choice')


	def battle(self, enemy):
		#go over attack choices for each instance 
		for x in self.type:
			print(x)
			#pick attack
			#note to user who is attacking 
		print("%s turn to attack %s"%(self.name, enemy.name))
		#get user input
		if (self.hp > 1):
		user_choice = input('Choose your attack ')
		#use user input to apply attack to enemy 
		for x, y in self.type.moves():
				if (x == 'fireball'):
					self.type['fireball'] = random.randint(240,300)
				elif (x == 'blaze claw'):
					self.type['blaze claw'] = random.randint(150, 180)
				elif (x == 'tail slash'):
					self.type['tail slash'] = random.randint(90, 100)
				elif (x == 'water jet'):
					self.type['water jet'] = random.randint(220, 260)
				elif (x == 'water whip'):
					self.type['water whip'] = random.randint(160, 180)
				elif (x == 'hydrate'):
					self.type['hydrate'] = random.randint(-200, -1)
		choosen_attack = self.type[user_choice]
		#Attack while HP > 1 
				

			enemy.hp = enemy.hp - choosen_attack
			print("%s did %d damage to %s"%(self.name, choosen_attack, enemy.name))
			print("%s has %d HP left"%(enemy.name, enemy.hp))
			if (enemy.hp > 1):
				return enemy.battle(self)
				#enemy turn to attack 
			elif (enemy.hp < 1):
				print("%s is nocked out, %s won"%(enemy.name, self.name))


#Running the game / init your c;ass & call methods 
blaze = Pokemon('blaze', 900, 'fire')
mizu = Pokemon('mizu', 1100, 'water') 
Pokemon.battle(blaze,mizu)
