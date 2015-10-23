from random import randint
import time

class Magic8Ball(object):
	def __init__(self):
		super(Magic8Ball, self).__init__()

		self.response = { # The 8ball's responses
			1:"It is certain",
		    2: "It is decidedly so",
		    3: "Without a doubt",
		    4: "Yes, definitely",
		    5: "You may rely on it",
		    6: "As I see it, yes",
		    7: "Most likely",
		    8: "Outlook good",
		    9: "Yes",
		    10: "Signs point to yes",
		    11: "Reply hazy try again",
		    12: "Ask again later",
		    13: "Better not tell you now",
		    14: "Cannot predict now",
		    15: "Concentrate and ask again",
		    16: "Don't count on it",
		    17: "My reply is no",
		    18: "My sources say no",
		    19: "Outlook not so good",
		    20: "Very doubtful"}

		self.life_cycle()


	def life_cycle(self):
		self.state = 'started'
		self.spawn_ball()

		while self.state == 'running': self.ball_behaviour()


	def spawn_ball(self):
		self.state = 'running'
		print "You pick pick up the magic 8 ball"
		time.sleep(3)
		print "\n"


	def receive_question(self):
		return raw_input("Ask a question, or type exit to quit\n>> ").lower()


	def not_a_question(self):
		print "That's not a question! It didn't have a question mark."
		print "Please try again\n"
		self.ball_behaviour()


	def give_response(self):
		choice = randint(1, len(self.response)+1)
		print self.response[choice] + '\n'
		#print


	def ball_behaviour(self):
		question = self.receive_question()

		if question == 'exit':
			self.exit_application()

		elif '?' not in question: self.not_a_question()

		else: self.give_response()


	def exit_application(self):
		print "You have put the ball down.\nSee you next time"
		time.sleep(2)
		self.state = 'stopping'


if __name__ == '__main__':
	gamestate = 'running'
	ball = Magic8Ball()
	exit()
