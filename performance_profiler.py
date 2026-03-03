"""
Performance Profiler — Scalability & Resource Tracking
=======================================================
Tracks: training time, memory usage, CPU utilisation per task.
Exports results for Tableau Dashboard 4 (Scalability & Cost Analysis).

Usage:
    from performance_profiler import PipelineProfiler
    
    profiler = PipelineProfiler()
    record = profiler.start_timer("data_ingestion")
    # ... do work ...
    profiler.stop_timer(record)
    profiler.save_results()
"""

import time
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, Callable

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False
    print("Warning: psutil not installed. Memory tracking disabled.")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


class PipelineProfiler:
    """
    Tracks execution time and memory usage for pipeline tasks.
    Results exported for Tableau Dashboard 4.
    """
    
    def __init__(self, output_dir: str = "../results/metrics"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.records = []
        self.start_timestamp = datetime.now().isoformat()
    
    def start_timer(self, task_name: str) -> Dict[str, Any]:
        """Start timing a task. Returns record dict to pass to stop_timer."""
        record = {
            "task": task_name,
            "start_time": time.time(),
            "timestamp": datetime.now().isoformat()
        }
        if HAS_PSUTIL:
            process = psutil.Process()
            record["start_memory_mb"] = process.memory_info().rss / 1e6
            record["start_cpu_percent"] = process.cpu_percent()
        logger.info(f"Started: {task_name}")
        return record
    
    def stop_timer(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Stop timing and record metrics."""
        record["end_time"] = time.time()
        record["duration_seconds"] = round(record["end_time"] - record["start_time"], 3)
        
        if HAS_PSUTIL:
            process = psutil.Process()
            record["end_memory_mb"] = round(process.memory_info().rss / 1e6, 1)
            record["memory_delta_mb"] = round(
                record["end_memory_mb"] - record["start_memory_mb"], 1
            )
            record["end_cpu_percent"] = process.cpu_percent()
        
        self.records.append(record)
        logger.info(f"Completed: {record['task']} in {record['duration_seconds']}s")
        return record
    
    def track(self, task_name: str, func: Callable, *args, **kwargs) -> Any:
        """Convenience method to track a function call."""
        record = self.start_timer(task_name)
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            self.stop_timer(record)
    
    def save_results(self, filename: str = "profiling_results.json") -> Path:
        """Save all profiling records to JSON."""
        output = {
            "pipeline_start": self.start_timestamp,
            "pipeline_end": datetime.now().isoformat(),
            "total_tasks": len(self.records),
            "total_duration_seconds": sum(r.get("duration_seconds", 0) for r in self.records),
            "records": self.records
        }
        path = self.output_dir / filename
        with open(path, "w") as f:
            json.dump(output, f, indent=2, default=str)
        logger.info(f"Profiling results saved to {path}")
        return path
    
    def save_csv(self, filename: str = "profiling_results.csv") -> Path:
        """Save profiling records as CSV for Tableau."""
        import csv
        path = self.output_dir / filename
        if not self.records:
            logger.warning("No records to save")
            return path
        
        fieldnames = ["task", "duration_seconds", "timestamp"]
        if HAS_PSUTIL:
            fieldnames.extend(["start_memory_mb", "end_memory_mb", "memory_delta_mb"])
        
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(self.records)
        
        logger.info(f"Profiling CSV saved to {path}")
        return path
    
    def get_summary(self) -> Dict[str, Any]:
        """Get summary statistics of profiling."""
        if not self.records:
            return {"message": "No records yet"}
        
        durations = [r["duration_seconds"] for r in self.records]
        return {
            "total_tasks": len(self.records),
            "total_duration_seconds": round(sum(durations), 2),
            "avg_duration_seconds": round(sum(durations) / len(durations), 2),
            "max_duration_seconds": round(max(durations), 2),
            "min_duration_seconds": round(min(durations), 2),
            "tasks": {r["task"]: r["duration_seconds"] for r in self.records}
        }
    
    def print_summary(self) -> None:
        """Print formatted summary to console."""
        summary = self.get_summary()
        print("\n" + "=" * 50)
        print(" PROFILING SUMMARY")
        print("=" * 50)
        print(f" Total tasks:    {summary.get('total_tasks', 0)}")
        print(f" Total time:     {summary.get('total_duration_seconds', 0)}s")
        print(f" Average time:   {summary.get('avg_duration_seconds', 0)}s")
        print("-" * 50)
        for task, duration in summary.get("tasks", {}).items():
            print(f"  {task}: {duration}s")
        print("=" * 50 + "\n")


# Example usage
if __name__ == "__main__":
    profiler = PipelineProfiler()
    
    # Example: Track a simple task
    record = profiler.start_timer("example_data_loading")
    time.sleep(0.5)  # Simulate work
    profiler.stop_timer(record)
    
    record = profiler.start_timer("example_model_training")
    time.sleep(0.3)  # Simulate work
    profiler.stop_timer(record)
