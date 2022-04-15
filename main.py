import time
import numpy as np
import cv2

def main():

    #videocapture object
    cap = cv2.VideoCapture("Question 3\DS-IQ-003-PixelVariation-Video.mp4")


    #getting the current frame 
    ret, current_frame = cap.read()
    previous_frame = current_frame




    #reading the complete video and calc. the frame difference
    while(ret): 

        #convering the frames into numpy array
        curr_arr= np.array(current_frame)
        prev_arr = np.array(previous_frame)

        #calculating the absolute difference between current and previous frames to find the pixelVariation
        diff_frame = abs(np.subtract(curr_arr,prev_arr))
        diff_frame_gray = cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY)
        

        #dispaying the frames
        cv2.imshow("my_bw",diff_frame_gray)
        cv2.imshow("orig",current_frame)
        time.sleep(0.01)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        previous_frame = current_frame.copy()
        ret, current_frame = cap.read()

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
