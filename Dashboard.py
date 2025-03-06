import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st


customer=pd.read_csv('D:\\Dashboard\\dashboard\customer_df.csv')
geolocation=pd.read_csv('D:\\Dashboard\\dashboard\\geolocation_df.csv')
new_order_review=pd.read_csv('D:\\Dashboard\\dashboard\\new_order_reviews_df.csv')
order_item=pd.read_csv('D:\\Dashboard\\dashboard\\order_items_df.csv')
order_payments=pd.read_csv('D:\\Dashboard\\dashboard\\order_payments_df.csv')
orders=pd.read_csv('D:\\Dashboard\\dashboard\\orders_df.csv')
product=pd.read_csv('D:\\Dashboard\\dashboard\\product_df.csv')
sellers=pd.read_csv('D:\\Dashboard\\dashboard\\sellers_df.csv')


with st.sidebar:
    st.image('D:\\Dashboard\\dashboard\\ecomerce.png')

st.header('E-Commerce')

st.subheader('Kategori Produk')

merged_data = pd.merge(order_item, product, on='product_id')
product_sales = merged_data.groupby('product_id').agg({'order_item_id': 'count'}).reset_index()
product_sales.rename(columns={'order_item_id': 'sales_quantity'}, inplace=True)
sorted_products = product_sales.sort_values(by='sales_quantity')
selected_products_with_names = pd.merge(sorted_products, product, on='product_id')
sum_order = selected_products_with_names.groupby(by="product_category_name").sales_quantity.sum()
sum_order=sum_order.to_frame()
sum_order.sort_values(by="sales_quantity", ascending=False)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(36, 15))
 
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sn.barplot(x="sales_quantity", y="product_category_name",hue="product_category_name", data=sum_order.sort_values(by="sales_quantity", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Kategori Produk Paling Banyak di Order", loc="center", fontsize=50)
ax[0].tick_params(axis ='y', labelsize=30)
ax[0].tick_params(axis='x', labelsize=30)
 
sn.barplot(x="sales_quantity", y="product_category_name",hue="product_category_name", data=sum_order.sort_values(by="sales_quantity", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Kategori Produk Paling Sedikit di Order", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=30)
ax[1].tick_params(axis='x', labelsize=30) 
 
plt.suptitle("Kategori Produk Paling Banyak dan Sedikit di Order", fontsize=55)
st.pyplot(plt)

st.subheader('Negara Customer')

bystate_df = customer.groupby(by="customer_state").customer_id.nunique().reset_index()
bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

plt.figure(figsize=(12, 7))

colors = ["#72BCD4"] + ["#D3D3D3"] * (len(bystate_df) - 1)

sn.barplot(
    x="customer_state",
    y="customer_count",
    hue="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors
)

plt.title("Jumlah Customers Berdasarkan Negara", loc="center", fontsize=16)
plt.xlabel("")  
plt.ylabel("")

st.pyplot (plt)

st.subheader('Kota Customer')

bystate_df = customer.groupby(by="customer_city").customer_id.nunique().reset_index()
bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

top_10_bystate_df = bystate_df.sort_values(by="customer_count", ascending=False).head(10)

plt.figure(figsize=(12, 7))

colors = ["#72BCD4"] + ["#D3D3D3"] * (len(top_10_bystate_df) - 1)

sn.barplot(
    x="customer_city",
    y="customer_count",
    hue="customer_city",
    data=top_10_bystate_df,
    palette=colors
)

plt.title("Top 10 Jumlah Customers Berdasarkan Kota", loc="center", fontsize=16)

plt.xticks(rotation=55)
plt.xlabel("")  
plt.ylabel("")

st.pyplot(plt)

st.subheader('Score Reviews')

review = new_order_review.groupby(by="review_score").review_id.count().sort_values(ascending=False).reset_index()


plt.figure(figsize=(7, 5))
sn.barplot(
    x="review_score",
    y="review_id",
    data=review,
    color="#72BCD4" ) 

plt.title("Review Score dari Customers", loc="center", fontsize=16)
plt.xlabel(" ")
plt.ylabel(" ")
st.pyplot(plt)


st.subheader('Metode Pembayaran')

pay_type = order_payments.groupby(by="payment_type").order_id.count().sort_values(ascending=False).reset_index()


plt.figure(figsize=(5, 5))

sn.barplot(
    x="payment_type",
    y="order_id",
    data=pay_type,
    color="#72BCD4"  
)


plt.title("Metode Pembayaran dari Customers", loc="center", fontsize=16)
plt.xticks(rotation=55)
plt.xlabel("")
plt.ylabel("")


st.pyplot(plt)

st.subheader('Status Order')

order_stat = orders.groupby(by="order_status").order_id.count().sort_values(ascending=False).reset_index()


plt.figure(figsize=(7, 5))


sn.barplot(
    x="order_status",
    y="order_id",
    data=order_stat,
    color="#72BCD4"  
)


plt.title("Status Order Customers", loc="center", fontsize=16)


plt.xticks(rotation=55)
plt.xlabel("")
plt.ylabel("")

st.pyplot(plt)
