import pickle
import base64
class Decoder():
    def decode(data):
        #data_str = data.decode('utf-8')
        print("=====Decoder===")
        try:
            df = pickle.loads(base64.b64decode(data.encode()))
        except Exception as ex:
            print("Exception in decoder ====>",ex)

        #print(df)
        return df

class Encoder():
    def encode(df):
        pickled = pickle.dumps(df)
        pickled_b64 = base64.b64encode(pickled)
        return pickled_b64.decode("utf-8")