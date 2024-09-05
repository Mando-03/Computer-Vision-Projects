import pickle,os,cv2
import face_recognition  
import firebase_admin
from firebase_admin import credentials,storage 


cred = credentials.Certificate("serviceAccountKey.json")  # get it from firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': "get your own buddy",
    'storageBucket': "get your own buddy"})


folderPath = 'Images'
PathList = os.listdir(folderPath)

imgList = []
studentsIDs = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentsIDs.append(os.path.splitext(path)[0])
    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)  


def findEncoding(imageslist):
    encodeList = []
    for img in imageslist:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print('encoding started .....')
encodeListKnown = findEncoding(imgList)
print('encoding completed')
encodeListKnownwithIDs = [encodeListKnown ,studentsIDs ]
file = open('EncodeFile', 'wb')
pickle.dump(encodeListKnownwithIDs, file)
file.close()
print('file saved')