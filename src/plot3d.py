import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px

def load_data(path="data/Jan_June2025.csv"):
    return pd.read_csv(path)

def plot_matplotlib(df):
    x, y, z, mag = df["LocX [m]"], df["LocY [m]"], df["LocZ [m]"], df["Local Magnitude"]
    sizes = (mag - mag.min() + 1) * 20

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x, y, z, c=mag, s=sizes, cmap="viridis", alpha=0.6)

    ax.set_xlabel("LocX [m]")
    ax.set_ylabel("LocY [m]")
    ax.set_zlabel("LocZ [m]")
    plt.colorbar(sc, label="Local Magnitude")
    plt.title("3D Scatter (Matplotlib)")
    plt.show()

def plot_plotly(df):
    sizes = (df["Local Magnitude"] - df["Local Magnitude"].min() + 1) * 5
    fig = px.scatter_3d(
        df,
        x="LocX [m]",
        y="LocY [m]",
        z="LocZ [m]",
        size=sizes,
        color="Local Magnitude",
        hover_data=["EventDate", "EventTimeInDay", "TriggerCount"],
        opacity=0.7,
        color_continuous_scale="Viridis",
        title="3D Scatter (Plotly)"
    )
    fig.update_layout(
        scene=dict(
            xaxis_title="LocX [m]",
            yaxis_title="LocY [m]",
            zaxis_title="LocZ [m]"
        ),
        margin=dict(l=0, r=0, b=0, t=30)
    )
    fig.show()

if __name__ == "__main__":
    df = load_data()
    print("✅ Data loaded. First rows:\n", df.head())

    # Run either plot
    plot_matplotlib(df)
    plot_plotly(df)
