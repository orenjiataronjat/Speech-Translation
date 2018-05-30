import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()

def recordAudio():
	with sr.Microphone() as source:
		print('start speaking')
		audio = r.listen(source)

	detectedText = r.recognize_google(audio)

	print(detectedText)
	return detectedText

def translate(language, detectedText):
	translator = Translator()
	translation = translator.translate(detectedText, dest=language)
	print(translation.text)

def selectLanguage():
	print('-----------------------')
	print('|   Select language   |')
	print('-----------------------')
	print('|0| Arabic.           |')
	print('|1| English.          |')
	print('|2| French.           |')
	print('|3| German.           |')
	print('|4| Hebrew.           |')
	print('|5| Italian.          |')
	print('|6| Japanese.         |')
	print('|7| Korean.           |')
	print('|8| Russian.          |')
	print('|9| Speanish.         |')
	answer = input('-----------------------\n')

	language = ['ar', 'en', 'fr','de', 'he', 'it', 'ja','ko', 'ru', 'es']
	try: 
		return language[int(answer)]
	except ValueError:
		print('Invalid selection')
		return selectLanguage()

def menu(language, detectedText):
	print('-----------------------')
	print('|  Speech Translator  |')
	print('-----------------------')
	print('|A| Record new audio. |')
	print('|B| Select language   |')
	print('|C| Print translation |')
	print('|Q| Quit              |')
	answer = input('-----------------------\n')

	if answer == "A" or answer == "a":
		recordedText = recordAudio()
		menu(language, recordedText)
	elif answer == "B" or answer ==  "b":
		switchLanguage = selectLanguage()
		menu(switchLanguage, detectedText)
	elif answer == "C" or answer ==  "c":
		translate(language, detectedText)
		menu(language, detectedText)
	elif answer == "Q" or answer ==  "q":
		exit()
	else:
		print('Did not understand input')
		menu(language, detectedText)

menu('ja','')