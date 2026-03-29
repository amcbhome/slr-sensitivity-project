import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Cost Sensitivity Analysis", layout="wide")

st.title("📊 Maintenance Cost Sensitivity Analysis")

st.markdown("""
This dashboard compares **January and October regression models** to show how
maintenance costs respond differently to production activity.

- January: Lower variable cost (flatter slope)
- October: Higher variable cost (steeper slope)
""")

# Regression parameters (from your calculations)
jan_a, jan_b = 218.85, 2.97
oct_a, oct_b = 124.24, 3.396

# X range
x = np.linspace(100, 300, 50)

# Calculate lines
jan_y = jan_a + jan_b * x
oct_y = oct_a + oct_b * x

# Interactive slider
x_selected = st.slider("Select Machine Hours", 100, 300, 260)

jan_point = jan_a + jan_b * x_selected
oct_point = oct_a + oct_b * x_selected

# Plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=jan_y, mode='lines', name='January'))
fig.add_trace(go.Scatter(x=x, y=oct_y, mode='lines', name='October'))

# Highlight selected points
fig.add_trace(go.Scatter(x=[x_selected], y=[jan_point],
                        mode='markers', name='Jan Selected'))

fig.add_trace(go.Scatter(x=[x_selected], y=[oct_point],
                        mode='markers', name='Oct Selected'))

fig.update_layout(
    title="Cost vs Machine Hours",
    xaxis_title="Machine Hours",
    yaxis_title="Maintenance Cost"
)

st.plotly_chart(fig, use_container_width=True)

# Output values
st.subheader("📌 Selected Output")

col1, col2 = st.columns(2)

with col1:
    st.metric("January Cost", f"{jan_point:.2f}")

with col2:
    st.metric("October Cost", f"{oct_point:.2f}")

# Explanation
st.subheader("🧠 Interpretation")

st.markdown(f"""
At **{x_selected} machine hours**:

- January cost = **£{jan_point:.2f}**
- October cost = **£{oct_point:.2f}**

👉 October increases faster because it has a **higher slope (variable cost)**.

This demonstrates that:
- **Cost sensitivity to activity differs by month**
- Higher slopes indicate **greater variable cost per unit**
""")
