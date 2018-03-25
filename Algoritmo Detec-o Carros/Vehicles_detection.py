# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2
# capture frames from a video
cap = cv2.VideoCapture('recorte.mp4')


# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')
trajeto1 = 0
trajeto2 = 0
listaValores1 = []
listaValores2 = []

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        if x > 1830 and y > 800:
            trajeto1 = trajeto1 + 1
            dado = [x,y]
            listaValores1.append(dado)
        if x < 270 and y < 560:
            trajeto2 = trajeto2 + 1
            dado = [x,y]
            listaValores2.append(dado)

        if w > 270 and h > 100:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    height , width , layers =  frames.shape
    new_h= int(height/3)
    new_w= int(width/3)
    frames = cv2.resize(frames, (new_w, new_h))
    cv2.imshow('video2', frames)

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
print("Trajeto 1:",trajeto1)
print("Trajeto 2:",trajeto2)
listaValores1.sort()
listaValores2.sort()
print(listaValores1)
print()
print(listaValores2)

# De-allocate any associated memory usage
cv2.destroyAllWindows()
