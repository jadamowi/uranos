import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame(pd.read_csv(r'C:\Users\jakub\Downloads\religion_vs_GDP_per_Capita.csv',
                              sep=',',
                              index_col='country')
                  ).drop(['Unnamed: 0'], axis=1)

# Generate correlation matrix
corr = df.corr(method='pearson')

# Generate chart in seaborn
xlim = [0, 85000]
ylim = [0, 100]

chart = sns.jointplot(
    x="US$",
    y="religiousity%",
    data=df,
    kind="reg",
    color=(0.1, 0.4, 0.5),
    xlim=xlim,
    ylim=ylim,
    marker="+"
)


chart.set_axis_labels('GDP per capita [$]', 'Religiosity [%]', fontsize=10)

chart.fig.suptitle('Religiosity vs GDP in countries')
chart.fig.set_figwidth(15)
chart.fig.set_figheight(6)

plt.show()
