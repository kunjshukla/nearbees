from ultralytics import YOLO
import cv2 as cv
import os

# Check if the image file exists
image_path = "sunflower1.jpg"
if not os.path.exists(image_path):
    print(f"Image '{image_path}' not found.")
else:
    # Load the image and model
    image = cv.imread(image_path)
    model = YOLO("best.pt")

    # Define class names (adjust according to your YOLO model's trained classes)
    class_names = ["Rose", "SunFlower"]  # Example class names

    # Perform object detection
    results = model(image)

    # Annotate image with bounding boxes and class names
    for box, cls_idx in zip(results[0].boxes.xyxy, results[0].boxes.cls):
        x1, y1, x2, y2 = box[:4].tolist()
        class_name = class_names[int(cls_idx)]  # Get the class name from the index
        cv.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  # Draw the bounding box

        # Put the class label above the bounding box
        cv.putText(
            image,
            class_name,
            (int(x1), int(y1) - 10),  # Position the label above the bounding box
            cv.FONT_HERSHEY_SIMPLEX,
            0.5,  # Font scale
            (255, 255, 0),  # Font color
            2,  # Font thickness
        )

    # Show the annotated image and keep the window open until a key is pressed
    cv.imshow("Annotated Image with Labels", image)
    cv.waitKey(0)  # Keep the window open until a key is pressed
    cv.destroyAllWindows()  # Close the window
