### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# the __init__ function is missing... need to add def __init__(self, cardlist) and any other parameters or attributes
#Also need to assign variable e.g. self.cardlist =[];


  def check_for_ace(self, card):
    if card.value = 1: #will need to import the Card class to use its methods otherwise it won't recognise .value 
      #Also need to use double equals card.value == 1,  not card.value=1.
      return True
    else
      return False
   

  dif highest_card(self, card1 card2): #def keyword required for creating a function is missing here
  if card1.value > card2.value: 
    return card #typo, should be card1, not card
  else:
    return card2
  


def cards_total(self, cards): #could the lack of indentation here throw up an error?
  total #this line seems incomplete, should it be total=0 ?
  for card in cards: 
    total += card.value
    return "You have a total of" + total
  
```
