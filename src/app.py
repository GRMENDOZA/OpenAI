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
        max_tokens = 4000,
        n = 1,
        stop = None,
        temperature = 0.3
    )

    response = completion.choices[0].text
    print(response)