from openai import OpenAI
import json
def parse_data(user_message):
    client = OpenAI(
        api_key="*********"    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    bottext = completion.choices[0].message.content.strip()
    trimmed_str = bottext.replace('```json\n', '').replace('```', '')

    print(trimmed_str)
    resume_dict=trimmed_str.strip()
    print(resume_dict)
    return resume_dict