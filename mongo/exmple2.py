from mongo_db import client
from gridfs import GridFS

db = client.school
gfs = GridFS(db, collection="book")

file = open("/Users/carline/Downloads/江西阿里云大数据学院学员手册.pdf",
            "rb"
            )
args = {"type": "PDF", "keyword": "学员手册"}
gfs.put(file, filename="江西阿里云大数据学员手册.pdf", **args)
file.close()
