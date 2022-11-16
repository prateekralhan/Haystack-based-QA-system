import streamlit as st
from PIL import Image
from haystack.document_stores import SQLDocumentStore
from haystack.nodes import FARMReader, TfidfRetriever
from haystack.pipelines import ExtractiveQAPipeline

st.set_page_config(
    page_title="Haystack QA",
    page_icon="🛠",
    layout="centered",
    initial_sidebar_state="auto",
)

main_image = Image.open('static/main_banner.png')

@st.cache(persist=True,allow_output_mutation=False,show_spinner=False,suppress_st_warning=True)
def instantiate_model(question):
    params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 3}}
    reader = FARMReader(model_name_or_path="reader")
    document_store = SQLDocumentStore(url="sqlite:///qa.db")
    retriever = TfidfRetriever(document_store=document_store)
    pipe = ExtractiveQAPipeline(reader, retriever)
    prediction = pipe.run(query=question, params=params)
    return prediction

st.image(main_image,use_column_width='auto')
st.title("✨Question Answering system 📑")
question = st.text_area("Please enter your question:")
col1, col2 = st.columns(2)
with col1:
    retriever_top_k = st.slider('Please select the top N relevant documents in document store to be searched for', 1, 10, 1)
with col2:
    reader_top_k = st.slider('Please select the top M answers searched in retrieved N documents', 1, 10, 1)
if st.button("Fetch me the Answers 🚀"):
    if (len(question) != 0):
        with st.spinner("Getting the right answers... 💫"):
            prediction = instantiate_model(question)
            for ans in prediction['answers']:
                st.write(ans.answer) # main answer
                st.write(ans.context) # context
                st.write('---')
    else:
        st.warning('⚠ Please enter the question! 😯')

st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Haystack - QA WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a> with the help of [haystack](https://github.com/deepset-ai/haystack) built by [deepset-ai](https://github.com/deepset-ai) ✨</center><hr>", unsafe_allow_html=True)

