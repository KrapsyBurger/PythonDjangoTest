import wikipediaapi
from django.core.mail import send_mail
from django.conf import settings

def percentage_of_big_words(summary):
	words = summary.split()
	index = 0
	big_words_nbr = 0
	total_words_nbr = len(words)
	while index < total_words_nbr:
		if len(words[index]) >= 5:
			big_words_nbr += 1
		index += 1
	return (big_words_nbr / total_words_nbr) * 100

def wikipedia_summary_fetch(title, email):
	try:
		wiki_wiki = wikipediaapi.Wikipedia('OOTITest (nathanfascia@gmail.com)', 'en')
		page_py = wiki_wiki.page(title)

		if page_py.exists():
			if percentage_of_big_words(page_py.summary) > 20:
				subject = 'OOTI Test wiki'
				message = 'This page\'s summary contains more than 20% of big words !'
				from_email = 'OOTITest@gmail.com'
				recipient_list = [email]
				send_mail(subject, message, from_email, recipient_list)
				return 'An email has been sent to ' + email
			return 'This page doesnt have that much big words :('

		
		return 'This page doesnt seem to exist :/'
	except Exception as e:
		return f"Error: {e}"
