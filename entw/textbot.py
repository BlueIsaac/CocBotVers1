def get_response(message: str) -> str:
    if message == "info":
        return '''
        Guten Tag, tapfere Krieger!

Herzlich willkommen im Clan Wachsam, wo die Freude am Spielen genauso groß ist wie unser Eifer, unsere Dörfer zu schützen. 
Hier in unserem bescheidenen Clan legen wir großen Wert auf Gemeinschaft und Zusammenarbeit.

Wir sind keine gewöhnliche Truppe von Einzelkämpfern. Nein, wir sind eine eingeschworene Gemeinschaft von Clanspielern, die sich gegenseitig unterstützen, als wären wir eine große Familie. 
Wenn du auf der Suche nach einem Ort bist, an dem du nicht nur Dörfer errichtest, sondern auch langanhaltende Freundschaften aufbaust, dann bist du hier richtig.

Unsere Maxime lautet: "Der Spaß am Spiel steht an erster Stelle." Wir mögen es, uns im Chat auszutauschen, uns über erfolgreiche Angriffe und Verteidigungen zu freuen und uns gegenseitig mit Truppen zu versorgen. 
Aber lass dich nicht täuschen – wir nehmen das Spiel ernst, und Aktivität ist bei uns Pflicht. Wenn du bereit bist, gemeinsam mit uns zu kämpfen, zu siegen und zu feiern, dann bist du herzlich willkommen.

Unser Clan ist wie ein schützender Schild, der dich in den Wirren von Clash of Clans begleitet. Wir sind hier, um dir zu helfen, zu unterstützen und Spaß zu haben. 
Also, zieh dein Schwert und deine Rüstung an, schließe dich uns an und lass uns die Clash-Welt gemeinsam erobern!

Möge unser Clan Wachsam immer stark sein und unser Teamgeist nie erlöschen. Auf in die Schlacht, meine Freunde! Clash on! 🛡️💪🌟
        '''
    if message == "regeln":
        return '''
        Regeln des Clan Wachsam:

Aktivität: Bitte sei aktiv im Spiel. Maximal fünf Tage Inaktivität sind erlaubt. Längere Abwesenheit führt zum Ausschluss aus dem Clan.

Freundlichkeit und Hilfsbereitschaft: Ein freundlicher und hilfsbereiter Umgang im Clan ist Pflicht. Beleidigungen und kindisches Verhalten im Chat sind nicht gestattet.

Clankrieg:

Bei Clankriegen ist der erste Angriff IMMER auf die eigene Nummer durchzuführen.
Der zweite Angriff ist erlaubt, WENN:
Jemand bereits seine eigene Nummer angegriffen hat und Verbesserungen möglich sind (z.B., aus 1 Stern werden 2 oder 3 Sterne).
Es sind nur noch 4 Stunden bis zum Kriegsende übrig.
Die Vize-Anführer oder der Anführer Anweisungen im Chat hinterlassen haben.
Clankriegsliga:

In der Clankriegsliga ist immer auf die eigene Nummer anzugreifen, es sei denn, die Vize-Anführer oder der Anführer haben im Chat andere Anweisungen gegeben.
Clanstadt:

Während des Überfallwochenendes sollte jeder Clanmitglied teilnehmen.
Verbesserungen in der Clanstadt sollten nur an priorisierten Gegenständen vorgenommen werden.
Clanspiele:

Die Teilnahme an den Clanspielen ist Pflicht, und jeder sollte mindestens 1000 Punkte sammeln.
Bei dreifach wiederholter Nichterfüllung ohne triftigen Grund erfolgt der Ausschluss aus dem Clan.
Wenn zweimal in Folge überhaupt nicht teilgenommen wird, führt dies ebenfalls zum Ausschluss.
Lasst uns gemeinsam diese Regeln respektieren und unser Dorf zu noch größerem Ruhm führen! 💪🛡️🌟
        '''

    if message == 'willkommen':
        return '''
        **Willkommen im Clandiscord-Server!** :tada:

Wir freuen uns, dich in unserer Community begrüßen zu dürfen. Bevor du loslegst, gibt es ein paar wichtige Dinge, die du wissen solltest:

1. **Vorstellung**: Du kannst dich gerne im Channel spielername-vorname vorstellen damit wir wissen wer du bist.

2. **Regeln**: Bitte lies die Regeln im #regeln Channel (Oder durch Verwendung !regeln hier im chat) aufmerksam durch und akzeptiere sie. Die Einhaltung unserer Regeln ist entscheidend, um eine freundliche und respektvolle Umgebung für alle zu schaffen.

3. **Befehle**: Unser Bot steht dir zur Verfügung! Du kannst `!info` verwenden, um mehr über den Server und seine Funktionen zu erfahren. !hilfe zeigt dir an welche kommandos dieser Bot momentan beherrscht.

4. **Kommunikation**: Nutze die passenden Channels für deine Gespräche und Diskussionen. Bitte vermeide Spam und Respektlosigkeit gegenüber anderen Mitgliedern.

5. **Fragen stellen**: Wenn du Fragen hast, zögere nicht, sie im #chat-Channel zu stellen. Unsere Mitglieder helfen dir gerne weiter.

6. **Community**: Wir sind eine freundliche und hilfsbereite Gemeinschaft. Sei nett zu anderen Mitgliedern und respektiere ihre Meinungen und Ideen.

**Vielen Dank für deine Teilnahme an unserer Community!** Wir wünschen dir viel Spaß und eine großartige Zeit auf unserem Server. Bei weiteren Fragen stehen wir dir gerne zur Verfügung.

        '''
    if message == "hilfe":
        return '''
        Willkommen bei unserem Bot! Hier sind einige der verfügbaren Befehle:

- `!info`: Erfahre mehr über unseren Clan und unsere Community.
- `!regeln`: Lies unsere Regeln, um ein respektvolles Umfeld sicherzustellen.
- `!hallo`: Erhalte eine freundliche Begrüßung vom Bot.
- `!ping`: Teste die Reaktionszeit des Bots.
- `!hilfe`: Zeigt diese Hilfe-Nachricht an, um dir bei der Verwendung der Befehle zu helfen.

Wenn du Fragen hast oder weitere Hilfe benötigst, zögere nicht, im Chat danach zu fragen. Viel Spaß!
'''