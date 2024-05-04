#Import Necessary Libraries
import numpy as np
import pandas as pd
import streamlit as st

# Initialization Function
def init():

    if "init" not in st.session_state:
    
        url = "https://drive.google.com/file/d/16NdRk9DcEb_wTsRkZ3WfORNYG2J18PZ2/view?usp=sharing"
        url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
        
        use_df = pd.read_csv(url)
        use_df = use_df[["L1", "L2", "L3", "L4", "L5", "Words"]]
    
        st.session_state.init = use_df
        
        st.dataframe(st.session_state.init, height = 500, width = 1200, hide_index=True)
        s = use_df.shape
        st.write( "Number of Words: " + str(s[0]))
        
        return use_df
        
    
    use_df = st.session_state.init
    return use_df

# Showing DataFrame in each Iteration
def show_df():

        st.dataframe(st.session_state.init, height = 500, width = 1200, hide_index=True)
        s = use_df.shape
        st.write( "Number of Words: " + str(s[0]))

# Remove Cases of Letters with/without Function
def remove_cases(l, df, p = None):

    l = l.upper()

    if p != None:

        idx = ["L1", "L2", "L3", "L4","L5"]
        i = idx[p-1]
        df = df[df[i] != l]

    else:

        df = df[df["L1"] != l]
        df = df[df["L2"] != l]
        df = df[df["L3"] != l]
        df = df[df["L4"] != l]
        df = df[df["L5"] != l]

    df = df.reset_index(drop=True)
    st.session_state.init = df
    return df
    
# Find All Cases of a Letter
def find_cases(l, df, p = None):

    l = l.upper()
    if(p != None):

        idx = ["L1", "L2", "L3", "L4","L5"]
        i = idx[p-1]

        df = df[df[i] == l]
        
    else:
    
      idx = list()
      for i in df["Words"]:
      
        if(l in i):
        
            val = np.where(df["Words"] == i)[0][0]
            idx.append(val)
            
      df = df.iloc[idx]
    
    df = df.reset_index(drop=True)
    st.session_state.init = df
    return df
        

# Main App Code

st.title("Wordle Game Helper")
st.divider()

use_df = init()

#########################################################################

st.sidebar.title("Options")

#########################################################################

o1_form = st.sidebar.form("Removing Cases of a Letter")
o1_form.header("Removing Cases of a Letter")
l = o1_form.text_input(" Enter Choice of Letter", max_chars=1)
o1_submit = o1_form.form_submit_button()
        
if o1_submit:

        st.empty()
        st.write("Removing Letter: " + l.upper())
        use_df = remove_cases(l, use_df)
        
        show_df()
    
#######################################################################

o2_form = st.sidebar.form("Removing Cases of a Letter with Position")
o2_form.header("Removing Cases of a Letter with Position")
l = o2_form.text_input(" Enter Choice of Letter", max_chars=1)
p = o2_form.number_input("Enter Position of Letter", min_value = 1, max_value = 5)
o2_submit = o2_form.form_submit_button()
        
if o2_submit:

        st.empty()
        st.write("Removing Letter: " + l.upper() + " At Position: " + str(p))
        use_df = remove_cases(l, use_df, p)
        
        show_df()

#######################################################################

o3_form = st.sidebar.form("Finding All Cases of a Letter")
o3_form.header("Finding All Cases of a Letter")
l = o3_form.text_input(" Enter Choice of Letter", max_chars=1)
o3_submit = o3_form.form_submit_button()
        
if o3_submit:

        st.empty()
        st.write("Cases of Letter: " + l.upper())
        use_df = find_cases(l, use_df)
        
        show_df()
        
#######################################################################

o4_form = st.sidebar.form("Finding Cases of a Letter with Position")
o4_form.header("Finding Cases of a Letter with Position")
l = o4_form.text_input(" Enter Choice of Letter", max_chars=1)
p = o4_form.number_input("Enter Position of Letter", min_value = 1, max_value = 5)
o4_submit = o4_form.form_submit_button()
        
if o4_submit:

        st.empty()
        st.write("Cases of Letter: " + l.upper() + " with Position: " + str(p))
        use_df = find_cases(l, use_df, p)
        
        show_df()

#######################################################################
