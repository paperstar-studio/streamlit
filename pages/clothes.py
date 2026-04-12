import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone


st.set_page_config( page_title="paperstar studio", page_icon=":shark:", layout='centered')
session_state = st.session_state
load_dotenv()

st.markdown("""<h1 style="text-align: center"> clothes </h1><p style="text-align: center">in my (digital) wardrobe datamodel</p><hr/>""", unsafe_allow_html=True)
st.markdown("""
:green-badge[ as a child] i don't remember my clothes except a few of my favorite pieces \n\n
:green-badge[ as a young adult] i spent more money than i'm comfortable admitting on a brand that shortly after went out of business \n\n
:green-badge[ now] i feel badly dressed, for now i'm ok with that \n\n
:blue-badge[ in university ] i learned that a datamodel is a 'representation' of a real life thing \n\n
:violet-badge[:material/star: the goal] is to feel delighted by my clothes \n\n
---
""")
# i'm looking at people in real life who look good and trying to blatantly copy them

brands = pd.DataFrame([
    {'brand_id':0, 'brand':'UNKNOWN'},		{'brand_id':1, 'brand':'levis'},		{'brand_id':2, 'brand':'uniqlo'},
    {'brand_id':3, 'brand':'patagonia'},	{'brand_id':4, 'brand':'dariadeh'},		{'brand_id':5, 'brand':'thought'},
    {'brand_id':6, 'brand':'H&M'},			{'brand_id':7, 'brand':'Nike'},			{'brand_id':8, 'brand':'armedangle'},
    {'brand_id':9, 'brand':'happy socks'},	{'brand_id':10,'brand':'iuman'},		{'brand_id':11, 'brand':'RalphLauren'},
])

df = pd.DataFrame([
    # UNKOWN
    {'type':'tops',      'name':'tshirt_striped',   'brand_id':0, 'color':'multi',  'size': 'M',   'thrift':1, 'price_to_me': 0,     'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    {'type':'tops',      'name':'sweatshirt_evo',   'brand_id':0, 'color':'purple', 'size': 'L',   'thrift':1, 'price_to_me': 0.00,  'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    {'type':'jacket',    'name':'jacket_leather',   'brand_id':0, 'color':'black',  'size': 'S',   'thrift':1, 'price_to_me': 25,    'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    {'type':'jacket',    'name':'jacket_ski',       'brand_id':0, 'color':'pink',   'size': 'one', 'thrift':1, 'price_to_me': 0.00,  'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    {'type':'jacket',    'name':'jacket',           'brand_id':0, 'color':'red',    'size': 'one', 'thrift':1, 'price_to_me': 0.00,  'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    # levis
    {'type':'pants',     'name':'jeans',            'brand_id':1, 'color':'black',  'size': '32',  'thrift':1, 'price_to_me': 25,    'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    # uniqlo
    {'type':'pants',     'name':'belt',             'brand_id':2, 'color':'black',  'size': 'one', 'thrift':0, 'price_to_me': 19.99, 'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    {'type':'pants',     'name':'sweatpants',       'brand_id':2, 'color':'black',  'size': 'M',   'thrift':0, 'price_to_me': 34.90, 'bought': datetime(2025, 2, 23), 'wear_since': datetime(2025, 2, 23), 'end':datetime.now()},
    {'type':'tops',      'name':'sweatshirt',       'brand_id':2, 'color':'black',  'size': 'M',   'thrift':0, 'price_to_me': 39.90, 'bought': datetime(2025, 2, 23), 'wear_since': datetime(2025, 2, 23), 'end':datetime.now()},
    {'type':'pants',     'name':'sweatpants',       'brand_id':2, 'color':'grey',   'size': 'L',   'thrift':0, 'price_to_me': 34.99, 'bought': datetime(2025, 2, 23), 'wear_since': datetime(2025, 2, 23), 'end':datetime.now()},
    {'type':'tops',      'name':'sweatshirt',       'brand_id':2, 'color':'grey',   'size': 'XL',  'thrift':0, 'price_to_me': 39.90, 'bought': datetime(2025, 2, 23), 'wear_since': datetime(2025, 2, 23), 'end':datetime.now()},
    {'type':'jacket',    'name':'UV_jacket',        'brand_id':2, 'color':'black',  'size': 'XL',  'thrift':0, 'price_to_me': 39.90, 'bought': datetime(2025, 2, 23), 'wear_since': datetime(2025, 2, 23), 'end':datetime.now()},
    {'type':'tops',      'name':'tshirt',          'brand_id':2, 'color':'black',  'size': 'XXXL','thrift':0, 'price_to_me': 14.90, 'bought': datetime(2025, 2, 23), 'wear_since': datetime(2025, 2, 23), 'end':datetime.now()},
    # patagonia
    {'type':'tops',      'name':'tshirt',          'brand_id':3, 'color':'black',  'size': 'L',   'thrift':1, 'price_to_me': 45,    'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    {'type':'tops',      'name':'tshirt',          'brand_id':3, 'color':'grey',   'size': 'M',   'thrift':1, 'price_to_me': 45,    'bought': datetime(2025, 6, 1), 'wear_since': datetime(2025, 6, 1), 'end':datetime.now()}, # from sophies parents
    {'type':'tops',      'name':'longsleeve',       'brand_id':3, 'color':'green',  'size': 'M',   'thrift':0, 'price_to_me': 55,    'bought': datetime(2025, 6, 1), 'wear_since': datetime(2025, 6, 1), 'end':datetime.now()}, # from sophies parents
    {'type':'pants',     'name':'rain_shell',       'brand_id':3, 'color':'black',  'size': 'M',   'thrift':0, 'price_to_me': 98,    'bought': datetime(2025, 6, 1), 'wear_since': datetime(2025, 6, 1), 'end':datetime.now()},
    #dariadeh
    {'type':'pants',     'name':'Alice shorts',     'brand_id':4, 'color':'lilac',  'size': 'XL',  'thrift':0, 'price_to_me': 89,    'bought': datetime(2025, 8, 16), 'wear_since': datetime(2025, 8, 16), 'end':datetime.now()},
    {'type':'tops',      'name':'Alice shirt',      'brand_id':4, 'color':'lilac',  'size': 'XL',  'thrift':0, 'price_to_me': 129,   'bought': datetime(2025, 8, 16), 'wear_since': datetime(2025, 8, 16), 'end':datetime.now()},
    {'type':'tops',      'name':'tshirt',          'brand_id':4, 'color':'black',  'size': 'L',   'thrift':1, 'price_to_me': 59.00, 'bought': datetime(2025, 4, 21), 'wear_since': datetime(2025, 4, 21), 'end':datetime.now()},
    # thought    
    {'type':'underwear', 'name':'socks polkadot',   'brand_id':5, 'color':'multi',  'size': 'L',   'thrift':1, 'price_to_me': 7.5,   'bought': datetime(2025, 1, 1)},
    {'type':'underwear', 'name':'socks_polkadot2',  'brand_id':5, 'color':'multi',  'size': 'L',   'thrift':1, 'price_to_me': 7.5,   'bought': datetime(2025, 1, 1)},
    {'type':'underwear', 'name':'socks_stripe',     'brand_id':5, 'color':'multi',  'size': 'L',   'thrift':1, 'price_to_me': 7.5,   'bought': datetime(2025, 1, 1)},
    {'type':'underwear', 'name':'socks_stripe2',    'brand_id':5, 'color':'multi',  'size': 'L',   'thrift':1, 'price_to_me': 7.5,   'bought': datetime(2025, 1, 1)},
    # H&M
    {'type':'underwear', 'name':'underwear',        'brand_id':6, 'color':'grey',   'size': 'M',   'thrift':0, 'price_to_me': 4.0,   'bought': datetime(2024, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    {'type':'sport',     'name':'swim_shorts',      'brand_id':6, 'color':'black',  'size': 'one', 'thrift':0, 'price_to_me': 14.99, 'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    {'type':'tops',      'name':'tshirt',           'brand_id':6, 'color':'white',  'size': 'M', 'thrift':0, 'price_to_me': 5.99, 'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    # nike
    {'type':'sport',     'name':'headband',         'brand_id':7, 'color':'white',  'size': 'one', 'thrift':0, 'price_to_me': 12.99, 'bought': datetime(2025, 1, 1), 'wear_since': datetime(2025, 1, 1), 'end':datetime.now()},
    # armedangle
    {'type':'underwear', 'name':'underwear',        'brand_id':8, 'color':'blue',   'size': 'M',   'thrift':1, 'price_to_me': 15.0,   'bought': datetime(2025, 3, 1), 'wear_since': datetime(2026, 3, 1), 'end':datetime.now()},
    {'type':'underwear', 'name':'socks',            'brand_id':8, 'color':'pink',   'size': 'M',   'thrift':1, 'price_to_me': 15.0,   'bought': datetime(2025, 3, 1), 'wear_since': datetime.now(), 'end':datetime.now()},
    # happy socks
    #{'type':'underwear', 'name':'socks_bear',       'brand_id':9, 'color':'black',  'size': 'L',   'thrift':0, 'price_to_me': 10,    'bought': datetime(2025, 1, 1)},
    # iuman
    {'type':'underwear', 'name':'underwear',        'brand_id':10,'color':'green',  'size': 'M',   'thrift':0, 'price_to_me': 9.0,   'bought': datetime(2026, 1, 15), 'wear_since': datetime(2026, 1, 15), 'end':datetime.now()},
    {'type':'underwear', 'name':'underwear',        'brand_id':10,'color':'blue',   'size': 'M',   'thrift':0, 'price_to_me': 9.0,   'bought': datetime(2026, 1, 15), 'wear_since': datetime(2026, 1, 15), 'end':datetime.now()},
    {'type':'underwear', 'name':'underwear',        'brand_id':10,'color':'red',    'size': 'M',   'thrift':0, 'price_to_me': 9.0,   'bought': datetime(2026, 1, 15), 'wear_since': datetime(2026, 1, 15), 'end':datetime.now()},
    # RalphLauren
    {'type':'tops',      'name':'sweatshirt',       'brand_id':11, 'color':'black',  'size': 'M',   'thrift':1, 'price_to_me': 0.00,    'bought': datetime(2025, 1, 1), 'wear_since': datetime(2024,1,1), 'end':datetime.now()},

])
df = pd.merge(df, brands, on='brand_id')
df.insert(loc=0, column='img', value=f"https://raw.githubusercontent.com/paperstar-studio/images/refs/heads/main/" + df['brand'] + "_" + df['name'] + "_" + df['color'] + ".jpeg")

st.markdown(""" <p style="text-align: center;">my current physical wardrobe consists of</p>""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric('number of pieces',        len(df.index),                                                              delta=None, delta_color="normal", help=None, label_visibility="visible", border=False)
with col2: st.metric('thrifted / fair fashion', f"{round(len(df[df['thrift'] == True].index) / len(df.index) * 100)} %",  delta=None, delta_color="normal", help=None, label_visibility="visible", border=False)
with col3: st.metric('total cost',              f"€ {round(df['price_to_me'].sum())}",                                            delta=None, delta_color="normal", help=None, label_visibility="visible", border=False)

st.markdown('''<style>
[data-testid="stMetricLabel"] > label {justufy-content: center;}
[data-testid="stMetricValue"] > div {text-align: center;}
</style>''', unsafe_allow_html=True)
st.divider()

st.markdown(""" <h3 style="text-align: center;">summaries</h3>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(""" <h5 style="text-align: center">by clothing type</h5> """, unsafe_allow_html=True)
    st.code(df.groupby('type', as_index=True).agg({'name':'count','price_to_me':'sum'}).sort_values('price_to_me', ascending=False), language='plaintext')
with col2:
    st.markdown(""" <h5 style="text-align: center">by brand</h5> """, unsafe_allow_html=True)
    st.code(df.groupby('brand', as_index=True).agg({'name':'count','price_to_me':'sum'}).sort_values('price_to_me', ascending=False), language='plaintext')
st.divider()


df = df.drop(columns=['brand_id'])
st.dataframe(df, height=(2+ len(df.index))*35 + 3,
    column_config={
    "img": st.column_config.ImageColumn( "img", help="latest photo of this clothing item"),
    "bought": st.column_config.DateColumn( "bought", help=""),
    }
 )


gantt = px.timeline(df.sort_values("bought", ascending=False), 'bought', 'end', color='type',)
st.plotly_chart(gantt)


st.markdown(""" <h3 style="text-align: center;">clothes i want</h3>""", unsafe_allow_html=True)
#st.link_button("Nike X Off-white Running Shorts","https://images.vestiairecollective.com/images/resized/w=1246,q=75,f=auto,/produit/black-other-nike-x-off-white-shorts-50362607-1_2.jpg")

st.link_button("North Face Himalayan Suit","https://www.thenorthface.com/de-at/p/herren-211701/himalayan-suit-fur-herren-NF0A8BH9?color=56P")





