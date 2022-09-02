import altair as alt
import streamlit as st

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

def get_chart(data):
    st.title("💬 Commenting app")

    source = "https://raw.githubusercontent.com/ham811/forest.ly/main/data/de.csv"
    all_symbols = source.symbol.unique()
    symbols = st.multiselect("Choose stocks to visualize", all_symbols, all_symbols[:3])

    space(1)

    source = source[source.symbol.isin(symbols)]
    chart = chart.get_chart(source)
    st.altair_chart(chart, use_container_width=True)

    space(2)

    hover = alt.selection_single(
        fields=["population"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Forest Data Analytics")
        .mark_line()
        .encode(
            x="population",
            y="Forest Parameter",
            color="symbol",
            strokeDash="symbol",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="population",
            y="Forest Parameter",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("population", title="Date"),
                alt.Tooltip("Forest Parameter", title="Forest Parameter (Unit)"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()