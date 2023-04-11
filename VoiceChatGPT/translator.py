import speech_recognition as sr
import openai
import const



listener = sr.Recognizer()

# Set up the OpenAI API client
# This is private
openai.api_key = const.key
# Set up the model and prompt
model_engine = "text-davinci-003"


def translateText(sound):
	texto = listener.recognize_google(sound, language='es')
	completion = openai.Completion.create( engine=model_engine, prompt=texto, max_tokens=1024, n=1, stop=None, temperature=0.5,)
	toRet = completion.choices[0].text.replace("\n","")
	print(toRet)
	return texto,toRet


