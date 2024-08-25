import streamlit as st
import pandas as pd
import numpy as np

st.title('Depreciation Schedule Manager')

name = st.text_input('Name', placeholder = '123 Main St')

placed_in_service_date = st.date_input('Placed-in-Service Date', format = "MM/DD/YYYY", help = 'Generally property is considered placed in service when it is ready and available for a \
    specific use, regardless of whether or not it is actually used at the time. For example, a \
    house purchased for use as rental property is placed in service when it is ready and \
    available to rent, even if it is not actually rented at that time. ')

cost_basis = st.number_input('Cost Basis', format = '%0.2f', help = 'The cost basis of a rental property is essentially the \
                             original value of the property, plus any additional costs incurred in the process of purchasing \
                             such as agent fees.')

recovery_period = st.selectbox('Recovery Period (Years)', (10, 15, 27.5, 40))

def depreciation(cost_basis, recovery_period):
    annual_depreciation = cost_basis / recovery_period
    monthly_depreciation = annual_depreciation / 12
    annual_depreciation_percentage = annual_depreciation / cost_basis
    monthly_depreciation_percentage = monthly_depreciation / cost_basis
    return annual_depreciation, monthly_depreciation, annual_depreciation_percentage, monthly_depreciation_percentage

depreciation(cost_basis, recovery_period)

st.write('Annual depreciation allowance is: ' + {annual_depreciation})

# def total_periods(placed_in_service_date, cost_basis):
#     placed_in_service_date.astype('float64')
#     total_periods = placed_in_service_date * recovery_period
#     print(total_periods)

# total_periods(placed_in_service_date, cost_basis)
# type(placed_in_service_date)

# print(total_periods)