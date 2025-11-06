# class MyData:
#     def __init__(self,data:list) ->None:
#         self.data:list = data
#         self.index = 0
        
#     def __iter__(self):
#         return self
    
#     def __next__(self)->int:
#         value = self.data[self.index]
#         self.index +=1
#         return value
#         return 1    
        
# data = MyData([1,2,3,4,5])

# # for x in range() # range -> __iter__()를 호출
# for x in data:
#     print(x)





# # class Student:
    
# #     name:str
# #     id:str
# #     age:int
# #     count:ClassVar[int] = 0
    
# #     def __init__(self,name:str,id:str,age:int) ->None:
# #         self.name = name
# #         self.id = id
# #         self.age = age
        
# # obj = Student()

# #dataset
# #feature, label
class MyDataset:
    def __init__(self, feature:list, label:list) -> None:
        self.feature:list = feature
        self.label:list = label
        
    def __iter__(self):
        for x,y in zip(self.feature, self.label):
            yield x,y 
            
    def __str__(self):
        return f"Dataset:\nfeature:{self.feature}\
            \n label:{self.label}"
    
    def __repr__(self):
        return "For log, debug and Doc"    
    
    def __getitem__(self,index:int) -> tuple:
         return self.feature[index], self.label[index] 
     
    def __setitem__(self,index:int, value:tuple[list,list]) ->None:
         self.feature[index] = value[0]
         self.label[index] = value[1] 
         

dataset = MyDataset([1,2,3],[10,20,30])

for  x,y in dataset:
    print({x},{y})

    

    





# # print(dataset.feature)
# # print(dataset.label)


# # dataset[2] = ([5], [50])
# # print(dataset[2])


# def bar():...
# def test():
#     yield 1
#     print("a")
#     yield 2
#     print("b")
#     yield 3
#     print("c")
# obj = test()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

# def my_range(num:int):
#     count:int = 0
#     while(count < num):
#         yield count
#         count +=1
    
# for x in my_range(5):
#     print(x)
