import pygame, random #Imports the modules we need

pygame.init() #Initializes pygame

def striplist(l):
    return([x.strip() for x in l])

def openit(name):
    f = open()# I think this should be f = open(name)
    return striplist(f.readlines())

width,height = (640,480) #Sets the variable width to 640 and the variable height to 480. These numbers represent the number                                 #                         of pixels
screen = pygame.display.set_mode((width,height)) # Creates a surface and assigns the tag "screen" to it

def get_words(text): # This finds the words inside the text
    for i in text:
        if len(i.split()) > 5: # If the amount of letters in i is more than 5 then...
        words.extend(i.split()) # Add those letters to the words list!

def clean_text(remove = [',','.','@','%','#','$','*','(',')','^']): # This function removes unwanted characters from our text
    I = 0
    for i in lines:
        lines[I] = filter(lambda x: x not in remove,i)
        I += 1

class TypingGameWord(pygame.sprite.Sprite): # This is the class for words that will display them on screen
   
    def __init__(self, word): # This Initializes the object
        pygame.sprite.Sprite.__init__(self) # Initalizes the sprite object so that self inherits the functions and attributes #                                             from the sprite class
        self.font = pygame.font.Font(None,100) # Makes the font object
        self.originalWord = word
        self.word = word
        self.updateSurface()
    
    def checkLetter(self, letter):
        "Checks a letter that the player typed.  Returns true if the word is empty, otherwise false."
        if letter == self.word[0]:
            self.word = self.word[1:]
            self.updateSurface()
        return self.word == ""
    
    def updateSurface(self): # Updates the object
        self.image = self.font.render(self.word, True, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (320,240)

running = True

word= TypingGameWord("Test!") #set our initial word
while running: # The main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False # Ends the program
            else:
                if word.checkLetter(event.unicode): #event.unicode is the letter the user typed
                    word = TypingGameWord("Another test!")
    screen.fill((0,0,0)) # Colors the screen black
    screen.blit(word.image, word.rect) # Puts the word on the screen
    pygame.display.flip() #Updates the screen

pygame.quit() # Bye bye!
