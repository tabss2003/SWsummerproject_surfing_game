import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("C:/Users/tabss/Downloads/summerproject-game-firebase-adminsdk-o40x0-e3aea148b1.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#문서 자체 읽어오기
rank_ref = db.collection('랭킹').document('기록')
rank_read = db.collection('랭킹').stream()
def Score_storage(distance):
    
    rank_ref = db.collection('랭킹').document('기록')
    rank_read = db.collection('랭킹').stream()

    for doc in rank_read:
        print(f'{doc.id} =>{doc.to_dict()}')
    
    k=rank_ref.get()
    print('K:',k)
    print('d:',k.to_dict())
    a=dict(k.to_dict())
    print(a)
    b=a.values()
    print(b)

    for key,value in a.items():
        print(key,"?",value)
Score_storage(1)
