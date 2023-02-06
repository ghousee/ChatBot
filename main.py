import re
import long_responses as lg

def message_probability(user_message, recognized_words, single_response = False, required_words = []):
    message_certainty = 0
    has_required = True
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    #Calculates how many words are present in each predefined user message
    percentage = float(message_certainty) / float(len(recognized_words))

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Testing response system
while True:
    print('Bot: ' + get_response(input('You: ')))