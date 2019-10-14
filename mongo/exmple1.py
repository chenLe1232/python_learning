from mongo_db import client
#
# client.school.teachers.insert_one({"name":"乐臣"})
# client.school.teachers.insert_many([
#     {"name": "凡总"},
#     {"name": "乐乐"}


# 无条件查询集合里面所有的数据
teachers = client.school.teachers.find({"name":{"$gte":"乐臣"}})
for i in teachers:
    print( i)

print("----------------------------")
#
# teachers_one = client.school.teachers.find_one({"name":"乐臣"})
# print(teachers_one["_id"], teachers_one["name"])

# 修改数据
# try:
#     client.school.teachers.update_many(
#         {}, {"$set": {"role": ["班主任"]}}
#     )
#     client.school.teachers.update_one(
#         {"name":"乐臣"}, {"$set": {"sex": "女"}}
#     )
#     client.school.teachers.update_one(
#         {"name":"乐臣"}, {"$push": {"role": "年级主任"}}
#     )
#
# except Exception as e :
#     print(e)