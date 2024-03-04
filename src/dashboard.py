# import streamlit as st
# import pandas as pd
# import numpy as np
# import altair as alt

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# c = (
#    alt.Chart(chart_data)
#    .mark_circle()
#    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
# )

# st.altair_chart(c, use_container_width=True)



# import streamlit as st
# import pandas as pd

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))


# Define CSS style for table
# table_style = """
#     <style>
#         .dvn-scroller {
#             padding: 5000px; /* Adjust padding as needed */
#         }
#     </style>
# """

# Display CSS style
#st.write(table_style, unsafe_allow_html=True)

# import streamlit as st
# import pandas as pd

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )


import streamlit as st
import time
from component.Header import create_header
from component.Table    import create_table

create_header()
create_table()
