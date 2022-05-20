from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)


def parse_text(text: str):
    messages = [text]
    messages.extend(text.split(r'.'))
    results = model.predict(messages, k=2)

    output_data = []
    for message, sentiment in zip(messages, results):
        output_data.append(
            {
                'message': message,
                'sentiment': sentiment
            }
        )

    return output_data
