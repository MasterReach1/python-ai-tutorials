def create_response(client, user_message):
    response_list = [
        {"role": "system",
         "content": "You will be provided with statements. Detect all curse words and replace them with nicer words. If there are no curse words, simply reply with 'none'."},
         {"role": "user",
          "content": user_message}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=response_list,
        temperature=0.7,
        max_tokens=64
    )

    return response.choices[0].message.content