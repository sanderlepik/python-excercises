'''Script to evaluate poker hands'''
import re


class BestPokerHand:

    def __init__(self, poker_hands):
        self.poker_hand_list = poker_hands.split()

        self.card_ranks = {'2': 1,
                      '3': 2,
                      '4': 3,
                      '5': 4,
                      '6': 5,
                      '7': 6,
                      '8': 7,
                      '9': 8,
                      '10': 9,
                      'J': 10,
                      'Q': 11,
                      'K': 12,
                      'A': 13}

        print "All the poker hands are: "
        for poker_hand in self.poker_hand_list:
            print poker_hand

    def rank_hands(self):
        '''
        This function tries to evaluate hand and if it fails caused by 10 in the hand, then splits numbers from letters and evaluates hand again
        :return: highest_ranked_hand
        '''
        highest_rank = 0
        highest_ranked_hand = ""

        for poker_hand in self.poker_hand_list:
            try:
                first_card = list(poker_hand)[0]
                second_card = list(poker_hand)[1]
                rank = self.card_ranks[first_card] + self.card_ranks[second_card]
                if rank > highest_rank:
                    highest_rank = rank
                    highest_ranked_hand = poker_hand

            except KeyError:
                poker_hand = re.split('(\d+)', poker_hand)
                first_card = poker_hand[0]
                second_card = poker_hand[1]
                rank = self.card_ranks[first_card] + self.card_ranks[second_card]
                if rank > highest_rank:
                    highest_rank = rank
                    highest_ranked_hand = poker_hand

        print "The best poker hand is: " + highest_ranked_hand
        return highest_ranked_hand

if __name__ == "__main__":
    poker_hands = BestPokerHand('AA 68 AQ 5K A10')
    poker_hands.rank_hands()