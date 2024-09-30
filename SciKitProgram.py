import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    #data.fillna('None', inplace=True)
    # NEED to fill in 0 for numericals and none for categoricals
    return data
    

# Preprocess the data
def preprocess_data(data, target_column):
    X = data.drop(columns=[target_column])  # Features
    y = data[target_column]  # Target variable
    
    # Identify categorical and numerical columns
    categorical_cols = X.select_dtypes(include=['object']).columns
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
    
    return X, y, categorical_cols, numerical_cols

# Create the model pipeline
def create_pipeline(categorical_cols, numerical_cols):
    # Preprocessing for numerical data
    numerical_transformer = 'passthrough'  # No transformation for numerical data

    # Preprocessing for categorical data
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    # Combine preprocessors
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    # Create a pipeline that first transforms data and then fits a model
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    
    return model

# Train and evaluate the model
def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = create_pipeline(X.select_dtypes(include=['object']).columns, X.select_dtypes(include=['int64', 'float64']).columns)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

# Main execution
if __name__ == "__main__":
    file_path = 'Weather.csv'
    
    data = load_data(file_path)
    target_column = 'date'  
    
    X, y, categorical_cols, numerical_cols = preprocess_data(data, target_column)
    train_and_evaluate(X, y)
