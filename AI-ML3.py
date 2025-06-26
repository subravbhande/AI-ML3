# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 2: Load the dataset
df = pd.read_csv("EducationDataset_Preprocessed.csv")

print("First 5 Rows:\n", df.head())
print("Shape of Dataset:", df.shape)
print("Missing Values:\n", df.isnull().sum())

# Step 3: Select features and target variable
x = df[["no_of_schools_sr_sec"]]   # independent variable
y = df["no_of_schools_total"]      # dependent variable


# Step 4: Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LinearRegression()
model.fit(x_train, y_train)

# Step 6: Predict on test data
y_pred = model.predict(x_test)

# Step 7: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation Metrics:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

# Step 8: Visualize the results
plt.scatter(x_test, y_test, color='red', label='Actual')
plt.plot(x_test, y_pred , color='blue', linewidth=2, label='Regression Line')
plt.xlabel("No. of Sr. Sec. Schools")
plt.ylabel("No. of Total Schools")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

# Step 9: Coefficients
print("\nModel Coefficients:")
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)
