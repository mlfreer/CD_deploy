
from __future__ import division

from otree.api import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    # define template
    def is_displayed(self):
        return self.player.subsession.round_number == 1


class OpinionPoll(Page):
    template_name = 'FivePThreeSTwoR_Info/OpinionPoll.html'
    form_model = 'player'
    form_fields = ['opinion']
    def vars_for_template(player):
        public_signal = player.group.str_public_evidence
        #private_signal = player.str_private_evidence
        return dict(
            public_signal = public_signal,
            #private_signal = private_signal,
            )

 

class OpinionPollWaitPage(WaitPage):
    def after_all_players_arrive(self): 
        self.group.get_results_opinion()
    # make sure that this function runs properly, since it is defined at the group level, while the self of the page is paricipant (incarnation of the player at the round)

class OpinionResults(Page):
    template_name = 'FivePThreeSTwoR_Info/OpinionPollResults.html'
    def vars_for_template(player):
        opinion1 = player.group.opinions_result1
        opinion2 = player.group.opinions_result2
        opinion3 = player.group.opinions_result3
        opinion4 = player.group.opinions_result4
        opinion5 = player.group.opinions_result5
        return dict(
            opinion1 = opinion1,
            opinion2 = opinion2,
            opinion3 = opinion3,
            opinion4 = opinion4,
            opinion5 = opinion5,
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
    template_name = 'FivePThreeSTwoR_Info/Disclosure.html'
    form_model = 'player'
    form_fields = ['disclose']
    def vars_for_template(player):
        public_signal = player.group.str_public_evidence
        #private_signal = player.str_private_evidence
        opinion1 = player.group.opinions_result1
        opinion2 = player.group.opinions_result2
        opinion3 = player.group.opinions_result3
        opinion4 = player.group.opinions_result4
        opinion5 = player.group.opinions_result5
        return dict(
            public_signal = public_signal,
            opinion1 = opinion1,
            opinion2 = opinion2,
            opinion3 = opinion3,
            opinion4 = opinion4,
            opinion5 = opinion5,
            #private_signal = private_signal,
            )
    def before_next_page(self):
        if self.player.disclose > 0:
            self.player.iteration =  self.player.iteration + 1
        # recording the data about 
        if self.player.opinion_iteration1 < -1:
            self.player.opinion_iteration1 = self.player.opinion
        elif self.player.opinion_iteration2 < -1:
            self.player.opinion_iteration2 = self.player.opinion
#        elif self.player.opinion_iteration3 < -1:
#            self.player.opinion_iteration3 = self.player.opinion
#        elif self.player.opinion_iteration4 < -1:
#            self.player.opinion_iteration4 = self.player.opinion
#        elif self.player.opinion_iteration5 < -1:
#            self.player.opinion_iteration5 = self.player.opinion

class DisclosureWaitPage(WaitPage):
    def after_all_players_arrive(self): 
        self.group.get_results_disclose()
    # incude after_all_players_arrive function

class Voting(Page):
    template_name = 'FivePThreeSTwoR_Info/Vote.html'
    form_model = 'player'
    form_fields = ['vote']
    # include vars_for_template
    
    def before_next_page(self):
        if self.player.iteration > 0:
            self.player.iteration = 3 - self.player.iteration
        # still the MAGIC NUMBER present

    def vars_for_template(player):
        public_signal = player.group.str_public_evidence
        #private_signal = player.str_private_evidence
        decision1 = player.group.disclosure_decision1
        decision2 = player.group.disclosure_decision2
        decision3 = player.group.disclosure_decision3
        decision4 = player.group.disclosure_decision4
        decision5 = player.group.disclosure_decision5

        evidence1 = player.group.disclosure_information1
        evidence2 = player.group.disclosure_information2
        evidence3 = player.group.disclosure_information3
        evidence4 = player.group.disclosure_information4
        evidence5 = player.group.disclosure_information5

        opinion1 = player.group.opinions_result1
        opinion2 = player.group.opinions_result2
        opinion3 = player.group.opinions_result3
        opinion4 = player.group.opinions_result4
        opinion5 = player.group.opinions_result5

        return dict(
            public_signal = public_signal,
            #private_signal = private_signal,
            decision1 = decision1,
            decision2 = decision2,
            decision3 = decision3,
            decision4 = decision4,
            decision5 = decision5,
            evidence1 = evidence1,
            evidence2 = evidence2,
            evidence3 = evidence3,
            evidence4 = evidence4,
            evidence5 = evidence5,
            opinion1 = opinion1,
            opinion2 = opinion2,
            opinion3 = opinion3,
            opinion4 = opinion4,
            opinion5 = opinion5,
            )

class VotingWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    template_name = 'FivePThreeSTwoR_Info/Results.html'
    def vars_for_template(player):
        guess = player.group.str_group_guess
        return dict(
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
    template_name = 'FivePThreeSTwoR_Info/FinalResults.html'


page_sequence = [
    Welcome,
    OpinionPoll, # first iteration
    OpinionPollWaitPage,
    Disclosure,
    DisclosureWaitPage,
    OpinionPoll, # second iteration
    OpinionPollWaitPage,
    Disclosure,
    DisclosureWaitPage, # end of deliberation stage
    Voting, 
    VotingWaitPage,
    Results,
    FinalWaitPage, # once the experiment is finished
    FinalPage
]
