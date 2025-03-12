import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read csv file
csv_file = "./stat/stat_test_data.csv"

df = pd.read_csv(csv_file)

# Create a chart
plt.figure(figsize=(13, 10))

sns.set(font_scale=3, style="whitegrid")

# plot bar chart (Dice vs Trainable Layers)
ax = sns.barplot(x="Fine-tuning Strategy", y="Dice",
                 hue="Train Size",
                 palette="flare",
                 data=df)

sns.move_legend(ax, "lower center",
                bbox_to_anchor=(.5, 0.97),
                ncol=4, title="Train Size", frameon=False)

plt.xlabel("Fine-tuning Strategy", fontsize=30)
plt.ylabel("DSC")

plt.legend(title="Train Size",
           bbox_to_anchor=(0., 1.02, 1., .102),
           loc='lower left',
           fontsize=27,
           title_fontsize=27,
           ncol=4, mode="expand", borderaxespad=0.)


# display plots
plt.grid(False)
plt.show()
