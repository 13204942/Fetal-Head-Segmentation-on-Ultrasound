import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read csv file
csv_file = "./stat/stat_test_data.csv"

df = pd.read_csv(csv_file)

# Create a chart
plt.figure(figsize=(13, 10))

sns.set(font_scale=3, style="whitegrid")

# boxplot (Dice vs Train Size)
# y = PA, Dice, mIoU
ax = sns.boxplot(x="Train Size", y="Dice", hue="Fine-tuning Strategy", data=df, flierprops={"marker": "o"})

plt.xlabel("Training Size", fontsize=35)
plt.ylabel("DSC", fontsize=35)

# Move the legend to the bottom right
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 0))

new_labels = ['U-Net baseline', 'strategy (c)', 'strategy (i)']
for t, l in zip(ax.legend().texts, new_labels):
    t.set_text(l)

# display plots
plt.grid(True)
plt.show()
