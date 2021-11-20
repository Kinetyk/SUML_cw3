import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model2.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

def main():

	st.set_page_config(page_title="Czy wyzdrowiejesz po tygodniu leczenia?")
	overview = st.container()

	st.image("https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5f45c7bcd65e9b287f6b6c73%2FAI-and-healthcare%2F960x0.jpg%3Ffit%3Dscale")

	with overview:
		st.title("Czy wyzdrowiejesz po tygodniu leczenia?")
		symptoms_slider = st.slider("objawy", value=2, min_value=1, max_value=5)
		age_slider = st.slider( "wiek", value=28, min_value=11, max_value=77)
		diseases_slider = st.slider( "choroby", value=1, min_value=0, max_value=5)
		height_slider = st.slider( "wzrost", value=170, min_value=159, max_value=200)

	data = [[symptoms_slider, age_slider,  diseases_slider, height_slider]]
	cure = model.predict(data)
	s_confidence = model.predict_proba(data)

	with overview:
		st.header("Czy wyzdrowiejesz po tygodniu? {0}".format("Tak" if cure[0] == 1 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][cure][0] * 100))

if __name__ == "__main__":
    main()