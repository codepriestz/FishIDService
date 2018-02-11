import uuid
import base64
import uuid
from fr_utils import *
from inception_blocks_v2 import *
from Dao import idtoencoding,sourcenametoidaccess


class facialrecogition:
    def  __init__(self):
            self.idtoencoding=idtoencoding()
            self.idtoname=sourcenametoidaccess()
            pass
    def runalgorith(self,base6,lat,long):
            #save base64 file to a folder
            imgdata=base64.b64decode(base64)
            filename = lat+long+str(uuid.uuid4()) # I assume you have a way of picking unique filenames
            with open(filename, 'wb') as f:
                f.write(imgdata)
            #send the path and the location data to the algorithm function to  get the encoding vector
            a=algorithmfunction(filename,lat,long)
            list=[]
            #check the the list of encodings  and check the one closest
            for x in self.idtoencoding.findall('{}'):
                if a-x['encoding']<0.5:
                    list.append(x)


#fish_model = faceRecoModel(input_shape=(3, 96, 96))
#fish_model.compile(optimizer = 'adam', loss = triplet_loss, metrics = ['accuracy'])
#load_weights_from_FaceNet(fish_model)


def algorithmfunction(filepath,lat,long):
        img_to_encoding(image_path, fish_model)
def differencebtwencoding(a,b):
        return tf.reduce_sum(tf.square(tf.subtract(a,b)))


#
def img_to_encoding(image_path, model):
    img1 = cv2.imread(image_path, 1)
    img2 = cv2.resize(img1, (96, 96))
    img = img2[...,::-1]
    img = np.around(np.transpose(img, (2,0,1))/255.0, decimals=12)
    x_train = np.array([img])
    embedding = model.predict_on_batch(x_train)
    return embedding



def what_is_it(image_path, database, model):
    
    ### START CODE HERE ### 
    
    ## Step 1: Compute the target "encoding" for the image. Use img_to_encoding() see example above. ## (≈ 1 line)
    encoding = img_to_encoding(image_path, model)
    
    ## Step 2: Find the closest encoding ##
    
    # Initialize "min_dist" to a large value, say 100 (≈1 line)
    min_dist = 100
    
    # Loop over the database dictionary's names and encodings.
    for (name, db_enc) in database.items():
        
        # Compute L2 distance between the target "encoding" and the current "emb" from the database. (≈ 1 line)
        dist = np.sqrt(np.sum((encoding-db_enc)**2))

        # If this distance is less than the min_dist, then set min_dist to dist, and identity to name. (≈ 3 lines)
        if dist < min_dist:
            min_dist = dist
            identity = name

    ### END CODE HERE ###
    
    if min_dist > 0.7:
        print("Not in the database.")
    else:
        print ("it's " + str(identity) + ", the distance is " + str(min_dist))
        
    return min_dist, identity



