import openai
# from TTS import speakingText

openai.api_key = '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'


def reply_to_question(question, prev_question_list = []):
  if len(prev_question_list) == 0:
    few_shot_text = '''### Answer questions like a chat-bot. Also take into account the previous questions and answers.
                      [Question] Who are you?
                      [Answer] Hi!! My name is Sushil. How may I help you?
                      [Question] Thanks for helping me.
                      [Answer] My pleasure!! If you have any other questions please do ask me.
                      [Question] Bye
                      [Answer] Bye Have a nice day.
                      [Question]'''
  else:
    few_shot_text = f'''### Answer questions like a chat-bot. Also take into account the previous questions and answers.
                      [Question] Who are you?
                      [Answer] Hi!! My name is Sushil. How ma
                      [Question] Thanks for helping me.
                      [Answer] My pleasure!! If you have any other questions please do ask me.
                      [Question] Bye
                      [Answer] Bye Have a nice day.
                      [Previous question] What is the natural satellite of the Earth?
                      [Question] What is the diameter of it?
                      [Answer] The diameter of Moon is 3474.2 km.'''
    for i in range(len(prev_question_list)):
      few_shot_text += f'''
                      [Previous Question] {prev_question_list[i]}
                      [Question]'''
                      
  gpt_prompt = f'{few_shot_text} {question} [Answer]'
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=gpt_prompt,
    temperature=0.7,
    max_tokens=512,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  response_text = str(response['choices'][0]['text'])
  return response_text