# 🚗 Car Parking Space Detection System

A **Computer Vision-based** parking space detection system developed using **Python** and **OpenCV**. This project is designed to **monitor and detect vacant and occupied parking spots** in real-time, providing an efficient solution for parking management systems.

## 📌 Features

- Real-time detection of empty and occupied parking spaces
- Customizable parking spot selection
- Visual display with color-coded indicators (Green = Available, Red = Occupied)
- Accurate space availability count
- Works with videos, live streams, or static images

## 🖥️ Technologies Used

- Python
- OpenCV
- Numpy
- cvzone
- Pickle (for saving parking spot positions)

## ⚙️ How It Works

1. **Predefine Parking Spaces**  
   Select and save parking space positions using the **position marking tool** (`ParkingPos`).

2. **Video Processing**  
   - Convert frames to grayscale  
   - Apply Gaussian blur and adaptive thresholding  
   - Use morphological transformations for better detection

3. **Space Analysis**  
   - Count white pixels in each parking region  
   - If below a certain threshold → **Available**  
   - Otherwise → **Occupied**

4. **Visualization**  
   - Green rectangle for empty spaces  
   - Red rectangle for occupied spaces  
   - Free count displayed on screen

## 📂 Project Structure


## ▶️ How to Run

1. Clone the repository or download the files.
2. Run `ParkingPosEditor.py` to select parking spots and save positions.
3. Run `parkingDetection.py` to start the detection system.

## 📌 Future Enhancements

- Live camera feed integration
- Dynamic threshold adjustment
- Cloud-based data logging for parking analytics

## 📧 Contact

For suggestions or collaboration:  
[Your Name] — [Your Email or LinkedIn URL]

## 📃 License

This project is open-source and free to use for educational purposes.
