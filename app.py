import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS / MODERN DARK THEME
# ============================================================
st.markdown("""
<style>
    /* ========================================================
       GLOBAL DARK THEME
       ======================================================== */
    html, body, [class*="css"], .stApp {
        background: #0b1220 !important;
        color: #e5e7eb !important;
    }

    .stApp {
        min-height: 100vh;
    }

    [data-testid="stAppViewContainer"] {
        background: #0b1220 !important;
        min-height: 100vh;
    }

    [data-testid="stMain"] {
        background: #0b1220 !important;
        min-height: 100vh;
    }

    .main {
        padding-top: 0 !important;
        background: #0b1220 !important;
        min-height: 100vh;
    }

    /* Compact top spacing — dashboard starts near the top */
    [data-testid="stAppViewContainer"] .main .block-container,
    [data-testid="stMainBlockContainer"] {
        padding-top: 0 !important;
        padding-bottom: 2.5rem !important;
        max-width: 1500px !important;
        min-height: 100vh !important;
    }

    .block-container {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    header[data-testid="stHeader"] {
        background: #0b1220 !important;
        min-height: 0 !important;
        height: 2rem !important;
    }

    /* Force normal Streamlit text to be readable */
    .stApp p,
    .stApp span,
    .stApp label,
    .stApp div,
    .stApp small {
        color: #e5e7eb;
    }

    /* ========================================================
       SIDEBAR
       ======================================================== */
    [data-testid="stSidebar"] {
        background: #111827 !important;
        border-right: 1px solid #273449 !important;
        min-height: 100vh !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.9rem !important;
        min-height: 100vh !important;
    }

    [data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    .sidebar-heading {
        font-size: 1.25rem;
        font-weight: 800;
        margin: 0 0 0.25rem 0;
        letter-spacing: 0.2px;
        color: #f8fafc !important;
    }

    .sidebar-subtitle {
        color: #94a3b8 !important;
        font-size: 0.82rem;
        margin-bottom: 1.1rem;
    }

    /* Professional dropdown containers */
    [data-testid="stSidebar"] [data-testid="stExpander"] {
        background: #151f31 !important;
        border: 1px solid #2d3b52 !important;
        border-radius: 12px !important;
        margin-bottom: 0.7rem !important;
        overflow: hidden;
    }

    [data-testid="stSidebar"] [data-testid="stExpander"] summary {
        color: #f8fafc !important;
        font-weight: 700 !important;
    }

    [data-testid="stSidebar"] [data-testid="stExpander"] summary span {
        color: #f8fafc !important;
    }

    /* Multiselect */
    [data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background: #182235 !important;
        border: 1px solid #3a4860 !important;
        border-radius: 10px !important;
        min-height: 46px;
        box-shadow: none !important;
    }

    [data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
        border-color: #8b5cf6 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] {
        background: #6d4aff !important;
        border-radius: 7px !important;
        border: none !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] span,
    [data-testid="stSidebar"] [data-baseweb="tag"] svg {
        color: #ffffff !important;
        fill: #ffffff !important;
    }

    [data-testid="stSidebar"] input {
        color: #f8fafc !important;
        caret-color: #a78bfa !important;
    }

    /* Dropdown popup */
    [data-baseweb="popover"],
    [data-baseweb="menu"] {
        background: #182235 !important;
        color: #f8fafc !important;
    }

    [data-baseweb="menu"] li,
    [role="option"] {
        color: #e5e7eb !important;
        background: #182235 !important;
    }

    [role="option"]:hover {
        background: #26334a !important;
    }

    /* Date picker */
    [data-testid="stSidebar"] [data-testid="stDateInput"] input {
        background: #182235 !important;
        border: 1px solid #3a4860 !important;
        color: #f8fafc !important;
        border-radius: 10px !important;
    }

    /* ========================================================
       HEADER / TEXT
       ======================================================== */
    .dashboard-title {
        margin-top: 0 !important;
        padding-top: 0 !important;
        margin-top: 0 !important;
        padding-top: 0 !important;
        font-size: 2.55rem;
        font-weight: 850;
        margin-bottom: 0.15rem;
        letter-spacing: -1.2px;
        color: #f8fafc !important;
    }

    .dashboard-title + .dashboard-subtitle {
        margin-top: 0 !important;
    }

    .dashboard-subtitle {
        color: #94a3b8 !important;
        font-size: 1rem;
        margin-bottom: 1.6rem;
    }

    .section-title {
        font-size: 1.4rem;
        font-weight: 800;
        margin-top: 0.7rem;
        margin-bottom: 1rem;
        color: #f8fafc !important;
    }

    /* Make Streamlit headings explicitly bright */
    .stApp h1, .stApp h2, .stApp h3,
    .stApp h4, .stApp h5, .stApp h6 {
        color: #f8fafc !important;
    }

    /* ========================================================
       KPI CARDS — FIX DARK/INVISIBLE LABELS
       ======================================================== */
    div[data-testid="metric-container"] {
        background: linear-gradient(145deg, #151f31, #111827) !important;
        border: 1px solid #273449 !important;
        border-radius: 16px !important;
        padding: 17px 18px !important;
        box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    }

    div[data-testid="metric-container"] *,
    div[data-testid="stMetric"],
    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] *,
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] * {
        color: #f8fafc !important;
    }

    div[data-testid="stMetricLabel"] {
        color: #cbd5e1 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc !important;
        font-weight: 800 !important;
    }

    /* ========================================================
       INSIGHTS / NOTES
       ======================================================== */
    .insight-box {
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 18px;
        background: #151f31;
        color: #e5e7eb !important;
        margin-top: 12px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.14);
    }

    .insight-box * {
        color: #e5e7eb !important;
    }

    .small-note {
        color: #94a3b8 !important;
        font-size: 0.8rem;
        line-height: 1.4;
    }

    /* ========================================================
       TABS — FIX INVISIBLE TAB TEXT
       ======================================================== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        border-bottom: 1px solid #273449 !important;
    }

    .stTabs [data-baseweb="tab"] {
        padding: 12px 16px;
        color: #cbd5e1 !important;
        font-weight: 650;
    }

    .stTabs [data-baseweb="tab"] *,
    .stTabs [data-baseweb="tab"] span {
        color: #cbd5e1 !important;
    }

    .stTabs [aria-selected="true"],
    .stTabs [aria-selected="true"] * {
        color: #a78bfa !important;
    }

    /* ========================================================
       COMMON STREAMLIT WIDGET TEXT
       ======================================================== */
    .stSelectbox label,
    .stMultiSelect label,
    .stDateInput label,
    .stSlider label {
        color: #cbd5e1 !important;
    }

    .stCaption,
    [data-testid="stCaptionContainer"] {
        color: #94a3b8 !important;
    }

    hr {
        border-color: #273449 !important;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        border: 1px solid #273449;
        border-radius: 12px;
        overflow: hidden;
    }

    /* ========================================================
       VISUAL HEIGHT / ALIGNMENT
       Both dashboard area and sidebar occupy the full viewport.
       ======================================================== */
    [data-testid="stSidebar"] section {
        min-height: 100vh !important;
    }

    [data-testid="stMainBlockContainer"] {
        min-height: calc(100vh - 4rem) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA LOADING
# ============================================================
@st.cache_data
def load_data(path="Superstore.csv"):
    df = pd.read_csv(path)

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # Postal Code is an identifier, not a numeric measure
    if "Postal Code" in df.columns:
        df["Postal Code"] = df["Postal Code"].astype("Int64").astype(str)

    # Useful calculated fields
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
    df["Profit Margin"] = df["Profit"].div(df["Sales"]).where(df["Sales"] != 0) * 100

    return df


# ============================================================
# HELPERS
# ============================================================
def money(value):
    return f"${value:,.2f}"


def compact_money(value):
    value = float(value)
    if abs(value) >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    if abs(value) >= 1_000:
        return f"${value/1_000:.1f}K"
    return f"${value:,.0f}"


def pct(value):
    if pd.isna(value):
        return "N/A"
    return f"{value:.2f}%"


def apply_filters(df):
    filtered = df.copy()

    st.sidebar.markdown(
        '<div class="sidebar-heading">🎛️ Filters</div>',
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        '<div class="sidebar-subtitle">Use the filters to refine your analysis</div>',
        unsafe_allow_html=True
    )

    categories = sorted(df["Category"].dropna().unique())
    segments = sorted(df["Segment"].dropna().unique())
    regions = sorted(df["Region"].dropna().unique())
    states = sorted(df["State"].dropna().unique())

    # Each filter is kept inside a compact expander so the sidebar
    # behaves like a professional filter panel instead of a long list.
    with st.sidebar.expander("📂 Category", expanded=False):
        selected_categories = st.multiselect(
            "Select category",
            categories,
            default=categories,
            placeholder="Choose category...",
            label_visibility="collapsed",
            key="filter_category"
        )

    with st.sidebar.expander("👥 Segment", expanded=False):
        selected_segments = st.multiselect(
            "Select segment",
            segments,
            default=segments,
            placeholder="Choose segment...",
            label_visibility="collapsed",
            key="filter_segment"
        )

    with st.sidebar.expander("🌎 Region", expanded=False):
        selected_regions = st.multiselect(
            "Select region",
            regions,
            default=regions,
            placeholder="Choose region...",
            label_visibility="collapsed",
            key="filter_region"
        )

    with st.sidebar.expander("📍 State", expanded=False):
        selected_states = st.multiselect(
            "Select state",
            states,
            default=states,
            placeholder="Choose state...",
            label_visibility="collapsed",
            key="filter_state"
        )

    min_date = df["Order Date"].min().date()
    max_date = df["Order Date"].max().date()

    with st.sidebar.expander("📅 Order Date", expanded=False):
        selected_dates = st.date_input(
            "Select date range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            label_visibility="collapsed",
            key="filter_date"
        )

    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
        filtered = filtered[
            (filtered["Order Date"].dt.date >= start_date) &
            (filtered["Order Date"].dt.date <= end_date)
        ]

    if selected_categories:
        filtered = filtered[filtered["Category"].isin(selected_categories)]
    else:
        filtered = filtered.iloc[0:0]

    if selected_segments:
        filtered = filtered[filtered["Segment"].isin(selected_segments)]
    else:
        filtered = filtered.iloc[0:0]

    if selected_regions:
        filtered = filtered[filtered["Region"].isin(selected_regions)]
    else:
        filtered = filtered.iloc[0:0]

    if selected_states:
        filtered = filtered[filtered["State"].isin(selected_states)]
    else:
        filtered = filtered.iloc[0:0]

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        '<div class="small-note">💡 Click any filter to open its dropdown menu.</div>',
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        '<div class="small-note">Built with Streamlit • Pandas • Plotly</div>',
        unsafe_allow_html=True
    )

    return filtered


def chart_layout(fig, height=390):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc"),
        title_font=dict(color="#ffffff", size=17),
        legend=dict(
            title_font=dict(color="#ffffff", size=13),
            font=dict(color="#ffffff", size=13)
        ),
        xaxis=dict(gridcolor="#263449", zerolinecolor="#334155"),
        yaxis=dict(gridcolor="#263449", zerolinecolor="#334155", tickfont=dict(size=11, color="#cbd5e1")),
        height=height,
        margin=dict(l=15, r=15, t=55, b=15),
        hovermode="x unified",
        legend_title_text=""
    )
    return fig


# ============================================================
# LOAD DATA
# ============================================================
try:
    df = load_data("Superstore.csv")
except FileNotFoundError:
    st.error(
        "Superstore.csv was not found. Keep Superstore.csv in the same "
        "folder as app.py."
    )
    st.stop()
except Exception as e:
    st.error(f"Unable to load the dataset: {e}")
    st.stop()

required_columns = [
    "Order ID", "Order Date", "Ship Date", "Ship Mode", "Customer ID",
    "Customer Name", "Segment", "State", "Region", "Category",
    "Sub-Category", "Product Name", "Sales", "Quantity", "Discount", "Profit"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"Missing required columns: {', '.join(missing_columns)}")
    st.stop()

filtered_df = apply_filters(df)


# ============================================================
# HEADER
# ============================================================
st.markdown(
    '<div class="dashboard-title">📊 Sales Analytics Dashboard</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="dashboard-subtitle">'
    'Interactive business intelligence dashboard • Sales, profit, products & regional performance'
    '</div>',
    unsafe_allow_html=True
)

if filtered_df.empty:
    st.warning("No records match the selected filters. Please change the filters.")
    st.stop()


# ============================================================
# KPIs
# ============================================================
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_quantity = filtered_df["Quantity"].sum()
avg_order_value = total_sales / total_orders if total_orders else 0
profit_margin = (total_profit / total_sales * 100) if total_sales else 0

k1, k2, k3, k4, k5 = st.columns(5)

k1.metric("💰 Total Sales", compact_money(total_sales))
k2.metric("📈 Total Profit", compact_money(total_profit))
k3.metric("🧾 Orders", f"{total_orders:,}")
k4.metric("📦 Quantity Sold", f"{total_quantity:,}")
k5.metric("🎯 Profit Margin", pct(profit_margin))

st.caption(
    f"Showing {len(filtered_df):,} sales records from "
    f"{filtered_df['Order Date'].min().strftime('%d %b %Y')} to "
    f"{filtered_df['Order Date'].max().strftime('%d %b %Y')}"
)

st.markdown("---")


# ============================================================
# TABS
# ============================================================
tab_overview, tab_sales, tab_profit, tab_products, tab_geo = st.tabs(
    ["🏠 Overview", "💰 Sales", "📈 Profit", "🏆 Products", "🌎 Geography"]
)


# ============================================================
# OVERVIEW TAB
# ============================================================
with tab_overview:
    st.markdown('<div class="section-title">Business Overview</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        category_sales = (
            filtered_df.groupby("Category", as_index=False)["Sales"]
            .sum()
            .sort_values("Sales", ascending=False)
        )

        fig = px.bar(
            category_sales,
            x="Category",
            y="Sales",
            title="Sales by Category",
            text_auto=".2s"
        )
        fig.update_traces(textposition="outside")
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    with col2:
        segment_sales = (
            filtered_df.groupby("Segment", as_index=False)["Sales"]
            .sum()
            .sort_values("Sales", ascending=False)
        )

        fig = px.pie(
            segment_sales,
            names="Segment",
            values="Sales",
            title="Sales Distribution by Segment",
            hole=0.48
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        monthly = (
            filtered_df.groupby("Month", as_index=False)["Sales"]
            .sum()
            .sort_values("Month")
        )

        fig = px.line(
            monthly,
            x="Month",
            y="Sales",
            title="Monthly Sales Trend",
            markers=True
        )
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    with col4:
        monthly_profit = (
            filtered_df.groupby("Month", as_index=False)["Profit"]
            .sum()
            .sort_values("Month")
        )

        fig = px.line(
            monthly_profit,
            x="Month",
            y="Profit",
            title="Monthly Profit Trend",
            markers=True
        )
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    # Quick insights
    best_category = category_sales.iloc[0]["Category"]
    best_category_sales = category_sales.iloc[0]["Sales"]

    best_segment = segment_sales.iloc[0]["Segment"]
    best_segment_sales = segment_sales.iloc[0]["Sales"]

    best_product_row = (
        filtered_df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .iloc[0]
    )

    st.markdown(
        f"""
        <div class="insight-box">
        <b>💡 Quick Insights</b><br><br>
        • Highest sales category: <b>{best_category}</b>
        ({money(best_category_sales)})<br>
        • Leading customer segment: <b>{best_segment}</b>
        ({money(best_segment_sales)})<br>
        • Top product by sales: <b>{best_product_row['Product Name']}</b>
        ({money(best_product_row['Sales'])})
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SALES TAB
# ============================================================
with tab_sales:
    st.markdown('<div class="section-title">Sales Performance</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        subcategory_sales = (
            filtered_df.groupby("Sub-Category", as_index=False)["Sales"]
            .sum()
            .sort_values("Sales", ascending=True)
        )

        fig = px.bar(
            subcategory_sales,
            x="Sales",
            y="Sub-Category",
            orientation="h",
            title="Sales by Sub-Category",
            text_auto=".2s"
        )
        st.plotly_chart(chart_layout(fig, 470), use_container_width=True)

    with col2:
        ship_sales = (
            filtered_df.groupby("Ship Mode", as_index=False)["Sales"]
            .sum()
            .sort_values("Sales", ascending=False)
        )

        fig = px.bar(
            ship_sales,
            x="Ship Mode",
            y="Sales",
            title="Sales by Ship Mode",
            text_auto=".2s"
        )
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    monthly_sales = (
        filtered_df.groupby("Month", as_index=False)
        .agg(Sales=("Sales", "sum"), Orders=("Order ID", "nunique"))
        .sort_values("Month")
    )

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=monthly_sales["Month"],
            y=monthly_sales["Sales"],
            name="Sales"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=monthly_sales["Month"],
            y=monthly_sales["Orders"],
            name="Orders",
            mode="lines+markers",
            yaxis="y2"
        )
    )
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#cbd5e1"),
        title_font=dict(color="#f8fafc", size=17),
        title="Monthly Sales & Orders",
        yaxis=dict(title="Sales"),
        yaxis2=dict(
            title="Orders",
            overlaying="y",
            side="right"
        ),
        height=430,
        margin=dict(l=15, r=15, t=55, b=15)
    )
    st.plotly_chart(fig, use_container_width=True)


# ============================================================
# PROFIT TAB
# ============================================================
with tab_profit:
    st.markdown('<div class="section-title">Profitability Analysis</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        profit_category = (
            filtered_df.groupby("Category", as_index=False)["Profit"]
            .sum()
            .sort_values("Profit", ascending=False)
        )

        fig = px.bar(
            profit_category,
            x="Category",
            y="Profit",
            title="Profit by Category",
            text_auto=".2s"
        )
        fig.add_hline(y=0, line_dash="dash")
        st.plotly_chart(chart_layout(fig), use_container_width=True)

    with col2:
        profit_subcategory = (
            filtered_df.groupby("Sub-Category", as_index=False)["Profit"]
            .sum()
            .sort_values("Profit", ascending=True)
        )

        fig = px.bar(
            profit_subcategory,
            x="Profit",
            y="Sub-Category",
            orientation="h",
            title="Profit by Sub-Category",
            text_auto=".2s"
        )
        fig.add_vline(x=0, line_dash="dash")
        st.plotly_chart(chart_layout(fig, 470), use_container_width=True)

    sales_profit = filtered_df[["Sales", "Profit", "Category"]].copy()

    fig = px.scatter(
        sales_profit,
        x="Sales",
        y="Profit",
        color="Category",
        hover_data=["Sales", "Profit"],
        title="Sales vs Profit",
        opacity=0.68
    )
    fig.add_hline(y=0, line_dash="dash")
    st.plotly_chart(chart_layout(fig, 480), use_container_width=True)

    loss_orders = int((filtered_df["Profit"] < 0).sum())
    profitable_orders = int((filtered_df["Profit"] >= 0).sum())

    p1, p2, p3 = st.columns(3)
    p1.metric("Profitable Records", f"{profitable_orders:,}")
    p2.metric("Loss-Making Records", f"{loss_orders:,}")
    p3.metric("Average Profit / Record", money(filtered_df["Profit"].mean()))


# ============================================================
# PRODUCTS TAB
# ============================================================
with tab_products:
    st.markdown('<div class="section-title">Product Performance</div>', unsafe_allow_html=True)

    product_sales = (
        filtered_df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    product_profit = (
        filtered_df.groupby("Product Name", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
        .head(10)
    )

    # Short labels are used ONLY on charts so long product names
    # don't squeeze the bars and make the visualization unreadable.
    # Full product names remain available in the hover tooltip and table.
    def short_product_name(name, max_chars=27):
        name = str(name).strip()
        if len(name) <= max_chars:
            return name
        return name[:max_chars - 3].rstrip() + "..."

    product_sales["Chart Name"] = product_sales["Product Name"].apply(short_product_name)
    product_profit["Chart Name"] = product_profit["Product Name"].apply(short_product_name)

    col1, col2 = st.columns(2)

    with col1:
        sales_chart = product_sales.sort_values("Sales")

        fig = px.bar(
            sales_chart,
            x="Sales",
            y="Chart Name",
            orientation="h",
            title="Top 10 Products — Sales",
            text_auto=".2s",
            custom_data=["Product Name"]
        )

        fig.update_traces(
            hovertemplate="<b>%{customdata[0]}</b><br>Sales: %{x:$,.2f}<extra></extra>"
        )

        st.plotly_chart(chart_layout(fig, 520), use_container_width=True)

    with col2:
        profit_chart = product_profit.sort_values("Profit")

        fig = px.bar(
            profit_chart,
            x="Profit",
            y="Chart Name",
            orientation="h",
            title="Top 10 Products — Profit",
            text_auto=".2s",
            custom_data=["Product Name"]
        )

        fig.update_traces(
            hovertemplate="<b>%{customdata[0]}</b><br>Profit: %{x:$,.2f}<extra></extra>"
        )

        fig.add_vline(x=0, line_dash="dash")
        st.plotly_chart(chart_layout(fig, 520), use_container_width=True)

    st.markdown("### Product Performance Table")

    display_table = product_sales[["Product Name", "Sales"]].copy()

    profit_lookup = product_profit.set_index("Product Name")["Profit"]
    display_table["Profit"] = display_table["Product Name"].map(profit_lookup).fillna(0)

    quantity_lookup = (
        filtered_df.groupby("Product Name")["Quantity"]
        .sum()
    )
    display_table["Quantity"] = display_table["Product Name"].map(quantity_lookup).fillna(0).astype(int)

    display_table["Sales"] = display_table["Sales"].map(lambda x: f"${x:,.2f}")
    display_table["Profit"] = display_table["Profit"].map(lambda x: f"${x:,.2f}")

    st.dataframe(
        display_table,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# GEOGRAPHY TAB
# ============================================================
with tab_geo:
    st.markdown('<div class="section-title">Geographic Performance</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        state_sales = (
            filtered_df.groupby("State", as_index=False)["Sales"]
            .sum()
            .sort_values("Sales", ascending=False)
            .head(15)
        )

        fig = px.bar(
            state_sales.sort_values("Sales"),
            x="Sales",
            y="State",
            orientation="h",
            title="Top 15 States by Sales",
            text_auto=".2s"
        )
        st.plotly_chart(chart_layout(fig, 520), use_container_width=True)

    with col2:
        state_profit = (
            filtered_df.groupby("State", as_index=False)["Profit"]
            .sum()
            .sort_values("Profit", ascending=False)
            .head(15)
        )

        fig = px.bar(
            state_profit.sort_values("Profit"),
            x="Profit",
            y="State",
            orientation="h",
            title="Top 15 States by Profit",
            text_auto=".2s"
        )
        fig.add_vline(x=0, line_dash="dash")
        st.plotly_chart(chart_layout(fig, 520), use_container_width=True)

    region_summary = (
        filtered_df.groupby("Region", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    st.markdown("### Region Performance")
    st.dataframe(
        region_summary.style.format({
            "Sales": "${:,.2f}",
            "Profit": "${:,.2f}",
            "Orders": "{:,.0f}",
            "Quantity": "{:,.0f}"
        }),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption(
    "Sales Analytics Dashboard • Built with Streamlit + Pandas + Plotly"
)
