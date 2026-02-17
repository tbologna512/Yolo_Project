import argparse
from ultralytics import YOLO

def parse_source(src: str):
    """
    Accepts:
      - usb0 / usb1 / usb2 (webcams)
      - an integer camera index like 0, 1, 2
      - a file path (image/video)
    """
    s = src.strip().lower()
    if s.startswith("usb") and s[3:].isdigit():
        return int(s[3:])
    if s.isdigit():
        return int(s)
    return src  # treat as path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="models/my_model.pt",
                    help="Path to model weights (default: models/my_model.pt)")
    ap.add_argument("--source", default="usb0",
                    help="usb0/usb1/usb2, a camera index (0/1/2), or a file path")
    ap.add_argument("--imgsz", type=int, default=640,
                    help="Inference image size (default: 640)")
    args = ap.parse_args()

    source = parse_source(args.source)

    model = YOLO(args.model)

    # stream=True prevents results from accumulating in RAM on long webcam runs
    # verbose=False reduces per-frame logging in the terminal
    results = model.predict(source=source, imgsz=args.imgsz, show=True, stream=True, verbose=False)

    # IMPORTANT: consume the generator so the stream actually runs
    for _ in results:
        pass


if __name__ == "__main__":
    main()
