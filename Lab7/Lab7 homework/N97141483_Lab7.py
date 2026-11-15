
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = np.loadtxt("Bank_Customer.csv", skiprows=1, dtype=str, delimiter=',')

'''
Your work
非數值型資料需轉換成數值型資料 (country, gender)
去除掉無意義的特徵類別 (customer_id)
標準化特徵 (StandardScaler)
'''

# 移除 customer_id
data = data[:, 1:]

# 將 country 轉換成數值
countries = np.unique(data[:, 1])
data[:, 1] = np.searchsorted(countries, data[:, 1]).astype(str)

# 將 gender 轉換成數值
genders = np.unique(data[:, 2])
data[:, 2] = np.searchsorted(genders, data[:, 2]).astype(str)

# 轉換成數值型資料
data = data.astype(float)

# 分離特徵與分類結果 churn
x = data[:, :-1]
y = data[:, -1].astype(int)

'''
Your work
切割 data 為 x_train, x_test, y_train, y_test
請學習 train_test_split 的使用方法
'''

# 切割訓練集與測試集（80% 訓練、20% 測試）
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 標準化特徵
# 只使用訓練資料計算標準化參數，避免資料洩漏
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# 儲存標準化後的資料
# 訓練資料與測試資料合併，最後一欄為 churn
pre_data = np.vstack((
    np.column_stack((x_train, y_train)),
    np.column_stack((x_test, y_test))
))

np.savetxt("Bank_Customer_Preprocessed.csv", pre_data, delimiter=",")

from sklearn.linear_model import LogisticRegression

# 決策分類器
clf = LogisticRegression()

# 使用訓練集來訓練我們的分類器
clf.fit(x_train, y_train)

# 測試資料集中進行預測
pred = clf.predict(x_test)

#print (pred) # 預測分類，即客戶是否流失
#print (y_test) # 分類
print(str(accuracy_score(pred, y_test)*100) + "% ")  # 預測精度
