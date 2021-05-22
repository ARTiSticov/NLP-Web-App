import streamlit as st
import ktrain



st.title('NLP Sentiment Analysis using BERT model')
st.subheader('Predict if the sentence or review is Positive or Negative')


@st.cache(allow_output_mutation=True)
def load_model():
    model = ktrain.load_predictor('mypredictor')

    return model


with st.spinner('Loading Model Into Memory...'):
    model = load_model()
    
    
input = st.text_area('Enter your text', 'Type here')
if input != 'Type here':
    
    with st.spinner('Doing AI things...'):
        output = model.predict(input)


    if output == 'pos':
        st.success('This sentence or review, is most likely Positive')
    elif output == 'neg':
        st.error('This sentence or review, is most likely Negative')
    else:
        st.warning('Please, Type the sentence or the review to make predictions')