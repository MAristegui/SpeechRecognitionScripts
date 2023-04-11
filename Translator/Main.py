import speech_recognition as sr
from googletrans import Translator
import googletrans

language_dictionary = {'Ingles':'en',
					'Español':'es',
					'Frances':'fr',
					'Aleman':'de',
					'Italiano':'it',
					'Portugués':'pt',
					'Turco':'tr'}

translator = Translator()
listener = sr.Recognizer()


def getOptions():
	return language_dictionary.keys()

def translateText(origin, dest, sound):
	texto = listener.recognize_google(sound, language=language_dictionary.get(origin))
	translate_text = translator.translate(texto,dest=language_dictionary.get(dest))
	return texto, translate_text.text


