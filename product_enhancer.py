import pandas as pd
import numpy as np

# Parameters
num_rows = 100
category_1 = 'Category1'
category_2 = 'Category2'
category_1_percentage = 0.8
category_2_percentage = 0.2

# Calculate the number of rows per category
num_category_1 = int(num_rows * category_1_percentage)
num_category_2 = num_rows - num_category_1

# Create product IDs
product_ids = np.arange(1, num_rows + 1)

# Create descriptions
descriptions = [f'Product {i}' for i in product_ids]

# Create random amounts
amounts = np.random.randint(100, 1000, size=num_rows)

# Create categories
categories = [category_1] * num_category_1 + [category_2] * num_category_2
np.random.shuffle(categories)  # Shuffle to mix categories

# Create max quantities
max_quantities = np.random.randint(1, 100, size=num_rows)

# Create DataFrame
data = {
    'productId': product_ids,
    'description': descriptions,
    'amt': amounts,
    'category': categories,
    'max_qty': max_quantities
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
