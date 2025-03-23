import streamlit as st 
import pandas as pd 
import altair as alt 

#page configurations
st.set_page_config(page_title='NCDA', page_icon='images/Flag_of_Nakuru_County.gif')

df = pd.read_csv(
    filepath_or_buffer='data/Revenue Performance in the FY 2023-24.csv',
    engine= 'c',
    usecols=['S/No.', 'Revenue Category', 'Annual Budget Allocation  (Kshs)', 'Actual Receipts (Kshs)', 'Actual Receipts as Percentage of Annual Budget Allocation (%)'],
    #skiprows=[1,3,23,24,29,30],
)

bar_df = df[['Revenue Category', 'Annual Budget Allocation  (Kshs)', 'Actual Receipts (Kshs)', 'Actual Receipts as Percentage of Annual Budget Allocation (%)']].loc[[1, 22, 28, 29]]

st.header('A. Overview of FY 2023/24 Budget', divider='green')
st.write("""Nakuru county’s approved supplementary budget for the financial year 2023/24 was Kshs.23.31 billion, comprising Kshs.9.68
billion (41.5 %) and Kshs.13.63 billion (58.5 %) allocation for development and recurrent
programmes, respectively. The approved budget estimates represented an increase of 9.9 % compared
to the previous financial year when it was Kshs.21.21 billion and comprised of Kshs.8.34 billion towards
development expenditure and Kshs.12.87 billion for recurrent expenditure.\n
To finance the budget, the County expected to receive Kshs.13.59 billion (58.3 %) as the equitable share
of revenue raised nationally, Kshs.1.2 billion (6.5 %) as additional allocations/conditional grants, a cash
balance of Kshs.3.60 billion (15.5 %) brought forward from FY 2022/23 and generate Kshs.4.1 billion
(17.6 %) as gross own source revenue. The own-source revenue includes Kshs.1.7 billion (41.5 %)
as Facility Improvement Fund (revenue from health facilities) and Kshs.2.4 billion (58.5 per cent) as ordinary
own-source revenue.""")
st.header('B. Revenue Performance', divider='green')
st.write("""The total funds available for budget implementation during the period amounted to Kshs.20.44 billion.\n
In FY 2023/24, the County generated a total of Kshs.3.32 billion from its sources of revenue, inclusive of FIF.
This amount represented an increase of 6.1 % compared to Kshs.3.13 billion realized in FY 2022/23 and
was 81.0 % of the annual target and 26.6 % of the equitable revenue share disbursed during the
period. The revenue streams which contributed the highest OSR receipts are shown in the pie chart below.\n
The highest revenue stream, Kshs.1.47 billion, was from Health/Hospital fees, which contributed 44 % of
the total OSR receipts during the reporting period.""")
st.subheader('Revenue Performance in the FY 2023/24')
st.write('**SUMMARY**')
bar_df

st.write('**DETAILED**')
df
fig_alt = alt.Chart(bar_df).mark_bar().encode(
    x=alt.X('Revenue Category',
            sort = alt.EncodingSortField(
                field='Actual Receipts (Kshs)',  # The field to use for the sort
                order="descending"  # The order to sort in
            )
    ),
    y='Actual Receipts (Kshs)'
    ).properties(
        width=300,
        height=700
    )
st.altair_chart(fig_alt, use_container_width=True)

col1, col2 = st.columns(2, gap='medium', vertical_alignment='bottom', border=True)
col1.image('images/Trend in Own-Source Revenue Collection from the FY 2017-18 to the FY 2023-24.png', caption='**Trend in Own-Source Revenue Collection**')
col2.image('images/Top Streams of Own Source Revenue in the FY 2023-24.png', caption='**Top Streams of Own Source Revenue**')
' '
' '
st.header('C. Exchequer Issues', divider='green')
st.write("""The Controller of Budget approved withdrawals of Kshs.16.44 billion from the CRF account during the reporting
period, which comprised Kshs.4.51 billion (27.6 per cent) for development programmes and Kshs.11.93 billion
(72.4 per cent) for recurrent programmes. Analysis of the recurrent exchequers released in the FY 2023/24
indicates that Kshs.6.75 billion was released towards Employee Compensation and Kshs.5.18 billion for
Operations and Maintenance expenditure.\n
The available cash balance in the County Revenue Fund Account at the end of FY 2023/24 was Kshs.1.35 billion. This will be
"Balance b/f from FY2023/24" for the next financial year.""")
pie_df = pd.read_csv('data/Programme Expenditures.csv')
pie_alt = alt.Chart(pie_df).mark_arc().encode(
    theta='Expenditure',
    color='Programmes (in Billions)')
pie = pie_alt.mark_arc(outerRadius=120)
text = pie_alt.mark_text(radius=200, size=20).encode(text="Expenditure")
st.altair_chart(pie_alt + text)

st.header('D. County Expenditure Review', divider='green')
st.write("""The County spent Kshs.16.43 billion on development and recurrent programmes in the reporting period. The
expenditure represented 99.9 % of the total funds released by the CoB and comprised of Kshs.4.45 billion
and Kshs.11.98 billion on development and recurrent programmes, respectively. Expenditure on development
programmes represented an absorption rate of 46.0 %, while recurrent expenditure represented 87.9 % of the annual recurrent expenditure budget.""")

st.header('E. Settlement of Pending Bills', divider='green')
st.write("""At the beginning of FY 2023/24, the County reported a stock of pending bills amounting to Kshs.1.62 billion,
comprising of Kshs.1.38 billion for recurrent expenditure and Kshs.236.41 million for development activities.
In the FY 2023/24, the County settled pending bills amounting to Kshs.569.46 million, which consisted of
Kshs.387.97 million for recurrent expenditure and Kshs.181.49 million for development programmes.
Therefore, as of the end of FY 2023/24, the outstanding amount was Kshs.1.10 billion. This does not include
unsettled bills incurred in FY 2023/24.\n
The County Assembly reported outstanding pending bills of Kshs.81.21 million as of 30th June 2024.""")

st.header('F. Expenditure by Economic Classification', divider='green')
st.write("""Analysis of expenditure by economic classification indicates that the County Executive spent Kshs.6.29 billion
on employee compensation, Kshs.4.65 billion on operations and maintenance, and Kshs.4.37 billion on
development activities. Similarly, the County Assembly spent Kshs.462.10 million on employee compensation, Kshs.584.40 million
on operations and maintenance, and Kshs.88.07 million on development activities, as shown below.""")
st.subheader('Summary of Budget and Expenditure by Economic Classification')
two_df = pd.read_csv('data/Expenditure by Economic Classification.csv')
two_df

st.header('G. Expenditure on Employees’ Compensation')
st.write("""In FY 2023/24, expenditure on employee compensation was Kshs.6.75 billion, or 33.0 % of the available
revenue, which amounted to Kshs.20.44 billion. This expenditure represented a decrease from Kshs.6.92 billion
reported in FY 2022/23. The wage bill included Kshs.4.29 billion paid to health sector employees, translating to
63.5 % of the total wage bill. The trend of personnel expenditure as a percentage of total revenue from FY
2017/18 to FY 2023/24 is shown below.""")
st.image('images/Percentage of Wage Bill to Total Revenue from FY 2017-18 to FY 2023-24.png')
st.write("""Further analysis indicates that PE costs amounting to Kshs.6.17 billion were processed through the Integrated
Personnel and Payroll Database (IPPD) system, while Kshs.582.61 million was processed through manual
payrolls. The manual payrolls accounted for 8.6 per cent of the total PE cost.\n
The County Assembly spent Kshs.38.47 million on committee sitting allowances for the 74 MCAs against the
annual budget allocation of Kshs.38.98 million. The average monthly sitting allowance was Kshs.43,321 per
MCA. The County Assembly has established 23 Committees.""")

st.header('H. County Emergency Fund and County-Established Funds', divider='green')
st.write("""Section 116 of the PFM Act 2012 allows County governments to establish other public funds with approval
from the County Executive Committee and the County Assembly. The County allocated Kshs.779.53 million to
county-established funds in FY 2023/24, constituting 3.3 % of the County's overall budget. Further, the
County allocated Kshs.70 million to the Emergency Fund in line with Section 110 of the PFM Act, 2012.
The table below summarises each established Fund's budget allocation and performance during the reporting
period.""")
st.subheader('Performance of County Established Funds in the FY 2023/24')
three_df = pd.read_csv('data/County Established Funds in the FY 2023-24.csv')
three_df

st.header('I. Expenditure on Operations and Maintenance', divider='green')
st.write('The figure below summarises the Operations and Maintenance expenditure by major categories.')
st.image('images/Operations and Maintenance Expenditure by Major Categories.png')
' '
st.write("""Expenditure on domestic travel amounted to Kshs.544.13 million and comprised Kshs.135.81 million spent
by the County Assembly and Kshs.426.31 million by the County Executive. Expenditure on foreign travel
amounted to Kshs.102.89 million and comprised Kshs.41.81 million by the County Assembly and Kshs.61.08
million by the County Executive. Expenditure on foreign travel is summarized in the table below.""")
st.subheader('Summary of Highest Expenditure on Foreign Travel as of 30th June 2024')
four_df = pd.read_csv('data/Summary of Highest Expenditure on Foreign Travel as of 30th June 2024.csv')
four_df

st.header('J. Development Expenditure', divider='green')
st.write("""In the FY 2023/24, the County reported expenditure of Kshs.4.45 billion on development programmes,
representing an increase of 47.8 % compared to FY 2022/23 when the County spent Kshs.3.01 billion.
The table below summarises development projects with the highest expenditure in the reporting period.""")
st.subheader('List of Development Projects with the Highest Expenditure')
five_df = pd.read_csv('data/List of Development Projects with the Highest Expenditure.csv')
five_df

st.header('K. Budget Performance by Department', divider='green')
st.write('The table below summarises the approved budget allocation, expenditure and absorption rate by departments in the FY 2023/24.')
st.subheader('Budget Allocation and Absorption Rate by Department')
six_df = pd.read_csv('data/Budget Allocation and Absorption Rate by Department.csv')
six_df
st.write("""Analysis of expenditure by departments shows that the Department of County Public Service Board recorded
the highest absorption rate of development budget at 98.0 %, followed by the Office of the Governor and
Deputy Governor at 97.0 %. The County Assembly had the highest percentage of recurrent expenditure
to budget at 95.7 % while the Molo Municipality did not report any expenditure.""")

st.header('L. Budget Execution by Programmes and Sub-Programmes', divider='green')
st.write('The table below summarises the budget execution by programmes and sub-programmes in the FY 2023/24.')
st.subheader('Budget Execution by Programmes and Sub-Programmes')
seven_df = pd.read_csv('data/Programmes and Sub-Programmes.csv')
seven_df