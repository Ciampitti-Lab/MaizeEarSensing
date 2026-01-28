import pyrealsense2 as rs
import numpy as np
import cv2
import argparse
import os.path

parser = argparse.ArgumentParser(description="Read recorded bag file and display depth stream in jet colormap.")
parser.add_argument("-i", "--input", type=str, help="Path to the bag file")
args = parser.parse_args()

if not args.input:
    print("No input paramater have been given.")
    print("For help type --help")
    exit()
if os.path.splitext(args.input)[1] != ".bag":
    print("The given file is not of correct file format.")
    print("Only .bag files are accepted")
    exit()
try:
    pipeline = rs.pipeline()
    config = rs.config()
    rs.config.enable_device_from_file(config, args.input)
    pipeline.start(config)

    aligned_stream = rs.align(rs.stream.color)
    cv2.namedWindow("Depth Stream", cv2.WINDOW_AUTOSIZE)
    
    colorizer = rs.colorizer()
    while True:
        frames = pipeline.wait_for_frames()
        frames = aligned_stream.process(frames)

        depth_frame = frames.get_depth_frame()
        depth_color_frame = colorizer.colorize(depth_frame)
        depth_color_image = np.asanyarray(depth_color_frame.get_data())

        color_frame = frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())

        # Render image in opencv window
        concatenated_images = np.concatenate((color_image, depth_color_image), axis=1)

        cv2.imshow("Data Stream", concatenated_images)
        key = cv2.waitKey(1)
        # if pressed escape exit program
        if key == 27:
            cv2.destroyAllWindows()
            break
finally:
    pass
