import plotly.express as px
import csv
with open(r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\cafe.csv") as f:

    df=csv.DictReader(f)
    fig=px.scatter(df,x="sleep in hours",y="Coffee in ml")
    fig.show()


