# message_generator.py

import openai

openai.api_key = "your-openai-api-key"  # Replace this with your actual key

def generate_messages(candidates, job_description):
    messages = []

    for candidate in candidates:
        prompt = (
            f"Write a short, professional LinkedIn message to {candidate['name']} "
            f"for the following job opportunity:\n\n"
            f"{job_description}\n\n"
            f"The candidate's background is: {candidate['headline']}.\n\n"
            f"Explain why they might be a great fit, and keep it polite and concise."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=100
            )
            msg = response.choices[0].message.content
        except Exception as e:
            msg = f"Failed to generate message due to error: {str(e)}"

        messages.append(msg)

    return messages
