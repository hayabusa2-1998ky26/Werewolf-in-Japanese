import random
import time
import math
import sys
def yakusyoku_gime():
    global players, i, play_member, zinrou_member, zinrou1, zinrou2, players_safe, uranaisi, kyouzin, kyouzin_member, turibito, turibito_member, kariudo, kariudo_member, reibai, reibai_member
    zinrou1 = random.randint(0, play_member - 1)
    zinrou2 = random.randint(0, play_member - 1)
    while zinrou2 == zinrou1:
        zinrou2 = random.randint(0, play_member - 1)
    if zinrou_member == 1:
        zinrou2 = -1
    if uranaisi_member == 1:
        uranaisi = random.randint(0, play_member - 1)
        while zinrou1 == uranaisi or zinrou2 == uranaisi:
            uranaisi = random.randint(0, play_member - 1)
    else:
        uranaisi = -1
    if kyouzin_member == 1:
        kyouzin = random.randint(0, play_member - 1)
        while zinrou1 == kyouzin or zinrou2 == kyouzin or uranaisi == kyouzin:
            kyouzin = random.randint(0, play_member - 1)
    else:
        kyouzin = -1
    if turibito_member == 1:
        turibito = random.randint(0, play_member - 1)
        while zinrou1 == turibito or zinrou2 == turibito or uranaisi == turibito or kyouzin == turibito:
            turibito = random.randint(0, play_member - 1)
    else:
        turibito = -1
    if kariudo_member == 1:
        kariudo = random.randint(0, play_member - 1)
        while zinrou1 == kariudo or zinrou2 == kariudo or uranaisi == kariudo or kyouzin == kariudo or turibito == kariudo:
            kariudo = random.randint(0, play_member - 1)
    else:
        kariudo = -1
    if reibai_member == 1:
        reibai = random.randint(0, play_member - 1)
        while zinrou1 == reibai or zinrou2 == reibai or uranaisi == reibai or kyouzin == reibai or turibito == reibai or kariudo == reibai:
            reibai = random.randint(0, play_member - 1)
    else:
        reibai = -1
def yakusyoku_haihu():
    global play_member, zinrou1, zinrou2, players_safe, uranaisi, uranai, kyouzin, kyouzin_haaku, kyouzin_member, turibito, reibai, reibai_kaisuu, kariudo
    for i in range(play_member):
        print(str(players[i]) + "、こちらへ来て、他の人は見えないところへ離れてください。")
        while True:
            print("他の人は離れましたか?(y/n)")
            yorosiidesuka = input()
            if yorosiidesuka == "y":
                break
        print("今回のあなたの役職は...")
        if i == zinrou1 or i == zinrou2:
            print("「人狼」(人狼陣営)")
            print("です。")
            if zinrou2 == -1:
                if kyouzin_member == 0:
                    print("仲間はいません。")
            else:
                if i == zinrou1:
                    print("仲間は" + players[zinrou2] + "です。")
                elif i == zinrou2:
                    print("仲間は" + players[zinrou1] + "です。")
            if kyouzin_member == 1:
                print("村に狂人が紛れ込んだようです。")
                print("狂人はあなたの味方をしてくれるでしょう・")
        elif i == uranaisi:
            print("「占師」(村人陣営)")
            print("です。")
            print("今回占える回数は" + str(uranai) + "回です。")
            print("慎重に使いましょう。")
        elif i == kyouzin:
            print("「狂人」(人狼陣営)")
            print("です。")
            print("殺すことはできませんが、人狼の手伝いをしましょう。")
            print("人狼は狂人がだれかはわかりません。")
            if kyouzin_haaku == 1:
                if zinrou2 == -1:
                    print("人狼は" + players[zinrou1] + "です。")
                else:
                    print("人狼は" + players[zinrou2] + "と、")
                    print("人狼は" + players[zinrou1] + "です。")
            else:
                print("今回は狂人は人狼がだれかわからない設定になっています。")
        elif i == turibito:
            print("「吊人」(第三陣営)")
            print("です。")
            print("会議で吊られたら勝ちです。怪しい行動をしてつられましょう。")
            print("人狼に殺されたら負けになります。")
        elif i == kariudo:
            print("「狩人」(村人陣営)")
            print("です。")
            print("毎夜のうち一回だけだれかを人狼からまもることができます。")
            print("占師や霊媒などを守りましょう。")
        elif i == reibai:
            print("「霊媒」(村人陣営)")
            print("です。")
            print("死んだ人が誰だったのかを見ることができます。")
            print("今回霊媒できる回数は" + str(reibai_kaisuu) + "回です。")
        else:
            print("「村人」(村人陣営)")
            print("です。")
        while True:
            print("次の人に回してください。(y/n)")
            yorosiidesuka = input()
            if yorosiidesuka == "y":
                break
        for j in range(1100):
            print("")
def night():
    global players, i, play_member, zinrou_member, zinrou1, zinrou2, players_safe, killed, killed_people, players_safe_toriaezu, uranaisi, uranai, kyouzin_member, kyouzin, turibito, kariudo, kariudo_mamori, reibai, reibai_kaisuu
    killed = []
    kariudo_mamori = -1
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
                abirity= "n"
                while True:
                    while True:
                        try:
                            abirity= int(input())
                        except:
                            print("整数で答えてください")
                        else:
                            if j == abirity- 1:
                                print("それは自分です。自分は殺せません。")
                            elif players_safe_toriaezu[abirity- 1] == 0:
                                print("その人はすでに死んでいます。殺せません。")
                            elif j == zinrou1 and abirity- 1 == zinrou2:
                                print("その人は仲間です。本当に殺しますか?") 
                                break
                            elif j == zinrou2 and abirity- 1 == zinrou1:
                                print("その人は仲間です。本当に殺しますか?") 
                                break
                            elif int(abirity) > -1 and int(abirity) < play_member + 1:
                                break
                            else:
                                print("範囲内で答えてください。")
                    if abirity== 0:
                        print("誰も殺さらない" + "でよろしいですか?(y/n)")
                    else:
                        print(players[int(abirity- 1)] + "でよろしいですか?(y/n)")
                    yorosiidesuka = input()
                    if yorosiidesuka == "y":
                        break
                    elif yorosiidesuka == "n":
                        nandemonai = 1
                        print("誰を殺しますか? 番号で決めてください。")
                if abirity== 0:
                    print("誰も殺しませんでした。")
                else:
                    print(str(players[abirity- 1]) + "を殺しました。")
                    killed_people += 1
                    killed.append(abirity- 1)
                    players_safe_toriaezu[abirity- 1] = 0
            elif j == uranaisi:
                if not uranai == 0:
                    print("あなたは占師です。誰を占いますか? 番号で決めてください。")
                    print(0, "誰も占わない。")
                    for k in range(play_member):
                        print(k + 1, players[k])
                    abirity= "n"
                    while True:
                        while True:
                            try:
                                abirity= int(input())
                            except:
                                print("整数で答えてください")
                            else:
                                if j == abirity- 1:
                                    print("それは自分です。自分は占えません")
                                elif players_safe[abirity- 1] == 0:
                                    print("その人はすでに死んでいます。占えません。")
                                elif int(abirity) > -1 and int(abirity) < play_member + 1:
                                    break
                                else:
                                    print("範囲内で答えてください。")
                        if abirity== 0:
                            print("誰も占わない" + "でよろしいですか?(y/n)")
                        else:
                            print(players[int(abirity- 1)] + "でよろしいですか?(y/n)")
                        yorosiidesuka = input()
                        if yorosiidesuka == "y":
                            break
                        elif yorosiidesuka == "n":
                            nandemonai = 1
                            print("誰を占いますか? 番号で決めてください。")
                    if abirity== 0:
                        print("誰も占いませんでした。")
                    else:
                        print(str(players[abirity- 1]) + "を占いました。")
                        if abirity- 1 == zinrou2:
                            print("その人は人狼です。会議で報告しましょう。") 
                            break
                        elif abirity- 1 == zinrou1:
                            print("その人は人狼です。会議で報告しましょう。")
                        elif abirity- 1 == turibito:
                            print("その人は吊人です。吊ってしまったら負けになります。")
                        elif abirity - 1 == kariudo:
                            print("その人は狩人です。誰かを守ってくれます。")
                        elif abirity - 1 == reibai:
                            print("その人は霊媒です。会議で報告しましょう。")
                        else:
                            if kyouzin_member == 1:
                                print("その人は村人でした。狂人の可能性もあるので注意しましょう。")
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
            elif j == kyouzin:
                print("あなたは狂人です。今寝ています・・・。")
                print("役職のターンの時間の長さを減らすために、何秒か待ってもらいます。")
                print("だいたい5秒がたつまでお待ちください・・・。")
                t1 = time.time()
                matutime = random.randint(5, 7)
                while True:
                    if time.time() - t1 > matutime:
                        break
                print("お待たせしました。")
            elif j == turibito:
                print("あなたは吊人です。今寝ています・・・。")
                print("役職のターンの時間の長さを減らすために、何秒か待ってもらいます。")
                print("だいたい5秒がたつまでお待ちください・・・。")
                t1 = time.time()
                matutime = random.randint(5, 7)
                while True:
                    if time.time() - t1 > matutime:
                        break
                print("お待たせしました。")
            elif j == kariudo:
                print("あなたは狩人です。誰を守りますか？番号で答えてください。")
                print(0, "誰も守らない。")
                for k in range(play_member):
                    print(k + 1, players[k])
                abirity= "n"
                while True:
                    while True:
                        try:
                            abirity= int(input())
                        except:
                            print("整数で答えてください")
                        else:
                            if j == abirity- 1:
                                print("それは自分ですがよろしいですか?自分も守ることができます。")
                                break
                            elif players_safe[abirity- 1] == 0:
                                print("その人はすでに死んでいます。守れません。")
                            elif int(abirity) > -1 and int(abirity) < play_member + 1:
                                break
                            else:
                                print("範囲内で答えてください。")
                    if abirity== 0:
                        print("本当に、誰も守らない" + "でよろしいですか?(y/n)")
                    else:
                        print(players[int(abirity- 1)] + "でよろしいですか?(y/n)")
                    yorosiidesuka = input()
                    if yorosiidesuka == "y":
                        break
                    elif yorosiidesuka == "n":
                        nandemonai = 1
                        print("誰を守りますか? 番号で決めてください。")
                if abirity== 0:
                    print("誰も守りませんでした。")
                else:
                    print(str(players[abirity- 1]) + "を守りました。")
                    kariudo_mamori = abirity - 1
            elif j == reibai:
                if not reibai_kaisuu == 0:
                    print("あなたは霊媒です。誰を霊媒しますか? 番号で決めてください。")
                    print(0, "誰も霊媒しない。")
                    for k in range(play_member):
                        print(k + 1, players[k])
                    abirity= "n"
                    while True:
                        while True:
                            try:
                                abirity= int(input())
                            except:
                                print("整数で答えてください")
                            else:
                                try:
                                    if j == abirity- 1:
                                        print("それは自分です。自分は霊媒できません")
                                    elif players_safe[abirity- 1] == 1 and abirity != 0:
                                        print("その人はまだ生きています。霊媒できません。")
                                    elif int(abirity) > -1 and int(abirity) < play_member + 1:
                                        break
                                except:
                                    print("範囲内で答えてください。")
                        if abirity== 0:
                            print("誰も霊媒しない" + "でよろしいですか?(y/n)")
                        else:
                            print(players[int(abirity- 1)] + "でよろしいですか?(y/n)")
                        yorosiidesuka = input()
                        if yorosiidesuka == "y":
                            break
                        elif yorosiidesuka == "n":
                            nandemonai = 1
                            print("誰を霊媒しますか? 番号で決めてください。")
                    if abirity== 0:
                        print("誰も霊媒しませんでした。")
                    else:
                        print(str(players[abirity- 1]) + "を霊媒しました。")
                        if abirity- 1 == zinrou2:
                            print("その人は人狼でした。人狼は吊れているようです。") 
                            break
                        elif abirity- 1 == zinrou1:
                            print("その人は人狼でした。人狼は吊れているようです。")
                        elif abirity- 1 == turibito:
                            print("その人は吊人でした。しかし既に死んでいるため脅威ではありません。")
                        elif abirity - 1 == uranaisi:
                            print("その人は占師でした。会議で報告しましょう。")
                        else:
                            if kyouzin_member == 1:
                                print("その人は村人でした。狂人の可能性もあるので注意しましょう。")
                            else:
                                print("その人は村人でした。")
                        reibai_kaisuu -= 1
                else:
                    print("あなたは霊媒です。")
                    print("既に霊媒し終えています。")
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
    global players, play_member, zinrou_member, zinrou1, zinrou2, players_safe, killed, killed_people, died_zinrou_people, votted, players_safe_toriaezu, kyouzin_member, kyouzin, turibito, turibito_die, kariudo_member, kariudo, kariudo_mamori, reibai_member, reibai
    print("朝になりました。")
    if players_safe_toriaezu[kariudo_mamori] == 0 and kariudo_mamori != -1:
        players_safe_toriaezu[kariudo_mamori] = 1
        killed.remove(kariudo_mamori)
        print("誰かが人狼から誰かを守ったようです。")
    a = tuple(players_safe_toriaezu)
    players_safe = a
    if len(killed) == 0:
        print("昨夜死んだ人はいませんでした。")
    else:
        print("昨夜、")
        for i in range(len(killed)):
            print(players[killed[i]])
        print("が殺されました。")
    syouri_kakunin()
    print("人狼が誰かを話し合いましょう。")
    print("制限時間は2分です。")
    while True:
        print("議論を始めますか?(y/n)")
        yorosiidesuka = input()
        if yorosiidesuka == "y":
            break
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
            print("死んでいると投票できません。ほかの人を選んでください。")
        else:
            print("あなたは誰に投票しますか?番号で決めてください。")
            for k in range(play_member):
                print(k + 1, players[k])
            abirity= "n"
            while True:
                while True:
                    try:
                        abirity= int(input())
                    except:
                        print("整数で答えてください")
                    else:
                        if j == abirity- 1:
                            print("それは自分です。自分は投票できません。ほかの人を選んでください。")
                        elif players_safe[abirity- 1] == 0:
                            print("その人はすでに死んでいます。投票できません。ほかの人を選んでください。")
                        elif j == zinrou1 and abirity- 1 == zinrou2:
                            print("その人は仲間です。本当に投票しますか?") 
                            break
                        elif j == zinrou2 and abirity- 1 == zinrou1:
                            print("その人は仲間です。本当に投票しますか?") 
                            break
                        elif int(abirity) > -1 and int(abirity) < play_member + 1:
                            break
                        else:
                            print("範囲内で答えてください。")
                print(players[int(abirity- 1)] + "でよろしいですか?(y/n)")
                yorosiidesuka = input()
                if yorosiidesuka == "y":
                    break
                elif yorosiidesuka == "n":
                    nandemonai = 1
                    print("誰を投票しますか? 番号で決めてください。")
            print(str(players[abirity- 1]) + "に投票しました。")
            votted.append(abirity- 1)
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
            if i == zinrou1 or i == zinrou2 or i == kyouzin:
                died_zinrou_people += 1
            elif i == turibito:
                turibito_die = 1
            else:
                killed_people += 1
    players_safe = players_safe_toriaezu
    print("が処刑されます。")
def syouri_kakunin():
    global players, play_member, zinrou_member, zinrou1, zinrou2, players_safe, killed, killed_people, died_zinrou_people, kyouzin_member, kyouzin, turibito, turibito_die, kariudo, reibai
    while True:
        print("勝利判定をしますか?。(y/n)")
        yorosiidesuka = input()
        if yorosiidesuka == "y":
            break
    print("勝利判定を行います。")
    syouri = 1
    if turibito_die == 1:
        print("吊人の勝利です。")
    elif play_member - killed_people - zinrou_member < zinrou_member - died_zinrou_people + 1 + kyouzin_member:
        print("人狼陣営の勝利です。")
    elif zinrou_member + kyouzin_member - died_zinrou_people == 0 or (zinrou_member + kyouzin_member - died_zinrou_people - 1 == 0 and (kyouzin_member == 1 and players_safe[kyouzin] == 1)):
        print("村人陣営の勝利です。")
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
            elif i == kyouzin:
                print(players[i], "狂人", safe)
            elif i == turibito:
                print(players[i], "吊人", safe)
            elif i == kariudo:
                print(players[i], "狩人", safe)
            elif i == reibai:
                print(players[i], "霊媒", safe)
            else:
                print(players[i], "村人", safe)
        print("")
        print("お疲れさまでした。")
        sys.exit()

# 設定(入力してください。)
# プレイする人
players = ["player1", "player2", "player3", "player4", "player5"]
# 占師の人数[0~1]
uranaisi_member = 0
# 占いができる回数[1~2]
uranai = 1
# 狩人の人数[0~1](β版)
kariudo_member = 1
# 霊媒の人数[0~1](β版)
reibai_member = 1
# 霊媒ができる回数[1~2]
reibai_kaisuu = 2
# 人狼の人数[1~2]
zinrou_member = 1
# 狂人の人数[0~1]
kyouzin_member = 0
# 狂人が人狼を誰かを知るか(1ならする、0ならしない。)
kyouzin_haaku = 1
# 吊人の人数[0~1]
turibito_member = 0



# 役職説明:
# 村人陣営
# 村人
# ただの村人。特殊能力なし。
# 占師
# 夜に、生きているだれかの役職を知ることができる。ただし狂人は村人とでる。
# 狩人
# 毎夜、誰か一人を人狼から守ることができる。回数制限はない。ただし、村人陣営じゃなくても守ることができてしまう。
# 霊媒
# 夜に、死んだだれかの役職を知ることができる。ただし狂人は村人とでる。

# 人狼陣営
# 人狼
# 普通の人狼。1夜に一人殺すことができる。人狼は狂人が誰かはわからない。
# 狂人
# 狂った村人。人狼が勝つと一緒に勝利するが、殺すことはできない。

# 第三陣営
# 吊人
# 吊られたら勝ちの第三陣営。人狼に殺されるのは負け判定。



# 勝利条件:
# 村人陣営勝利条件:
# だれか1人村人陣営を残した状態で、人狼全員を吊りきったら勝ち。狂人は残っていても問題ない。

# 人狼陣営勝利条件:
# 全員殺すか、村の人数の半分以上が人狼陣営になったら勝ち。吊人がつられてしまった場合、勝利は吊人に優先される。

# 第三陣営勝利条件:
# 吊人
# 会議内で吊られたら勝ち。人狼に殺されたら負け。



play_member = len(players)
players_safe = []
players_safe_toriaezu = []
i = 0
zinrou1 = 0
zinrou2 = 0
uranaisi = 0
turibito = 0
turibito_die = 0
killed_people = 0
died_zinrou_people = 0
play_member = int(play_member)
zinrou_member = int(zinrou_member)
for i in range(play_member):
    players_safe.append(1)
    players_safe_toriaezu.append(1)
if (zinrou_member + kyouzin_member) * 2 + 1 > play_member:
    print("人狼陣営の人数が多すぎます。")
    sys.exit()
if play_member < uranaisi_member + reibai_member + kariudo_member + zinrou_member + kyouzin_member + turibito_member:
    print("役職の数がプレイ人数を上回っています。")
    sys.exit()
print("ゲームを始めます。")
print("役職の配布をします。")
yakusyoku_gime()
yakusyoku_haihu()
print("では始めます。")
while True:
    night()
    votted = []
    morning()
    syouri_kakunin()