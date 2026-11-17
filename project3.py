import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
file_path =input("Enter your dataset path: ")
if Path(file_path).suffix.lower() == ".csv":
    data = pd.read_csv(file_path,sep=';')
else :
    data = pd.read_excel(file_path)

features = input("Enter features columns: ").split(',')
features = [f.strip() for f in features]
target = input("Enter target column: ").strip()
data = data[features + [target]]
x = data.drop(columns=[target]).values.tolist()
y = data[target].tolist()
iterations = int(input("Enter number of iterations: "))
test_percentage = float(input("Enter test percentage: "))
test_size = test_percentage / 100
decimal = int(input("Enter decimal places: "))
best_accuracy = 0
besst_model = None
for  i in range(iterations):
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=test_size)
    linear=LinearRegression()
    linear.fit(x_train,y_train)
    accuracy=linear.score(x_test,y_test)
    print(accuracy)
    if accuracy>best_accuracy:
        best_accuracy=accuracy
        best_model=linear
        best_x_test = x_test
        best_y_test = y_test
print(f"best accuracy : {best_accuracy}")
result = besst_model.predict(best_x_test)
for i in range (len(result)):
    print(f"{best_x_test[i]}{best_y_test[i]}=>{round(result[i],decimal)}")