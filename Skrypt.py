import math
zmienna='t'
while zmienna!='n':
  figura= input('Podaj jedną figurę prostokąt[P] lub trójkąt[T], z której chcesz obliczyć obwód i pole \n')
  if figura=='P':
    wzór= input('Na podstawie jakich danych chcesz obliczyć pole i obwód prostokąta?: \n[A]Długosci boków a i b \n[B]Długosci jednego boku i przekątnej \n')
    if wzór=='A':
      a=float(input('Podaj długość boku a ').replace(",", "."))
      b=float(input('Podaj długość boku b ').replace(",", "."))
      if a>0 and b>0:  
        print('Obwód prostokąta wynosi: ',2*(a+b),'\nPole prostokąta wynosi: ',a*b)
      else:
        print('Boki muszą być większe od 0')
    elif wzór=='B':
      a=float(input('Podaj długość boku a ').replace(",", "."))
      d=float(input('Podaj długość przekątnej ').replace(",", "."))
      if d>a and a>0 and d>0:
        b=math.sqrt((d**2)-(a**2))
        print('Obwód prostokąta wynosi: ',2*(a+b),'\nPole prostokąta wynosi: ',a*b)
      else:
        print('Przekątna musi być dłuższa od boku.\nBok i przekątna muszą być większe od 0')
    else:
      print('Wybrano złą opcję')
  elif figura=='T':
    wzór= input('Na podstawie jakich danych chcesz obliczyć pole i obwód trójkąta?: \n[A]Długość wszystkich boków(policzy pole i obwód) \n[B]Podstawę i wysokosć(policzy tylko pole) \n[C]Długość sąsiednich boków i kąt pomiędzy nimi(policzy tylko pole) \n')
    if wzór=='A':
      a=float(input('Podaj długość boku a ').replace(",", "."))
      b=float(input('Podaj długość boku b ').replace(",", "."))
      c=float(input('Podaj długość boku c ').replace(",", "."))
      if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        p=(a+b+c)*0.5
        print('Obwód trójkąta wynosi: ',a+b+c,'\nPole trójkąta wynosi: ',math.sqrt(p*(p-a)*(p-b)*(p-c)))
      else:
        print('Nie można utworzyć trójkąta z podanych długości boków')
    elif wzór=='B':
      a=float(input('Podaj długość podstawy ').replace(",", "."))
      h=float(input('Podaj wysokość trójkąta ').replace(",", "."))
      if a>0 and h>0:
        print('Pole trójkąta wynosi: ',0.5*(a*h))
      else:
        print('Podstawa i wysokość muszą być większe od 0')
    elif wzór=='C':
      a=float(input('Podaj długość boku a ').replace(",", "."))
      b=float(input('Podaj długość boku b').replace(",", "."))
      kąt=float(input('Podaj kąt pomiędzy bokami w stopniach').replace(",", "."))
      if a>0 and b>0 and kąt<180 and kąt>0:
        print('Pole trójkąta wynosi: ',0.5*(a*b)*math.sin(math.radians(kąt)))
      elif kąt>=180:
        print('Kąt jest za duży')
      elif kąt<=0:
        print('Kąt jest za mały')
      else:  
        print('Długość boków musi być większa od 0')
    else:
      print('Wybrano złą opcję')
  else:
    print('Zły wybór')
  zmienna=input('Czy chcesz spróbować jeszcze raz? t/n: ')      
