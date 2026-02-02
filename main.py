from omegaconf import DictConfig
from app.utils.config_utils import with_config, print_config
from app.utils.logging import setup_logging, get_logger
import asyncio  
from app.services.router_service import QueryRouter
from app.services.docling_service import parse_and_chunk_document

from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

@with_config
def main(cfg: DictConfig):
    
    print_config(cfg)
    setup_logging(log_level=cfg.logging.level)
    logger.info(f"App Name: {cfg.app.app_name}")
    
    # router = QueryRouter()
    # print(router.route("How many customers do we have?"))
    # print(router.explain_routing("How many customers do we have?"))
    # print(router.get_routing_confidence("How many customers do we have?"))

    chunks = parse_and_chunk_document("test_data/Understanding_Climate_Change.pdf")
    for chunk in chunks:
        print("\n")
        print(chunk)

@with_config
async def amain(cfg: DictConfig):
    print_config(cfg)

    setup_logging(log_level=cfg.logging.level)


if __name__ == "__main__":
    main()
    # asyncio.run(amain())
