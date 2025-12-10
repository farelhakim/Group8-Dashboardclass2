# dashboard.py
# Sales dashboard demo with multilingual UI (fixed)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

st.set_page_config(layout="wide", page_title="Sales Dashboard")

# --- Translations dictionary ---
TRANSLATIONS = {
    "english": {
        "title": "Sales Dashboard",
        "kpi_total_sales": "Total Sales",
        "kpi_units": "Total Units Sold",
        "kpi_net_sales": "Net Sales",
        "kpi_rating": "Average Rating",
        "city": "City",
        "date": "Date Range",
        "customer_type": "Customer type",
        "product_line": "Product line",
        "payment": "Payment",
        "monthly_sales": "Monthly Sales",
        "units_sold": "Units Sold",
        "payment_methods": "Payment Methods",
        "rate_by_city": "Rate Based on City",
        "language": "Select language"
    },
    "indonesia": {
        "title": "Dasbor Penjualan",
        "kpi_total_sales": "Total Penjualan",
        "kpi_units": "Total Unit Terjual",
        "kpi_net_sales": "Penjualan Bersih",
        "kpi_rating": "Rata-rata Rating",
        "city": "Kota",
        "date": "Rentang Tanggal",
        "customer_type": "Tipe Pelanggan",
        "product_line": "Produk",
        "payment": "Pembayaran",
        "monthly_sales": "Penjualan Bulanan",
        "units_sold": "Unit Terjual",
        "payment_methods": "Metode Pembayaran",
        "rate_by_city": "Rating Berdasarkan Kota",
        "language": "Pilih bahasa"
    },
    "mandarin": {
        "title": "销售仪表盘",
        "kpi_total_sales": "总销售额",
        "kpi_units": "销售总量",
        "kpi_net_sales": "净销售额",
        "kpi_rating": "平均评分",
        "city": "城市",
        "date": "日期范围",
        "customer_type": "客户类型",
        "product_line": "产品线",
        "payment": "支付方式",
        "monthly_sales": "每月销售",
        "units_sold": "售出单位",
        "payment_methods": "支付方式",
        "rate_by_city": "按城市评分",
        "language": "选择语言"
    },
    "japan": {
        "title": "販売ダッシュボード",
        "kpi_total_sales": "総売上",
        "kpi_units": "総販売数",
        "kpi_net_sales": "純売上",
        "kpi_rating": "平均評価",
        "city": "都市",
        "date": "日付範囲",
        "customer_type": "顧客タイプ",
        "product_line": "製品ライン",
        "payment": "支払い",
        "monthly_sales": "月次売上",
        "units_sold": "販売ユニット",
        "payment_methods": "支払い方法",
        "rate_by_city": "都市別評価",
        "language": "言語を選択"
    },
    "korea": {
        "title": "판매 대시보드",
        "kpi_total_sales": "총 판매",
        "kpi_units": "총 판매 수량",
        "kpi_net_sales": "순매출",
        "kpi_rating": "평균 평점",
        "city": "도시",
        "date": "기간",
        "customer_type": "고객 유형",
        "product_line": "제품 군",
        "payment": "결제",
        "monthly_sales": "월별 판매",
        "units_sold": "판매된 수량",
        "payment_methods": "결제 수단",
        "rate_by_city": "도시별 평점",
        "language": "언어 선택"
    },
    "finlandia": {
        "title": "Myyntidashboard",
        "kpi_total_sales": "Kokonaismyynti",
        "kpi_units": "Myydyt yksiköt",
        "kpi_net_sales": "Nettomyynti",
        "kpi_rating": "Keskimääräinen arvostelu",
        "city": "Kaupunki",
        "date": "Päivämäärä",
        "customer_type": "Asiakastyyppi",
        "product_line": "Tuoteryhmä",
        "payment": "Maksu",
        "monthly_sales": "Kuukausimyynti",
        "units_sold": "Myytyjä yksiköitä",
        "payment_methods": "Maksutavat",
        "rate_by_city": "Arvio kaupungin mukaan",
        "language": "Valitse kieli"
    },
    "arab": {
        "title": "لوحة المبيعات",
        "kpi_total_sales": "إجمالي المبيعات",
        "kpi_units": "إجمالي الوحدات المبيعة",
        "kpi_net_sales": "صافي المبيعات",
        "kpi_rating": "متوسط التقييم",
        "city": "المدينة",
        "date": "نطاق التاريخ",
        "customer_type": "نوع العميل",
        "product_line": "خط المنتج",
        "payment": "الدفع",
        "monthly_sales": "المبيعات الشهرية",
        "units_sold": "الوحدات المباعة",
        "payment_methods": "طرق الدفع",
        "rate_by_city": "التقييم حسب المدينة",
        "language": "اختر اللغة"
    },
    "meksiko": {
        "title": "Panel de Ventas",
        "kpi_total_sales": "Ventas Totales",
        "kpi_units": "Total Unidades Vendidas",
        "kpi_net_sales": "Ventas Netas",
        "kpi_rating": "Calificación Promedio",
        "city": "Ciudad",
        "date": "Rango de Fecha",
        "customer_type": "Tipo de Cliente",
        "product_line": "Línea de Producto",
        "payment": "Pago",
        "monthly_sales": "Ventas Mensuales",
        "units_sold": "Unidades Vendidas",
        "payment_methods": "Métodos de Pago",
        "rate_by_city": "Calificación por Ciudad",
        "language": "Seleccionar idioma"
    },
    "jerman": {
        "title": "Verkaufs-Dashboard",
        "kpi_total_sales": "Gesamtumsatz",
        "kpi_units": "Verkaufte Einheiten",
        "kpi_net_sales": "Netto-Umsatz",
        "kpi_rating": "Durchschnittsbewertung",
        "city": "Stadt",
        "date": "Datumsbereich",
        "customer_type": "Kundentyp",
        "product_line": "Produktlinie",
        "payment": "Zahlung",
        "monthly_sales": "Monatlicher Umsatz",
        "units_sold": "Verkaufte Einheiten",
        "payment_methods": "Zahlungsmethoden",
        "rate_by_city": "Bewertung nach Stadt",
        "language": "Sprache auswählen"
    },
    "thailand": {
        "title": "แดชบอร์ดการขาย",
        "kpi_total_sales": "ยอดขายรวม",
        "kpi_units": "จำนวนหน่วยที่ขาย",
        "kpi_net_sales": "ยอดขายสุทธิ",
        "kpi_rating": "คะแนนเฉลี่ย",
        "city": "เมือง",
        "date": "ช่วงวันที่",
        "customer_type": "ประเภทลูกค้า",
        "product_line": "ประเภทสินค้า",
        "payment": "การชำระเงิน",
        "monthly_sales": "ยอดขายรายเดือน",
        "units_sold": "หน่วยที่ขาย",
        "payment_methods": "วิธีการชำระเงิน",
        "rate_by_city": "คะแนนตามเมือง",
        "language": "เลือกภาษา"
    },
    "filipina": {
        "title": "Sales Dashboard",
        "kpi_total_sales": "Kabuuang Benta",
        "kpi_units": "Bilang ng Nabentang Yunit",
        "kpi_net_sales": "Netong Benta",
        "kpi_rating": "Karaniwang Rating",
        "city": "Lungsod",
        "date": "Saklaw ng Petsa",
        "customer_type": "Uri ng Customer",
        "product_line": "Linya ng Produkto",
        "payment": "Paraan ng Bayad",
        "monthly_sales": "Buwang Benta",
        "units_sold": "Nabentang Yunit",
        "payment_methods": "Mga Paraan ng Pagbabayad",
        "rate_by_city": "Rating Ayon sa Lungsod",
        "language": "Piliin ang wika"
    },
    "francis": {
        "title": "Tableau de Ventes",
        "kpi_total_sales": "Ventes Totales",
        "kpi_units": "Unités Vendues",
        "kpi_net_sales": "Ventes Nettes",
        "kpi_rating": "Note Moyenne",
        "city": "Ville",
        "date": "Plage de dates",
        "customer_type": "Type de client",
        "product_line": "Gamme de produits",
        "payment": "Paiement",
        "monthly_sales": "Ventes Mensuelles",
        "units_sold": "Unités Vendues",
        "payment_methods": "Méthodes de paiement",
        "rate_by_city": "Note par Ville",
        "language": "Choisir la langue"
    },
    "brazil": {
        "title": "Painel de Vendas",
        "kpi_total_sales": "Vendas Totais",
        "kpi_units": "Total de Unidades Vendidas",
        "kpi_net_sales": "Vendas Líquidas",
        "kpi_rating": "Avaliação Média",
        "city": "Cidade",
        "date": "Intervalo de Data",
        "customer_type": "Tipo de Cliente",
        "product_line": "Linha de Produto",
        "payment": "Pagamento",
        "monthly_sales": "Vendas Mensais",
        "units_sold": "Unidades Vendidas",
        "payment_methods": "Métodos de Pagamento",
        "rate_by_city": "Avaliação por Cidade",
        "language": "Selecione o idioma"
    },
    "rusia": {
        "title": "Панель продаж",
        "kpi_total_sales": "Общие продажи",
        "kpi_units": "Всего продано единиц",
        "kpi_net_sales": "Чистые продажи",
        "kpi_rating": "Средняя оценка",
        "city": "Город",
        "date": "Диапазон дат",
        "customer_type": "Тип клиента",
        "product_line": "Линейка продуктов",
        "payment": "Оплата",
        "monthly_sales": "Ежемесячные продажи",
        "units_sold": "Проданные единицы",
        "payment_methods": "Способы оплаты",
        "rate_by_city": "Рейтинг по городу",
        "language": "Выберите язык"
    }
}

LANG_KEYS = list(TRANSLATIONS.keys())
LANG_DISPLAY = {
    "english": "English",
    "indonesia": "Indonesia",
    "mandarin": "中文 (Mandarin)",
    "japan": "日本語 (Japanese)",
    "korea": "한국어 (Korean)",
    "finlandia": "Suomi (Finnish)",
    "arab": "العربية (Arabic)",
    "meksiko": "Español (Mexico)",
    "jerman": "Deutsch (German)",
    "thailand": "ไทย (Thai)",
    "filipina": "Filipino (Tagalog)",
    "francis": "Français (French)",
    "brazil": "Português (Brazil)",
    "rusia": "Русский (Russian)"
}

# --- Dummy dataset generator ---
@st.cache_data
def generate_data(seed=42, n=500):
    np.random.seed(seed)
    cities = ["Yangon", "Naypyitaw", "Mandalay"]
    product_lines = [
        "Electronic accessories",
        "Fashion accessories",
        "Food and beverages",
        "Health and beauty",
        "Home and lifestyle",
        "Sports and travel",
    ]
    payments = ["Cash", "Credit card", "Ewallet"]
    customer_types = ["Member", "Normal"]

    dates = pd.date_range(start="2019-01-01", end="2019-12-31", freq="D")
    chosen_dates = np.random.choice(dates, size=n)
    data = pd.DataFrame({
        "Date": chosen_dates,
        "City": np.random.choice(cities, size=n),
        "Product line": np.random.choice(product_lines, size=n),
        "Payment": np.random.choice(payments, size=n),
        "Customer type": np.random.choice(customer_types, size=n),
        "Units": np.random.randint(1, 50, size=n),
    })
    price_map = {
        "Electronic accessories": 20,
        "Fashion accessories": 10,
        "Food and beverages": 7,
        "Health and beauty": 12,
        "Home and lifestyle": 15,
        "Sports and travel": 18,
    }
    data["PricePerUnit"] = data["Product line"].map(price_map)
    data["Sales"] = data["Units"] * data["PricePerUnit"] * (1 + np.random.randn(n) * 0.05)
    data["Rating"] = np.clip(np.round(np.random.normal(6.8, 0.7, size=n), 2), 1, 10)
    return data

# load data
df = generate_data()

# --- Sidebar: language selection and filters ---
st.sidebar.title("🌐 Languages")
selected_lang_key = st.sidebar.selectbox("", options=LANG_KEYS, format_func=lambda k: LANG_DISPLAY.get(k, k))
T = TRANSLATIONS[selected_lang_key]

st.title(T["title"])

# Filters
with st.sidebar.form(key="filters"):
    st.write(T["date"])
    date_min = st.date_input("", value=df["Date"].min())
    date_max = st.date_input("", value=df["Date"].max())

    cities = st.multiselect(T["city"], options=sorted(df["City"].unique()), default=sorted(df["City"].unique()))
    cust = st.multiselect(T["customer_type"], options=sorted(df["Customer type"].unique()), default=sorted(df["Customer type"].unique()))
    products = st.multiselect(T["product_line"], options=sorted(df["Product line"].unique()), default=sorted(df["Product line"].unique()))
    payments = st.multiselect(T["payment"], options=sorted(df["Payment"].unique()), default=sorted(df["Payment"].unique()))
    submitted = st.form_submit_button("Apply")

# apply filters
mask = (
    (df["Date"] >= pd.to_datetime(date_min)) &
    (df["Date"] <= pd.to_datetime(date_max)) &
    (df["City"].isin(cities)) &
    (df["Customer type"].isin(cust)) &
    (df["Product line"].isin(products)) &
    (df["Payment"].isin(payments))
)
filtered = df[mask]

# --- KPIs ---
total_sales = filtered["Sales"].sum()
total_units = filtered["Units"].sum()
net_sales = total_sales * 0.95  # example
avg_rating = filtered["Rating"].mean()

k1, k2, k3, k4 = st.columns([2,2,2,2])
with k1:
    st.metric(label=T["kpi_total_sales"], value=f"${total_sales:,.0f}")
with k2:
    st.metric(label=T["kpi_units"], value=f"{total_units:,}")
with k3:
    st.metric(label=T["kpi_net_sales"], value=f"${net_sales:,.0f}")
with k4:
    st.metric(label=T["kpi_rating"], value=f"{avg_rating:.2f}")

# --- Layout charts ---
col1, col2 = st.columns([2,3])

# Left column: Monthly sales and Units sold
with col1:
    st.subheader(T["monthly_sales"])
    monthly = filtered.copy()
    if not monthly.empty:
        monthly["Month"] = monthly["Date"].dt.to_period("M").dt.to_timestamp()
        monthly_grp = monthly.groupby("Month")["Sales"].sum().reset_index()
        fig_month = px.line(monthly_grp, x="Month", y="Sales", markers=True)
        fig_month.update_layout(margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_month, use_container_width=True)
    else:
        st.info("No data for the selected filters")

    st.subheader(T["units_sold"])
    units_grp = filtered.groupby("Product line")["Units"].sum().reset_index()
    if not units_grp.empty:
        fig_units = px.bar(units_grp, x="Product line", y="Units", text_auto=True)
        fig_units.update_layout(margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_units, use_container_width=True)
    else:
        st.info("No data")

# Right column: Payment methods pie and rating by city
with col2:
    st.subheader(T["payment_methods"])
    pay_grp = filtered.groupby("Payment")["Sales"].sum().reset_index()
    if not pay_grp.empty:
        fig_pay = px.pie(pay_grp, names="Payment", values="Sales", hole=0)
        fig_pay.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig_pay, use_container_width=True)
    else:
        st.info("No data")

    st.subheader(T["rate_by_city"])
    rate_grp = filtered.groupby("City")["Rating"].mean().reset_index()
    if not rate_grp.empty:
        fig_rate = px.bar(rate_grp, x="Rating", y="City", orientation="h", text_auto=True)
        fig_rate.update_layout(margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_rate, use_container_width=True)
    else:
        st.info("No data")

# Footer notes
st.markdown("---")
st.caption("Demo dashboard dibuat dengan Streamlit • Data sintetis")
