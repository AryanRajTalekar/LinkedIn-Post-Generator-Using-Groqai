from llm_helper import llm
from few_shot import FewShotPosts


few_shot = FewShotPosts()

def get_length_str(length):
    if length == "short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    

def get_prompt(length,language,tag):
    length_str = get_length_str(length)
    prompt =f'''
    Generate a LinkedIn Post using the below instructions.No preamble.
    1. Topic:{tag}
    2.Length:{length}
    3.Langauge:{language}
    If Langauge is Hinglish then it means it is  a mix of Hindi and English.
    The script for the generated post should always be English.





'''
    examples = few_shot.get_filtered_posts(length,language,tag)
    if len(examples)>0:
        prompt += "4) use the writing style as per the following examples."
        for i,post in enumerate(examples):
            post_text = post['text']
            prompt += f"\n\n Example{i+1}: \n\n {post_text}"

            if i == 2:
                break

    return prompt


def generate_post(length,language,tag):
    prompt = get_prompt(length,language,tag)
    response = llm.invoke(prompt)
    return response.content