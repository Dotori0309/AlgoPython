import matplotlib.pyplot as plt

X = [ "Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun" ]
Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2 , 22.4]
Y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1 , 26.3]

Y3 = [40, 20, 10, 30]
Y3_labels = ["Eating Out", "Shopping", "Groceries", "Housing"]

# 막대그래프
plt.bar(X, Y1)
plt.show()

# 파이차트
explode = [0.1, 0, 0, 0]    # 하나의 파이를 분리하여 표시
plt.pie(Y3, labels=Y3_labels, explode = explode)

plt.show()

