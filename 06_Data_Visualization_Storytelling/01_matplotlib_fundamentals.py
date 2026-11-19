
"""
File: 01_matplotlib_fundamentals.py
Topic: Matplotlib Fundamentals

Description:
    Demonstrates different visualization techniques
    using a monthly business sales dataset.

Author: Kazi Mustafijur Rahaman
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def create_visualizations():

    print("=" * 55)
    print("MATPLOTLIB FUNDAMENTALS")
    print("=" * 55)

    # Monthly sales dataset.

    months = [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun"
    ]

    revenue = np.array([
        12000, 15000, 13500,
        18000, 21000, 24000
    ])

    customers = np.array([
        120, 145, 138,
        170, 195, 220
    ])

    # Create a 2x2 dashboard.

    fig, axes = plt.subplots(
        2, 2,
        figsize=(13, 9)
    )

    # 1. Line chart.

    axes[0, 0].plot(
        months,
        revenue,
        marker="o",
        linewidth=2
    )

    axes[0, 0].set_title("Monthly Revenue Trend")
    axes[0, 0].set_xlabel("Month")
    axes[0, 0].set_ylabel("Revenue (INR)")
    axes[0, 0].grid(True, alpha=0.3)

    # 2. Bar chart.

    axes[0, 1].bar(
        months,
        revenue
    )

    axes[0, 1].set_title("Monthly Revenue Comparison")
    axes[0, 1].set_xlabel("Month")
    axes[0, 1].set_ylabel("Revenue (INR)")

    # 3. Scatter plot.

    axes[1, 0].scatter(
        customers,
        revenue,
        s=80
    )

    axes[1, 0].set_title("Customers vs Revenue")
    axes[1, 0].set_xlabel("Customers")
    axes[1, 0].set_ylabel("Revenue (INR)")
    axes[1, 0].grid(True, alpha=0.3)

    # 4. Histogram.

    axes[1, 1].hist(
        revenue,
        bins=5,
        edgecolor="black"
    )

    axes[1, 1].set_title("Revenue Distribution")
    axes[1, 1].set_xlabel("Revenue (INR)")
    axes[1, 1].set_ylabel("Frequency")

    # Dashboard title.

    fig.suptitle(
        "Business Revenue Analysis",
        fontsize=16
    )

    fig.tight_layout()

    # Save visualization.

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "01_matplotlib_dashboard.png"

    fig.savefig(
        output_file,
        dpi=150,
        bbox_inches="tight"
    )

    # Display summary.

    print(f"Total revenue: Rs. {np.sum(revenue):,}")

    print(
        f"Average monthly revenue: Rs. "
        f"{np.mean(revenue):,.2f}"
    )

    highest_month = months[np.argmax(revenue)]

    print(
        f"Highest revenue month: "
        f"{highest_month}"
    )

    print(f"Chart saved: outputs/{output_file.name}")

    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    create_visualizations()
