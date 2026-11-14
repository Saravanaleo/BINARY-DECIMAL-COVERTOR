bin_num=int(input("Enter Binary Number :"))
dec_num,i=0,0

while bin_num>0:
    rem=bin_num%10
    quot=rem*(2**i)
    dec_num=dec_num+quot
    bin_num=bin_num//10
    i=i+1
print("Your Binary Number is",dec_num )

# alternate method
bin_num=input("Enter Binary Number :")
dec_num=int(bin_num,2)
print("Your Dec Number is",dec_num)