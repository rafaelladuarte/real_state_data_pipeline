from scr.etl.treatment.images import treatment_images
from scr.etl.treatment.migrate import raw_data_to_postgres


treatment_images()

raw_data_to_postgres()
