#6230
a = [88,30,61,55,95]

for i in range (0, 5):
  if a[i] < 60:
    print('%d번 학생은' % (i+1), '%d점으로 불합격입니다.' % a[i])
  else:
    print('%d번 학생은' % (i+1), '%d점으로 합격입니다.' % a[i])

 --------------------------------------------------------------
#6231
for i in range(1,101):
    print(i)
 --------------------------------------------------------------

#6234
for i in range(1,101):
    if i %2 == 0 :
        print(i, end =' ')
        
----------------------------------------------------------------
#6238
for i in range(1,101):
  if i%2 ==1:
    print(i, end=", " if i!=99 else "" ) #이 구문 외워두자.. 끝에 , 삭제해주는 거..
    
    
----------------------------------------------------------------

#6240
sum = 0
for i in range(1,101):
    if i%3 == 0:
        sum += i
        
print("1부터 100사이의 숫자 중 3의 배수의 총합: %d" %sum)

----------------------------------------------------------------

#6242
student = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
blood = {'A': 0, 'O':0,'B':0, 'AB':0}
for i in range (10):
  if student[i] == 'A':
    blood['A']+=1
  elif student[i] == 'B':
    blood['B']+=1
  elif student[i] == 'O':
    blood['O']+=1
  else:
    blood['AB']+=1
    
print(blood)


---------------------------------------------------------------

#6244

student = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sums = 0
i = 0
a= 0
while i<10 and i<len(student):
  if student[i] >= 80:
    a += student.pop(i)
    
  else:
    i+=1
print(a)

---------------------------------------------------------------
#6246 

i=0
while i<5:
  print('*'*(5-i))
  i+=1
  
  
--------------------------------------------------------------

#6247

i, j = 0, 7

while i<4 :
  print(' '*i+'*'*j)
  i+=1
  j-=2
  
----------------------------------------------------------

#6251

i,j = 4,1
for k in range (5):
  print(' '*i+'*'*j)
 
  i-=1
  j+=1
