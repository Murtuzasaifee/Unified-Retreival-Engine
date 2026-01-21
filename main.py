from omegaconf import DictConfig
from app.utils.config_utils import with_config, print_config
from app.utils.logging import setup_logging, get_logger
import asyncio  

from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

@with_config
def main(cfg: DictConfig):
    
    print_config(cfg)
    setup_logging(log_level=cfg.logging.level)
    logger.info(f"App Name: {cfg.app.app_name}")
    

@with_config
async def amain(cfg: DictConfig):
    print_config(cfg)

    setup_logging(log_level=cfg.logging.level)


if __name__ == "__main__":
    main()
    # asyncio.run(amain())
