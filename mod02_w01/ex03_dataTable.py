import pandas as pd

df = pd.read_csv("Module2/Week1/advertising.csv")
data = df.to_numpy()


# Question 15


def get_col(data, num_col):
    for i in range(len(data)):
        yield data[i][num_col]


sales_col = list(get_col(data, 3))
max_sales = max(sales_col)
print("15C.", f"Max: {max_sales} - Index: {sales_col.index(max_sales)}", sep="\n")

# Question 16

tv_col = list(get_col(data, 0))
average_tv = sum(tv_col) / len(tv_col)
print("16B.", average_tv, sep="\n")

# Question 17

sales_col = list(get_col(data, 3))
bigger20_sales = [num for num in sales_col if num >= 20]
print("17A.", len(bigger20_sales), sep="\n")


# Question 18

radio_sales_col = [list(get_col(data, 1)), list(get_col(data, 3))]
bigger15_sales_idx = [idx for idx, num in enumerate(radio_sales_col[1]) if num >= 15]
bigger15_radio = [radio_sales_col[0][idx] for idx in bigger15_sales_idx]
average_radio = sum(bigger15_radio) / len(bigger15_radio)
print("18B.", average_radio, sep="\n")


# Question 19

news_col = list(df['Newspaper'])
sales_col = list(df['Sales'])
average_news = sum(news_col) / len(news_col)
bigger_average_news = [sales_col[index] for index, num in enumerate(news_col) if num > average_news]
print("19C", sum(bigger_average_news), sep="\n")
# Question 20

average_sales = sum(sales_col) / len(sales_col)
scores = [0] * len(sales_col)
for i in range(len(sales_col)):
    if sales_col[i] > average_sales:
        scores[i] = "Good"
    elif sales_col[i] == average_sales:
        scores[i] = "Average"
    else:
        scores[i] = "Bad"
print("20C.", scores[7:10], sep="\n")


# Question 21

closest_val = min(sales_col, key=lambda x: abs(x - average_sales))
scores1 = [0] * len(sales_col)
for i in range(len(sales_col)):
    if sales_col[i] > closest_val:
        scores1[i] = "Good"
    elif sales_col[i] == closest_val:
        scores1[i] = "Average"
    else:
        scores1[i] = "Bad"

print("21C.", scores1[7:10], sep="\n")