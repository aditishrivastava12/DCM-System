from bardapi import Bard

token ='agg5tVTuH-ZvpKPpAWLxkc0-VL6R6sFnoFe9NcUXiCIfzmZUokdwuvahTpTywlOhBD7Waw.'
bard = Bard(token)

def get_chat_response(user_text):
    ans = bard.get_answer(user_text)['content']
    print(ans);
    return ans