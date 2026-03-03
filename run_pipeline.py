"""
German Weather Big Data ML Pipeline — Main Runner
===================================================
Orchestrates: Ingestion -> Feature Engineering -> Training -> Evaluation

Usage:
    python run_pipeline.py --steps all
    python run_pipeline.py --steps ingest features train evaluate
    
Note: Full implementation is in the Google Colab notebook.
      This script provides a local entry point and documentation.
"""

import argparse
import time
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


def run_step(name: str, description: str) -> None:
    logger.info("=" * 60)
    logger.info(f"STEP: {name}")
    logger.info(f"  {description}")
    logger.info("  -> See Google Colab notebook for full implementation")
    logger.info("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="German Weather Big Data ML Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python run_pipeline.py --steps all
    python run_pipeline.py --steps ingest features
    python run_pipeline.py --steps train evaluate
        """
    )
    parser.add_argument(
        "--steps",
        nargs="+",
        default=["all"],
        choices=["all", "ingest", "features", "train", "evaluate"],
        help="Pipeline steps to run (default: all)"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="../config/spark_config.yaml",
        help="Path to Spark configuration file"
    )
    args = parser.parse_args()

    start_time = time.time()
    
    steps = args.steps
    if "all" in steps:
        steps = ["ingest", "features", "train", "evaluate"]

    step_descriptions = {
        "ingest": "Download DWD data from opendata.dwd.de, validate schema, convert to Parquet",
        "features": "Clean data, handle missing values, engineer features, build Spark ML vectors",
        "train": "Train LR, RF, GBT (PySpark MLlib) + SVM (scikit-learn) with cross-validation",
        "evaluate": "Calculate metrics, bootstrap CIs, stability analysis, export for Tableau"
    }

    logger.info("")
    logger.info("=" * 60)
    logger.info(" GERMAN WEATHER BIG DATA ML PIPELINE")
    logger.info("=" * 60)
    logger.info(f" Config: {args.config}")
    logger.info(f" Steps: {', '.join(steps)}")
    logger.info("=" * 60)
    logger.info("")

    for step in steps:
        run_step(step.upper(), step_descriptions[step])
        time.sleep(0.5)

    elapsed = time.time() - start_time
    logger.info("")
    logger.info(f"Pipeline documentation complete in {elapsed:.1f}s")
    logger.info("Run the Google Colab notebook for full execution.")
    logger.info("")


if __name__ == "__main__":
    main()
