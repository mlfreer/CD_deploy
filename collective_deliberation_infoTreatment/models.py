
from __future__ import division

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as cu, currency_range
)

import random
import decimal
import random
import otree.models


doc = "The experiment consists of 15 rounds. Before making any decision, subjects will be randomly divided into groups of three players. The groups may change from round to round. Members within the group will be able to exchange information about a task, but the identities, earnings, group membership and decisions will not be revealed to other participants. \nEach group of three participants will be asked to decide whether to invest in a project in each round. Two colors, gray and orange, identify different projects. The computer selects one of the colors with a probability of 50% each. We refer to this color as the state of the world. When a project's color matches the randomly selected color, the project delivers a high payoff. Otherwise, it delivers a small payoff. In the experiment, payoffs are given in an experimental currency unit, converted into US dollars at the end.\nTwo out of three members of each group will receive a private evidence about the state of world color. In one treatment, there is one additional public evidence available to all members. Each evidence matches the color of the state of the world with a 60% probability.  For instance, the state of the world is orange, then each of the private and the public evidences has a 60% probability of being orange and a 40% probability of being gray. \nAfter this, the experiment has three stages. In the first stage,  participants will be able to share opinions about what project the group should invest. They decide on one of the two colors available. In the second stage, participants will be able to disclose their private evidences at a cost E$ 5. They decide whether to disclose their private information. Finally, in the third stage, each group member will be asked to vote for one of the two projects. The project that gets two or more votes becomes the implemented project. After decisions have been made, participants are allowed to know the true state of the world, and the round earnings are determined.\nAt each stage, participants have a screen with click options for each alternative, and circles of color gray or orange constitute the evidences. There is no other form of communication in the experiment. At the end of each round, earnings for that round and states of the world will be displayed.\nEach session is expected to last under 90 minutes, including the payments. Subjects can earn between 10 and 100 experimental dollars (depending on decisions and randomly assigned states of the world), but are expected to earn about $11 USD on average (not including the show-up fee). Total payoff for each subject is determined only by her earnings in one randomly selected round. The computer will randomly pick the payment round for each subject, and the payoff will be displayed to the subject. Each subject will then be paid privately according to the rate 1 experimental dollar = 20 cents USD. Participating subjects will be taken to a Google Form after the experiment to fill out their payment information as well.    \n"
class Constants(BaseConstants):
    name_in_url = 'collective_deliberation_infoTreatment'
    players_per_group = 3
    num_rounds = 15
    disclose_cost = 5
    high_payoff = 110
    low_payoff = 10
    weights_evidences = (0.6, 0.4)

    paying_round= random.randint(1,num_rounds)
    exchange_rate = 5 #exchange rate tokens to dollars
    showup_fee = cu(10)

class Subsession(BaseSubsession):
      
    def get_start(self):
        """
        Gets the next round ready to run
        """
        for g in self.get_groups():
            g.get_start()
                                   
            for p in g.get_players():
                p.set_evidences()
        # Let's do this at the end        
        #if self.round_number == Constants.num_rounds:
            #for g in self.get_groups():
            #   g.final_payoff()

    def creating_session(self):
        self.group_randomly()  # I think that this reshuffles the groups.... but i am not sure.
        self.get_start()
        for p in self.get_players():
            p.get_mynumber()
    


class Group(BaseGroup):
    # variables:
    # -- state of the worlds
    # -- results of the opinion
    # -- results of disclosure
    # -- results of the voting
    # -- realization [voting x state of the world] ? 
    # -- public(ized) evidence [we need to store all the evidence which has been made public]

    # functions:
    # set/get (initiation)
    # aggregate the opinion
    # aggreagte the disclosure
    # aggreagate the voting
    # compute the outcome (realization)
    # compute the final payoff... 

    state_of_world = models.IntegerField()
    public_evidence = models.IntegerField()
    str_public_evidence = models.StringField() # evidence in words (for presentation)
    correct_guess = models.BooleanField(initial=False)
    group_guess = models.IntegerField()
    str_group_guess = models.StringField() # in words (for presentation)

    #voting in the opinion stage
    opinions_result1 = models.StringField()
    opinions_result2 = models.StringField()
    opinions_result3 = models.StringField()
    #opinions_result4 = models.StringField()
    #opinions_result5 = models.StringField()
    # im still not sure that we should have it as string, since the decision variables are integers

    # disclosure decision
    disclosure_decision1 = models.StringField()
    disclosure_decision2 = models.StringField()
    disclosure_decision3 = models.StringField()
    #disclosure_decision4 = models.StringField()
    #disclosure_decision5 = models.StringField()

    # Diclodure information/outcome, what the player is disclosing
    disclosure_information1 = models.StringField(initial = 'None')
    disclosure_information2 = models.StringField(initial = 'None')
    disclosure_information3 = models.StringField(initial = 'None')
    #disclosure_information4 = models.StringField(initial = 'None')
    #disclosure_information5 = models.StringField(initial = 'None')
    
    # final votes? yes, these are final votes.
    gray_votes = models.IntegerField()

    def get_start(self):
        """ 
        Sets the state of the world and draws the public evidence
        """

        # generating the state of the world
        self.state_of_world = random.choice([-1, 1]) # -1 means Gray  and 1 means Orange
        
        # generating the piece of public evidence
        list_choice = [self.state_of_world, (-1)*self.state_of_world] 
        random_list = random.choices(list_choice, weights= Constants.weights_evidences)
        self.public_evidence = random_list[0]

        if self.public_evidence == -1 : # here we are simply defining the public evidence in words for presentation
            self.str_public_evidence = 'Gray'
        else:
            self.str_public_evidence = 'Orange'
        p_number = []
        
   
   
    def get_results_opinion(self):
        """
        Get the result variables from the opinion stage 
        """
        list_p = []

        for p in self.get_players():
            
            if p.opinion== 1:
                list_p.append('Orange')
            if p.opinion== -1:
                list_p.append('Gray')
            if p.opinion== 0:
                list_p.append('No answer')
        
        # saving the results of the opinio
        self.opinions_result1 = list_p[0]
        self.opinions_result2 = list_p[1]
        self.opinions_result3 = list_p[2]
        #self.opinions_result4 = list_p[3]
        #self.opinions_result5 = list_p[4]
         

    def get_results_disclose(self):
        """
        Get the result variables from the disclose stage
        """
        list_d = [] # what is this variable for?
        list_c = [] # what is this variable for?

        for p in self.get_players():

            if p.disclose== 0:
                list_d.append('does not disclose')
                list_c.append('None')
            if p.disclose== 1:
                list_d.append('discloses')
                p.publicized_evidence = p.private_evidence
                if p.publicized_evidence == -1:
                    list_c.append('Gray')
                else:
                    list_c.append('Orange')

            else:
                list_d.append('is an uninformed player')
                list_c.append('None')
        # saving the results of the disclosure...
        self.disclosure_decision1 = list_d[0]
        self.disclosure_decision2 = list_d[1]
        self.disclosure_decision3 = list_d[2]
        #self.disclosure_decision4 = list_d[3]
        #self.disclosure_decision5 = list_d[4]

        # saving the disclosed information
        self.disclosure_information1 = list_c[0]
        self.disclosure_information2 = list_c[1]
        self.disclosure_information3 = list_c[2]
        #self.disclosure_information4 = list_c[3]
        #self.disclosure_information5 = list_c[4]

 
    def get_results_voting(self):
        """
        Get the result variables at voting stage
        """
        players = self.get_players()
        self.gray_votes = 0
        # here you were adding float to integer, that is the source of error. 
        # you can only add variables of the same type, i.e. use 0 instead of 0.0 

        for p in players:
            if p.vote< 0:
                self.gray_votes = self.gray_votes - p.vote # gray votes labeled as -1 
    
    # this function is good!
    
    def set_payoffs(self):
        """
        computes the outcome (realization). 
        Determines the groups payoff based on their responses on vote stage.
        """
        players = self.get_players()
        self.gray_votes = 0
        # here you were adding float to integer, that is the source of error. 
        # you can only add variables of the same type, i.e. use 0 instead of 0.0 

        for p in players:
            if p.vote< 0:
                self.gray_votes = self.gray_votes - p.vote # gray vote is labeled as -1
        
        if self.gray_votes <= 1:
            self.group_guess = 1 # means Orange
            self.str_group_guess = 'Orange'
          
        else:
            self.group_guess = -1 # means gray
            self.str_group_guess = 'Gray'
        
        if self.group_guess == self.state_of_world:
            self.correct_guess = True
        
        if self.correct_guess == False: 
            for p in players:
                p.earnings = Constants.low_payoff - p.disclose*Constants.disclose_cost
        else:
            for p in players:
                p.earnings = Constants.high_payoff - p.disclose*Constants.disclose_cost
        # this function seems to be working okay

    def set_final_profit(self):
        for p in self.get_players():
            player_in_paying_round = p.in_round(Constants.paying_round)
            p.final_earnings = player_in_paying_round.earnings/Constants.exchange_rate
            p.final_profit = p.final_earnings + Constants.showup_fee
            p.payoff = p.final_profit


    


class Player(BasePlayer):
    # good practice: always define the default values, the reason for the mistakes was in failing to define them.
   
    # decision variables   
    opinion = models.IntegerField(choices=[[1, 'Orange'], [-1, 'Gray'], [0, 'None']], label='Which project do you prefer?', widget=widgets.RadioSelectHorizontal) # change name everywhere else
    disclose = models.IntegerField(choices=[[1, 'Yes'], [0, 'No']], label='Would you like to disclose your private evidence?', widget=widgets.RadioSelectHorizontal, default= 0, blank=True)
    vote = models.IntegerField(choices=[[1, 'Orange'], [-1, 'Gray']], label='Which project would you like to get implemented?', widget=widgets.RadioSelectHorizontal)
    # you also need to track whether the subject has already disclosed information or not
    # the idea is that we can repeat the same page but for that we need to record the "past decision"
    iteration = models.IntegerField(initial=0) # This variable records the number of iterations that a player takes to disclose his private information. It can be 0, 1 or 2. zero means that private evidence was never disclose.

    # opinions:
    opinion_iteration1 = models.IntegerField(default=-2) # first iteration of the opinion extraction
    opinion_iteration2 = models.IntegerField(default=-2) # second iteration of the opinion extraction
    #opinion_iteration3 = models.IntegerField(default=-2)
    #opinion_iteration4 = models.IntegerField(default=-2)

    # information variables
    private_evidence = models.IntegerField()
    str_private_evidence = models.StringField(initial='None') # evidence in words (for presentation)
    publicized_evidence = models.IntegerField(initial=0)
    
    # profit variables
    earnings = models.CurrencyField(initial=0)
    # NB! there are standard variables like profit and final_profit... we may want to employ them [check it out, but we may not even need to define them]
    final_earnings = models.CurrencyField(initial=0) # final earnings for the profit formation
    final_profit = models.CurrencyField(initial=0) # final profit including the show up fee

    # paying round:
    paying_round = models.IntegerField(initial=0)

    # type variables
    MyNumber = models.IntegerField(initial=0) #my number in group
    type = models.IntegerField(initial=0) # 1 informed and 0 uninformed player
    

    # also it may make sense to make it for +1 and for -1 ? 
    # Edgar: I dont think so. I think it should be simply equal to the private evidence when it is disclosed. 
    # I moved it to the player level so i dont need to define a set but a single value.

    def get_mynumber(self):
        """
        Retrieves player's ID number
        """
        self.MyNumber = self.id_in_group

    def set_evidences(self):
        """
        generates random private evidences 
        """
        mynumber = self.id_in_group
        if mynumber<3:
            self.type = 1
            list_choice2 = [self.group.state_of_world, (-1)*self.group.state_of_world]
            random_list = random.choices(list_choice2, weights= Constants.weights_evidences)
            self.private_evidence = random_list[0]
            if self.private_evidence == -1:
                self.str_private_evidence = 'Gray'
            if self.private_evidence == 1:
                self.str_private_evidence = 'Orange'




