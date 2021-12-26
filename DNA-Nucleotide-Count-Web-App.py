import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page Title
image = Image.open('Images/dna-logo.jpg')

st.image(image, use_column_width = True)

st.write("""
# DNA Nucleotide Count Web App

***
""")
#  About section
expander_bar = st.expander("About")
expander_bar.markdown("""
This app counts the nucleotide composition of query DNA!
* **Python libraries:** altair, pandas, streamlit
""")

# Input text box
st.header("Enter DNA squence")

squence_input = "CGATTCCTTCTGCGGACCATACCGTCCTGATACTTTGGTCATGTTTCCGTTGTAGGAGTGAACCCACTTGCCTTTGCGTCTTAATACCAATGAAAAACCTATGCACTTTGTACAGGGTACCATCGGGATTCTGAACCCTCAGATAGTGGGGATCCCGGGTATAGACCTTTATCTGCGGTCCAACTTAGGCATAAACCTCCATGCTACCTTGTCAGACCCACCCTGCACGAGGTAAATATGGGACGCGTCCGACCTGGCTCCTGGCGTTCTACGCCGCCACGTGTTCGTTAACTGTTGATTGGTAGCACAAAAGTAATACCATGGTCCTTGAAATTCGGCTCAGTTAGTTCGAGCGTAATGTCACAAATGGCGCAGAACGGCAATGAGTGTTTGACACTAGGTGGTGTTCAGTTCGGTAACGGAGAGACTGTGCGGCATACTTAATTATACATTTGAAACGCGCCCAAGTGACGCTAGGCAAGTCAGAGCAGGTTCCCGTGTTAGCTTAAGGGTAAACATACAAGTCGATTGAAGATGGGTAGGGGGCTTCAATTCGTCCAGCACTCTACGGTACCTCCGAGAGCAAGTAGGGCACCCTGTAGTTCGAAGCGGAACTATTTCGTGGGGCGAGCCCACATCGTCTCTTCTGCGGATGACTTAACACGTTAGGGAGGTGGAGTTGATTCGAACGATGGTTATAAATCAAAAAAACGGAACGCTGTCTGGAGGATGAATCTAACGGTGCGTAACTCGATCACTCACTCGCTATTCGAACTGCGCGAAAGTTCCCAGCGCTCATACACTTGGTTCCGAGGCCTGTCCTGATATATGAACCCAAACTAGAGCGGGGCTGTTGACGTTTGGAGTTGAAAAAATCTAATATTCCAATCGGCTTCAACGTGCACCACCGCAGGCGGCTGACGAGGGGCTCACACCGAGAAAGTAGACTGTTGCGCGTTGGGGGTAGCGCCGGCTAACAAAGACGCCTGGTACAGCAGGA"

sequence = st.text_area("Sequence input", squence_input, height = 200)

st.write("""
***
""")

## Print the input DNA Seqeunce
st.header('Input DNA Query')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

#print dictionary
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
	d = dict([
		('A', seq.count('A')),
		('T', seq.count('T')),
		('G', seq.count('G')),
		('C', seq.count('C'))
		])
	return d
X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

st.subheader('2. Print Text')
st.write('There are ' + str(X['A']) + ' ***adenine ***(A)')
st.write('There are ' + str(X['T']) + ' ***thymine ***(T)')
st.write('There are ' + str(X['G']) + ' ***guanine ***(G)')
st.write('There are ' + str(X['C']) + ' ***cytosine*** (C)')

# Dataframe
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient = 'index')
df = df.rename({0: 'count'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

#BarChart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
	x = "nucleotide",
	y = "count"
)
p = p.properties(
	width = alt.Step(90)  #Controls with of the bar
)
st.write(p)