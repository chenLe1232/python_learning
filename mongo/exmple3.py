from mongo_db import client
from gridfs import GridFS
import math
import datetime
from bson.objectid import ObjectId

db = client.school
gfs = GridFS(db, collection="book")
book = gfs.find_one({"filename":"江西阿里云大数据学员手册.pdf"})
print(book.filename)
print("%dM" % math.ceil(book.length/1024/1024))
print(book)

books = gfs.find({"type":"PDF"})
for one in books:
    uploadDate = one.uploadDate + datetime.timedelta(hours=8)
    uploadDate = uploadDate.strftime("%Y-%m-%d %H:%M:%S")
    print(one._id, one.filename, uploadDate)

rs = gfs.exists(ObjectId("5d921d64e3d62be4973c4a26"))
print(rs)
rs = gfs.exists(**{"type": "PDF"})
print(rs)

document = gfs.get(ObjectId("5d921d64e3d62be4973c4a26"))
file = open("/Users/carline/Documents/面试相关/大数据学员手册.pdf", "wb")
file.write(document.read())
file.close()

gfs.delete(ObjectId("5d921d64e3d62be4973c4a26"))
print("文件已经删除了")