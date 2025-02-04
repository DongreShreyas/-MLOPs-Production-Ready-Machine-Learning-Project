import logging
import os


from from_root import from_root
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

Log_Dir="Logs"

Logs_Path=os.path.join(from_root(),Log_Dir, LOG_FILE)

os.makedirs(Log_Dir,exist_ok=True)


logging.basicConfig(
    filename=Logs_Path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)   