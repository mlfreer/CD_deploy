
from __future__ import division

from otree.api import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

# Structure of the code:

# Welcome Page -- with instructions
# Template only.

# WaitPage? which initiates the round: determines all the random variables
# Function: initiate the round (set the variables)

# Opinion Poll Voting -- Opinion Poll Page where you enter the votes
# Output: Public(ized) Evidence
# Input: Opinion (-1,0,1)

# Optinion Poll Wait Page -- where votes are aggregated
# Function: aggregate the opinionns

# Disclosure Decision Stage -- voters decide whether to disclose or not the private evidence
# Output: Opinions
# Input: Disclosure Decision

# Disclosure Wait Page -- where these decisions are aggregated
# Function: Aggregate Disclosure Decisions (update the publicized evidence variable)
# transfer to voting/opinion polling page 
# page with instructions:


class Welcome(Page):
    # define template
    def is_displayed(self):
        return self.player.subsession.round_number == 1


class OpinionPoll(Page):
    template_name = 'No_info_treatment/OpinionPoll.html'
    form_model = 'player'
    form_fields = ['opinion']
    def vars_for_template(player):
        public_signal = player.group.str_public_evidence
        #private_signal = player.str_private_evidence
        return dict(
            public_signal = public_signal,
            #private_signal = private_signal,
            )

    # need to pass the vars for template (check vars_for_template function)
    # public signal/evidence
 

class OpinionPollWaitPage(WaitPage):
    def after_all_players_arrive(self): 
        self.group.get_results_opinion()
    # make sure that this function runs properly, since it is defined at the group level, while the self of the page is paricipant (incarnation of the player at the round)

class OpinionResults(Page):
    template_name = 'No_info_treatment/OpinionPollResults.html'
    def vars_for_template(player):
        opinion1 = player.group.opinions_result1
        opinion2 = player.group.opinions_result2
        opinion3 = player.group.opinions_result3
        return dict(
            opinion1 = opinion1,
            opinion2 = opinion2,
            opinion3 = opinion3,
        )

    # poll results
    # publisized info and public info
    # given a choice only to those who still have private evidence
    pass

class Disclosure(Page):
    # include template
    # include form_model
    # include form_field
    # include vars_for_template
    template_name = 'No_info_treatment/Disclosure.html'
    form_model = 'player'
    form_fields = ['disclose']
    def vars_for_template(player):
        public_signal = player.group.str_public_evidence
        #private_signal = player.str_private_evidence
        opinion1 = player.group.opinions_result1
        opinion2 = player.group.opinions_result2
        opinion3 = player.group.opinions_result3
        return dict(
            public_signal = public_signal,
            opinion1 = opinion1,
            opinion2 = opinion2,
            opinion3 = opinion3,
            #private_signal = private_signal,
            )

class DisclosureWaitPage(WaitPage):
    def after_all_players_arrive(self): 
        self.group.get_results_disclose()
    # incude after_all_players_arrive function


class Voting(Page):
    template_name = 'No_info_treatment/Vote.html'
    form_model = 'player'
    form_fields = ['vote']
    # include vars_for_template
    def vars_for_template(player):
        public_signal = player.group.str_public_evidence
        #private_signal = player.str_private_evidence
        decision1 = player.group.disclosure_decision1
        decision2 = player.group.disclosure_decision2
        decision3 = player.group.disclosure_decision3

        evidence1 = player.group.disclosure_information1
        evidence2 = player.group.disclosure_information2
        evidence3 = player.group.disclosure_information3

        opinion1 = player.group.opinions_result1
        opinion2 = player.group.opinions_result2
        opinion3 = player.group.opinions_result3

        return dict(
            public_signal = public_signal,
            #private_signal = private_signal,
            decision1 = decision1,
            decision2 = decision2,
            decision3 = decision3,
            evidence1 = evidence1,
            evidence2 = evidence2,
            evidence3 = evidence3,
            opinion1 = opinion1,
            opinion2 = opinion2,
            opinion3 = opinion3,
            )


class VotingWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    template_name = 'No_info_treatment/Results.html'
    def vars_for_template(player):
        votes_gray = player.group.gray_votes
        guess = player.group.str_group_guess
        return dict(
            votes_gray = votes_gray,
            votes_orange = 3 - votes_gray,
            guess = guess,
        )
    pass

class FinalWaitPage(WaitPage):
    def is_displayed(self):
        return self.group.subsession.round_number == Constants.num_rounds
    def after_all_players_arrive(self):
        if self.group.subsession.round_number == Constants.num_rounds:
            self.group.set_final_profit()

class FinalPage(Page):
    def is_displayed(self):
        return self.player.subsession.round_number == Constants.num_rounds
    template_name = 'collective_deliberation_infoTreatment/FinalResults.html'


page_sequence = [
    Welcome,
    OpinionPoll, # first iteration
    OpinionPollWaitPage,
    Disclosure,
    DisclosureWaitPage,
    OpinionPoll, # second iteration
    OpinionPollWaitPage,
    Disclosure,
    DisclosureWaitPage,
#    OpinionPoll, # third iteration
#    OpinionPollWaitPage,
#    Disclosure,
#    DisclosureWaitPage, # end of deliberation stage
    Voting, 
    VotingWaitPage,
    Results,
    FinalWaitPage, # once the experiment is finished
    FinalPage
]
