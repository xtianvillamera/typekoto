# CS11 THRU
# BIBAL, GIDANZ RAFTERJUDE E. , 2015-07805
# VILLAMERA, CHRISTIAN L. , 2016-01218

import pygame
import random
import time
pygame.init()


class TheGame():
	def __init__(self):
		
		# Screen Display of Game
		self.length = 700
		self.width = 650
		self.size = (self.width,self.length)
		self.screenDisplay = pygame.display.set_mode(self.size)
		self.icon = pygame.image.load('others/logo.png')
		pygame.display.set_icon(self.icon)
		
		# Tuples of Words
		self.vocab =  ["abs","ace","act","age","ago","aid","air","alt","ape","ark","ask","axe","aye","bad","ban","bar","bet","bid","bio","bit","bow","box","bra","bro","bug","bye","cab","cam","can","car","cat","chi","cob","con","cop","cow","cry","cue","cum","cut","dam","dib","die","dim","doe","dog","dot","dry","due","dye","ear","eco","ego","elf","emo","end","eng","eon","era","est","evo","exo","fab","fan","fat","fax","fed","few","fib","fin","flu","fly","foe","fog","fox","fry","fun","fur","gal","gap","gay","gel","gem","geo","get","gin","gio","gnu","gov","gum","guy","gym","gyp","had","hat","haw","hen","hex","hid","hit","hoe","hop","hot","how","hub","hue","hum","hyp","ice","icy","ink","ion","ios","irk","ivy","jar","jaw","jew","jin","joy","jug","kaf","keg","key","kid","kit","koi","kyu","lad","law","lay","lie","lip","lot","lux","mac","mad","max","men","mew","mix","mud","mut","myc","nap","net","new","not","nox","nut","oak","oft","oil","old","one","opt","orb","ore","owl","oxy","pac","pan","paw","pax","pie","pit","ply","pod","pow","pro","pun","pyx","qat","qin","qis","qua","raw","red","rep","rex","rip","rod","row","rub","rye","sad","sat","saw","say","sex","she","shy","six","ski","sky","spy","sub","sun","tan","tax","ten","thy","tie","tip","toy","tsk","two","ugh","uke","uni","urn","use","van","vat","vex","via","vly","vow","vox","war","was","wax","web","who","why","wig","win","won","wry","xis","yak","yep","yes","ygo","yin","you","yup","zap","zax","zed","zel","zig","zit","zoa",
						"quod","flax","flex","jaws","jays","jehu","jefe","falx","faux","quag","zing","kick","qaid","quad","hoax","joys","lynx","zigs","khaf","jury","hawk","haji","xyst","jows","john","joey","howk","fyke","gaze","geez","sexy","jowl","josh","jive","vext","quai","yack","hack","quin","quit","yock","calx","coax","caky","size","tzar","suqs","coxa","crux","exec","expo","wavy","exam","raze","wack","waff","ritz","feck","jabs","whys","wick","nazi","moxa","whey","jibs","orzo","ooze","jibe","whew","jobs","mojo","maxi","lutz","jupe","jube","juba","mixt","minx","koph","ouzo","oxim","ibex","icky","iffy","izar","huff","huck","heck","hick","hock","howf","jagg","laze","jaup","poky","jeep","jazz","fizz","fuzz","buzz","razz","quiz","hajj","jeez","whiz","hazy","fozy","zyme","joky","qoph","juju","jeux","mazy","phiz","chez","cozy","jinx","waxy","jack","dozy","jock","jiff","zerk","zonk","foxy","zeks","pixy","zarf","oozy","zany","oyez","futz","quey","quay","lazy","friz","sizy","faze","boxy","fuze","haze","zinc","bize","jouk","kyak","junk","czar","jump","bozo","juke","jink","jake","jibb","jerk","jamb","jauk","hadj","zaps","doxy","jimp","zebu","dexy","joke","meze","zoic","maze","mozo","zoom","quip","putz","wych","prez","zips","fuji","onyx","adze","zags","oryx","doze","zeds","daze","flux","nixy","ditz","quid","keck","fixt","java",
						"adult", "ahead", "above", "acute", "admit", "basis", "bench", "bread", "baker", "blame", "child", "claim", "cable", "carry", "class", "death", "dozen", "delay", "doing", "dress", "elite", "enemy", "enjoy", "entry", "equal", "fight", "fault", "field", "force", "fluid", "giant", "glass", "guide", "guess", "grown",  "happy", "heart", "house", "horse", "hotel", "image", "ideal", "input", "issue", "inner", "judge", "joint", "jimmy", "jones", "known", "layer", "leave", "lives", "limit", "legal", "major", "making", "metal", "minor", "mixed", "never", "north", "novel", "night", "noise", "ocean", "often", "other", "order", "ought", "paper", "peace", "plain", "plant", "point", "queen", "quite", "quiet", "quick", "ratio", "ready", "river", "right", "rival", "scale", "seven", "shape", "sharp", "shelf", "table", "thank", "their", "teeth", "theft", "unit", "union", "until", "usual", "upper", "video", "visit", "video", "virus", "voice", "waste", "watch", "wheel", "world", "worth", "yield", "youth", "young", "zebra", 
						"abused","absent","abroad","acacia","actions","banana","barker","babies","bacons","barley","carver","canner","campus","carrot","cedula","degree","detach","define","dialed","double","either","eighth","encode","excess","exhale","faggot","faults","flavor","fellow","fenced","gasped","giants","galaxy","gallon","gasper","healer","header","heroes","holder","hornet","income","inside","iodine","invite","island","joined","jumper","juiced","judged","joggle","kidney","killer","kettle","kiddie","kennel","lenses","layers","liable","legacy","lasers","manage","mantel","marked","marvel","masked","newbie","newest","noised","noodle","normal","option","owners","outman","oppose","orally","parker","parked","peaked","pencil","phobia","quills","quiets","quotes","quilts","quells","rabbit","ranger","rapped","rasper","rammed","sachet","saddle","salted","sashed","sadism","teased","temple","thrown","thrice","thrift","usable","violet","waiter","xylene","yucked","zombie", 
						"abjoint","accoied","accuser","airfare","adviser","bedroom","brother","barrier","battery","banking","century","charity","chicken","complex","council","desktop","diamond","diverse","drawning","dynamic","evident","expense","express","edition","economy","faculty","finance","fortune","freedom","fitness","genetic","gateway","gigabit","gallery","genuine","holiday","history","healthy","highway","hundred","imagine","instant","inquiry","initial","interim","journey","justice","justify","jointly","journal","kingdom","kitchen","knowing","keeping","killing","largely","logical","library","limited","leisure","manager","measure","million","mixture","mystery","natural","nervous","network","neutral","nursing","officer","optical","opinion","outside","organic","package","pattern","phoenix","poverty","problem","quality","quarter","replace","revenue","routine","science","sixteen","station","summary","suspect","telecom","therapy","teacher","tonight","traffic","uniform","utility","unknown","upgrade","unusula","veteran","venture","violent","virtual","victory","warrant","western","weekend","witness","written",
						"absolute","academic","aircraft","artistic","athletic","bachelor","bacteria","bathroom","birthday","building","campaign","category","cellular","catholic","chemical","database","daughter","diameter","director","dramatic","economic","entrance","exercise","equality","exchange","facility","festival","fraction","football","flagship","goodwill","grateful","guardian","generous","governor","hardware","highland","humanity","historic","heritage","ideology","industry","innocent","invasion","isolated","judgment","judicial","junction","japanese","jumpoffs","keyboard","youself","blizzard","skipjack","sizzling","landlord","lifetime","likewise","lighting","laughter","magazine","memorial","midnight","mortgage","mountain","national","negative","nineteen","notebook","numerous","optional","offshore","ordinary","opposite","organize","painting","petition","physical","portrait","powerful","quantity","question","quizzers","register","required","romantic","religion","resigned","sampling","scenario","seasonal","shipping","software","tactical","teaching","terminal","taxpayer","thousand","ultimate","umbrella","universe","unlikely","unlawful","variable","valuable","vertical","violence","volatile","warranty","wildlife","withdraw","workshop","woodland",
						"putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus","putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus","putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus","putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus","putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus","putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus","putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus","putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus","putimestwo","putimestwo","putimestwo","puslow","puslow","puslow","puplus","puplus"]
		
		self.lessKnownWords = {"Abnormous":"Misshapen","Acrasia":"Lack of selfcontrol","Agonous":"Struggling","Agelast":"A person who never laughs","Avatrol":"A bastard","Baithe":"To agree or consent","Balbutiate":"To stutter or stammer","Bogglish":"To be uncertain, doubtful or a wee bit skittish about something","Borborygmus":"A rumbling in the lower intestines","Bloviate":"To speak in a pompous or overbearing way","Cereologist":"A person who specializes in investigating crop circles","Concinnous":"Neat and eloquent","Corrade":"To gather together from many different sources","Cromulent":"Adjective meaning acceptable or legitimate","Cunctipotent":"Having all things","Deglutition":"The act of swallowing","Delitescent":"Hidden or concealed","Discerp":"To tear something apart to shreds","Dyslogistic":"Disapproving","Drumble":"Moving in a slow or sluggish manner","Emacity":"A fondness for buying things","Esquivalience":"A copyright or plagiarism trap","Ergophobic":"Someone who fears work","Epithymy":"Desire or Lust","Faitour":"A cheat, an imposter","Furciferous":"To be like a brat, rascal","Foudroyant":"Adjective meaning thundering noisy","Fleer":"To laugh in a disrespectful or jeering manner","Glaikery":"Foolish conduct","Gnast":"A spark or a snuff of a candle","Gangrel":"A child who is just starting to walk","Halch":"To hug or embrace","Hibernacle":"Winter retreat of a hibernating animal","Hofles":"Unreasonable or Excessive","Infelicific":"To make unhappy","Impignorate":"To pawn or mortgage something","Ichnography":"A building's floorplan","Ithyphallic":"Indecent or obscene","Inunct":"To apply ointment to someone or something","Jectigation":"A movement that's like wagging or trembling","Jargogle":"To confuse or mix things up","Knabble":"To nibble or small bites","Kench":"To laugh really loud","Lethean ":"A state of oblivion or forgetfulness","Lopeholt":"A place that's safe; refuge","Limerance":"The initial exhilarating rush of falling in love; the state of being in love","Luculence":"Beauty; Fineness; orclear certainty","Mesonoxian":"Pertains to midnight","Misogynist":"A person who hates women","Mussitation":"To mutter or murmur","Mundation":"The act of cleaning or the state of being clean","Motatorious":"In constant motion","Naufragate":"To wreck something","Nithing":"A contemptible or despicable  person","Noceur":"A person who stays up late","Nudiustertian":" It means the day before yesterday","Orcast":"Poverty; indigence","Ombrifuge":"A shelter from rain","Oultrepreu":"Extremely brave","Ostrobogulous":"Bizarre,unusual or interesting","Passiuncle":"A petty or contemptible passion","Pelmatogram":"Footprint","Peramene":"Very pleasant","Philopolemical":"Loving to fight","Prufrockian":"A personality type that is timid and indecisive and full of unfulfilled aspirations","Quagswag":"To shake back and forth","Quantophrenia":"An obsessive reliance on mathematical methods or results","Quaclsalver":"A charlatan","Rimbombo":"The sound of a booming roar","Rhinarium":"The hairless and moist nose of some mammals","Rawky":"Foggy,damp and cold","Rhyparographer":"An artist whose subject matter  is sorrowful or unpleasant topics","Scamander":"To wander about","Samentale":"Agreement","Sitooterie":"A summerhouse or gazebo","Sternutation":"The act of sneezing or a sneeze","Theopneust":"Adjective meaning divinely inspired","Troke":"To fail; unable to do something;  or,to deceive","Typhlobasia":"Kissing with the eyes closed","Undaftiness":"Untidiness","Ubiation":"The act of occupying a new place","Velleity":"A wish or inclination that has no action","Visagiste":"A makeup artist","Verticordious":"To turn the heart from evil","Whelve":"To turn something over and hide something underneath","Winebibber":"A person who habitually drinks a lot of alcohol","Xesturgy":"To polish","Xenology":"The study of extraterrestrial phenomena","Yemeles":"Careless; negligent","Yisel":"A hostage","Ziraleet":"Any expression of joy","Zoilist":"A person who takes joy in finding fault"}
		unfamWords = self.lessKnownWords.keys()
		unfamWords = [item.lower() for item in unfamWords]
		self.vocab.extend(unfamWords)
		
		self.adj = ("adventurous","adorable","affectionate","agreeable","alert","beautiful","brilliant","brave","bountiful","beloved","cheerful","cooperative","cudly","creamy","creative","dependable","delicious","delightful","dazzling","diligent","enchanting","ethical","elegant","exemplary","expert","fabulous","funny","fantastic","friendly","fearless","generous","glamorous","gifted","goodnatured","grateful","helpful","healthy","handsome","honest","honorable","idealistic","idolized","incredible","immaculate","intelligent","joyful","jubilant","kindhearted","kind","knowlegeable","lovely","loving","lucky","magnificent","majestic","nice","obedient","outstanding","pretty","dead","suicidal","psychopath","sociopath","murderer","dangerous","fucked","adorable as hell","maggot","stupid","boring","idiotic","idle","illogical","imaginative","immature","immodest","impatient","imperturbable","impetuous","impractical","quarrelsome","ridiculuos","selfish","tired","popular","unpopular","unreliable","obnoxious","pathetic","ugly","numb","naive","clingy","negative","naughty","drunk","belowaverage","dirty","drowsy")
		#self.vocab.extend(self.adj)
		self.vocab = tuple(self.vocab)

		# List of Colors
		self.GOLD = (255,215,0)
		self.BLACK = (0,0,0)
		self.MIDNIGHTBLUE = (25,25,112)
		self.WHITE = (255,255,255)
		self.POWDERBLUE =(176,224,230)
		self.STEELBLUE = (70,130,180)
		self.KHAKI = (240,230,140)
		self.DARKKHAKI = (189,183,107)
		self.LIGHTCYAN = (224,255,255)
		self.DARKCYAN = (0,139,139)
		self.PALEGREEN = (152,251,152)
		self.DARKGREEN = (0,100,0)
		self.LIGHTCORAL = (240,128,128) 
		self.INDIANRED = ((205,92,92))
		self.PALETURQ = (175,238,238)
		self.DARKTURQ = (0,206,209)
		self.CORNSILK = (255,248,220)
		self.SANDYBROWN = (244,164,96)
		self.CHARTREUSE = (127,255,0)
		self.OLIVEDRAB = (107,142,35)
		self.SADDLEBROWN = (139,69,19)
		self.SLATEGRAY = (112,128,144)
		self.THISTLE = 	(216,191,216)
		self.MAROON = (128,0,0)


		# Starting Platform Positions
		self.firstPlatXPos = 250
		self.firstPlatYPos = 200
		
		# The Character Position
		self.charXPos = 285
		self.charYPos = 155
		
		self.platWid = 100
		self.platLen = 10
		
		# Movement of the Platform Downward
		self.platformYPos = 0
		
		# List of Coordinates WRT their Positon
		self.platforms = []
		self.messages = []
		self.word = []


		
		self.music = 'others/Freezing.mp3' 
		# Fonts, Images
		self.supSmallFont = pygame.font.Font('others/ARJULIAN.ttf', 15)
		self.smallFont = pygame.font.Font('others/ARJULIAN.ttf', 25)
		self.medFont = pygame.font.Font('others/ARJULIAN.ttf', 50)
		self.largeFont = pygame.font.Font('others/ARJULIAN.ttf', 100)
		
		self.imgPlat1 = pygame.image.load('others/platform1.png')
		self.wood = pygame.image.load('others/wood.jpg')
		
		self.place1 = pygame.image.load('others/place1.jpg')
		self.place2 = pygame.image.load('others/place2.jpg')
		self.place3 = pygame.image.load('others/place3.jpg')
		self.place4 = pygame.image.load('others/place4.jpg')

		self.thumb1 = pygame.image.load('others/thumb1.jpg')
		self.thumb2 = pygame.image.load('others/thumb2.jpg')
		self.thumb3 = pygame.image.load('others/thumb3.jpg')
		self.thumb4 = pygame.image.load('others/thumb4.jpg')

		self.backG = self.place1
		
		
		self.city = pygame.image.load('others/city.jpg')
		self.tywrt = pygame.image.load('others/typewriter.png')

		self.library = pygame.image.load('others/library.jpg')
		self.qMark = pygame.image.load('others/questionmark.jpg')
		self.imgForYou = pygame.image.load('others/forYou.jpg')
		self.settings = pygame.image.load('others/settings.jpg')


		self.alien1 = pygame.image.load('others/alien1.png')
		self.alien2 = pygame.image.load('others/alien2.png')
		self.joker = pygame.image.load('others/joker.png')
		self.zombie = pygame.image.load('others/zombie.png')
		self.man = pygame.image.load('others/man.png')
		self.woman = pygame.image.load('others/woman.png')

		self.charPlay = self.joker
		self.charPlay = self.zombie

		# Score
		self.score = 0
		#self.platforms.append([self.platformXPos,self.platformYPos])
		
		#self.leader = []
		#self.f = open('leader.txt','r')
		self.leader = [line.strip() for line in open("leader.txt", 'r')]
		
		#self.leader =  self.f.read()
		#self.leader = self.leader.split()
		#self.f.close()
		self.f = open('leader.txt','a+')
		
		#self.leader.append(re)
		pygame.display.set_caption("Type Ko 'To")

		#pygame.display.update()

		self.clock = pygame.time.Clock()

	def scoreOnScreen(self,message, color,xPos,yPos,size = "small"):
		#self.scoreSurf, self.textRect = self.textObj(message,color,size)
		#self.scoreRect.center = (xPos), (yPos)
		self.scoreDisp = self.medFont.render(message, True, color)
		self.screenDisplay.blit(self.scoreDisp, [xPos,yPos])

	def charPlayer(self):
		
		#self.character = pygame.draw.rect(self.screenDisplay, self.BLACK, [self.charXPos,self.charYPos,10,10]) 
		self.character = self.screenDisplay.blit(self.charPlay, [self.charXPos,self.charYPos])
		

	def platDraw(self):
		for p in self.platforms:
			#self.platform = pygame.draw.rect(self.screenDisplay, self.BLACK, [p[0],p[1],self.platWid,self.platLen], 2)		
			self.screenDisplay.blit(self.imgPlat1,[p[0],p[1]])

	def firstPlat(self):
		#pygame.draw.rect(self.screenDisplay,self.BLACK,[self.firstPlatXPos,self.firstPlatYPos,self.platWid,self.platLen],2)	
		self.screenDisplay.blit(self.imgPlat1,[self.firstPlatXPos,self.firstPlatYPos])

	def generatePlat(self):
		self.platformXPos = random.randint(0,(self.width-self.platWid))
		self.platformYPos = 0
		self.platforms.append([self.platformXPos,0])
		self.messages.append([self.platformXPos,25])
									
	def textObj(self,text,color,size):
		if size == "small":
			self.text = self.smallFont.render(text,True,color)
		elif size == "super":
			self.text = self.supSmallFont.render(text,True,color)	
		elif size == "medium":
			self.text = self.medFont.render(text,True,color)
		elif size == "large":
			self.text = self.largeFont.render(text,True,color)
		return self.text, self.text.get_rect() 		

	def messageOnScreen(self,message, color,y_displace = 0,size = "small"):		
		#self.text = self.font.render(message, True, color)
		#self.screenDisplay.blit(self.text, [xPos,yPos])
		self.textSurf, self.textRect = self.textObj(message,color,size)
		self.textRect.center = (self.width / 2), (self.length / 2)+y_displace
		self.screenDisplay.blit(self.textSurf, self.textRect)

	def textOnPlat(self, color):
		message = self.vocab[random.randint(0,len(self.vocab)-1)]
		self.word.append(message)
		self.font = pygame.font.SysFont(None, 30)
		#self.text = self.font.render(message, True, color)
		index = 0
		for m in self.messages:
			self.text = self.font.render(self.word[index], True, color)
			self.screenDisplay.blit(self.text, [m[0],m[1]])		
			index += 1	

	def textArrow(self):
		
		backFont = pygame.font.Font('others/ARJULIAN.ttf',20)
		backText = backFont.render('BACK', True, self.BLACK)
		self.screenDisplay.blit(backText, (40, 40)) 	

	def buttonArrow(self, where = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()

		if 150 > mousePos[0] > 0 and 75 > mousePos[1] > 0:
			pygame.draw.polygon(self.screenDisplay,self.POWDERBLUE,[(150,40),(150,65),(40,65),(40,90),(0,52),(40,0),(40,40)])
			self.clock.tick(100)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
			#if mouseClick[0] == 1 and where != None:
						if where == 'menu':
							self.introGame()
						elif where == 'help':
							self.helpGame()
						elif where == 'trivia':
							self.triviaGame()
						elif where == 'word':
							self.forYouGame()
						elif where == 'settings':
							self.settingsGame()			
						
								
		else:
			pygame.draw.polygon(self.screenDisplay,self.STEELBLUE,[(150,40),(150,65),(40,65),(40,90),(0,52),(40,0),(40,40)])		 	
						
		self.textArrow()

	def textToButton(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty):
		gameFont = pygame.font.Font('others/ARCADECLASSIC.TTF', 50)
		font = gameFont.render(message, True, self.MIDNIGHTBLUE)
		self.screenDisplay.blit(font, [textx,texty])		


	def buttonSettings(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''
		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						#if mouseClick[0] == 1 and action != None:
						if action == "char":
							self.charGame()

						if action == "place":
							self.placeGame()
						if action == "music":		
							self.musicGame()
						if action == "exit":
							self.introGame()									

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))
			

		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)	

	
	def charButtonSettings(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''
		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						#if mouseClick[0] == 1 and action != None:
						if action == "alien1":
							self.charPlay = self.alien1
							self.settingsGame()
						if action == "alien2":
							self.charPlay = self.alien2
							self.settingsGame()
						if action == "joker":		
							self.charPlay = self.joker
							self.settingsGame()
						if action == "zombie":
							self.charPlay = self.zombie
							self.settingsGame()
						if action == "man":
							self.charPlay = self.man
							self.settingsGame()
						if action == "woman":
							self.charPlay = self.woman
							self.settingsGame()

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))
			

		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)						
		

	#def whatChar(self):
	
	#	char = self.charGame()
	#	return char			

	def charGame(self):
		howG = True

		while howG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.settings,[0,0])
			self.buttonArrow(where = 'settings')

			#pygame.draw.rect(self.screenDisplay, self.PALETURQ, [30,80,580,300])

			self.screenDisplay.blit(self.alien1,[150,130])
			self.charButtonSettings('ALIEN 1',100,180,200,40,120,175, self.DARKCYAN, self.LIGHTCYAN, action="alien1")
			
			
			self.screenDisplay.blit(self.alien2,[350,130])
			self.charButtonSettings('ALIEN 2',300,180,200,40, 320,175, self.DARKKHAKI, self.KHAKI, action="alien2")
			
			self.screenDisplay.blit(self.joker,[150,250])
			self.charButtonSettings('JOKER',100,300,200,40, 120,295, self.DARKGREEN, self.PALEGREEN, action="joker")
			
			self.screenDisplay.blit(self.zombie,[350,250])
			self.charButtonSettings('ZOMBIE',300,300,200,40, 320,295, self.SANDYBROWN, self.CORNSILK, action="zombie")
			
			self.screenDisplay.blit(self.man,[150,370])
			self.charButtonSettings('MAN',100,420,200,40, 120,415, self.DARKTURQ, self.PALETURQ, action="man")

			self.screenDisplay.blit(self.woman,[350,370])
			self.charButtonSettings('WOMAN',300,420,200,40, 320,415, self.OLIVEDRAB, self.CHARTREUSE, action="woman")
			
			#self.messageOnScreen("Unlike Doodle Jump's gameplay on which ",self.SADDLEBROWN,-250,'small')

			howFont = pygame.font.Font('others/ARCADECLASSIC.TTF',50)
			howText = howFont.render('CHOOSE YOUR CHARACTER', True, self.GOLD)
			self.screenDisplay.blit(howText,[100,500])			

			pygame.display.update()
			self.clock.tick(30)	
				
	def placeButtonSettings(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''
		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						#if mouseClick[0] == 1 and action != None:
						if action == "thumb1":
							self.backG = self.place1
							self.settingsGame()
						if action == "thumb2":
							self.backG= self.place2
							self.settingsGame()
						if action == "thumb3":		
							self.backG = self.place3
							self.settingsGame()
						if action == "thumb4":
							self.backG = self.place4
							self.settingsGame()
					

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))
			

		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)	

	

	def placeGame(self):
		
		howG = True

		while howG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.settings,[0,0])
			self.buttonArrow(where = 'settings')

			#pygame.draw.rect(self.screenDisplay, self.PALETURQ, [30,80,580,300])

			self.screenDisplay.blit(self.thumb1,[150,130])
			self.placeButtonSettings('DESSERT',100,180,210,40,120,175, self.DARKCYAN, self.LIGHTCYAN, action="thumb1")
			
			
			self.screenDisplay.blit(self.thumb2,[400,130])
			self.placeButtonSettings('SUNSET',400,180,200,40, 420,175, self.DARKKHAKI, self.KHAKI, action="thumb2")
			
			
			self.screenDisplay.blit(self.thumb3,[150,370])
			self.placeButtonSettings('ABANDONED',100,420,280,40, 120,415, self.DARKTURQ, self.PALETURQ, action="thumb3")

			self.screenDisplay.blit(self.thumb4,[400,370])
			self.placeButtonSettings('MOUNTAIN',400,420,260,40, 420,415, self.OLIVEDRAB, self.CHARTREUSE, action="thumb4")
			
			#self.messageOnScreen("Unlike Doodle Jump's gameplay on which ",self.SADDLEBROWN,-250,'small')

			howFont = pygame.font.Font('others/ARCADECLASSIC.TTF',50)
			howText = howFont.render('CHOOSE YOUR PLACE', True, self.GOLD)
			self.screenDisplay.blit(howText,[100,500])			

			pygame.display.update()
			self.clock.tick(30)	
	
						
	def musicButtonSettings(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''
		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						#if mouseClick[0] == 1 and action != None:
						if action == "prophecy":
							self.music = 'others/A Prophecy.mp3'
							self.settingsGame()
						if action == "freezing":
							self.music = 'others/Freezing.mp3'
							self.settingsGame()
						if action == "i wont":		
							self.music = 'others/I Wont.mp3'
							self.settingsGame()
						if action == "chemical":
							self.music = 'others/Chemical Plant.mp3'
							self.settingsGame()
						if action == "miserable":
							self.music = 'others/Miserable.mp3'
							self.settingsGame()
						if action == "uptown":
							self.music = 'others/Uptown.mp3'
							self.settingsGame()	

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))
			

		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)						
		

	#def whatChar(self):
	
	#	char = self.charGame()
	#	return char			

	def musicGame(self):
		howG = True

		while howG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.settings,[0,0])
			self.buttonArrow(where = 'settings')

			#pygame.draw.rect(self.screenDisplay, self.PALETURQ, [30,80,580,300])

			
			self.musicButtonSettings('A Prophecy',100,180,500,40,220,175, self.DARKCYAN, self.LIGHTCYAN, action="prophecy")
			
			
			
			self.musicButtonSettings('Freezing Moon',100,240,500,40, 220,235, self.DARKKHAKI, self.KHAKI, action="freezing")
			
			
			self.musicButtonSettings('I Wont Give Up',100,300,500,40, 220,295, self.DARKGREEN, self.PALEGREEN, action="i wont")
			
			
			self.musicButtonSettings('Miserable at Best',100,360,500,40, 100,355, self.SANDYBROWN, self.CORNSILK, action="miserable")
			
			
			self.musicButtonSettings('Uptown Funk',100,420,500,40, 220,415, self.DARKTURQ, self.PALETURQ, action="uptown")

			
			self.musicButtonSettings('Chemical Plant',100,480,500,40, 220,475, self.OLIVEDRAB, self.CHARTREUSE, action="chemical")



			#self.messageOnScreen("Unlike Doodle Jump's gameplay on which ",self.SADDLEBROWN,-250,'small')

			howFont = pygame.font.Font('others/ARCADECLASSIC.TTF',50)
			howText = howFont.render('CHOOSE YOUR MUSIC', True, self.GOLD)
			self.screenDisplay.blit(howText,[100,600])			

			pygame.display.update()
			self.clock.tick(30)		

	

	def settingsGame(self):

		self.settingsG = True

		while self.settingsG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.settings,[0,0])
			self.buttonArrow(where = 'menu')

			self.buttonSettings('CHARACTERS',150,180,350,40, 190,175, self.DARKKHAKI, self.KHAKI, action="char")
			self.buttonSettings('PLACE',150,230,350,40, 240,225, self.DARKGREEN, self.PALEGREEN, action="place")
			self.buttonSettings('MUSIC',150,280,350,40, 280,275, self.SANDYBROWN, self.CORNSILK, action="music")
			self.buttonSettings('EXIT',150,380,350,40,170,375,self.INDIANRED, self.LIGHTCORAL, action = 'exit' )

			pygame.display.update()
			self.clock.tick(30)	

	
	def buttonHelp(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''
		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						#if mouseClick[0] == 1 and action != None:
						if action == "how":
							self.howToPlay()
							
						if action == "about":
							self.aboutPlay()
							
						if action == "exit":
							self.introGame()
											

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))
			

		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)	

						

	def howToPlay(self):
		howG = True

		while howG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.library,[0,0])
			self.buttonArrow(where = 'help')
			pygame.draw.rect(self.screenDisplay, self.PALETURQ, [30,80,580,300])

			self.messageOnScreen("Unlike Doodle Jump's gameplay on which ",self.SADDLEBROWN,-250,'small')
			self.messageOnScreen("player should tilt the device",self.SADDLEBROWN,-230,'small')
			self.messageOnScreen("to move on one platform into another or ",self.SADDLEBROWN,-210,'small')
			self.messageOnScreen("in other case, it uses arrow keys,",self.SADDLEBROWN,-190,'small')
			self.messageOnScreen("Type Ko 'To's gameplay includes typing words ",self.SADDLEBROWN,-170,'small')
			self.messageOnScreen("to move on one platform into another.",self.SADDLEBROWN,-150,'small')
			self.messageOnScreen("If the player types the next word",self.SADDLEBROWN,-130,'small')
			self.messageOnScreen("incorrectly, he/she should type again",self.SADDLEBROWN,-110,'small')
			self.messageOnScreen("the whole word. ",self.SADDLEBROWN,-90,'small')
			self.messageOnScreen("The player should strictly type the words  ",self.SADDLEBROWN,-70,'small')
			self.messageOnScreen("in order of its appearance.",self.SADDLEBROWN,-50,'small')
			self.messageOnScreen("It will be considered wrong if the ",self.SADDLEBROWN,-30,'small')
			self.messageOnScreen("player type the word even if there is",self.SADDLEBROWN,-10,'small')
			self.messageOnScreen("another word that went first to it.",self.SADDLEBROWN,10,'small')

			howFont = pygame.font.Font('others/ARCADECLASSIC.TTF',100)
			howText = howFont.render('HOW TO PLAY', True, self.GOLD)
			self.screenDisplay.blit(howText,[100,500])			

			pygame.display.update()
			self.clock.tick(30)	

	def aboutPlay(self):
		aboutG = True

		while aboutG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.library,[0,0])
			self.buttonArrow(where = 'help')

			pygame.draw.rect(self.screenDisplay, self.PALEGREEN, [30,80,580,300])

			self.messageOnScreen("Type Ko 'To is a platforming video game",self.SADDLEBROWN,-250,'small')
			self.messageOnScreen("based on Doodle Jump, Papijump and ",self.SADDLEBROWN,-230,'small')
			self.messageOnScreen("Typing Master. The goal of this game ",self.SADDLEBROWN,-210,'small')
			self.messageOnScreen("is to guide the playing character on ",self.SADDLEBROWN,-190,'small')
			self.messageOnScreen("a never-ending series of platforms ",self.SADDLEBROWN,-170,'small')
			self.messageOnScreen("without the bottom of the screen ",self.SADDLEBROWN,-150,'small')
			self.messageOnScreen("reaching the character. Players ",self.SADDLEBROWN,-130,'small')
			self.messageOnScreen("should type in order of the words",self.SADDLEBROWN,-110,'small')
			self.messageOnScreen("that correspond to each platforms",self.SADDLEBROWN,-90,'small')
			self.messageOnScreen("that will appear. The longer the player plays, ",self.SADDLEBROWN,-70,'small')
			self.messageOnScreen("the faster of the pace will be,",self.SADDLEBROWN,-50,'small')
			self.messageOnScreen("thus increasing its difficulty.",self.SADDLEBROWN,-30,'small')
			self.messageOnScreen(" The game will end if the bottom of",self.SADDLEBROWN,-10,'small')
			self.messageOnScreen("the screen reaches the playing character.",self.SADDLEBROWN,10,'small')
			self.messageOnScreen("",self.SADDLEBROWN,10,'small')

			aboutFont = pygame.font.Font('others/ARCADECLASSIC.TTF',100)
			aboutText = aboutFont.render('ABOUT', True, self.GOLD)
			self.screenDisplay.blit(aboutText,[100,400])
	
			pygame.display.update()
			self.clock.tick(30)			

	
	def helpGame(self):

		self.helpG = True

		while self.helpG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.library,[0,0])
			self.buttonArrow(where = 'menu')

			self.buttonHelp('HOW TO PLAY',150,230,350,40,170,225,self.DARKCYAN, self.LIGHTCYAN, action = 'how' )
			self.buttonHelp('ABOUT',150,280,350,40,280,275,self.INDIANRED, self.LIGHTCORAL, action = 'about' )
			self.buttonHelp('EXIT',150,380,350,40,170,375,self.DARKKHAKI, self.KHAKI, action = 'exit' )

			pygame.display.update()
			self.clock.tick(30)		
		

	def wordForYou(self):
		wordG = True

		word = self.adj[random.randint(0,len(self.adj)-1)]
		
		while wordG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.imgForYou,[0,0])
			self.buttonArrow(where = 'word')

			pygame.draw.rect(self.screenDisplay, self.THISTLE, [30,80,580,300])

			self.messageOnScreen("You are",self.MAROON,-230,'large')
			self.messageOnScreen(word,self.MAROON,-150,'medium')
			self.messageOnScreen("Yeah, we all know",self.MAROON,-20,'super')

			pygame.draw.rect(self.screenDisplay, self.LIGHTCORAL, [30,420,610,100])
			aboutFont = pygame.font.Font('others/ARCADECLASSIC.TTF',80)
			aboutText = aboutFont.render('You are busted', True, self.GOLD)
			self.screenDisplay.blit(aboutText,[50,430])
	
			pygame.display.update()
			self.clock.tick(15)	

	def buttonForYou(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''
		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						#if mouseClick[0] == 1 and action != None:
						if action == "word":
							self.wordForYou()
							
						if action == "exit":
							self.introGame()
											

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))
			

		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)	

						

	def forYouGame(self):

		self.forYouG = True

		while self.forYouG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.imgForYou,[0,0])
			self.buttonArrow(where = 'menu')

			self.buttonForYou('I HAVE A WORD FOR YOU',130,230,500,40,150,225,self.INDIANRED, self.LIGHTCORAL, action = 'word' )
			self.buttonForYou('EXIT',150,380,480,40,170,375,self.DARKKHAKI, self.KHAKI, action = 'exit' )

			pygame.display.update()
			self.clock.tick(30)	

	def wordTrivia(self):
		wordG = True

		less = self.lessKnownWords.items()
		word,defi = less[random.randint(0,len(less)-1)]
		
		while wordG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.qMark,[0,0])
			self.buttonArrow(where = 'trivia')

			pygame.draw.rect(self.screenDisplay, self.THISTLE, [30,80,580,300])

			self.messageOnScreen(word,self.MAROON,-230,'large')
			self.messageOnScreen("means",self.MAROON,-150,'small')
			self.messageOnScreen(defi,self.MAROON,-120,'super')

			pygame.draw.rect(self.screenDisplay, self.LIGHTCORAL, [30,420,610,100])
			aboutFont = pygame.font.Font('others/ARCADECLASSIC.TTF',100)
			aboutText = aboutFont.render('DID YOU KNOW', True, self.GOLD)
			self.screenDisplay.blit(aboutText,[50,400])
	
			pygame.display.update()
			self.clock.tick(15)	

	def buttonTrivia(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''
		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						#if mouseClick[0] == 1 and action != None:
						if action == "know":
							self.wordTrivia()
							
						if action == "exit":
							self.introGame()
											

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))
			

		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)	

						

	def triviaGame(self):
		self.triviaG = True

		while self.triviaG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.qMark,[0,0])
			self.buttonArrow(where = 'menu')

			self.buttonTrivia('DID YOU KNOW?',150,230,350,40,170,225,self.DARKGREEN, self.PALEGREEN, action = 'know' )
			self.buttonTrivia('EXIT',150,380,350,40,170,375,self.SANDYBROWN, self.CORNSILK, action = 'exit' )

			pygame.display.update()
			self.clock.tick(30)	

	def buttonOver(self,message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''
		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						
						if action == "play":
							TheGame().run()
							
						if action == "exit":
							pygame.quit()
							quit()
											

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))
			

		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)	

	def overMenu(self):
		self.overG = True

		while self.overG:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			pygame.draw.rect(self.screenDisplay,self.DARKTURQ,[50,230,530,230])

			self.buttonOver('PLAY AGAIN',150,230,350,40,170,225,self.DARKCYAN, self.LIGHTCYAN, action = 'play' )
			self.buttonOver('EXIT',150,280,350,40,170,275,self.INDIANRED, self.LIGHTCORAL, action = 'exit' )

			pygame.display.update()
			self.clock.tick(30)

	def overGame(self):

		name = ''
		over = True
		#events = pygame.event.get()
		
		pygame.draw.rect(self.screenDisplay,self.DARKTURQ,[50,230,530,280])
		self.messageOnScreen("Game Over",self.BLACK,-100,size = "medium")
		if 300 >= self.score:
			self.messageOnScreen("BOOO! NOOB",self.BLACK,-50,size = "medium")
		elif 750 >= self.score > 300:
			self.messageOnScreen("PRACTICE PA",self.BLACK,-50,size = "medium")
		elif 1500 >= self.score > 750:
			self.messageOnScreen("UHM SIGE PEDE NA",self.BLACK,-50,size = "medium")
		elif 2000 >= self.score > 1500:
			self.messageOnScreen("OKAY MEDYO MAGALING KA",self.BLACK,-50,size = "medium")	
		elif self.score > 2000:
			self.messageOnScreen("GALING MO NAMAN PO",self.BLACK,-50,size = "medium")			 	
		self.messageOnScreen("Your Score: ",self.BLACK,-10,size = "medium")
		self.messageOnScreen(str(self.score),self.BLACK,30,size = "medium")
		self.messageOnScreen("What is your name? ",self.BLACK,70,size = "medium")	

		while over:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.unicode.isalpha():
						name += event.unicode
						#pygame.display.update()
					elif event.key == pygame.K_BACKSPACE:
						name = name[:-1]

						#pygame.display.update()
					elif event.key == pygame.K_RETURN:
						tu = (name,self.score)

						
						self.f.write("%s\n" %str(tu))
						self.overMenu()
						#pygame.display.update()

					#if event.key == pygame.K_p:
					#	self.gameOver = False
						#print "ulit"
					#	TheGame().run()	

					#if event.key == pygame.K_q:
					#	self.gameExit = True
					#	self.gameOver = False
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				
					
				
			typeFont = pygame.font.SysFont(None, 50)
			nameText = typeFont.render(name, True, self.WHITE)
			rect = nameText.get_rect()
			rect.center = self.screenDisplay.get_rect().center
			self.screenDisplay.blit(nameText, [200,450])		
			
			pygame.display.update()
 				

			self.clock.tick(15)			
	
	def leaderboard(self):
		leaderFont = pygame.font.SysFont(None, 50)
		
		
		leader = True
		self.screenDisplay.blit(self.wood,[0,0])
		self.messageOnScreen("Leaderboard:",self.WHITE,-230,"medium")
		a = 0
		name = []
		score = []
		l = []

	
		for pair in self.leader:
			extract = pair[2:-1]
			l.append(extract)
			exName,exScore = l[a].split()
			name.append(exName)
			score.append(exScore)
			a += 1
		
		score = [ int(x) for x in score]
		highScore = sorted(score, reverse = True)
		highName = []
	

		for x in highScore:
			a = 0
			for y in score:
				if x == y:
					highName.append(name[a])
				a += 1

		height = 160
		add = 0		
		for x in range(len(highScore)):
			leaderText = leaderFont.render(str(x+1), True, self.WHITE)		
			self.screenDisplay.blit(leaderText, [30,height+add])
			
			leaderText = leaderFont.render("-", True, self.WHITE)		
			self.screenDisplay.blit(leaderText, [85,height+add])

			leaderText = leaderFont.render((highName[x][:-1]), True, self.WHITE)
			self.screenDisplay.blit(leaderText, [100,height+add])

			leaderText = leaderFont.render(": ", True, self.WHITE)
			self.screenDisplay.blit(leaderText, [480,height+add])		

			leaderText = leaderFont.render((str(highScore[x])), True, self.WHITE)
			self.screenDisplay.blit(leaderText, [500,height+add])

			add += 50
			if x == 9:
				break
					
		#print name	
		#print self.leader
		pygame.display.update()

		while leader:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()


			

				
			
			self.buttonArrow(where = 'menu')		
			
			pygame.display.update()	
			#self.screenDisplay.fill(self.GOLD)
			self.clock.tick(10)	

	def run(self):
		pygame.mixer.music.load(self.music)
		pygame.mixer.music.play(-1)

		self.gameExit = False
		self.gameOver = False		
		self.platformYMove = 0
		#self.generatePlat()
		self.i = 0
		self.FPS = 8
		self.a = 0
		self.b = 0
		self.name = ''
		self.wordThatType = ''
		#txtbx = eztext.Input(maxlength=45, color = self.WHITE, prompt='type here')

		while not self.gameExit:			

			self.i += 1
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.type == pygame.KEYDOWN:
						#if event.key == pygame.K_p:
						#	self.pauseGame()
						if event.unicode.isalpha():
							self.wordThatType += event.unicode
						elif event.key == pygame.K_BACKSPACE:
							self.wordThatType = self.wordThatType[:-1]
						elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
							if self.wordThatType == self.word[self.b]:
								if self.word[self.b][:2] == 'pu':
									if self.word[self.b][2:] == "timestwo":
										
										self.score = self.score * 2
									if self.word[self.b][2:] == "slow":
										
										self.FPS = self.FPS - 2
									if self.word[self.b][2:] == "plus":
										
										self.score += 10000		

								self.wordThatType = ""
								self.score += 50
								self.charXPos = self.platforms[self.a][0] + 45
								self.charYPos = self.platforms[self.a][1] - 50
								self.a += 1		
							else:
								self.wordThatType = ""
								self.b -= 1	
							self.b += 1	
		
				if event.type == pygame.QUIT:
					self.gameExit = True
				
				self.platformYMove = 5

			if self.charYPos >= self.length+10:
				self.overGame()
			
			
				
			#self.screenDisplay.fill(self.GOLD)	
			self.screenDisplay.blit(self.backG,(0,0))
			self.scoreOnScreen("Score:",self.WHITE,0,0)

			self.typeFont = pygame.font.SysFont(None, 50)
			self.block = self.typeDisplay = self.typeFont.render(self.wordThatType, True, self.WHITE)
			self.typeHere = self.typeFont.render('TYPE HERE: ', True, self.WHITE)
			self.rect = self.block.get_rect()
			self.rect.center = self.screenDisplay.get_rect().center
			self.screenDisplay.blit(self.typeHere, [50,650])
			self.screenDisplay.blit(self.block, [300,650])
			
			#if self.i != 0 and self.i%36 == 0:
			#	self.charXPos = self.platforms[self.a][0] + 45
			#	self.charYPos = self.platforms[self.a][1] - 13
			#	self.a += 1

			self.firstPlatYPos += self.platformYMove	
			self.firstPlat()
			self.charYPos += self.platformYMove
			#self.charGame()
			self.charPlayer()

			for p in self.platforms:
				p[1] += self.platformYMove
			for m in self.messages:
				m[1] += self.platformYMove 
			if self.i != 0 and self.i%10 == 0:
				self.score += 5
			
			if self.firstPlatYPos > 400:
				if self.i != 0 and self.i%20 == 0:
					self.generatePlat()
				self.scoreOnScreen(str(self.score),self.WHITE,140,0)
				self.platDraw()
				self.textOnPlat(self.WHITE)
				pygame.display.update()

			if self.i != 0 and self.i%200 == 0:
				if self.FPS == 19:
					self.FPS = 19
				else:
					self.FPS += 1	
			
			self.clock.tick(self.FPS)

		pygame.quit()
		quit()

	def buttonIntro(self, message, buttonx, buttony, buttonwidth, buttonheight, textx, texty, darkercolor, lightcolor, action = None):
		mousePos = pygame.mouse.get_pos()
		mouseClick = pygame.mouse.get_pressed()
		place = ''

		if buttonx + buttonwidth > mousePos[0] > buttonx and buttony + buttonheight > mousePos[1] > buttony:
			pygame.draw.rect(self.screenDisplay, lightcolor, (buttonx,buttony,buttonwidth,buttonheight))
			self.clock.tick(20)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
			#if mouseClick[0] == 1 and action != None:
						if action == "play":
							self.run()
						if action == "trivia":
							self.triviaGame()
						if action == "word":
							self.forYouGame()	
						if action == "help":
							self.helpGame()
						if action == "settings":
							self.settingsGame()
						if action == "leader":
							self.leaderboard()
						if action == "exit":
							pygame.quit()
							quit()						

		else:
			pygame.draw.rect(self.screenDisplay, darkercolor, (buttonx,buttony,buttonwidth,buttonheight))			

		
		self.textToButton(message,buttonx,buttony,buttonwidth,buttonheight,textx,texty)	

	def introGame(self):
		gameFont = pygame.font.Font('others/ARCADECLASSIC.TTF', 50)
		titleFont = pygame.font.Font('others/RAVIE.TTF', 50)
		intro = True

		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screenDisplay.blit(self.city,[0,0])
			
			self.screenDisplay.blit(self.tywrt,[450,550])
			
			titleGame = titleFont.render("TYPE  KO  TO", True, self.GOLD)
			self.screenDisplay.blit(titleGame, [120,70])

			self.buttonIntro('PLAY',150,130,350,40, 280,125, self.DARKCYAN, self.LIGHTCYAN, action="play")
			self.buttonIntro('TRIVIA',150,180,350,40, 240,175, self.DARKKHAKI, self.KHAKI, action="trivia")
			self.buttonIntro('WORD FOR YOU',150,230,350,40, 170,225, self.DARKGREEN, self.PALEGREEN, action="word")
			self.buttonIntro('HELP',150,280,350,40, 280,275, self.SANDYBROWN, self.CORNSILK, action="help")
			self.buttonIntro('SETTINGS',150,330,350,40, 230,325, self.DARKTURQ, self.PALETURQ, action="settings")
			self.buttonIntro('LEADERBOARD',150,380,350,40, 170,375, self.OLIVEDRAB, self.CHARTREUSE, action="leader")
			self.buttonIntro('EXIT',150,430,350,40, 280,425, self.INDIANRED, self.LIGHTCORAL, action="exit")

			pygame.display.update()
			self.clock.tick(30)


TheGame().introGame()
TheGame().f.close()