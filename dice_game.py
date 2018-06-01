import dice

num = int(input('4,6,8,12,20のどれで勝負しますか?:'))
my_dice = dice.Dice(num)
computer_dice = dice.Dice(num)

my_pip = my_dice.shoot()
cpu_pip = computer_dice.shoot()

print('CPU:'+str(cpu_pip)+'あなた:'+str(my_pip))

if my_pip > cpu_pip:
    print('おめでとうございます。あなたの勝ちです。')
elif my_pip < cpu_pip:
    print('残念！あなたの負けです。')
else:
    print('引き分けです。')
