class Allergies:
    ALLERGIES_SCORE = ['cats', 'pollen', 'chocolate', 
            'tomatoes', 'strawberries', 'shellfish',
            'peanuts', 'eggs']

    def __init__(self, score):
        self.score = '{0:08b}'.format(score)[-8:]

    @property
    def allergens(self):
        return zip(self.ALLERGIES_SCORE, self.score)

    @property
    def lst(self):
        only_true = filter(lambda x: bool(int(x[1])), self.allergens)
        return [x[0] for x in only_true]

    def is_allergic_to(self, name):
        return dict(self.allergens)[name]== '1'
