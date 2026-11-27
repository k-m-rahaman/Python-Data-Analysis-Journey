
# Linear Regression

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score


def main():
    # Generate sample regression data
    X, y = make_regression(
        n_samples=200,
        n_features=1,
        noise=15,
        random_state=42
    )

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, predictions)

    print("LINEAR REGRESSION")
    print("-----------------")

    print("Coefficient:", round(model.coef_[0], 2))
    print("Intercept:", round(model.intercept_, 2))

    print("\nMODEL EVALUATION")
    print("----------------")

    print("Mean Absolute Error:", round(mae, 2))
    print("Mean Squared Error:", round(mse, 2))
    print("Root Mean Squared Error:", round(rmse, 2))
    print("R2 Score:", round(r2, 3))

    # Predict a new value
    new_value = [[2.0]]
    result = model.predict(new_value)

    print("\nPrediction for input 2.0:", round(result[0], 2))


if __name__ == "__main__":
    main()
