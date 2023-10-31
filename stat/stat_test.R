library(readr)

data_file = "stat_test_data.csv"

stat_test_data <- read_csv(data_file)
stat_test_data$`Trainable Layers` <- as.factor(stat_test_data$`Trainable Layers`)
stat_test_data$`Train Size` <- as.factor(stat_test_data$`Train Size`)

stat_test_data = dplyr::rename(stat_test_data, layers = `Trainable Layers`)
stat_test_data = dplyr::rename(stat_test_data, tr_size = `Train Size`)

set.seed(1234)
dplyr::sample_n(stat_test_data, 10)
levels(stat_test_data$layers)
levels(stat_test_data$tr_size)

# Statistically analyse Trainable Layers
tmp_data <- stat_test_data[c(1,3)]  # Dice
#tmp_data <- stat_test_data[c(1,2)]  # PA
#tmp_data <- stat_test_data[c(1,4)]  # mIoU

aggregate(tmp_data$Dice, list(tmp_data$layers), FUN=mean)
aggregate(tmp_data$Dice, list(tmp_data$layers), FUN=var)

# Statistically analyse Train Size
#tmp_data <- stat_test_data[c(5,2)]  # PA
#tmp_data <- stat_test_data[c(5,3)]  # Dice
#tmp_data <- stat_test_data[c(5,4)]  # mIoU

# Compute the analysis of variance
## layers
#res.aov <- aov(Dice ~ layers, data = tmp_data)
#res.aov <- aov(PA ~ layers, data = tmp_data)
#res.aov <- aov(mIoU ~ layers, data = tmp_data)

## tr_size
res.aov <- aov(Dice ~ tr_size, data = tmp_data)
#res.aov <- aov(PA ~ tr_size, data = tmp_data)
#res.aov <- aov(mIoU ~ tr_size, data = tmp_data)


# Summary of the analysis
summary(res.aov)

# Tukey multiple pairwise-comparisons
TukeyHSD(res.aov)
