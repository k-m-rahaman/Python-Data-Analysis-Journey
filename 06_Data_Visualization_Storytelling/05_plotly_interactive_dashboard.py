
"""
File: 05_plotly_interactive_dashboard.py
Topic: Interactive Visualization with Plotly

Description:
    Creates an interactive business dashboard
    using Plotly and monthly sales data.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

from plotly.subplots import make_subplots


def create_interactive_dashboard():

    print("=" * 55)
    print("PLOTLY INTERACTIVE DASHBOARD")
    print("=" * 55)

    # Monthly business dataset.

    sales = pd.DataFrame({

        "month": [
            "Jan", "Feb", "Mar",
            "Apr", "May", "Jun"
        ],

        "revenue": [
            12000, 15000, 13500,
            18000, 21000, 24000
        ],

        "orders": [
            120, 145, 138,
            170, 195, 220
        ]
    })

    # Create dashboard layout.

    fig = make_subplots(

        rows=1,
        cols=2,

        subplot_titles=[
            "Monthly Revenue Trend",
            "Monthly Orders"
        ]
    )

    # 1. Interactive line chart.

    fig.add_trace(

        go.Scatter(

            x=sales["month"],

            y=sales["revenue"],

            mode="lines+markers",

            name="Revenue",

            hovertemplate=(
                "Month: %{x}<br>"
                "Revenue: Rs. %{y:,.0f}"
                "<extra></extra>"
            )
        ),

        row=1,
        col=1
    )

    # 2. Interactive bar chart.

    fig.add_trace(

        go.Bar(

            x=sales["month"],

            y=sales["orders"],

            name="Orders",

            hovertemplate=(
                "Month: %{x}<br>"
                "Orders: %{y}"
                "<extra></extra>"
            )
        ),

        row=1,
        col=2
    )

    # Customize dashboard.

    fig.update_layout(

        title_text="Business Performance Dashboard",

        template="plotly_white",

        height=550,

        width=1100,

        showlegend=False
    )

    fig.update_xaxes(
        title_text="Month"
    )

    fig.update_yaxes(
        title_text="Revenue (INR)",
        row=1,
        col=1
    )

    fig.update_yaxes(
        title_text="Number of Orders",
        row=1,
        col=2
    )

    # Save interactive dashboard.

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_file = (
        output_dir / "05_interactive_dashboard.html"
    )

    fig.write_html(

        str(output_file),

        include_plotlyjs="cdn",

        full_html=True
    )

    # Display business summary.

    print(
        f"\nTotal revenue: Rs. "
        f"{sales['revenue'].sum():,}"
    )

    print(
        f"Total orders: "
        f"{sales['orders'].sum()}"
    )

    print(
        f"Average monthly revenue: Rs. "
        f"{sales['revenue'].mean():,.2f}"
    )

    print("\nInteractive dashboard created successfully.")

    print(
        "Dashboard saved: "
        "outputs/05_interactive_dashboard.html"
    )


if __name__ == "__main__":
    create_interactive_dashboard()
