import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read csv file
csv_file = "./stat/stat_test_data.csv"

df = pd.read_csv(csv_file)

# Create a chart
plt.figure(figsize=(13, 10))

sns.set(font_scale=3, style="whitegrid")

'''
# boxplot (Dice vs Train Size)
# y = PA, Dice, mIoU
ax = sns.boxplot(x="Train Size", y="Dice", hue="Trainable Layers", data=df)

plt.xlabel("Train Size", fontsize=35)
plt.ylabel("DSC", fontsize=35)
plt.title("DSC vs. Train Size by Trainable Layers", fontsize=35)
plt.legend(title="Trainable Layers")

# Move the legend to the bottom right
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 0))


# scatter plot (Dice vs PA)
sns.scatterplot(x="PA", y="Dice", hue="Trainable Layers", data=df, s=180)
ax = sns.regplot(x='PA', y='Dice', data=df, line_kws={'color': 'r'}, scatter=False)

plt.xlabel("PA", fontsize=40)
plt.ylabel("DSC", fontsize=40)
plt.title("PA vs. DSC by Trainable Layers", fontsize=40)

plt.legend(loc='lower right', fontsize="30")


# scatter plot (Dice vs mIoU)
sns.scatterplot(x="mIoU", y="Dice", hue="Trainable Layers", data=df, s=180)
ax = sns.regplot(x='mIoU', y='Dice', data=df, line_kws={'color': 'r'}, scatter=False)

plt.xlabel("mIoU", fontsize=40)
plt.ylabel("DSC", fontsize=40)
plt.title("mIoU vs. DSC by Trainable Layers", fontsize=40)

plt.legend(loc='lower right', fontsize="30")

'''
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
