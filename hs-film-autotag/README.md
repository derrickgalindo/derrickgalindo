# HS film auto-tagging: go / no-go research

Evidence behind the decision doc "Auto-Tagging HS Football Film: Go / No-Go"
(https://claude.ai/artifact/VMj4Qncw7Kt1tFqxo93Mr9).

| Path | What it is |
| --- | --- |
| `bench/bench_pipeline.py` | CPU benchmark: decode, snap signal, field lines, 7 detector configs |
| `sim/adoption_sim.py` | Monte Carlo adoption model for 1,104 Texas UIL 11-man programs |
| `model/build_workbook.py` | Builds `model/unit_economics.xlsx` (formulas) from the results below |
| `results/benchmark_results.json` | Measured timings, person counts, manual frame review |
| `results/adoption_grid.csv`, `results/adoption_trajectory.json` | Simulation outputs (seed 20261023) |

## Reproduce

Requires `ffmpeg`, Python 3.11+, `numpy`, `opencv-python-headless`, `onnxruntime`, `openpyxl`.

```bash
# Footage: CC BY-NC-SA 4.0, Watertown HS vs Wakefield, Oct 2 2014 (evaluation use only)
ffmpeg -ss 1500 -i "https://archive.org/download/whs-football-vs-wakefield-october-2-2014/WHS%20Football%20vs%20Wakefield%20October%202%2C%202014.mp4" \
  -t 600 -c copy watertown_1080p_seg.mp4

# Models (ONNX): RF-DETR (Apache-2.0) from huggingface.co/onnx-community/rfdetr_{nano,medium}-ONNX,
# YOLO11 (AGPL-3.0) from huggingface.co/EdgeFirst/yolo11-det. Layout expected in MODELS_DIR:
#   rfdetr_nano-ONNX/model.onnx, rfdetr_medium-ONNX/model.onnx, yolo11{n,s,m}-det-fp32.onnx

python -I bench/bench_pipeline.py watertown_1080p_seg.mp4 MODELS_DIR OUT_DIR
python -I bench/bench_pipeline.py watertown_1080p_seg.mp4 MODELS_DIR OUT_DIR2 --skip-decode \
  --snap-times 139,177,289,369,421,599,11,459 --extra-frames 32
python -I sim/adoption_sim.py SIM_OUT
python -I model/build_workbook.py .   # then recalculate in Excel or LibreOffice
```

The snap times above are hand-labelled pre-snap moments in the 10-minute segment.
No GPU was available, so GPU figures in the doc come from vendor-published latency.
