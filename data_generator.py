import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata

# Step 1: Load the real dataset
real_df = pd.read_csv("Syndemics_Nov2023.csv")   

# Step 2: Define metadata for the dataset
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(real_df)
print(f" Step 2 completed !!!")

# Step 3: Train the SDV GaussianCopulaSynthesizer model
synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(real_df)
print(f" Step 3 completed !!!")

# Step 4: Generate synthetic data
synthetic_df = synthesizer.sample(num_rows=len(real_df))
print(f" Step 4 completed !!!")

# Step 5: Save the synthetic dataset
synthetic_df.to_csv("Syndemics_dummy_data.csv", index=False)
print(f" Step 5 completed !!!")

print("✅ Synthetic dataset generated successfully and saved as 'synthetic_data.csv'!")
