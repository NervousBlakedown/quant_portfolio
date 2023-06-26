# Quant Risk Assessment: Credit Risk Model
# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import plotly.express as px
import plotly.graph_objs as go

# Set a random seed for reproducibility
np.random.seed(0)

# Create a customer_id column in df with unique random long floats
# customer_ids = np.unique(np.random.randint(1, 1e10, size=2*n_samples)[:n_samples])

If customer_ids length is less than n_samples (due to np.unique), regenerate the ids
while len(customer_ids) < n_samples:
    additional_ids = np.random.rand(n_samples - len(customer_ids)) * 1e10
    customer_ids = np.unique(np.concatenate((customer_ids, additional_ids)))

# Define the number of samples
n_samples = 1000

# Create a dictionary with data
data = {
    # 'customer_id': np.unique(np.random.rand(n_samples) * 100000), #1e10),
    'customer_id': np.random.randint(1000, 198234870, n_samples),
    'age': np.random.randint(18, 70, n_samples),
    'income': np.random.randint(30000, 80000, n_samples),
    'loan_amount': np.random.randint(5000, 50000, n_samples),
    'default': np.random.randint(0, 2, n_samples)  # 0 for repaid, 1 for default
}

# Create a DataFrame
credit_risk_data = pd.DataFrame(data)

# Check the first few rows of the DataFrame
print(credit_risk_data.head())

# Make variable 'df' for consistency (not needed, but helpful in this case)
df = credit_risk_data

# Add index value: customer id column to df
df['customer_id'] = customer_ids

# Calculate the percentages of people who defaulted on loans and who didn't
percentage_default = (df['default'].sum() / len(df)) * 100
percentage_no_default = 100 - percentage_default

# Assume 'age', 'income', 'loan_amount' are the features 
# And 'default' is the target variable with values 0 (No Default) or 1 (Default)
X = df[['age', 'income', 'loan_amount']]
y = df['default']

# Split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Print the confusion matrix
print(confusion_matrix(y_test, y_pred))

# Print the classification report
print(classification_report(y_test, y_pred))

# Visualize the data with scatter matrix plot using Plotly
# fig = px.scatter_matrix(df, dimensions=["age", "income", "loan_amount"], color="default")
# fig.show()

# Separate the data into two dataframes based on the 'default' column
df_0 = df[df['default'] == 0]
df_1 = df[df['default'] == 1]

# Create a scatter3d trace for each dataframe
trace0 = go.Scatter3d(
    x=df_0['age'],
    y=df_0['income'],
    z=df_0['loan_amount'],
    mode='markers',
    marker=dict(size=5, color='blue', symbol='circle'),
    name='Repaid',
    hovertext=df_0.index
)

trace1 = go.Scatter3d(
    x=df_1['age'],
    y=df_1['income'],
    z=df_1['loan_amount'],
    mode='markers',
    marker=dict(size=5, color='red', symbol='diamond'),
    name='Default',
    hovertext=df_1.index
)

# Combine traces into a list
data = [trace0, trace1]

# Create layout and add the calculated percentagess
layout = go.Layout(
    title={
        'text': '3D Scatter plot of Credit Risk Data',
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    scene=dict(
        xaxis_title='Age',
        yaxis_title='Income',
        zaxis_title='Loan Amount'
    ),
    autosize=True,
    margin=dict(l=0, r=0, b=0, t=0),
    title_x=0.5,  # this centers the title
    annotations=[
        dict(
            text=f"Percentage who defaulted: {percentage_default:.2f}%<br>"
                 f"Percentage who didn't default: {percentage_no_default:.2f}%",
            showarrow=False,
            align='right',
            x=1,
            y=1,
            xref='paper',
            yref='paper',
            xanchor='center',
            yanchor='bottom',
            font=dict(size=12)
        )
    ]
)

# Show 3D scatterplot (optional view, but interesting, regardless)
fig = go.Figure(data=data, layout=layout)
# fig = px.scatter_3d(df, x='age', y='income', z='loan_amount', color='default')
fig.show()
