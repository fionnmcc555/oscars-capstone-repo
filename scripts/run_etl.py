import os
import sys
from config.env_config import setup_env
from src.extract.extract import extract_data
from src.transform.transform import transform_data
from src.load.load import load_data

def main():
    try:
        # set up env from CLI args
        setup_env(sys.argv)
        env = os.getenv("ENV", "unknown")
        print(f"ETL pipeline run successfully in {env} environment!")

        # allow tests to redirect I/O
        raw_dir = os.getenv("RAW_DIR", "data/raw")
        out_dir = os.getenv("OUTPUT_DIR", "data/processed")
        skip_load = os.getenv("SKIP_LOAD", "").lower() in {"1", "true", "yes"}

        # extract
        extracted_data = extract_data()

        # save extracted data
        os.makedirs(raw_dir, exist_ok=True)
        extracted_output_path = os.path.join(raw_dir, "unclean_oscars.csv")
        extracted_data.to_csv(extracted_output_path, index=False)
        print(f"Extracted data saved to {extracted_output_path}")

        # transform
        transformed_data = transform_data(extracted_data)

        # save transformed data
        os.makedirs(out_dir, exist_ok=True)
        transformed_output_path = os.path.join(out_dir, "clean_oscars.csv")
        transformed_data.to_csv(transformed_output_path, index=False)
        print(f"Transformed data saved to {transformed_output_path}")

        # load (optional in tests)
        if not skip_load:
            load_data(transformed_data)
        else:
            print("SKIP_LOAD set — skipping load step")

        print(f"ETL pipeline completed successfully in {env}")

    except Exception as e:
        raise Exception(f"ETL pipeline failed: {e}")

if __name__ == "__main__":
    main()
