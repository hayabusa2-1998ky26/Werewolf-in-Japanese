import random
import time
import math
import sys
def situmon():
    global play_member, zinrou_member
    yorosiidesuka = "n"
    while True:
        print("何人でプレイしますか?(4~10)")
        while type(play_member) == int:
            try:
                play_member = int(input())
            except:
                print("整数で答えてください")
            else:
                if int(play_member) > 3 and int(play_member) < 11:
                    break
                else:
                    print("4~10で答えてください。")
        print(str(play_member) + "人でよろしいですか?(y/n)")
        yorosiidesuka = input()
        if yorosiidesuka == "y":
            break
        elif yorosiidesuka == "n":
            nandemonai = 1
    yorosiidesuka = "n"
    while True:
        if play_member > 6:
            print("人狼は何人入れますか?(1~2)")
        else:
            print("人狼は何人入れますか?(1~1)")
        while type(zinrou_member) == int:
            try:
                zinrou_member = int(input())
            except:
                print("整数で答えてください")
            else:
                if play_member > 6:
                    if int(zinrou_member) > 0 and int(zinrou_member) < 3:
                        break
                    else:
                        print("1~2で答えてください。")
                else:
                    if int(zinrou_member) > 0 and int(zinrou_member) < 2:
                        break
                    else:
                        print("1で答えてください。")
        print(str(zinrou_member) + "人でよろしいですか?(y/n)")
        yorosiidesuka = input()
        if yorosiidesuka == "y":
            break
        elif yorosiidesuka == "n":
            nandemonai = 1
def member_situmon():
    global play_member, zinrou_member, players, i, players_safe
    yorosiidesuka = "n"
    while True:
        print("プレイヤー" + str(i + 1) + "、名前は何にしますか?")
        player_name = input()
        print(player_name + "でよろしいですか?(y/n)")
        yorosiidesuka = input()
        if yorosiidesuka == "y":
            break
        elif yorosiidesuka == "n":
            nandemonai = 1
    players.append(player_name)
    players_safe.append(1)
    players_safe_toriaezu.append(1)
def yakusyoku_gime():
    global players, i, play_member, zinrou_member, zinrou1, zinrou2, players_safe, uranaisi
    zinrou1 = random.randint(0, play_member - 1)
    zinrou2 = random.randint(0, play_member - 1)
    while zinrou2 == zinrou1:
        zinrou2 = random.randint(0, play_member - 1)
    if zinrou_member == 1:
        zinrou2 = -1
    uranaisi = random.randint(0, play_member - 1)
    while zinrou1 == uranaisi or zinrou2 == uranaisi:
        uranaisi = random.randint(0, play_member - 1)
def yakusyoku_haihu():
    global play_member, zinrou1, zinrou2, players_safe, uranaisi
    for i in range(play_member):
        print(str(players[i]) + "、こちらへ来て、他の人は見えないところへ離れてください。")
        while True:
            print("他の人は離れましたか?(y/n)")
            yorosiidesuka = input()
            if yorosiidesuka == "y":
                break
        print("今回のあなたの役職は...")
        if i == zinrou1 or i == zinrou2:
            print("「人狼」")
            print("です。")
            if zinrou2 == -1:
                print("仲間はいません。")
            else:
                if i == zinrou1:
                    print("仲間は" + players[zinrou2] + "です。")
                elif i == zinrou2:
                    print("仲間は" + players[zinrou1] + "です。")
        elif i == uranaisi:
            print("「占師」")
            print("です。")
            print("今回占える回数は1回です。")
            print("慎重に使いましょう。")
        else:
            print("「村人」")
            print("です。")
        while True:
            print("次の人に回してください。(y/n)")
            yorosiidesuka = input()
            if yorosiidesuka == "y":
                break
        for j in range(1100):
            print("")
def night():
    global players, i, play_member, zinrou_member, zinrou1, zinrou2, players_safe, killed, killed_people, players_safe_toriaezu, uranaisi, uranai
    killed = []
    print("夜になりました。")
    for j in range(play_member):
        print(str(players[j]) + "、こちらへ来て、他の人は見えないところへ離れてください。")
        while True:
            print("他の人は離れましたか?(y/n)")
            yorosiidesuka = input()
            if yorosiidesuka == "y":
                break
        if players_safe[j] == 0:
            print("あなたは既に死んでいます。")
            print("役職のターンの時間の長さを減らすために、何秒か待ってもらいます。")
            print("だいたい5秒がたつまでお待ちください・・・。")
            t1 = time.time()
            matutime = random.randint(5, 7)
            while True:
                if time.time() - t1 > matutime:
                    break
            print("お待たせしました。")
        else:
            if j == zinrou1 or j == zinrou2:
                print("あなたは人狼です。誰を殺しますか? 番号で決めてください。")
                print(0, "誰も殺さない。")
                for k in range(play_member):
                    print(k + 1, players[k])
                kill = "n"
                while True:
                    while True:
                        try:
                            kill = int(input())
                        except:
                            print("整数で答えてください")
                        else:
                            if j == kill - 1:
                                print("それは自分です。自分は殺せません。")
                            elif players_safe_toriaezu[kill - 1] == 0:
                                print("その人はすでに死んでいます。殺せません。")
                            elif j == zinrou1 and kill - 1 == zinrou2:
                                print("その人は仲間です。本当に殺しますか?") 
                                break
                            elif j == zinrou2 and kill - 1 == zinrou1:
                                print("その人は仲間です。本当に殺しますか?") 
                                break
                            elif int(kill) > -1 and int(kill) < play_member + 1:
                                break
                            else:
                                print("範囲内で答えてください。")
                    if kill == 0:
                        print("誰も殺さらない" + "でよろしいですか?(y/n)")
                    else:
                        print(players[int(kill - 1)] + "でよろしいですか?(y/n)")
                    yorosiidesuka = input()
                    if yorosiidesuka == "y":
                        break
                    elif yorosiidesuka == "n":
                        nandemonai = 1
                        print("誰を殺しますか? 番号で決めてください。")
                if kill == 0:
                    print("誰も殺しませんでした。")
                else:
                    print(str(players[kill - 1]) + "を殺しました。")
                    killed_people += 1
                    killed.append(kill - 1)
                    players_safe_toriaezu[kill - 1] = 0
            elif j == uranaisi:
                if not uranai == 0:
                    print("あなたは占師です。誰を占いますか? 番号で決めてください。")
                    print(0, "誰も占わない。")
                    for k in range(play_member):
                        print(k + 1, players[k])
                    kill = "n"
                    while True:
                        while True:
                            try:
                                kill = int(input())
                            except:
                                print("整数で答えてください")
                            else:
                                if j == kill - 1:
                                    print("それは自分です。自分は占えません")
                                elif players_safe[kill - 1] == 0:
                                    print("その人はすでに死んでいます。占えません。")
                                elif int(kill) > -1 and int(kill) < play_member + 1:
                                    break
                                else:
                                    print("範囲内で答えてください。")
                        if kill == 0:
                            print("誰も占わない" + "でよろしいですか?(y/n)")
                        else:
                            print(players[int(kill - 1)] + "でよろしいですか?(y/n)")
                        yorosiidesuka = input()
                        if yorosiidesuka == "y":
                            break
                        elif yorosiidesuka == "n":
                            nandemonai = 1
                            print("誰を占いますか? 番号で決めてください。")
                    if kill == 0:
                        print("誰も占いませんでした。")
                    else:
                        print(str(players[kill - 1]) + "を占いました。")
                        if kill - 1 == zinrou2:
                            print("その人は人狼です。会議で報告しましょう。") 
                            break
                        elif kill - 1 == zinrou1:
                            print("その人は人狼です。会議で報告しましょう。")
                        else:
                            print("その人は村人でした。投票しないようにしましょう。")
                        uranai -= 1
                else:
                    print("あなたは占師です。")
                    print("既に占い終えています。")
                    print("役職のターンの時間の長さを減らすために、何秒か待ってもらいます。")
                    print("だいたい5秒がたつまでお待ちください・・・。")
                    t1 = time.time()
                    matutime = random.randint(5, 7)
                    while True:
                        if time.time() - t1 > matutime:
                            break
                    print("お待たせしました。")
            else:
                print("あなたは村人です。今寝ています・・・。")
                print("役職のターンの時間の長さを減らすために、何秒か待ってもらいます。")
                print("だいたい5秒がたつまでお待ちください・・・。")
                t1 = time.time()
                matutime = random.randint(5, 7)
                while True:
                    if time.time() - t1 > matutime:
                        break
                print("お待たせしました。")
        while True:
            print("次の人に回してください。(y/n)")
            yorosiidesuka = input()
            if yorosiidesuka == "y":
                break
        for j in range(1100):
            print("")
def morning():
    global players, play_member, zinrou_member, zinrou1, zinrou2, players_safe, killed, killed_people, died_zinrou_people, votted, players_safe_toriaezu
    print("朝になりました。")
    players_safe = tuple(players_safe_toriaezu)
    if len(killed) == 0:
        print("昨夜死んだ人はいませんでした。")
    else:
        print("昨夜、")
        for i in range(len(killed)):
            print(players[killed[i]])
        print("が殺されました。")
    print("人狼が誰かを話し合いましょう。")
    print("制限時間は2分です。")
    print("議論を始めてください。")
    t1 = time.time()
    while True:
        if time.time() - t1 > 119.5:
            print("議論は終わりです。")
            break
        while (time.time() - t1) % 1 < 0.9:
            a = "wait"
        while (time.time() - t1) % 1 > 0.9:
            a = "wait"
        print(120 - math.floor(time.time() - t1))
    print("誰に投票するか決めてください。")
    for j in range(play_member):
        print(str(players[j]) + "、こちらへ来て、他の人は見えないところへ離れてください。")
        while True:
            print("他の人は離れましたか?(y/n)")
            yorosiidesuka = input()
            if yorosiidesuka == "y":
                break
        if players_safe[j] == 0:
            print("あなたは既に死んでいます。")
            print("死んでいると投票できません。")
        else:
            print("あなたは誰に投票しますか?番号で決めてください。")
            for k in range(play_member):
                print(k + 1, players[k])
            kill = "n"
            while True:
                while True:
                    try:
                        kill = int(input())
                    except:
                        print("整数で答えてください")
                    else:
                        if j == kill - 1:
                            print("それは自分です。自分は投票できません。")
                        elif players_safe[kill - 1] == 0:
                            print("その人はすでに死んでいます。投票できません。")
                        elif j == zinrou1 and kill - 1 == zinrou2:
                            print("その人は仲間です。本当に投票しますか?") 
                            break
                        elif j == zinrou2 and kill - 1 == zinrou1:
                            print("その人は仲間です。本当に投票しますか?") 
                            break
                        elif int(kill) > -1 and int(kill) < play_member + 1:
                            break
                        else:
                            print("範囲内で答えてください。")
                print(players[int(kill - 1)] + "でよろしいですか?(y/n)")
                yorosiidesuka = input()
                if yorosiidesuka == "y":
                    break
                elif yorosiidesuka == "n":
                    nandemonai = 1
                    print("誰を投票しますか? 番号で決めてください。")
            print(str(players[kill - 1]) + "に投票しました。")
            votted.append(kill - 1)
            while True:
                print("次の人に回してください。(y/n)")
                yorosiidesuka = input()
                if yorosiidesuka == "y":
                    break
        for l in range(1100):
            print("")
    print("投票が終わりました。")
    print("投票数はこのようになっています。")
    votted_count = []
    for i in range(play_member):
        votted_count.append(0)
    for i in range(play_member - killed_people):
        votted_count[votted[i]] += 1
    for i in range(play_member):
        print(votted_count[i], players[i])
    print("")
    print("よって")
    for i in range(play_member):
        if max(votted_count) == votted_count[i]:
            print(players[i])
            players_safe_toriaezu[i] = 0
            if i == zinrou1 or i == zinrou2:
                died_zinrou_people += 1
            else:
                killed_people += 1
    players_safe = players_safe_toriaezu
    print("が処刑されます。")
    while True:
        print("勝利確認に進みます。(y/n)")
        yorosiidesuka = input()
        if yorosiidesuka == "y":
            break
def syouri_kakunin():
    global players, play_member, zinrou_member, zinrou1, zinrou2, players_safe, killed, killed_people, died_zinrou_people
    print("勝利判定を行います。")
    syouri = 1
    if play_member - killed_people - zinrou_member < zinrou_member - died_zinrou_people + 1:
        print("人狼の勝利です。")
    elif zinrou_member - died_zinrou_people == 0:
        print("村人の勝利です。")
    else:
        syouri = 0
        print("どの陣営もまだ勝利条件を満たしていません")
        print("試合は続きます。")
    if syouri == 1:
        print("内訳はこのようになっています。")
        for i in range(play_member):
            if players_safe[i] == 1:
                safe = "(生存)"
            else:
                safe = "(死亡)"
            if i == zinrou1 or i == zinrou2:
                print(players[i], "人狼", safe)
            elif i == uranaisi:
                print(players[i], "占師", safe)
            else:
                print(players[i], "村人", safe)
        print("")
        print("お疲れさまでした。")
        sys.exit()

uranai = 1
play_member = 0
zinrou_member = 0
players = []
players_safe = []
players_safe_toriaezu = []
i = 0
zinrou1 = 0
zinrou2 = 0
uranaisi = 0
killed_people = 0
died_zinrou_people = 0
situmon()
play_member = int(play_member)
zinrou_member = int(zinrou_member)
for i in range(play_member):
    member_situmon()
print("役職の配布をします。")
yakusyoku_gime()
yakusyoku_haihu()
print("では始めます。")
while True:
    # ||0, 死んでる   || 1,生きてる
    night()
    votted = []
    morning()
    syouri_kakunin()