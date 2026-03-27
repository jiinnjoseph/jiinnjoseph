import pandas as pd

# a={
#     'data':[1,2,3,4,],
#     'value':['one','two','three','four']
# }

# b=pd.DataFrame(a)
# print(b.to_string(index=False))

# a={
#     'Title':['Name','age','course'],
#      'Data':['Jithin','23','Python'],
# }

# b=pd.DataFrame(a)
# print(b.to_string(index=False))


# a=[(1,'Jithin',30),
#    (2,'Joseph',40)
   
#    ]

# b=pd.DataFrame(a,columns=['Roll no.','Name','Mark'])
# print(b.to_string(index=False))


# add files to csv
# b.to_csv('dataframe.csv',index=False)


# read csv file
b=pd.read_csv('Ev.csv')
print(b)




