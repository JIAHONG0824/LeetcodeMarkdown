import requests
import streamlit as st

@st.cache_data
def markdowngenerator(url):
    response = requests.get(url).json()
    return response

if __name__ == "__main__":
    st.title("Leetcode Markdown Generator")
    api="https://alfa-leetcode-api.onrender.com/select?titleSlug="
    name=st.text_input("Enter the problem name")
    try:
        if name:
            #preprocessing the problem name
            name = name.translate(str.maketrans(' ', '-', ',()'))
            name=name.lower()
            #combining the api and title slug
            url=api+name
            #getting the response from the api
            info=markdowngenerator(url)
            #getting the required information
            link=info['link']
            Id=info['questionId']
            Title=info['questionTitle']
            difficulty=info['difficulty']
            question=info['question']   
            #generating the markdown code
            markdown=f"### `{difficulty}` [{Id}. {Title}]({link})\n### "
            for tag in info['topicTags']:
                markdown+=f":label:`{tag['name']}` "
            markdown+=f"\n---\n{question}\n---"
            st.write("Markdown code:")
            st.code(markdown,language='markdown',line_numbers=True)
        else:
            st.write("you haven't entered the problem name")
    except:
        st.write("Problem not found")