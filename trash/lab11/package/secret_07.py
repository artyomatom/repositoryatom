from typing import List

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

def decode(secret_message: List[str]):
    if not secret_message:
        return None
    
    first_word = secret_message[0][3]
    second_word = secret_message[1][9:13]
    therd_word = secret_message[2][5:15:2]
    fourth_word = secret_message[3][12:6:-1]
    five_word = secret_message[4][20:15:-1]
    return f"{first_word} {second_word} {therd_word} {fourth_word} {five_word}"

# print(decode(secret_message))