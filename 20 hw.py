# Домашнее задание
# Реализуйте итератор колоды карт (52 штуки) CardDeck.
# Каждая карта представлена в виде строки типа «2 Пик».
# При вызове функции next() будет представлена
# следующая карта. По окончании перебора всех
# элементов возникнет ошибка StopIteration

CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_SUITS = ['pik', 'tref', 'chervi', 'bybni']

class CardDeck:

  def __init__(self, number):
      self.suit, self.value = divmod(number, 13)

  def __str__(self):
    return CARD_VALUES[self.value] + ' ' + CARD_SUITS[self.suit]

  def __repr__(self):
    return str(self)


iter_obj = []
#колода карт


#1
for i in range(52):
    iter_obj.append(CardDeck(i))
print(iter_obj)
print('******' * 10)


class IterStop:

    def __iter__(self):
        self.card_i = 0
        return self

    def __next__(self):
        if self.card_i < 52:
            next_card = iter_obj[self.card_i]
            self.card_i += 1
            return next_card
        else:
            raise StopIteration


#2
newDeck = IterStop()
Deck = iter(newDeck)
for i in Deck:
    print(i)

print('******' * 10)


#3
iter_obj = iter(iter_obj)
while True:
    try:
        i = next(iter_obj)
        print(i)
    except StopIteration:
        break



