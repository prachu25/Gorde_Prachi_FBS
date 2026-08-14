dic = {'id':101,
        'name': 'Joe', 
        'dept': 'HR', 
        'Salary': 25000
}

#1. dic.clear()          it clear dic
#2. dic2 = dic.copy()
#3. print(dic.get('id'))                if exixts it will give the vale
#4. print(dic.get('eid','Not Found'))   we meationsuch key which not exists then we can print msg
#5. print(dic.items())                  (key: value)

#6. print(dic.keys())      print all keys
#7. res = dic.pop('dept')
#8. print(res)
#9. print(dic)

#10. dic.popitem()                            it remove the last pair
#11. dic.update({'age':24, 'city':'Pune'})    we can pass one or multiple value
#12. print(dic.values())                      print all values
#13. print(dic)