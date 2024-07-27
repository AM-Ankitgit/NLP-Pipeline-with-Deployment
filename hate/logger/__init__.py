
import os
import logging
from datetime import datetime


folder_name = 'LOG'
os.makedirs(folder_name,exist_ok=True)

log_file_name = f'{datetime.now().strftime("%Y-%m-%d-%H-%S-%S")}.log'

log_file_path = os.path.join(folder_name,log_file_name)


logging.basicConfig(filename=log_file_path,
                    format="[%(asctime)s] %(name)s %(lineno)d  %(levelname)s  %(message)s",
                    level=logging.INFO,
                    )
