# Artificial Neural Network
# Ni Luh Made Dita Anjani
# 1301174676
# IFIK-41-01

x1 = [10, 25, 15, 16, 10, 25, 15, 16, 10, 25, 15, 16]
x2 = [25, 28, 20, 20, 25, 28, 20, 20, 25, 28, 20, 20]
r = [100, 250, 150, 120, 100, 250, 150, 120, 100, 250, 150, 120]
wnol = [1]
wsatu = [1]
wdua = [1]
lr = 0.0001
array_error =[]
j = 1

for i in range(len(x1)):
  temp = []
  y = (wnol[i]+(wsatu[i]*x1[i])+(wdua[i]*x2[i]))
  wo = wnol[i]+lr*(r[i] - y)*1
  ws = wsatu[i]+(lr*(r[i] - y)*x1[i])
  wd = wdua[i]+(lr*(r[i] - y)*x2[i])
  wnol.append(wo)
  wsatu.append(ws)
  wdua.append(wd)
  temp.append(wo)
  temp.append(ws)
  temp.append(wd)
  # print("ini temp : ",temp)
  re = r[i]
  ye = (wnol[i+1]+(wsatu[i+1]*x1[i])+(wdua[i+1]*x2[i]))
  error = 0.5*((re*re)-(2*re*ye)+(ye*ye))
  array_error.append(error)
  i+=1

  print('iterasi ke-', i)
  print("W0 : ",wnol)
  print("W1 : ",wsatu)
  print("W2 : ",wdua)
  print("error : ", array_error)
  print('\n')

  if (i == 4):
    epoch = array_error[0]+array_error[1]+array_error[2]+array_error[3]
    print("================================")
    print('epoch ke-1', epoch)
    print("================================")
  if(i==8):
    epoch = array_error[4]+array_error[5]+array_error[6]+array_error[7]
    print("================================")
    print('epoch ke-2', epoch)
    print("================================")
  if(i==12):
    epoch = array_error[8]+array_error[9]+array_error[10]+array_error[11]
    print("================================")
    print('epoch ke-3', epoch)
    print("================================")
  print("\n")
