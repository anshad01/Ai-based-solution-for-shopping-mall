# import cv2
# from keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# from django.shortcuts import redirect
#
# def ipcam(request):
#     # define a video capture object
#     vid = cv2.VideoCapture('http://192.168.1.4:4747/video')
#     model = load_model('mask_detection_model.h5')
#
#     while (True):
#         ret, frame = vid.read()
#         test_image = cv2.resize(frame, (64, 64), interpolation=cv2.INTER_NEAREST)
#         test_image = image.img_to_array(test_image)
#         test_image = np.expand_dims(test_image, axis=0)
#         result = model.predict(x=test_image)
#         print(result)
#         if result[0][0] == 1:
#             prediction = 'with_mask'
#         else:
#             prediction = 'without_mask'
#
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         org = (50, 50)
#         fontScale = 1
#         color = (255, 0, 0)
#         thickness = 2
#         image1 = cv2.putText(frame, str(prediction), org, font,
#                              fontScale, color, thickness, cv2.LINE_AA)
#         cv2.imshow('frame', image1)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # After the loop release the cap object
#     vid.release()
#     # Destroy all the windows
#     cv2.destroyAllWindows()
#     return redirect('admin_home')
#
#
#
