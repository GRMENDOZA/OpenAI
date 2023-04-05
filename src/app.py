import openai

openai.api_key = "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"

while True:

    engine_model_gpt = "text-davinci-003"

    prompt = input("Enter new prompt: ")

    if prompt in ["exit","salir","fin"]:
        break

    completion = openai.Completion.create(
        engine = engine_model_gpt,
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.3
    )

    response = completion.choices[0].text
    print(response)