# live-Mobile-Camera-Access-Using-Python
To Access Live Mobile Camera Using Python 
# Environment setup:

1.Install Anaconda:

 https://www.anaconda.com/download/
 
2.Creating an environment with commands

   * To create an environment:
   
           conda create --name myenv
     
     !Note:
     Replace myenv with the environment name.
   
   * When conda asks you to proceed, type y:
   
           proceed ([y]/n)?
           
     This creates the myenv environment in /envs/. No packages will be installed in this environment.

     
       
3. Activating an environment
  
  * To activate an environment:
       
           conda activate myenv
   
   !Note:
Replace myenv with the environment name or or directory path

4. Install IP Webcam
       
     Install IP Webcam in playstore:
       
     ![WhatsApp Image 2022-07-14 at 9 22 47 PM](https://user-images.githubusercontent.com/53464755/179024697-2e1c5e5d-b222-4d91-8b1e-5511eda4f164.jpeg)
     
     Open IP Webcam app and scroll down click on Start server.
     
     ![WhatsApp Image 2022-07-14 at 9 28 04 PM](https://user-images.githubusercontent.com/53464755/179025665-15e6cbfd-86fc-4601-8a09-83af324f06b2.jpeg)

     
5. Install Python packages

     * Numpy
     * OpenCV

   Install the required packages by executing the following command.

       pip install (package name)
    
       example:
  
           $ pip install numpy
           
    Make sure pip is linked to Python
    
    Using Python virtual environment is highly recommended.
    
 ## Usage:
    
   webcam
    
   $ Live_CCTV.py
    
    !Note:
          
         * Replace username with the your IPWebcam app http link .

          capture = cv2.VideoCapture("http://username/video")
              
                  eg:
                     cap = cv2.VideoCapture('http://10..66.16:8080')
          
     ![WhatsApp Image 2022-07-14 at 9 34 00 PM](https://user-images.githubusercontent.com/53464755/179026696-31a1a243-4ed8-4618-9c8d-31ff9652f424.jpeg)

     When you run the script for the first time, it will download the pre-trained model from this link and place it under pre-trained directory in the current path.
## output

![vlcsnap-2022-07-14-20h57m01s865](https://user-images.githubusercontent.com/53464755/179019463-6fb0cb1b-6d6d-477c-917a-4e9de0060033.png)

## Help

If you are facing any difficulty, feel free to create a new issue or reach out on [Linkedin](https://www.linkedin.com/in/karthik-v-926656211/)
