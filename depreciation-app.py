import streamlit as st
import pandas as pd
import numpy as np

st.title('Depreciation Schedule Manager')

name = st.text_input('Name')
placed_in_service_date = st.date_input('Placed-in-Service Date', format = "MM/DD/YYYY", help = 'Generally property is considered placed in service when it is ready and available for a \
specific use, regardless of whether or not it is actually used at the time. For example, a \
house purchased for use as rental property is placed in service when it is ready and \
available to rent, even if it is not actually rented at that time. ')
cost_basis = st.number_input('Cost Basis', format = '%0.2f')
recovery_period = st.selectbox('Recovery Period', (10, 15, 27.5, 40))

# def total_periods(placed_in_service_date, cost_basis):
#     placed_in_service_date.astype('float64')
#     total_periods = placed_in_service_date * recovery_period
#     print(total_periods)

# total_periods(placed_in_service_date, cost_basis)
# type(placed_in_service_date)

# print(total_periods)